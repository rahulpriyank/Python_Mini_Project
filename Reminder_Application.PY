from socket import timeout
from pip import main
from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Swith off Your phone",
            message="Its too late, Please keep your phone away and go to your bed",
            timeout=10
        )
        time.sleep(60*60)
