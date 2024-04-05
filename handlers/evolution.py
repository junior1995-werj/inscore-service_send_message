
from datetime import datetime
import requests
from handlers.scheduler_api import SchedulleApi
from handlers.sellers_api import SellersApi
import pytz

tz = pytz.timezone('America/Sao_Paulo')

class Evolution:
    
    def __init__(self) -> None:
        self.types_message = {
            "default": "/message/sendText/",
            "video": "/message/sendMedia/",
            "photo": "/message/sendMedia/",
            "audio": "/message/sendWhatsAppAudio/",
            "document": "/message/sendMedia/",
            "survey" :"/message/sendPoll/"
        }
        self.metods = {
            "default": self.send_default,
            "video": self.send_video,
            "photo": self.send_photo,
            "audio": self.send_audio,
            "document": self.send_document,
        }
        self.headers = {
            "apikey": "",
            "Content-Type": "application/json",
            "User-Agent": "Cronjob"
        }
        self.schedulle_api = SchedulleApi()
        self.seller_api = SellersApi()

    def create_message(self, message):
        print(f"{datetime.now(tz=tz)} - Criando Mensagem")
        self.metods[message['type_message']](message=message)

    def send_photo(self, message):
        url = f"{message['connector']['connect_information']['api_url']}{self.types_message['photo']}{message['connector']['connect_information']['instance']}"

        self.headers["apikey"]=message['connector']['connect_information']['apikey']

        list_groups = self.seller_api.get_group_id(message)

        
        for group_id in list_groups:

            payload = {
                "number": group_id,
                "options": {
                    "delay": 1200,
                    "presence": "composing",
                    "mentions": {
                        "everyOne": message['mark_all']
                    }
                },
                "mediaMessage": {
                    "mediatype": "image",
                    "caption": message['message'],
                    "media": message['link_message']
                }
            }
        
            incidents = requests.post(url=url, headers=self.headers, json=payload)
            print(f"status send_message {incidents.status_code}")
            self.schedulle_api.set_status_message(incidents.status_code, message)

    
    def send_default(self, message):
        url = f"{message['connector']['connect_information']['api_url']}{self.types_message['default']}{message['connector']['connect_information']['instance']}"

        self.headers["apikey"]=message['connector']['connect_information']['apikey']
        
        list_groups = self.seller_api.get_group_id(message)

        for group_id in list_groups:

            payload = {
                "number": group_id,
                "options": {
                    "delay": 1200,
                    "presence": "composing",
                    "mentions": {
                        "everyOne": message['mark_all']
                    }
                },
                "textMessage": {
                    "text": message['message']
                }
            }
        
            incidents = requests.post(url=url, headers=self.headers, json=payload)
            print(f"status send_message {incidents.status_code}")
            self.schedulle_api.set_status_message(incidents.status_code, message)

        


    def send_audio(self, message):        
        url = f"{message['connector']['connect_information']['api_url']}{self.types_message['audio']}{message['connector']['connect_information']['instance']}"

        self.headers["apikey"]=message['connector']['connect_information']['apikey']

        list_groups = self.seller_api.get_group_id(message)

        for group_id in list_groups:

            payload = {
                "number": group_id,
                "options": {
                    "delay": 1200,
                    "presence": "composing",
                    "encoding": True,
                    "mentions": {
                        "everyOne": message['mark_all']
                    }
                },
                "audioMessage": {
                    "audio": message['link_message']
                }
            }
        
            incidents = requests.post(url=url, headers=self.headers, json=payload)
            print(f"status send_message {incidents.status_code}")
            self.schedulle_api.set_status_message(incidents.status_code, message)

    def send_video(self, message):
        url = f"{message['connector']['connect_information']['api_url']}{self.types_message['video']}{message['connector']['connect_information']['instance']}"

        self.headers["apikey"]=message['connector']['connect_information']['apikey']

        list_groups = self.seller_api.get_group_id(message)

        for group_id in list_groups:
            payload = {
                "number": group_id,
                "options": {
                    "delay": 1200,
                    "presence": "composing",
                    "encoding": True,
                    "mentions": {
                        "everyOne": message['mark_all']
                    }
                },
                "mediaMessage": {
                    "mediatype": "video",
                    "caption": message['message'],
                    "media": message['link_message']
                }
            }
        
            incidents = requests.post(url=url, headers=self.headers, json=payload)
            print(f"status send_message {incidents.status_code}")
            self.schedulle_api.set_status_message(incidents.status_code, message)
    
    def send_document(self, message):
        url = f"{message['connector']['connect_information']['api_url']}{self.types_message['document']}{message['connector']['connect_information']['instance']}"

        self.headers["apikey"]=message['connector']['connect_information']['apikey']

        list_groups = self.seller_api.get_group_id(message)

        for group_id in list_groups:

            payload = {
                "number": group_id,
                "options": {
                    "delay": 1200,
                    "presence": "composing",
                    "mentions": {
                        "everyOne": message['mark_all']
                    }
                },
                "mediaMessage": {
                    "mediatype": "document",
                    "filename": "envio.pdf",
                    "caption": message['message'],
                    "media": message['link_message']
                }
            }
    
            incidents = requests.post(url=url, headers=self.headers, json=payload)
            print(f"status send_message {incidents.status_code}")
            self.schedulle_api.set_status_message(incidents.status_code, message)

    
    def send_survey(self, message):
        url = f"{message['connector']['connect_information']['api_url']}{self.types_message['survey']}{message['connector']['connect_information']['instance']}"

        self.headers["apikey"]=message['connector']['connect_information']['apikey']

        list_groups = self.seller_api.get_group_id(message)

        for group_id in list_groups:
            payload = {
                "number": group_id,
                "options": {
                    "delay": 1200,
                    "presence": "composing",
                    "encoding": True,
                    "mentions": {
                        "everyOne": message['mark_all']
                    }
                },
                "mediaMessage": {
                    "mediatype": "document",
                    "filename": "envio.pdf",
                    "caption": message['message'],
                    "media": message['link_message']
                }
            }
        
            incidents = requests.post(url=url, headers=self.headers, json=payload)
            print(f"status send_message {incidents.status_code}")
            self.schedulle_api.set_status_message(incidents.status_code, message)

