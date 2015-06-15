'''
// setup environment
sudo easy_install pip

// lists installed modules and version
pip freeze

sudo pip install termcolor
sudo pip install beautifulsoup4
sudo pip install requests

// run
python spider.py
python spider.py -h
'''

import argparse
from packtpub import Packpub
from utils import current_ip_address
from logs import *

def do_login():
    login_soup = make_soup(BASE_DEV_URL + LOGIN_DEV_URL, DELAY_REQUEST)

def parse_environment(param):
    """
    Parse environment parameter: default is development
    """
    path = 'config/dev.cfg'

    if param and param.strip() == 'prod':
        path = 'config/prod.cfg'

    log_info('[*] config environment path: ' + path)
    return path

def main():
    parser = argparse.ArgumentParser(description='Download FREE eBook every day from www.packtpub.com', version='0.1')
    parser.add_argument('-e', '--environment', dest='environment', default='dev', help='configuration environment')
    args = parser.parse_args()

    try:
        environment_path = parse_environment(args.environment)
        #current_ip_address()

        packpub = Packpub(environment_path)
        packpub.login()

    except KeyboardInterrupt:
        log_error('[-] interrupted manually')
    except Exception as e:
        log_debug(e)
        log_error('[-] something weird occurred, exiting...')

if __name__ == '__main__':
    main()
