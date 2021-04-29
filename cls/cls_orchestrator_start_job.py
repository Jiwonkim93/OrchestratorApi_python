import requests
import urllib3
import pandas as pd
import json
import os
from cls.cls_orchestrator_main import Orchestrator

# For Preventing SSL Error
urllib3.disable_warnings()

class Orchestrator_Start_Job(Orchestrator):
    
    def __init__(self, base_url, tenant_name, id, pw):
        super(Orchestrator_Start_Job, self).__init__(base_url, tenant_name, id, pw)
        self.headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Bearer ' + self.api_key,
        }
        
        
    def make_arg_string(self, arg_dict):
        arg_list = []
        args=""
        for key, val in arg_dict.items():
            arg_list.append('\\"' + key + '\\":\\"' + val + '\\"')

        if arg_list:
            args = ",".join(arg_list)
            args = "{" + args + "}"

        return args


    def start_job(self, process_name, robot_name, args=""):
        response = self.call_process(process_name, robot_name, args)
        if response.status_code == 201:
            return process_name + ": Success"
        else:
            return process_name + ": Fail"
