import configparser
config = configparser.ConfigParser()
config.sections()

config.read('example.cfg')
config.sections()

for key in config['SectionOne']:
    print(key)

config['SectionOne']["status"]
