from configparser import ConfigParser


# Read config.ini file
config_object = ConfigParser()
config_object.read("English.ini", encoding="UTF-8")
conf_lang = config_object["DEFAULT"]

current_lang = {}

current_lang.update(conf_lang)


def change_language():
    current_lang.clear()
    config_object = ConfigParser()
    config_object.read("Czech.ini", encoding="UTF-8")
    conf_lang = config_object["DEFAULT"]
    current_lang.update(conf_lang)


