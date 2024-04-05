from datetime import datetime, timedelta, date
import requests
from config import settings
from handlers.sellers_api import SellersApi
import pytz

tz = pytz.timezone('America/Sao_Paulo')

utc=pytz.UTC

class SchedulleApi:
    def __init__(self) -> None:
        self.sellers_api = SellersApi()
        self.host = settings.SCHEDULE_API
        self.headers = {
            "Authorization": settings.TOKEN_SCHEDULE
        }

    def get_events(self) -> list: 
        
        today = datetime.now(tz=tz)
        today = today.date()
        print(f"{datetime.now(tz=tz)} - Data de procura: {today}")
        url = f"{self.host}evens-schedules/today/cron/{today}"
        incidents = requests.get(url=url, headers=self.headers)
        print(f"{datetime.now(tz=tz)} - Buscando eventos")
        
        if incidents.status_code == 200: 
            print(f"{datetime.now(tz=tz)} - Total eventos para hoje: {len(incidents.json())}")
            return self.validate_messages(incidents.json())
        else: 
            print(f"{datetime.now(tz=tz)} - Error: {incidents.status_code} - {incidents.text}")

        return []
    
    def validate_messages(self, list_messages:list) -> list:
        list_return = []
        now = datetime.now(tz=tz)
        least_five_minutes = now - timedelta(minutes=5)
        five_more_minutes = now + timedelta(minutes=1)
        least_five_minutes = least_five_minutes.minute
        five_more_minutes = five_more_minutes.minute
        print(f"{datetime.now(tz=tz)} - Validando eventos")
        for messages in list_messages:
            time_send_message = datetime.fromisoformat(messages['date_send_message']).minute
            hour_send_message = datetime.fromisoformat(messages['date_send_message']).hour
            print(f"{datetime.now(tz=tz)} - {least_five_minutes},  {time_send_message}, {five_more_minutes}")
            if now.hour == hour_send_message:
                print(f"{datetime.now(tz=tz)} - {least_five_minutes},  {time_send_message}, {five_more_minutes}")
                if  time_send_message == now.minute:
                    print(f"{datetime.now(tz=tz)} - Evento encontrado")
                    messages['connector'] = self.sellers_api.get_connection(messages['connection_id'])
                    list_return.append(messages)

                elif time_send_message < now.minute:
                    print(f"{datetime.now(tz=tz)} - Evento encontrado")
                    messages['connector'] = self.sellers_api.get_connection(messages['connection_id'])
                    list_return.append(messages)
                else:
                    continue
            else: continue
        return list_return

    def set_status_message(self, status_code, message):
        url = f"{self.host}evens-schedules/{message['id']}/"
        payload = {
            "send_message": True if status_code in [200, 201] else False,
            "log": status_code
        }
        
        incidents = requests.patch(url=url, headers=self.headers, json=payload)
        self.update_status_shcedule(status_code, message)
        return incidents.status_code

    def update_status_shcedule(self, status_code, message):
        url = f"{self.host}schedules-config/{message['schedule_id']}/"
        if status_code in [200, 201]:
            if message['event_count'] == message['total_events']:
                payload = {
                    "status_progress": "finished",
                }
                incidents = requests.patch(url=url, headers=self.headers, json=payload)
            else:
                payload = {
                    "status_progress": "in_progress",
                }
                incidents = requests.patch(url=url, headers=self.headers, json=payload)
        else: 
            payload = {
                    "status_progress": "error",
            }
            incidents = requests.patch(url=url, headers=self.headers, json=payload)
        return incidents.status_code