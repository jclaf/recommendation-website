# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])

import os


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "9U;1_YfaqZOPVjH a5}U/YIa"
