import pytz
from apscheduler.schedulers.background import BlockingScheduler
from django.core.management.base import BaseCommand
from src.dump_database import dump


class Command(BaseCommand):
    help = 'Run blocking scheduler to create periodical tasks'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Preparing scheduler'))
        scheduler = BlockingScheduler(timezone=pytz.UTC)

        scheduler.add_job(dump.send, 'cron', day="*/7")

        # ... add another jobs
        self.stdout.write(self.style.NOTICE('Start scheduler'))
        scheduler.start()