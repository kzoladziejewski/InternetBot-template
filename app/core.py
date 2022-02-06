import os
import sys
import argparse

from dotenv import load_dotenv
from selenium import webdriver

from app import run_app

LOGIN = None
PASSWORD = None
E_MAIL = None
URL = None
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
    parser.add_argument("--login", help="Login for use to login on webpage", type=str)
    parser.add_argument("--password", help="Password for use to login on webpage", type=str)
    parser.add_argument("--email", help="Email for use to login on webpage", type=str)
    parser.add_argument("--url", help="Url for use to login on webpage", type=str)
    parser.add_argument("--softwares", help="List of used webbrowser for bot - example: --software Chrome Firefox",
                        nargs="+")
    args = parser.parse_args()
    LOGIN = args.login
    PASSWORD = args.password
    E_MAIL = args.email
    URL = args.url
    SOFTWARES = args.softwares

if not LOGIN or not PASSWORD:
    raise Exception("Can not use bot without login and password - wihtout this data is not possible to use bot on"
                    "more complicated webpage. Please create file .env and fill variable in this template:"
                    "\nLOGIN={your login}\nPASSWORD={yout password}\nE_MAIL={Optionally this can be empty - when will"
                    " be not filled, script take LOGIN variable}\n\n OR provide in command line proper data: "
                    "login={your_login} password={your password}")

if not URL:
    URL = "http://www.google.com"

if not SOFTWARES:
    SOFTWARES = ['Chrome']


def get_webbrowser(webbrowser):
    if webbrowser == "chrome":
        from webdriver_manager.chrome import ChromeDriverManager
        return webdriver.Chrome(ChromeDriverManager().install())
    elif webbrowser == "chromium":
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.utils import ChromeType
        return webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    elif webbrowser == "firefox":
        from webdriver_manager.firefox import GeckoDriverManager
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif webbrowser == "ie" or webbrowser == "internetexplorer":
        from webdriver_manager.microsoft import IEDriverManager
        return webdriver.Ie(IEDriverManager().install())
    elif webbrowser == "edge":
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        return webdriver.Edge(EdgeChromiumDriverManager().install())
    elif webbrowser == "opera":
        from webdriver_manager.opera import OperaDriverManager
        return webdriver.Opera(executable_path=OperaDriverManager().install())
    else:
        raise Exception(f"Webbrowser {webbrowser} is not supported by this bot!")


os.environ['WDM_LOG_LEVEL'] = '0'
os.environ['WDM_PRINT_FIRST_LINE'] = 'False'

for webbrowser in SOFTWARES:
    driver = get_webbrowser(webbrowser.lower())
    driver.get(URL)
    run_app(driver, {"login": LOGIN, "password": PASSWORD, "email": E_MAIL, "url": URL})
    driver.close()
