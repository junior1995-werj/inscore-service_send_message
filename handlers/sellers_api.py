import requests
from datetime import datetime
from config import settings


class SellersApi:

    def __init__(self):
        self.host = settings.SELLERS_API
        self.headers = {
            "Authorization": settings.TOKEN_SELLERS
        }

    def get_connection(self, connector_id) -> list:
        url = f"{self.host}sellers-connectors/{connector_id}"
        connection = requests.get(url=url, headers=self.headers).json()
        return connection
    
    def get_group_id(self, message):
        url = f"{self.host}sellers-groups/?seller_id={message['seller_id']}"

        response = requests.get(url=url, headers=self.headers)

        list_groups= []
        if response.status_code in [200, 201]:
            for value in response.json():
                for groups in message['send_to']['groups']:
                    if groups == value['group_name'] and value['group_id'] not in list_groups:
                        list_groups.append(value['group_id'])

        return list_groups
        
    
