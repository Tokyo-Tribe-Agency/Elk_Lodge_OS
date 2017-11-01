import os
from django.core import management
from django.core.management.base import BaseCommand
from django.core.management.commands import makemigrations

class Command(BaseCommand):
    
    

    def handle(self, *args, **options):
        os.system('rm lodge/migrations/*.py;')   #deletes all of the .py files in the migrations directory except for the __init__.py file.
        os.system('touch lodge/migrations/__init__.py;') #re-create the __init__.py file.
        os.system('rm db.sqlite3;')  #deletes the database file.        
