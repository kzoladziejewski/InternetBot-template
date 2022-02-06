import os
import pathlib
import sys
import argparse

from dotenv import load_dotenv

LOGIN = None
PASSWORD = None
E_MAIL = None
URL=None
SOFTWARES = []
if len(sys.argv) == 1:
    load_dotenv()

    LOGIN = os.environ.get("LOGIN")
    PASSWORD = os.environ.get("PASSWORD")
    E_MAIL = os.environ.get("EMAIL") if os.environ.get("EMAIL") else os.environ.get("LOGIN")
    URL = os.environ.get("URL")
    SOFTWARES = os.environ.get("SOFTWARE").split(" ")

elif len(sys.argv) > 1:
    parser = argparse.ArgumentParser(description="Welcome to bot, please provide required data: login/email, password,"
                                                 " basic_url, supported webbrowser")

if not LOGIN or not PASSWORD:
    raise Exception("Can not use bot without login and password - wihtout this data is not possible to use bot on"
                    "more complicated webpage. Please create file .env and fill variable in this template:"
                    "\nLOGIN={your login}\nPASSWORD={yout password}\nE_MAIL={Optionally this can be empty - when will"
                    " be not filled, script take LOGIN variable}\n\n OR provide in command line proper data: "
                    "login={your_login} password={your password}")

if not URL:
    URL = "www.google.com"

if not SOFTWARES:
    SOFTWARES = ['Chrome']

