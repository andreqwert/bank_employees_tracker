import os
import argparse

from django.core.management import execute_from_command_line


parser = argparse.ArgumentParser(description='Remote control for employees tracking', add_help=True)
args = parser.parse_args()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
execute_from_command_line('manage.py runserver 0.0.0.0:8000'.split())



