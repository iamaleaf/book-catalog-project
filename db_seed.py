# -*- coding: utf-8 -*-
from app import app, db
from app.models import User, Category, Book


def deleteItems(items):
    for i in items:
        db.session.delete(i)
        db.session.commit()


def addItems(items):
    for i in items:
        db.session.add(i)
        db.session.commit()


def seedDB():
    # Delete all pre-existing data from the database
    deleteItems(Book.query.all())
    deleteItems(Category.query.all())
    deleteItems(User.query.all())
    # Add items to the db
    addItems(users)
    addItems(categories)
    addItems(books)


# lists
users = []
categories = []
books = []

# USERS
users.append(User(name="Jeffrey L. Jones", email="jeffreyjones@email.com"))
users.append(User(name="Robert N. Goley", email="robertgoley@gmail.com"))
users.append(User(name="Eric A. Fleming", email="ericflaming@email.com"))

# CATEGORIES
categories.append(Category(name="Biography"))
categories.append(Category(name="Children"))
categories.append(Category(name="Cooking"))
categories.append(Category(name="Fantasy"))
categories.append(Category(name="History"))
categories.append(Category(name="Horror"))
categories.append(Category(name="Mysteries"))
categories.append(Category(name="Romance"))
categories.append(Category(name="Teen"))

# BOOKS
# Biography
books.append(Book(name="Into the Wild",
                  author="Jon Krakauer",
                  description="In April 1992 a young man from a well-to-do \
family hitchhiked to Alaska and walked alone into the wilderness north of Mt. \
McKinley. His name was Christopher Johnson McCandless. He had given $25,000 \
in savings to charity, abandoned his car and most of his possessions, burned \
all the cash in his wallet, and invented a new life for himself. Four months \
later, his decomposed body was found by a moose hunter.  How McCandless came \
to die is the unforgettable story of Into the Wild.",
                  category=categories[0],
                  user=users[0]))
books.append(Book(name="The Glass Castle",
                  author="Jeannette Walls",
                  description="A tender, moving tale of unconditional love in \
a family that, despite its profound flaws, gave the author the fiery \
determination to carve out a successful life on her own terms.",
                  category=categories[0],
                  user=users[1]))
books.append(Book(name="The House on Mango Street",
                  author="Sandra Cisneros",
                  description="Told in a series of vignettes, sometimes \
heartbreaking, sometimes deeply is the story of a young Latina girl \
growing up in Chicago, inventing for herself who and what she will \
become. Few other books in our time have touched so many readers.",
                  category=categories[0],
                  user=users[2]))

# Children
books.append(Book(name="Charlotte's Web",
                  author="E.B. White",
                  description="Some Pig. Humble. Radiant. These are the words \
in Charlotte's Web, high up in Zuckerman's barn. Charlotte's spiderweb tells \
of her feelings for a little pig named Wilbur, who simply wants a friend. \
They also express the love of a girl named Fern, who saved Wilbur's life \
when he was born the runt of his litter.",
                  category=categories[1],
                  user=users[0]))
books.append(Book(name="Harry Potter and the Philosopher's Stone",
                  author="J.K Rowling",
                  description="This is the tale of Harry Potter, an ordinary \
11-year-old boy serving as a sort of slave for his aunt and uncle who learns \
that he is actually a wizard and has been invited to attend the Hogwarts \
School for Witchcraft and Wizardry.",
                  category=categories[1],
                  user=users[1]))
books.append(Book(name="Green Eggs and Ham",
                  author="Dr. Seuss",
                  description="Do you like green eggs and ham? asks Sam-I-am \
in this Beginner Book by Dr. Seuss. In a house or with a mouse? In a boat or \
with a goat? On a train or in a tree? Sam keeps asking persistently. With \
unmistakable characters and signature rhymes, Dr. Seuss's beloved favorite \
has cemented its place as a children's classic.",
                  category=categories[1],
                  user=users[2]))

# Cooking
books.append(Book(name="How to Cook Everything: Simple Recipes for Great Food",
                  author="Mark Bittmanr",
                  description="Here's the breakthrough one-stop cooking \
reference for today's generation of cooks! Nationally known cooking \
authority Mark Bittman shows you how to prepare great food for all \
occasions using simple techniques, fresh ingredients, and basic \
kitchen equipment. Just as important, How to Cook Everything takes a \
relaxed, straightforward approach to cooking, so you can enjoy yourself \
in the kitchen and still achieve outstanding results.",
                  category=categories[2],
                  user=users[0]))
books.append(Book(name="Dorie's Cookies",
                  author="Dorie Greenspan",
                  description="Over the course of her baking career, Dorie \
Greenspan has created more than 300 cookie recipes. Yet she has never \
written a book about them-until now. To merit her three purple stars of \
approval, every cookie had to be so special that it begged to be made again \
and again. Cookies for every taste and occasion are here.",
                  category=categories[2],
                  user=users[1]))
books.append(Book(name="The Weeknight Cookbook",
                  author="Justine Schofield",
                  description="Take the stress out of weeknight dinners by \
letting a well-stocked pantry, fridge and freezer do the work for you. \
Justine Schofield shows you how, with more than 100 simple meals based on \
everyday staples.",
                  category=categories[2],
                  user=users[2]))

# Fantasy
books.append(Book(name="The Hobbit",
                  author="J.R.R Tolkien",
                  description="Written for J.R.R. Tolkien's own children, The \
Hobbit met with instant critical acclaim when it was first published in 1937. \
Now recognized as a timeless classic, this introduction to the hobbit Bilbo \
Baggins, the wizard Gandalf, Gollum, and the spectacular world of \
Middle-earth recounts of the adventures of a reluctant hero, a \
powerful and dangerous ring, and the cruel dragon Smaug the \
Magnificent.",
                  category=categories[3],
                  user=users[0]))
books.append(Book(name="A Game of Thrones",
                  author="George R.R. Martin",
                  description="Here is the first volume in George R. R. \
Martin's magnificent cycle of novels that includes A Clash of Kings and \
A Storm of Swords. As a whole, this series comprises a genuine masterpiece \
of modern fantasy, bringing together the best the genre has to offer. Magic, \
mystery, intrigue, romance, and adventure fill these pages and transport us \
to a world unlike any we have ever experienced. Already hailed as a classic, \
George R. R. Martin's stunning series is destined to stand as one of the \
great achievements of imaginative fiction.",
                  category=categories[3],
                  user=users[1]))
books.append(Book(name="The Name of the Wind",
                  author="Patrick Rothfuss",
                  description="Told in Kvothe's own voice, this is the tale \
of the magically gifted young man who grows to be the most notorious wizard \
his \
world has ever seen. The intimate narrative of his childhood in a troupe of \
traveling players, his years spent as a near-feral orphan in a crime-ridden \
city, his daringly brazen yet successful bid to enter a legendary school of \
magic, and his life as a fugitive after the murder of a king form a gripping \
coming-of-age story unrivaled in recent literature.",
                  category=categories[3],
                  user=users[2]))

# History
books.append(Book(name="Guns, Germs, and Steel",
                  author="Jared Diamond",
                  description="In this artful, informative, and delightful \
(William H. McNeill, New York Review of Books) book, Jared Diamond \
convincingly argues that geographical and environmental factors shaped \
the modern world. \
Societies that had a head start in food production advanced beyond the \
hunter-gatherer stage, and then developed writing, technology, government, \
and organized religion-as well as nasty germs and potent weapons of war-and \
adventured on sea and land to conquer and decimate preliterate cultures. A \
major advance in our understanding of human societies, Guns, Germs, and Steel \
chronicles the way that the modern world came to be and stunningly dismantles \
racially based theories of human history.",
                  category=categories[4],
                  user=users[0]))
books.append(Book(name="The Diary of a Young Girl",
                  author="Anne Frank",
                  description="Discovered in the attic in which she spent the \
last years of her life, Anne Frank's remarkable diary has become a world \
classic-a powerful reminder of the horrors of war and an eloquent testament \
to the human spirit.",
                  category=categories[4],
                  user=users[1]))
books.append(Book(name="1776",
                  author="David McCullough",
                  description="In this masterful book, David McCullough tells \
the intensely human story of those who marched with General George Washington \
in the year of the Declaration of Independence, when the whole American cause \
was riding on their success, without which all hope for independence would \
have been dashed and the noble ideals of the Declaration would have amounted \
to little more than words on paper.",
                  category=categories[4],
                  user=users[2]))

# Horror
books.append(Book(name="The Shining",
                  author="Stephen King",
                  description="Jack Torrance's new job at the Overlook Hotel \
is the perfect chance for a fresh start. As the off-season caretaker at the \
atmospheric old hotel, he'll have plenty of time to spend reconnecting with \
his family and working on his writing. But as the harsh winter weather sets \
in, the idyllic location feels ever more remote...and more sinister. And the \
only one to notice the strange and terrible forces gathering around the \
Overlook is Danny Torrance, a uniquely gifted five-year-old.",
                  category=categories[5],
                  user=users[0]))
books.append(Book(name="Dracula",
                  author="Bram Stoker",
                  description="Jonathan Harker is travelling to Castle \
Dracula \
to see the Transylvanian noble, Count Dracula. He is begged by locals not to \
go there, because on the eve of St George's Day, when the clock strikes \
midnight, all the evil things in the world will come full sway. But business \
must be done, so Jonathan makes his way to the Castle - and then his \
nightmare begins. His beloved wife Meena and other lost souls have fallen \
under the Count's horrifying spell. Dracula must be destroyed...",
                  category=categories[5],
                  user=users[1]))
books.append(Book(name="Interview with the Vampire",
                  author="Anne Rice",
                  description="This is the story of Louis, as told in his own \
words, of his journey through mortal and immortal life. Louis recounts how \
he became a vampire at the hands of the radiant and sinister Lestat and \
how he became indoctrinated, unwillingly, into the vampire way of life. His \
story ebbs and flows through the streets of New Orleans, defining crucial \
moments such as his discovery of the exquisite lost young child Claudia, \
wanting not to hurt but to comfort her with the last breathsof humanity he \
has inside.",
                  category=categories[5],
                  user=users[2]))

# Mysteries
books.append(Book(name="And Then There Were None",
                  author="Agatha Christie",
                  description="First, there were ten-a curious assortment \
of strangers summoned as weekend guests to a private island off the coast \
of Devon. Their host, an eccentric millionaire unknown to all of them, is \
nowhere to be found. All that the guests have in common is a wicked past \
they're unwilling to reveal-and a secret that will seal their fate. For \
each has been marked for murder. One by one they fall prey. Before the \
weekend is out, there will be none. And only the dead are above suspicion.",
                  category=categories[6],
                  user=users[0]))
books.append(Book(name="Girl with the Dragon Tattoo",
                  author="Stieg Larsson",
                  description="An international publishing sensation, Stieg \
Larsson's The Girl with the Dragon Tattoo combines murder mystery, family \
saga, love story, and financial intrigue into one satisfyingly complex and \
entertainingly atmospheric novel.",
                  category=categories[6],
                  user=users[1]))
books.append(Book(name="Gone Girl",
                  author="Gillian Flynn",
                  description="One of the most critically acclaimed suspense \
writers of our time, New York Times bestseller Gillian Flynn takes that \
statement to its darkest place in this unputdownable masterpiece about a \
marriage gone terribly, terribly wrong. The Chicago Tribune proclaimed that \
her work draws you in and keeps you reading with the force of a pure but \
nasty addiction. Gone Girl's toxic mix of sharp-edged wit and deliciously \
chilling prose creates a nerve-fraying thriller that confounds you at \
every turn.",
                  category=categories[6],
                  user=users[2]))

# Romance
books.append(Book(name="False Step",
                  author="Victoria Helen Stone",
                  description="Stay calm, keep smiling, and watch your step. \
In this marriage of secrets and lies, nothing is what it seems.",
                  category=categories[7],
                  user=users[0]))
books.append(Book(name="The Notebook",
                  author="Nicholas Sparks",
                  description="Set amid the austere beauty of the North \
Carolina coast, The Notebook begins with the story of Noah Calhoun, a rural \
Southerner recently returned from the Second World War. Noah is restoring a \
plantation home to its former glory, and he is haunted by images of the \
beautiful girl he met fourteen years earlier, a girl he loved like no \
other. Unable to find her, yet unwilling to forget the summer they spent \
together, Noah is content to live with only memories...until she \
unexpectedly returns to his town to see him once again.",
                  category=categories[7],
                  user=users[1]))
books.append(Book(name="The Time Traveler's Wife",
                  author="Audrey Niffenegger",
                  description="A funny, often poignant tale of boy meets \
girl with a twist: what if one of them couldn't stop slipping in and out of \
time? Highly original and imaginative, this debut novel raises questions \
about life, love, and the effects of time on relationships.",
                  category=categories[7],
                  user=users[2]))

# Teen
books.append(Book(name="The Hunger Games",
                  author="Suzanne Collins",
                  description="Could you survive on your own, in the wild, \
with everyone out to make sure you don't live to see the morning?",
                  category=categories[8],
                  user=users[0]))
books.append(Book(name="Divergent",
                  author="Veronica Roth",
                  description="In a world divided by factions based on \
virtues, \
Tris learns she's Divergent and won't fit in. When she discovers a plot to \
destroy Divergents, Tris and the mysterious Four must find out what makes \
Divergents dangerous before it's too late.",
                  category=categories[8],
                  user=users[1]))
books.append(Book(name="Twilight",
                  author="Stephenie Meyer",
                  description="In the first book of the Twilight Saga, \
internationally bestselling author Stephenie Meyer introduces Bella Swan \
and Edward Cullen, a pair of star-crossed lovers whose forbidden \
relationship ripens against the backdrop of small-town suspicion and \
a mysterious coven of vampires. This is a love story with bite.",
                  category=categories[8],
                  user=users[2]))

seedDB()
