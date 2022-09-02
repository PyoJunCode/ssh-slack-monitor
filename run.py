import os
import time
import re

from dotenv import load_dotenv

from utils.slack_sender import SlackSender


class Watcher:
    def __init__(self):
        load_dotenv()
        token = os.getenv("slack_token")
        if token is None:
            raise Exception("Error: Slack token not exists.")
        log_path = os.getenv("LOG_PATH")
        if log_path is None or not os.path.exists(log_path):
            raise Exception(f"Error: Log file not exists in {log_path}")
        self.slack_client = SlackSender(token)

    def watch(self):
        print("Start monitoring...")
        status_list = ["Accepted", "Failed"]
        with open("/var/log/auth.log", "r") as f:
            f.seek(0, 2)
            while True:
                new = f.readline()
                if new:
                    if "sshd" in new:
                        for status in status_list:
                            start = re.search(status, new)
                            if start is not None:
                                yield status, new[start.start() :].strip()

                time.sleep(1)

    def trigger_slack(self, status, msg):
        self.slack_client.send_msg(status, msg)


if __name__ == "__main__":
    watcher = Watcher()
    for status, record in watcher.watch():
        watcher.trigger_slack(status, record)
