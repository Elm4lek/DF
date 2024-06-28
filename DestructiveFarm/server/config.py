# configuration file for destructivefarm. Put this in DestructiveFarm/server/
import os 

# generate a list of numbers between 0 and to_num (both included)
# they are the teams you want to attack.
# from that list, you can exclude your own team number,
# and the nop team number (usually 0)
def generate_team_numbers_to_attack(to_num, exclude=[]):
    for i in range(0, to_num+1):
        if i not in exclude:
           yield i

CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.

    # The clients will run sploits on TEAMS and
    # fetch FLAG_FORMAT from sploits' stdout.
    'TEAMS': {'Team #{}'.format(i): '10.60.{}.1'.format(i)
              for i in generate_team_numbers_to_attack(int(os.environ["NTEAM"]), exclude=[0, int(os.environ["OURIP"])])},
    'FLAG_FORMAT': r'[A-Z0-9]{31}=',

    # This configures how and where to submit flags.
    # The protocol must be a module in protocols/ directory.

     'SYSTEM_PROTOCOL': 'cyberchallenge', #DestructiveFarm/server/protocols/cyberchallege.py must exist
     'FLAG_SUBMIT_URL': 'http://10.10.0.1:8080/flags',
     'TEAM_TOKEN': os.environ["TOKEN"],

    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    'SUBMIT_FLAG_LIMIT': 50,
    'SUBMIT_PERIOD': 4,
    'FLAG_LIFETIME': 10 * 60,

    # Password for the web interface. You can use it with any login.
    # This value will be excluded from the config before sending it to farm clients.
    'SERVER_PASSWORD': os.environ["PASSWORD"],

    # Use authorization for API requests
    'ENABLE_API_AUTH': True,
    'API_TOKEN': os.environ["PASSWORD"]
}
