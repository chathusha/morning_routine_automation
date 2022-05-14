# packages
from browser import open_url
from notification import send_notification
from spotify import open_spotify

import logging
import time

def home_routine(spotify_path: str, urls:list) -> None:
    """
    The routine that runs at home.

    :param spotify_path: Local path of the Spotify.exe.
    :param urls: List of urls which need open in browser.

    :return: None
    """
    # setup the info logger
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # send the morning routine notification
    send_notification('Good morning!', 'Have a good day!')
    logging.info('Notification sent')

    time.sleep(5)

    # open Spotify
    open_spotify(spotify_path)
    logging.info('Spotify opened')

    time.sleep(5)

    # open urls
    for url in urls:
        open_url(url)
        time.sleep(5)
        
    logging.info('URLs opened')