import logging
import subprocess
from datetime import datetime

import dramatiq


@dramatiq.actor(max_retries=0)
def dump() -> None:
    date = datetime.now()
    date_time = str(date.strftime("%Y-%m-%d:%H:%M"))
    bash_command: str = f"./dump.sh {date_time}"
    logging.info("Start dump database")
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    process.communicate()
    logging.info("Database dump complete")
