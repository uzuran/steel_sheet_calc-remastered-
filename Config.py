import configparser

config = configparser.ConfigParser()

config["DEFAULT"] = {"title": "Config.py",
                     "compression": "yes",
                     "compression_level": "9"}

config["Config.py"] = {}
configuration = config["Config.py"]

# Font for all strings.
configuration["Font"] = "Calibri, 12"

# Config for buttons at the beginning of program
configuration["Main_button_width"] = "30"
configuration["Main_button_height"] = "30"

# Config for registration user_button, and login
configuration["lr_button_width"] = "17"
configuration["lr_button_height"] = "2"


# Config for registration user_button, and login
configuration["lr_button_width"] = "17"
configuration["lr_button_height"] = "2"
configuration["lr_button_height"] = "2"

# Main config for main labels.
main_background = "#d1dffa"
main_label_width = "300"
main_label_height = "2"

# Option for labels
option_for_labels = 5

# Green colour
green = "green"
