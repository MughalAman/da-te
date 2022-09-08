from datetime import datetime
from os.path import exists
import locale

#region config

display_default_lang = True
display_custom_lang = False
custom_language = None
date_format = "%A, %m %b %Y %H:%M:%S"

#endregion

def create_config_files():
    if not exists("da-te.conf"):
        with open("da-te.conf", "w") as config_file:
            config_file.write(f"display_default_lang = {display_default_lang}\n")
            config_file.write(f"display_custom_lang = {display_custom_lang}\n")
            config_file.write(f"custom_language = {custom_language}\n")
            config_file.write(f"date_format = {date_format}\n")
            config_file.write("check readme for more info!\n")
            config_file.write("made by Aman Mughal https://amppa.dev/")


def load_config_files():
    global display_default_lang
    global display_custom_lang
    global custom_language
    global date_format


    if exists("da-te.conf"):
        with open("da-te.conf", "r") as config_file:
            for line in config_file:
                if line.startswith("display_default_lang"):
                    display_default_lang = line.split("=")[1].strip()
                elif line.startswith("display_custom_lang"):
                    display_custom_lang = line.split("=")[1].strip()
                elif line.startswith("custom_language"):
                    custom_language = line.split("=")[1].strip()
                elif line.startswith("date_format"):
                    date_format = line.split("=")[1].strip()

def get_date():
    return datetime.now()


def format_date_time():
    locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
    date = get_date()
    formatted_date_strings = []

    if display_default_lang == "True":
        formatted_date_strings.append(date.strftime(date_format))

    if display_custom_lang == "True":
        locale.setlocale(locale.LC_TIME, custom_language)
        formatted_date_strings.append(date.strftime(date_format))

    return formatted_date_strings

def main():
    create_config_files()
    load_config_files()
    for date_string in format_date_time():
        print(date_string)

if __name__ == "__main__":
    main()

    



    

