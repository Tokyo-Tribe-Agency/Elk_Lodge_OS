from django.core import management
from django.core.management.base import BaseCommand
from django.core.management.commands import makemigrations
# from blogpost.factories import *


class Command(BaseCommand):
	def handle(self, *args, **options):
        management.call_command('makemigrations')
        management.call_command('migrate')
        