import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    "HOST": '127.0.0.1',
    "PORT": "27017",
    "NAME": "data-mercury-dev",
    "USER": "root",
    "PASSWORD": "root"

}
