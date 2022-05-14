import webbrowser

def open_url(url: str) -> None:
    """
    Opens the given url in a new tab in the default browser.

    :param url: The url to open.

    :return: None
    """
    webbrowser.open(url=url, new=2, autoraise=True)
