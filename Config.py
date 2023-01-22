from configparser import ConfigParser

# Read config.ini file
config_object = ConfigParser()
config_object.read("Config.ini")
conf = config_object["DEFAULT"]


def set_config(key, value):
    config_object.set("DEFAULT", key, value)
    with open('Config.ini', 'w') as configfile:
        config_object.write(configfile)


def get_config(key):
    return config_object.get("DEFAULT", key)
