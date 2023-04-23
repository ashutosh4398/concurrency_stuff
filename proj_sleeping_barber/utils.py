from datetime import datetime

def process_time():
    now = datetime.now()
    return now.strftime("%I:%M:%S %p")