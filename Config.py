from configparser import ConfigParser

# Read config.ini file
config_object = ConfigParser()
config_object.read("Config.ini")
conf = config_object["DEFAULT"]


def set_config(key, value):
    config_object.set("DEFAULT", key, value)


def get_config(key):
    return config_object.get("DEFAULT", key)



