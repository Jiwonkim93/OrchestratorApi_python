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
        self.headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Bearer ' + self.api_key,
        }

       
    def authentication(self):

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
        }

        data = {
            "tenancyName": self.tenant_name,
            "usernameOrEmailAddress": self.id,
            "password": self.pw
        }

        end_point = self.base_url + '/api/Account/Authenticate'

        try:
            response = requests.post(end_point, headers=headers, data=json.dumps(data).encode('utf-8'), verify=False)
            api_key = response.json()['result']
            return api_key

        except Exception as e:
            print(e)
            return 0
        

    def get_robot_id(self, robot_name):
        # filter top 1 with robot name is robot_name
        params = (
            ('$top', '1'),
            ('$filter', 'Name eq \'' + robot_name + '\''),
        )

        try:
            end_point = self.base_url + '/odata/Robots'
            response = requests.get(end_point.encode('utf-8'), headers=self.headers, params=params, verify=False)
            robot_id = response.json()['value'][0]['Id']
            return robot_id

        except:
            print("Check your robot name")


    def get_process_id(self, process_name):

        try:
            end_point = self.base_url + "/odata/Releases?$filter=ProcessKey%20eq%20%27" + process_name + "%27"
            response = requests.get(end_point.encode('utf-8'), headers=self.headers, verify=False)
            process_id = response.json()['value'][0]['Key']
            return process_id

        except:
            print("Check your process name")


    def call_process(self, process_name, robot_name, args=""):

        process_id = self.get_process_id(process_name)
        robot_id = self.get_robot_id(robot_name)

        if args:
            data = '{"startInfo":' \
                       '{"ReleaseKey": "' + str(process_id) + '",' \
                        '"Strategy": "Specific",' \
                        '"RobotIds": [ ' + str(robot_id) + ' ],' \
                        '"JobsCount": 0,' \
                        '"Source": "Manual",' \
                        '"InputArguments": "' + args + '"}}'

        else:
            data = '{"startInfo":\n   ' \
                        '{"ReleaseKey": "' + str(process_id) + '",' \
                        '"Strategy": "Specific",' \
                        '"RobotIds": [ ' + str(robot_id) + ' ],' \
                        '"JobsCount": 0,' \
                        '"Source": "Manual"}}'


        response = requests.post(self.base_url + '/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs',
                                 headers=self.headers, data=data, verify=False)
        return response


    def get_schedule_all(self):

        end_point = self.base_url + '/odata/ProcessSchedules'
        response = requests.get(end_point.encode('utf-8'), headers=self.headers, verify=False)

        return response.json(encoding='utf-8')


    def get_schedule(self, environment_name):

        # There are other filtering options maybe
        params = (
            ('$filter', 'EnvironmentName eq \'' + environment_name + '\''),
        )

        end_point = self.base_url + '/odata/ProcessSchedules'
        response = requests.get(end_point.encode('utf-8'), headers=self.headers, params=params, verify=False)

        return response.json(encoding='utf-8')
