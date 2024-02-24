import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'Waits for the database to be available'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Waiting for the database...'))
        db_conn = None
        retries = 0
        max_retries = 30  # Adjust the number of retries as needed

        while retries < max_retries:
            try:
                db_conn = connections['default']
                db_conn.ensure_connection()
                self.stdout.write(self.style.SUCCESS('Database available!'))
                break
            except OperationalError:
                self.stdout.write(self.style.SUCCESS('Database unavailable, waiting 1 second...'))
                time.sleep(1)
                retries += 1

        if not db_conn:
            self.stdout.write(self.style.ERROR('Unable to connect to the database. Exiting...'))
            raise SystemExit(1)