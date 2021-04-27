import requests
import urllib3
import json


# For Preventing SSL Error
urllib3.disable_warnings()

class Orchestrator():
    def __init__(self, base_url, tenant_name, id, pw):
        self.tenant_name = tenant_name
        self.id = id
        self.pw = pw
        self.base_url = base_url
        self.api_key = self.authentication()


    def authentication(self):

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
        }

        data = {
            "tenancyName": self.tenant_name,
            "usernameOrEmailAddress": self.id,
            "password": self.pw
        }

        end_point = self.base_url + 'api/Account/Authenticate'
        response = requests.post(end_point, headers=headers, data=json.dumps(data).encode('utf-8'), verify=False)
        api_key = response.json()['result']

        return api_key