import urllib3
import pandas as pd
from cls.cls_orchestrator_main import Orchestrator

# For Preventing SSL Error
urllib3.disable_warnings()

class Orchestrator_schedule(Orchestrator):
    def __init__(self, base_url, tenant_name, id, pw):
        super(Orchestrator_schedule, self).__init__(base_url, tenant_name, id, pw)


    def schedule_to_excel(self, schedule_json, export_path):

        col = ["Id", "ReleaseId", "Name", "Enabled", "ReleaseKey", "PackageName",
               "StartProcessCron", "StartProcessCronSummary", "JobPriority", "EnvironmentName", "EnvironmentId"]
        df = pd.DataFrame(columns=col)
        cnt = schedule_json['@odata.count']

        for idx in range(cnt):
            # There are more fields in schedule_json
            df.loc[idx, "Enabled"] = schedule_json['value'][idx]['Enabled']
            df.loc[idx, "Id"] = schedule_json['value'][idx]['Id']
            df.loc[idx, "ReleaseId"] = schedule_json['value'][idx]['ReleaseId']
            df.loc[idx, "Name"] = schedule_json['value'][idx]['Name']
            df.loc[idx, "ReleaseKey"] = schedule_json['value'][idx]['ReleaseKey']
            df.loc[idx, "PackageName"] = schedule_json['value'][idx]['PackageName']
            df.loc[idx, "StartProcessCron"] = schedule_json['value'][idx]['StartProcessCron']
            df.loc[idx, "StartProcessCronSummary"] = schedule_json['value'][idx]['StartProcessCronSummary']
            df.loc[idx, "JobPriority"] = schedule_json['value'][idx]['JobPriority']
            df.loc[idx, "EnvironmentName"] = schedule_json['value'][idx]['EnvironmentName']
            df.loc[idx, "EnvironmentId"] = schedule_json['value'][idx]['EnvironmentId']

        df.to_excel(export_path, sheet_name="Schedule", index=False)
