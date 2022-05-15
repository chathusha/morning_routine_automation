#! C:\Users\ROG\Documents\04. Hobbies\01. Python\07. Automation\venv\Scripts\python.exe

# local imports
from home_routine import home_routine

# packages
import time
import logging

# constants
SPOTIFY_PATH = "C:\\Users\\ROG\\AppData\\Roaming\\Spotify\\Spotify.exe"
URLS = [
    "https://ticktick.com/"
]

def main():
    # setup the info logger
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Script started')

    # get current time
    now = time.localtime()
    # convert time to string
    str_now = time.strftime('%H:%M', now)

    # run the morning routine if the script start before 9:30AM
    if (time.strptime(str_now, '%H:%M') < time.strptime('09:30', '%H:%M')):
        home_routine(SPOTIFY_PATH, URLS)
        logging.info('Script finished')

    else:
        logging.info('Script terminated')

if __name__ == '__main__':
    main()