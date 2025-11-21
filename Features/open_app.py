import os

APP_PATHS = {
    "youtube": "https://youtube.com",
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "spotify": "C:\\Users\\User\\AppData\\Roaming\\Spotify\\Spotify.exe",
    "Brave":"D:\\Dowloads"
}

def open_app(app_name: str):
    app_name = app_name.lower()
    if app_name in APP_PATHS:
        os.startfile(APP_PATHS[app_name])
        return f"Opening {app_name}"
    return f"App '{app_name}' not found."


print(open_app("brave"))