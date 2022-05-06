import subprocess
from datetime import datetime
import dramatiq


@dramatiq.actor(max_retries=0)
def dump():
    date = datetime.now()
    # bashCommand = "chmod +x ./dump.sh"
    # process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    # output, error = process.communicate()
    # print(output, error)
    bashCommand = f"./dump.sh {date}"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output, error)
