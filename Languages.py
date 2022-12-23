from configparser import ConfigParser
from OptionScreen import *
# Read config.ini file
config_object = ConfigParser()
config_object.read("Czech.ini", encoding="UTF-8")
conf_lang = config_object["DEFAULT"]

current_lang = dict(conf_lang)
