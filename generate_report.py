
def generate_report(events):
    machine_users = logged_users_machines(events)
    for machine, users in machine_users.items():
        print(machine, end=": ")
        print(", ".join([user for user in users]))

def logged_users_machines(events):
    machine_users = {}
    events = sorted(events, key=lambda e:e.time)
    for event in events:
        if event.type.lower() == "login":
           machine_users.setdefault(event.machine, set()).add(event.user)
        elif event.type.lower() == "logout":
            if event.machine in machine_users and event.user in machine_users[event.machine]:
                machine_users[event.machine].remove(event.user)
    return machine_users
class Event:
    def __init__(self, event_time, event_type, machine_name, user_name):
        self.time = event_time
        self.type = event_type
        self.machine = machine_name
        self.user = user_name

events_list = [
    Event('2020-01-21 12:45:56', 'Login', 'myworkstation.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'Maria'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
    Event('2020-01-24 11:24:35', 'login', 'mailserver.local', 'Ted')
]
generate_report(events_list)