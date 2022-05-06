import logging
import subprocess
from datetime import datetime

import dramatiq


@dramatiq.actor(max_retries=0)
def dump() -> None:
    date = datetime.now()
    bash_command: str = f"./dump.sh {date}"
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    logging.info(output, error)
