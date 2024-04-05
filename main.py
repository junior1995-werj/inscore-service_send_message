from time import sleep

import pytz
from handlers.scheduler_api import SchedulleApi
from handlers.evolution import Evolution
from datetime import datetime

schedulle_api = SchedulleApi()
evolution = Evolution()

tz = pytz.timezone('America/Sao_Paulo')

def controller():
    print(f"{datetime.now(tz=tz)} - Start cron: alert_topdesk_teams")
    list_messages = schedulle_api.get_events()
    print(f"{datetime.now(tz=tz)} - service: total send: {len(list_messages)}")
    for message in list_messages:
       evolution.create_message(message=message)

    print(f"{datetime.now(tz=tz)} - Finishing cron: alert_topdesk_teams")

if __name__ == "__main__":
    while True:
        controller()
        print(f"{datetime.now(tz=tz)} - service: sleep 10")
        sleep(10)