"""
Create a pointer for directory:
    calling py app -c or --config -> capability to edit config
    config dir: /something
    

Author: Christian M. Fulton
Date: 01.12.2022
"""
import configparser
import os
from os import path


# TODO: Move APP_LOCATION from both app.py and options.py into config.ini
APP_LOCATION = os.path.abspath("logstuff")


def main() -> None:
    """
    gather data
    """
    options.check_config()
    loopin = True
    fname = input("Enter the name for your file: ")

    make_dir()

    my_file = Manage(APP_LOCATION + "/" + get_dir() + "/" + fname)

    while loopin:
        usr_data = input("Enter the idea to log or to stop type !q: ")
        if usr_data == "!q":
            loopin = False
        else:
            my_file.write_line(usr_data)


def execute(args: str) -> None:
    """
    point execution in right direction
    """
    if len(args) > 1:
        options.flags(args)
    elif len(args) == 0:
        main()
    else:
        err = "Usage: python iLog <FLAG> [arg]"
        print(err)
