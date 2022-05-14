import subprocess

def open_spotify(path: str) -> None:
    """
    Open locally installed Spotify.

    :param path: Path to Spotify.exe.

    :return: None
    """
    subprocess.Popen(path)