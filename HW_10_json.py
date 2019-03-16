import json
from operator import itemgetter

python_books = """
   [
        {
            "title": "How to Make Mistakes in Python",
            "author": "Mike Pirnat",
            "authorUrl": "http://mike.pirnat.com/",
            "level": "Intermediate",
            "info": "Even the best programmers make mistakes. In this O’Reilly report, Mike Pirnat dissects some of his most memorable blunders, peeling them back layer-by-layer to reveal just what went wrong.",
            "url": "http://www.oreilly.com/programming/free/files/how-to-make-mistakes-in-python.pdf",
            "cover": "img/cover_how_to_make_mistakes_in_python.gif"
        },
        {
            "title": "Functional Programming in Python",
            "author": "David Mertz",
            "authorUrl": "http://www.oreilly.com/programming/free/functional-programming-python.csp",
            "level": "Intermediate",
            "info": "In this paper, David Mertz, a director of Python Software Foundation, examines the functional aspects of the language and points out which options work well and which ones you should generally decline.",
            "url": "http://www.oreilly.com/programming/free/files/functional-programming-python.pdf",
            "cover": "img/cover_functional_programming_in_python.gif"
        },
        {
            "title": "Picking a Python Version: A Manifesto",
            "author": "David Mertz",
            "authorUrl": "http://www.oreilly.com/programming/free/from-future-import-python.csp",
            "level": "Beginner",
            "info": "This report guides you through the implicit decision tree of choosing what Python version, implementation, and distribution is best suited for you.",
            "url": "http://www.oreilly.com/programming/free/files/from-future-import-python.pdf",
            "cover": "img/cover_picking_python_version_manifesto.gif"
        },
        {
            "title": "Python para Desenvolvedores (2nd Edition)",
            "author": "Luiz Eduardo Borges",
            "authorUrl": "http://ark4n.wordpress.com/python/",
            "level": "Intermediate",
            "info": "[PORTUGUESE] Este livro aborda assuntos que incluem: criação de interfaces com usuário, computação gráfica, aplicações para internet, sistemas distribuídos, entre outros.",
            "url": "http://ark4n.files.wordpress.com/2010/01/python_para_desenvolvedores_2ed.pdf",
            "cover": "img/cover_pypd_2ed_th.jpg"
        },
        {
            "title": "Intermediate Python",
            "author": "Muhammad Yasoob",
            "authorUrl": "http://pythontips.com/",
            "level": "Intermediate",
            "info": "Python is an amazing language with a strong and friendly community of programmers. However, there is a lack of documentation on what to learn after getting the basics of Python down your throat. Through this book I aim to solve this problem. I would give you bits of information about some interesting topics which you can further explore.  The topics which are discussed in this book open up your mind towards some nice corners of Python language. This book is an outcome of my desire to have something like this when I was beginning to learn Python.",
            "url": "https://media.readthedocs.org/pdf/intermediatepythongithubio/latest/intermediatepythongithubio.pdf",
            "cover": "img/cover_IntermediatePython_Yasoob2.jpg"
        },
        {
            "title": "How to Think Like a Computer Scientist: Second Interactive Edition",
            "author": "B. Miller & D. Ranum",
            "authorUrl": "http://reputablejournal.com",
            "level": "Beginner",
            "info": "This interactive book teaches you Python the interactive way, right in the browser.",
            "url": "http://interactivepython.org/runestone/static/thinkcspy/index.html",
            "cover": "img/runestone.png"
        },
        {
            "title": "How to Think Like a Computer Scientist: Learning with Python 2nd Ed.",
            "author": "Jeffrey Elkner...",
            "authorUrl": "http://greenteapress.com/",
            "level": "Beginner",
            "info": "This book teaches you Python right in the browser.",
            "url": "http://www.openbookproject.net/thinkcs/python/english2e/",
            "cover": "img/gasp_lessons.png"
        },
        {
            "title": "Problem Solving with Algorithms and Data Structures Using Python",
            "author": "B. Miller & D. Ranum",
            "authorUrl": "http://reputablejournal.com/",
            "level": "Intermediate",
            "info": "This book is a CS2 data structures textbook, with a review of Python concepts in chapter 1",
            "url": "http://interactivepython.org/runestone/static/pythonds/index.html",
            "cover": "img/PythonDScover.png"
        },
        {
            "title": "Learn Python The Hard Way",
            "author": "Zed A. Shaw",
            "authorUrl": "http://learnpythonthehardway.org/",
            "level": "Beginner",
            "info": "Have you always wanted to learn how to code but never thought you could? Do you want to challenge your brain in a new way? ",
            "url": "http://learnpythonthehardway.org/book",
            "cover": "img/cover_learnpython.jpg"
        },
        {
            "title": "Dive into Python (2004)",
            "author": "Mark Pilgrim",
            "authorUrl": "http://getpython3.com/diveintopython3/",
            "level": "Intermediate",
            "info": "Dive Into Python is a free Python book (from 2004) for experienced programmers. It covers many basics of the language",
            "url": "http://www.diveintopython.net/download/diveintopython-pdf-5.4.zip",
            "cover": "img/cover_divepython.jpg"
        },
        {
            "title": "Dive into Python 3",
            "author": "Mark Pilgrim",
            "authorUrl": "http://getpython3.com/diveintopython3/",
            "level": "Intermediate",
            "info": "Dive Into Python 3 covers what's new in Python 3 and how its differs from Python 2.",
            "url": "https://github.com/downloads/diveintomark/diveintopython3/dive-into-python3.pdf",
            "cover": "img/cover_divepython3.jpg"
        },
        {
            "title": "Think Python",
            "author": "Allen B. Downey",
            "authorUrl": "http://www.greenteapress.com/",
            "level": "Beginner",
            "info": "A very exhaustive book covering most of the language features, from datatypes to OOP and debugging.",
            "url": "http://www.greenteapress.com/thinkpython/thinkpython.pdf",
            "cover": "img/cover_thinkpython.jpg"
        },
        {
            "title": "Kivy programming Guide",
            "author": "Kivy",
            "authorUrl": "http://kivy.org/",
            "level": "Intermediate",
            "info": "Discover Kivy the multitouch Python framework for desktop and mobile, and learn how to create a simple game.",
            "url": "https://readthedocs.org/projects/kivy/downloads/",
            "cover": "img/cover_kivy.png"
        },
        {
            "title": "Django Tutorial",
            "author": "Community",
            "authorUrl": "https://docs.djangoproject.com/en/dev/intro/",
            "level": "Intermediate",
            "info": "With this hands-on tutorial, discover Django the popular high-level Python Web framework that encourages rapid development and clean, pragmatic design.",
            "url": "https://media.readthedocs.org/pdf/django/latest/django.pdf",
            "cover": "img/cover_django.png"
        },
        {
            "title": "Pyramid for Humans",
            "author": "Community",
            "authorUrl": "http://pyramid.readthedocs.org/en/latest/index.html",
            "level": "Intermediate",
            "info": "With this tutorial, discover Pyramid a Python web application development framework. Its primary goal is to make it easier for a Python developer to create web applications.",
            "url": "docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/index.html",
            "cover": "img/cover_pyramid.png"
        },
        {
            "title": "Flask microframework",
            "author": "Armin Ronacher",
            "authorUrl": "http://lucumr.pocoo.org/",
            "level": "Intermediate",
            "info": "Learn the Flask web microframework by example. Flask aims to keep the core simple but extensible and gives you freedom to choose the libraries of your choice.",
            "url": "http://flask.pocoo.org/docs/tutorial/",
            "cover": "img/cover_flask.png"
        },
        {
            "title": "Making games with Python and Pygame",
            "author": "Al Sweigart",
            "authorUrl": "http://inventwithpython.com",
            "level": "Intermediate",
            "info": "Making Games with Python & Pygame” covers the Pygame library with the source code for 11 games.",
            "url": "http://inventwithpython.com/pygame/chapters/",
            "cover": "img/cover_makinggame.png"
        },
        {
            "title": "High Performance Python tutorial",
            "author": "Ian Ozsvald",
            "authorUrl": "http://ianozsvald.com/2011/07/25/high-performance-python-tutorial-v0-2-from-europython-2011",
            "level": "Advanced",
            "info": "In this 55 pages tutorial, Ian Ozsvald shows you a number of techniques to get a 10-500 performance increase in your Python apps, from profiling, to PyPy, numPy, Multiprocessing...",
            "url": "http://ianozsvald.com/HighPerformancePythonfromTrainingatEuroPython2011_v0.2.pdf",
            "cover": "img/cover_highperf.png"
        },
        {
            "title": "A byte of Python",
            "author": "Swaroop C H",
            "authorUrl": "http://www.swaroopch.org/",
            "level": "Beginner",
            "info": "This book aims to help you learn the wonderful Python language and show how to get things done quickly and painlessly - in effect 'The Perfect Anti-venom to your programming problems'.",
            "url": "http://files.swaroopch.com/python/byte_of_python.pdf",
            "cover": "img/cover_swaroop.png"
        },
        {
            "title": "Python 101 - Introduction to Python",
            "author": "Dave Kuhlman",
            "authorUrl": "http://www.rexx.com/~dkuhlman",
            "level": "Beginner",
            "info": "This document is a syllabus for a first course in Python programming. This course contains an introduction to the Python language, instruction in the important and commonly used features of the language, and practical excercises in the use of those features.",
            "url": "http://www.davekuhlman.org/python_101.html",
            "cover": "img/cover_python101.png"
        },
        {
            "title": "The Standard Python Library",
            "author": "Fredrik Lundh",
            "authorUrl": "http://effbot.org/zone/",
            "level": "Intermediate",
            "info": "This book provides a brief description of each module of the +200 Python standard library and usage examples",
            "url": "http://effbot.org/zone/librarybook-index.htm",
            "cover": "img/cover_pythonstandardlibrairy.png"
        },
        {
            "title": "Snake Wrangling for Kids",
            "author": "Jason R. Briggs",
            "authorUrl": "http://jasonrbriggs.com",
            "level": "Beginner",
            "info": "[DOWNLOAD REQUIRED] For children 8 years and older, who would like to learn computer programming. It covers the very basics of programming, and uses the Python programming language to teach the concepts.",
            "url": "http://www.briggs.net.nz/snake-wrangling-for-kids.html",
            "cover": "img/cover_snakewrangling.png"
        },
        {
            "title": "Programming Computer Vision with Python",
            "author": "Jan Erik Solem",
            "authorUrl": "http://www.janeriksolem.net/",
            "level": "Advanced",
            "info": "[PDF DRAFT] This book gives an entry point to hands-on computer vision (images, videos...) with enough understanding of the underlying theory and algorithms.",
            "url": "http://programmingcomputervision.com/downloads/ProgrammingComputerVision_CCdraft.pdf",
            "cover": "img/cover_computervision.jpg"
        },
        {
            "title": "Natural Language Processing with Python",
            "author": "S. Bird, E. Klein...",
            "authorUrl": "http://www.nltk.org/",
            "level": "Advanced",
            "info": "Practical introduction to programming for language processing, written by the creators of NLTK.",
            "url": "http://www.nltk.org/book/",
            "cover": "img/cover_nltk.jpg"
        },
        {
            "title": "Think Complexity",
            "author": "Allen B. Downey",
            "authorUrl": "http://www.greenteapress.com/",
            "level": "Advanced",
            "info": "This book is about complexity science, data structures and algorithms, intermediate programming in Python, and the philosophy of science.",
            "url": "http://www.greenteapress.com/complexity/thinkcomplexity.pdf",
            "cover": "img/cover_complexity.jpg"
        },
        {
            "title": "Think Stats",
            "author": "Allen B. Downey",
            "authorUrl": "http://www.greenteapress.com/",
            "level": "Advanced",
            "info": "Think Stats is an introduction to Probability and Statistics for Python programmers.",
            "url": "http://greenteapress.com/thinkstats/thinkstats.pdf",
            "cover": "img/cover_stats.jpg"
        },
        {
            "title": "Think Stats 2e",
            "author": "Allen B. Downey",
            "authorUrl": "http://www.greenteapress.com/",
            "level": "Advanced",
            "info": "Think Stats is an introduction to Probability and Statistics for Python programmers.",
            "url": "http://greenteapress.com/thinkstats2/thinkstats2.pdf",
            "cover": "img/cover_stats.jpg"
        },
        {
            "title": "Python Module of the week",
            "author": "Doug Hellman",
            "authorUrl": "http://www.doughellmann.com/",
            "level": "Intermediate",
            "info": "The Python Module of the Week series, or PyMOTW, is a tour of the Python standard library through short and concrete examples. It covers more than 50 modules.",
            "url": "https://pymotw.com/2/contents.html",
            "cover": "img/cover_pymotw.png"
        },
        {
            "title": "An introduction to Python",
            "author": "John C. Lusth",
            "authorUrl": "http://lusth.cs.ua.edu/",
            "level": "Beginner",
            "info": "A complete scholar overview of all Python 3 functionnalities from the Alabama University.",
            "url": "http://beastie.cs.ua.edu/cs150/book/index.html",
            "cover": "img/cover_alabamaintro.png"
        },
        {
            "title": "Building skills in Programming",
            "author": "Steven F. Lot",
            "authorUrl": "http://www.itmaybeahack.com",
            "level": "Beginner",
            "info": "How do you learn to program? Through a series of simple exercises that teach programming fundamentals with an easy-to-use, easy-to-learn programming language.",
            "url": "http://www.itmaybeahack.com/homepage/books/nonprog/html/index.html",
            "cover": "img/cover_buildingskillnonpro.jpg"
        },
        {
            "title": "Building skills in Python",
            "author": "Steven F. Lot ",
            "authorUrl": "http://www.itmaybeahack.com",
            "level": "Beginner",
            "info": "This 450+ page book has 42 chapters that will help you build Python programming skills through a series of exercises. This book includes six projects from straight-forward to sophisticated that will help solidify your Python skills.",
            "url": "http://www.itmaybeahack.com/book/python-2.6/html/index.html",
            "cover": "img/cover_buildingskillspython.jpg"
        },
        {
            "title": "Building skills in OOP",
            "author": "Steven F. Lot ",
            "authorUrl": "http://homepage.mac.com/s_lott/",
            "level": "Intermediate",
            "info": "How do you move from OO programming to OO design? This 301-page book has 49 chapters that will help you build OO design skills through the creation of a moderately complex family of application programs.",
            "url": "http://www.itmaybeahack.com/book/oodesign-python-2.1/html/index.html",
            "cover": "img/cover_buildingskillsoop.jpg"
        },
        {
            "title": "Python Scientific lecture notes",
            "author": "By The Community",
            "authorUrl": "http://scipy-lectures.github.com/AUTHORS.html",
            "level": "Intermediate",
            "info": "Teaching material on the scientific Python ecosystem, a quick introduction to central tools and techniques. The different chapters each correspond to a 1 to 2 hours course with increasing level of expertise, from beginner to expert.",
            "url": "http://scipy-lectures.github.com/",
            "cover": "img/cover_scientific.jpg"
        },
        {
            "title": "Programmez avec Python 2",
            "author": "Gérard Swinnen",
            "authorUrl": "http://inforef.be/swi/python.htm",
            "level": "Beginner",
            "info": "[FRENCH] Apprenez à programmer avec Python 2. Découvrez la programmation et le language Python grâce à cet ouvrage de référence.",
            "url": "http://inforef.be/swi/download/apprendre_python.pdf",
            "cover": "img/cover_apprendrepython2.jpg"
        },
        {
            "title": "Programmez avec Python 3",
            "author": "Gérard Swinnen",
            "authorUrl": "http://inforef.be/swi/python.htm",
            "level": "Beginner",
            "info": "[FRENCH] Apprenez à programmer avec Python 3. Mise à jour du précédent ouvrage avec les spécificité de Python 3.",
            "url": "http://inforef.be/swi/download/apprendre_python3_5.pdf",
            "cover": "img/cover_apprendrepython3.jpg"
        },
        {
            "title": "Python for you and me",
            "author": "Kushal Das",
            "authorUrl": "http://kushaldas.in",
            "level": "Beginner",
            "info": "A book for the total new comers into Python world. Was started as book for students before they read Python tutorial.",
            "url": "http://pymbook.readthedocs.io/en/latest/",
            "cover": "img/pym.png"
        },
        {
            "title": "Python course",
            "author": "Patrick Fuchs",
            "authorUrl": "http://www.dsimb.inserm.fr/~fuchs/",
            "level": "Beginner",
            "info": "[FRENCH] Beginner and progressive course about Python theory and concepts",
            "url": "http://www.dsimb.inserm.fr/~fuchs/python/cours_python.pdf",
            "cover": "img/cover_python101.png"
        },
        {
            "title": "Data Structures and Algorithms with Object-Oriented Design Patterns in Python",
            "author": "Bruno R. Preiss",
            "authorUrl": "http://www.brpreiss.com",
            "level": "Intermediate",
            "info": "This book is about the fundamentals of data structures and algorithms. It uses object oriented design patterns and teaches topics like stacks, queues, lists, hashing and graphs. There are also versions for other programming languages.",
            "url": "http://www.brpreiss.com/books/opus7/html/book.html",
            "cover": "img/cover_datastructandalg.png"
        },
        {
            "title": "A bit of Python & other things.",
            "author": "Jesse Noller",
            "authorUrl": "http://jessenoller.com/",
            "level": "Beginner",
            "info": "A usefull page with good links to read about Python",
            "url": "http://jessenoller.com/good-to-great-python-reads/",
            "cover": "img/cover_jessenoller.png"
        },
        {
            "title": "Python Course",
            "author": "Google",
            "authorUrl": "http://developers.google.com",
            "level": "Beginner",
            "info": "This is a free class for people with a little bit of programming experience who want to learn Python.",
            "url": "https://developers.google.com/edu/python/",
            "cover": "img/cover_googledevelopers.png"
        },
        {
            "title": "Porting to Python 3: An in-depth guide",
            "author": "Lennart Regebro",
            "authorUrl": "http://regebro.wordpress.com/",
            "level": "Intermediate",
            "info": "This book guides you through the process of porting your Python 2 code to Python 3, from choosing a porting strategy to solving your distribution issues. Using plenty of code examples is takes you cross the hurdles and shows you the new Python features.",
            "url": "http://python3porting.com/pdfs/SupportingPython3-screen-1.0-latest.pdf",
            "cover": "img/cover_porting_python3.png"
        },
        {
            "title": "Non-Programmer's Tutorial for Python 3",
            "author": "Josh Cogliati and others",
            "authorUrl": "http://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3",
            "level": "Beginner",
            "info": "The Non-Programmers' Tutorial For Python 3 is a tutorial designed to be an introduction to the Python programming language. This guide is for someone with no programming experience.",
            "url": "http://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3",
            "cover": "img/Python3-powered.png"
        },
        {
            "title": "The Hitchhiker’s Guide to Python!",
            "author": "Kenneth Reitz",
            "authorUrl": "http://kennethreitz.com/",
            "level": "Beginner",
            "info": "This opinionated guide exists to provide both novice and expert Python developers a best-practice handbook to the installation, configuration, and usage of Python on a daily basis.",
            "url": "https://media.readthedocs.org/pdf/python-guide/latest/python-guide.pdf",
            "cover": "img/PythonGuide.png"
        },
        {
            "title": "Probabilistic Programming and Bayesian Methods for Hackers: Using Python and PyMC",
            "author": "Cam Davidson-Pilon",
            "authorUrl": "http://www.camdp.com",
            "level": "Intermediate",
            "info": "aka 'Bayesian Methods for Hackers': An introduction to Bayesian methods + probabilistic programming in data analysis with a computation/understanding-first, mathematics-second point of view. All in pure Python ;)",
            "url": "http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/",
            "cover": "img/BMH.png"
        },
        {
            "title": "web2py Complete Manual",
            "author": "Massimo Di Pierro",
            "authorUrl": "http://web2py.com",
            "level": "Intermediate",
            "info": "As you will learn in the following pages, web2py tries to lower the barrier of entry to web development by focusing on three main goals: ease of use, rapid development and security",
            "url": "https://dl.dropboxusercontent.com/u/18065445/web2py/web2py_manual_5th.pdf",
            "cover": "img/web2py.png"
        },
        {
            "title": "Hacking Secret Ciphers with Python",
            "author": "Al Sweigart",
            "authorUrl": "http://coffeeghost.net",
            "level": "Beginner",
            "info": "The book teaches complete beginners how to program in the Python programming language. The reader not only learns about several classical ciphers, but also how to write programs that encrypt and hack these ciphers.",
            "url": "http://inventwithpython.com/hackingciphers.pdf",
            "cover": "img/hackingcyphers.png"
        },
        {
            "title": "Modeling Creativity",
            "author": "Tom De Smedt",
            "authorUrl": "http://www.organisms.be/",
            "level": "Intermediate",
            "info": "Case studies in Python - using the libraries nodebox and pattern the author creates wonderful fractals and infographics; python code snippets included",
            "url": "http://www.clips.ua.ac.be/sites/default/files/modeling-creativity.pdf",
            "cover": "img/modelingcreativity.png"
        },
        {
            "title": "Test-Driven Development with Python",
            "author": "Harry Percival",
            "authorUrl": "http://www.oreillynet.com/pub/au/5721",
            "level": "Intermediate",
            "info": "This book uses a concrete example—the development of a website, from scratch—to teach the TDD metholology, and how it applies to web programming, from the basics of database integration and javascript, going via browser-automation tools like Selenium, to advanced (and trendy) topics like NoSQL, websockets and Async programming.",
            "url": "http://chimera.labs.oreilly.com/books/1234000000754/index.html",
            "cover": "img/testdriven.jpg"
        },
        {
            "title": "Getting Started with Django",
            "author": "Kenneth Love",
            "authorUrl": "http://brack3t.com/",
            "level": "Beginner",
            "info": "Getting Started with Django (or GSWD) is a series of video-based lessons meant to take you from novice to competent [1], or maybe even beyond.",
            "url": "http://gettingstartedwithdjango.com/",
            "cover": "img/cover_gettingstartedwithdjango.jpg"
        },
        {
            "title": "Python 3x Programming (sample)",
            "author": "Jody S. Ginther",
            "authorUrl": "http://www.toonzcat.com/book.html",
            "level": "Beginner",
            "info": "(4 free chapters) Python 3x Programming, Made Fun and Easier by Jody S. Ginther is for the beginning programmer who wants to learn visually and have some fun while learning programming. The full course will take the beginner from ground zero to making their own arcade style game complete with; music, sound, graphics, and how to make a distribution package to share it with your friends in 21 lessons.",
            "url": " http://www.toonzcat.com/media/pythonfree.pdf",
            "cover": "img/py3programming.png"
        },
        {
            "title": "Djen of Django",
            "author": "Agiliq",
            "authorUrl": "http://agiliq.com/",
            "level": "Intermediate",
            "info": "Djen of Django is a book consisting of a series of small Django projects based on small real-world examples. For instance, building a Pastebin, a Blog or a Project Management Application. Djen of Django focuses on teaching the reader Django best practices through the use of real-world examples.",
            "url": "http://agiliq.com/books/djenofdjango/",
            "cover": "img/djenofdjango.jpg"
        },
        {
            "title": "Python para todos",
            "author": "Raúl González Duque",
            "authorUrl": "http://mundogeek.net/",
            "level": "Beginner",
            "info": "[SPANISH] Libro sobre programación en Python a modo de tutorial, adecuado para todos los niveles de aprendizaje, desde novatos hasta expertos que quieren conocer más sobre Python.",
            "url": "http://edge.launchpad.net/improve-python-spanish-doc/0.4/0.4.0/+download/Python%20para%20todos.pdf",
            "cover": "img/tutorial-python.jpg"
        },
        {
            "title": "Python in Hydrology",
            "author": "Sat Kumar Tomer",
            "authorUrl": "http://civil.iisc.ernet.in/~satkumar/",
            "level": "Beginner",
            "info": "Python in Hydrology is written for learning Python using its applications in hydrology. The book covers the basic applications of hydrology, and also the advanced topic like use of copula.",
            "url": "http://www.greenteapress.com/pythonhydro/pythonhydro.pdf",
            "cover": "img/cover_python_in_hydrology.png"
        },
        {
            "title": "A Programmer's Guide to Data Mining",
            "author": "Ron Zacharski",
            "authorUrl": "http://zacharski.org/",
            "level": "Intermediate",
            "info": "A guide to practical data mining, collective intelligence, and building recommendation systems.",
            "url": "http://guidetodatamining.com/assets/guideChapters/Guide2DataMining.pdf",
            "cover": "img/cover_guidetodatamining.png"
        },
        {
            "title": "Invent Your Own Computer Games with Python",
            "author": "Al Sweigart",
            "authorUrl": "http://coffeeghost.net",
            "level": "Intermediate",
            "info": "Small and nice python game examples",
            "url": "http://inventwithpython.com/chapters/",
            "cover": "img/cover_inventgame.jpg"
        },
        {
            "title": "Biopython",
            "author": "Various authors",
            "authorUrl": "http://biopython.org/wiki/Main_Page",
            "level": "Intermediate",
            "info": "This is a tutorial and cookbook for Biopython (Biopython is a set of freely available toos for biological computations.",
            "url": "http://biopython.org/DIST/docs/tutorial/Tutorial.pdf",
            "cover": "img/cover_biopython.jpg"
        },
        {
            "title": "Text Processing in Python",
            "author": "David Mertz",
            "authorUrl": "http://gnosis.cx/TPiP/",
            "level": "Intermediate",
            "info": "This is an example-driven, hands on tutorial that carefully teaches programmers how to accomplish numerous text processing tasks using Python.",
            "url": "http://gnosis.cx/TPiP/",
            "cover": "img/cover_text_processing_in_python.jpg"
        },
        {
            "title": "How to Tango with Django",
            "author": "Leif Azzopardi",
            "authorUrl": "http://leifos.me",
            "level": "Beginner",
            "info": "A beginner's guide to web development with Django 1.7. This book has been designed to get you going fast and to learn by example. You'll learn the key aspects of the Python Django Framework by developing an application called Rango.",
            "url": "http://www.tangowithdjango.com/book17/",
            "cover": "img/cover_tangowithdjango.jpg"
        },
        {
            "title": "Python Practice Book",
            "author": "Anand Chitipothu.",
            "authorUrl": "http://anandology.com/",
            "level": "Beginner",
            "info": "This book is prepared from the training notes of Anand Chitipothu. Anand conducts Python trainings classes on a semi-regular basis in Bangalore, India.",
            "url": "http://anandology.com/python-practice-book/index.html",
            "cover": "img/cover_python_practice_book.png"
        },
        {
            "title": "Python Cookbook, Third Edition",
            "author": "Various authors",
            "authorUrl": "http://chimera.labs.oreilly.com/books/1230000000393",
            "level": "Intermediate",
            "info": "This book is aimed at more experienced Python programmers who are looking to deepen their understanding of the language and modern programming idioms.",
            "url": "http://chimera.labs.oreilly.com/books/1230000000393/index.html",
            "cover": "img/cover_python_cookbook.jpg"
        },
        {
            "title": "Explore Flask",
            "author": "Robert Picard.",
            "authorUrl": "http://robert.io",
            "level": "Intermediate",
            "info": "This book is a collection of the best practices for using Flask. There are a lot of pieces to the average Flask application.",
            "url": "http://exploreflask.com",
            "cover": "img/exploreflask.png"
        },
        {
            "title": "Django Girls Tutorial",
            "author": "Community",
            "authorUrl": "https://djangogirls.org/",
            "level": "Beginner",
            "info": "It's a very beginner-friendly tutorial with introductions to the command line, Python, Django, HTML and CSS. ",
            "url": "https://www.gitbook.com/download/pdf/book/djangogirls/djangogirls-tutorial?lang=en",
            "cover": "img/cover_djangogirls_tutorial.jpg"
        },
        {
            "title": "Algorithmic Problem Solving with Python",
            "author": "John B. Schneider...",
            "authorUrl": "http://www.eecs.wsu.edu/~schneidj/",
            "level": "Beginner",
            "info": "Python's syntax and idioms are much easier to learn than those of most other full-featured languages. This book uses programming language Python to introduce folks to programming and algorithmic thinking.",
            "url": "http://www.eecs.wsu.edu/~schneidj/PyBook/swan.pdf",
            "cover": "img/algo_ps_python.png"
        },
        {
            "title": "Make Games with Python",
            "author": "Sean M. Tracey",
            "authorUrl": "http://sean.mtracey.org/",
            "level": "Beginner",
            "info": "In this book, we are going to learn to make games on the Raspberry Pi with Pygame. We'll look at drawing, animation, keyboard and mouse controls, sound, and physics. This book isn't for absolute programming beginners, but it's not far from it.",
            "url": "https://www.raspberrypi.org/magpi-issues/Essentials_Games_v1.pdf",
            "cover": "img/make_games_with_python.png"
        },
        {
            "title": "Automate the Boring Stuff with Python ",
            "author": "Al Sweigart",
            "authorUrl": "http://inventwithpython.com/blog/author/admin/",
            "level": "Intermediate",
            "info": "Learn how to use Python to write programs that do in minutes what would take you hours to do by hand -- no prior programming experience required. Once you've mastered the basics of programming, you'll create Python programs that effortlessly perform useful and impressive feats of automation.",
            "url": "https://automatetheboringstuff.com/",
            "cover": "img/automate_cover_medium.png"
        },
        {
            "title": "High Performance Python",
            "author": "Ian Ozsvald",
            "authorUrl": "http://ianozsvald.com/",
            "level": "Intermediate",
            "info": "By exploring the fundamental theory behind design choices, this practical guide helps you gain a deeper understanding of Python's implementation. You'll learn how to locate performance bottlenecks and significantly speed up your code in high-data-volume programs.",
            "url": "http://ianozsvald.com/HighPerformancePythonfromTrainingatEuroPython2011_v0.2.pdf",
            "cover": "img/cover_highperf.png"
        },
        {
            "title": "Full Stack Python",
            "author": "Matt Makai",
            "authorUrl": "http://www.mattmakai.com/",
            "level": "Intermediate",
            "info": "You're knee deep in learning the Python programming language. The syntax is starting to make sense. Now you want to take your knowledge and make something real. This book explains each Python web application stack layer and provides the resources.",
            "url": "http://www.fullstackpython.com/table-of-contents.html",
            "cover": "img/fullstackpython.jpg"
        },
        {
            "title": "What You Need to Know about Python",
            "author": "Pierluigi Riti",
            "authorUrl": "https://www.packtpub.com/packt/free-ebook/what-you-need-know-about-python2",
            "level": "Beginner",
            "info": "The absolute essentials you need to know to get Python up and running",
            "url": "https://www.packtpub.com/packt/free-ebook/what-you-need-know-about-python2",
            "cover": "img/What_You_Need_to_Know_about_Python.jpg"
        },
        {
            "title": "Learning Python",
            "author": "Fabrizio Romano",
            "authorUrl": "https://www.packtpub.com/packt/free-ebook/learning-python",
            "level": "Intermediate",
            "info": "Learn to code like a professional with Python – an open source, versatile, and powerful programming language",
            "url": "https://www.packtpub.com/packt/free-ebook/learning-python",
            "cover": "img/Learning_Python.png"
        },
        {
            "title": "What You Need to Know about Machine Learning",
            "author": "Gabriel A. Cánepa",
            "authorUrl": "https://www.packtpub.com/packt/free-ebook/what-you-need-know-about-machine-learning2",
            "level": "Intermediate",
            "info": "This book lays the foundation for your work in the world of Machine Learning, providing the basic understanding, knowledge, and skills that you can build on with experience and time",
            "url": "https://www.packtpub.com/packt/free-ebook/what-you-need-know-about-machine-learning2",
            "cover": "img/What_You_Need_to_Know_about_Machine_Learning.jpg"
        },
        {
            "title": "Building Machine Learning Systems with Python",
            "author": "Willi Richert, Luis Pedro Coelho",
            "authorUrl": "https://www.packtpub.com/packt/free-ebook/python-machine-learning-algorithms",
            "level": "Intermediate",
            "info": "Expand your Python knowledge and learn all about machine-learning libraries in this user-friendly manual",
            "url": "https://www.packtpub.com/packt/free-ebook/python-machine-learning-algorithms",
            "cover": "img/Building Machine Learning Systems with Python.jpg"
        },
        {
            "title": "Practical Data Analysis",
            "author": "Hector Cuesta",
            "authorUrl": "https://www.packtpub.com/packt/free-ebook/practical-data-analysis",
            "level": "Intermediate",
            "info": "Transform, model and visualize your data through hands-on projects, developed in open source tools",
            "url": "https://www.packtpub.com/packt/free-ebook/practical-data-analysis",
            "cover": "img/Practical Data Analysis.jpg"
        },
        {
            "title": "Raspberry Pi Cookbook for Python Programmers",
            "author": "Tim Cox",
            "authorUrl": "https://www.packtpub.com/packt/free-ebook/python-raspberry-pi-cookbook",
            "level": "Intermediate",
            "info": "Over 50 tailor-made recipes for programmers to get the most out of Raspberry Pi using Python to unleash its huge potential",
            "url": "https://www.packtpub.com/packt/free-ebook/python-raspberry-pi-cookbook",
            "cover": "img/Raspberry Pi Cookbook for Python Programmers.jpg"
        }  ,
        {
            "title": "Annotated Algorithms In Python",
            "author": "Massimo Di Pierro",
            "authorUrl": "https://twitter.com/mdipierro",
            "level": "Advanced",
            "info": "This book is assembled from lectures given by the author over a period of 10 years at the School of Computing of DePaul University. The lectures cover multiple classes, including Analysis and Design of Algorithms, Scientific Computing, Monte Carlo Simulations, and Parallel Algorithms.",
            "url": "https://raw.githubusercontent.com/mdipierro/nlib/master/docs/book_numerical.pdf",
            "cover": "img/annotated-algorithms.jpg"
        },
        {
            "title": "Python for Everybody",
            "author": "Charles R. Severance",
            "authorUrl": "http://www.dr-chuck.com/",
            "level": "Beginner",
            "info": "The goal of this book is to provide an Informatics-oriented introduction to programming. The primary approach taken in this book is using Python to solve data analysis problems common in the world of Informatics.",
            "url": "https://www.py4e.com/book",
            "cover": "img/cover_python4everybody.jpg"
        },
        {
            "title": "20 Python libraries You Aren't Using (But Should)",
            "author": "Caleb Hattingh",
            "authorUrl": "http://www.oreilly.com/pub/au/6789",
            "level": "Intermediate",
            "info": "The Python ecosystem is vast and far-reaching in both scope and depth. Starting out in this crazy, open-source forest is daunting, and even with years of experience, it still requires continual effort to keep up-to-date with the best libraries and techniques. This report helps you explore some of the lesser known Python libraries and tools, including third-party modules and several extremely useful tools in the standard library that deserve more attention",
            "url": "http://www.oreilly.com/programming/free/20-python-libraries-you-arent-using-but-should.csp",
            "cover": "img/cover_20_python.png"
        },
        {
            "title": "Advanced Machine Learning with Python",
            "author": "John Hearty",
            "authorUrl": "https://www.packtpub.com/packt/free-ebook/advanced-python-machine-learning",
            "level": "Advanced",
            "info": "[registration] Solve challenging data science problems by mastering cutting-edge machine learning techniques in Python",
            "url": "https://www.packtpub.com/packt/free-ebook/advanced-python-machine-learning",
            "cover": "img/Advanced-Machine-Learning-with-Python.jpg"
        }
    ] """

json_python_books = json.loads(python_books)


def filter_books():
    books = []
    for dict in json_python_books:
        for k, v in dict.items():
            if v == "Advanced":
                book = [dict["title"], dict["author"],dict["url"]]
                books.append(book)

    return books

arranged_books = filter_books()
for num, book in enumerate(arranged_books, start = 1):
    print(f"{num}" + "." + " " + book[0] + "\n" + "     " + "[" + book[1] + "]" + "\n" + "     " + book[2])











