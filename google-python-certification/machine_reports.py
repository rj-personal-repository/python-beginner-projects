# Problem Statement
# We need to process a list of Event objects using 
# their attributes to generate a report that lists 
# all users currently logged in to the machines.
#
# what information can we use to input then what do we want on the output
# Attributes - Date, User, Machine, Type
# Machine
#  - User
#  - Type
#  - Date
#  - Status


def get_event_data(event):
    return event.date


def current_users(events):
    events.sort(key=get_event_data)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove[event.user]
    return machines

def generate_report(machines):
    for machine, users in  machine.items()
    if len(users) > 0:
        user_list = ",".join(users)
        print("{} : {}".format(machine, user_list))


