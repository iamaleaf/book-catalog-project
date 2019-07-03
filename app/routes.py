from flask import render_template, flash, request, redirect, url_for, jsonify
from app import app, db
from app.models import User, Category, Book
from sqlalchemy.orm.exc import NoResultFound

# Imports for anti forgery state token
from flask import session as login_session
import random
import string

# Imports for gconnect step
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

CLIENT_ID = json.loads(
    open('/var/www/Catalog/client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Book Catalog Application"

def getCategories():
    # categories list
    categories = Category.query.order_by(Category.name.asc()).all()
    return categories


# Create user
def createUser(login_session):
    user = User(name=login_session['username'],
                email=login_session['email'])
    db.session.add(user)
    db.session.commit()
    user = User.query.filter_by(email=login_session['email']).one()
    return user.id


# Get user
def getUserInfo(user_id):
    user = User.query.filter_by(id=user_id).one()
    return user


# Get user id from email
def getUserID(email):
    try:
        user = User.query.filter_by(email=email).one()
        return user.id
    except NoResultFound:
        return None


# Check if there is a user logged in
def getUsername():
    username = login_session.get('username')
    return username


# Create state token
@app.route('/login/')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    # Render the login template
    return render_template('login.html', STATE=state,
                           categories=getCategories(), user=getUsername())


# Google authentication login
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data
    # Exchange authorization code for credentials object
    try:
        oauth_flow = flow_from_clientsecrets('/var/www/Catalog/client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        # Initiate exchange with the exchange function
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(json.dumps('Failed to upgrade the \
authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Check that the access token is valid
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    # Create request with url and access token
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    if result.get('error') is not None:
        # send 500 internal server error to the client
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Verify access token is for the intended user
    google_id = credentials.id_token['sub']
    if result['user_id'] != google_id:
        response = make_response(json.dumps("Token user ID doesn't match \
given user ID,"), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Check if the user is already logged into the system
    stored_access_token = login_session.get('access_token')
    stored_google_id = login_session.get('google_id')
    if stored_access_token is not None and google_id == stored_google_id:
        response = make_response(json.dumps('Current user is already \
connected'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Store the access token in session
    login_session['access_token'] = credentials.access_token
    login_session['google_id'] = google_id
    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = answer.json()
    # Store user info in session
    login_session['username'] = data['name']
    login_session['email'] = data['email']
    # Verify if user exists, create one if not
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id
    # Send flash message
    flash("You are now logged in as %s" % login_session['username'])
    return "Welcome, %s" % login_session['username']


# Google disconnect
@app.route('/gdisconnect/')
def gdisconnect():
    access_token = login_session.get('access_token')
    # If token is empty, no record of user
    if access_token is None:
        response = make_response(json.dumps('Current user not \
connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Request Google to revoke token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' \
        % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    # Check response and clear login_session if OK
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['google_id']
        del login_session['username']
        del login_session['email']
        flash('Successfully disconnected')
        return redirect(url_for('showCatalog'))
    else:
        response = make_response(json.dumps('Failed to revoke token for given \
user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/')
@app.route('/catalog/')
def showCatalog():
    # last 10 books
    books = Book.query.order_by(Book.id.desc()).limit(10).all()
    user = login_session.get('username')
    return render_template('index.html', categories=getCategories(),
                           books=books, user=getUsername())


# Display category
@app.route('/catalog/category/<int:category_id>/')
def showCategory(category_id):
    # track if user is logged in to display add book link
    logged = False
    if 'username' in login_session:
        logged = True
    category = Category.query.filter_by(id=category_id).one()
    books = Book.query.filter_by(category_id=category_id).all()
    return render_template('category.html', categories=getCategories(),
                           category=category, books=books, user=getUsername())


# Display catalog JSON
@app.route('/catalog/JSON/')
def showCatalogJSON():
    books = Book.query.all()
    return jsonify(Books=[i.serialize for i in books])


# Create a new book
@app.route('/catalog/category/<int:category_id>/book/new/',
           methods=['GET', 'POST'])
def newBook(category_id):
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        book = Book(name=request.form['name'],
                    author=request.form['author'],
                    description=request.form['description'],
                    category=Category.query.filter_by(
                        name=request.form['category']).one(),
                    user_id=login_session['user_id'])
        db.session.add(book)
        db.session.commit()
        flash('New Book %s Successfully Created in %s' %
              (book.name, book.category.name))
        return redirect(url_for('showCategory', category_id=book.category_id))
    else:
        return render_template('newBook.html', category_id=category_id,
                               categories=getCategories(), user=getUsername())


# View a book
@app.route('/catalog/category/<int:category_id>/book/<int:book_id>/')
def showBook(category_id, book_id):
    book = Book.query.filter_by(id=book_id).one()
    if 'user_id' in login_session and \
            book.user_id == login_session['user_id']:
        return render_template('book.html', book=book, categories=getCategories(),
                               user=getUsername(), owner=True)
    else:
        return render_template('book.html', book=book, logged=False,
                               categories=getCategories(), user=getUsername())


# Edit a book
@app.route('/catalog/category/<int:category_id>/book/<int:book_id>/edit/',
           methods=['GET', 'POST'])
def editBook(category_id, book_id):
    # redirect if user not logged in
    if 'username' not in login_session:
        return redirect('/login')
    book = Book.query.filter_by(id=book_id).one()
    # check book owner
    if book.user_id != login_session['user_id']:
        flash('You are not authorized to edit this book')
        return redirect(url_for('showBook', category_id=category_id,
                                book_id=book_id))
    # process edit request
    if request.method == 'POST':
        if request.form['name']:
            book.name = request.form['name']
        if request.form['author']:
            book.author = request.form['author']
        if request.form['description']:
            book.description = request.form['description']
        if request.form['category']:
            category = Category.query.\
                filter_by(name=request.form['category']).one()
            book.category = category
        db.session.add(book)
        db.session.commit()
        flash("Book Successfully Edited")
        return redirect(url_for('showCategory', category_id=category_id))
    # return template
    else:
        return render_template('editBook.html',
                               category_id=category_id,
                               book=book,
                               categories=getCategories(),
                               user=getUsername())


# Delete a book
@app.route('/catalog/category/<int:category_id>/book/<int:book_id>/delete/',
           methods=['GET', 'POST'])
def deleteBook(category_id, book_id):
    # redirect if user not logged in
    if 'username' not in login_session:
        return redirect('/login')
    book = Book.query.filter_by(id=book_id).one()
    # check book owner
    if book.user_id != login_session['user_id']:
        flash('You are not authorized to delete this book')
        return redirect(url_for('showBook', category_id=category_id,
                                book_id=book_id))
    # process delete request
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash("Book Successfully Deleted")
        return redirect(url_for('showCategory', category_id=category_id))
    # return template
    else:
        return render_template('deleteBook.html',
                               category_id=category_id,
                               book=book,
                               categories=getCategories(),
                               user=getUsername())
