from win10toast import ToastNotifier

def send_notification(title: str, message: str, duration: int=10) -> None:
    """
    Show notifications on Windows 10.

    :param title: Title of the notification.
    :param message: Message of the notification.
    :param duration: Duration of the notification in seconds.

    :return: None
    """
    toast = ToastNotifier()
    toast.show_toast(title, message, duration=duration, threaded=True)