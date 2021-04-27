from cls.cls_orchestrator_schedule import Orchestrator_schedule

orchestrator = Orchestrator_schedule('your orchestrator url', 'your tanent name', 'id', 'pw')

# get schedule list - All schedules
schedule_all = orchestrator.get_schedule_all()

# get schedule list - Filtering with specific robot
schedule = orchestrator.get_schedule("your environment name ( robot name )")

# export schedule list to excel
orchestrator.schedule_to_excel(schedule, "your export excel path")
orchestrator.schedule_to_excel(schedule_all, "your export excel path")
