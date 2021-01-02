import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


print(BASE_DIR)














from django.db import models



import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()






class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Teacher(Person):
    dimploma = models.CharField(max_length=50)


gumby = Person.get(101)
gumby.last_name = 'ABCDEFG'
gumby.save()
gumby.dogs
["Sheila", "Bobique", ]











