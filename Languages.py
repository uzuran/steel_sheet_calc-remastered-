from configparser import ConfigParser
from Config import set_config, get_config


current_language = get_config(key="language")

# Read config.ini file
config_object = ConfigParser()
config_object.read(f"{current_language}.ini", encoding="UTF-8")
conf_lang = config_object["DEFAULT"]

current_lang = {}

current_lang.update(conf_lang)


def change_language(lang):
    current_lang.clear()
    config_object = ConfigParser()
    config_object.read(f"{lang}.ini", encoding="UTF-8")
    conf_lang = config_object["DEFAULT"]
    current_lang.update(conf_lang)
    set_config("language", lang)
