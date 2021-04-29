from cls.cls_orchestrator_get_info import Orchestrator_Start_Job

orchestrator = Orchestrator_Start_Job('your orchestrator url', 'your tanent name', 'id', 'pw')

# makes your arguments to dictionary ( key : value )
# String only can be passed
argument_dict = {
    "arg1": "happy",
    "arg2": "four seasons",
    "arg3": "fine"
}

robot_name = "your robot name"
process_name = "your process name"

# make argument_dict to string for passing
args = orchestrator.make_arg_string(argument_dict)

status = orchestrator.start_job(process_name, robot_name, args)
print(status)