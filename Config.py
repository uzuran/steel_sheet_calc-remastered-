from configparser import ConfigParser

# Read config.ini file
config_object = ConfigParser()
config_object.read("Config.ini")
conf = config_object["DEFAULT"]

# Basic configuration configparser
config = ConfigParser()
config["DEFAULT"] = {}
configuration = config["DEFAULT"]

# Font for all strings.
configuration["Font"] = "Calibri, 12"
configuration["Font_size"] = "12"

# Config for buttons at the beginning of program
configuration["Main_button_width"] = "30"
configuration["Main_button_height"] = "2"

# Config for registration user_button, and login
configuration["lr_button_width"] = "17"
configuration["lr_button_height"] = "2"


# Main config for main labels.
configuration["main_background"] = "#d1dffa"
configuration["main_label_width"] = "300"
configuration["main_label_height"] = "2"

# Option for labels
configuration["option_for_labels"] = "5"

# Option for labels
option_for_labels = 5

configuration["Colour_green"] = "green"



