import time
from datetime import datetime as dt

# Please, enter the site names which you want to block
sites_to_block = [
    "www.facebook.com",
    "facebook.com",
    "www.youtube.com",
    "youtube.com",
]

Linux = "/etc/hosts"
Windows = r"C:\Windows\System32\drivers\etc\hosts"
default_hoster = Windows # if you are on Linux please change it to Linux
redirect = "127.0.0.1"


def block_websites(start_hour, end_hour):
    while True:
        if (
            dt(dt.now().year, dt.now().month, dt.now().day, start_hour)
            < dt.now()
            < dt(dt.now().year, dt.now().month, dt.now().day, end_hour)
        ):
            print("In progress ....")
            with open(default_hoster, "r+") as hostfile:
                hosts = hostfile.read()
                for site in sites_to_block:
                    if site not in hosts:
                        hostfile.write(redirect + " " + site + "\n")
        else:
            with open(default_hoster, "r+") as hostfile:
                hosts = hostfile.readlines()
                hostfile.seek(0)
                for host in hosts:
                    if not any(site in host for site in sites_to_block):
                        hostfile.write(host)
                hostfile.truncate()
            print("Good")
        time.sleep(3)


if __name__ == "__main__":
    block_websites(9, 18)
