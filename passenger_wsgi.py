<<<<<<< HEAD
from src.app import app as aplication
=======
import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

wsgi = imp.load_source('wsgi', 'passenger_wsgi.py')
application = wsgi.application
>>>>>>> f485658d8716eb08bd427955c97863d2ba1b10ac
