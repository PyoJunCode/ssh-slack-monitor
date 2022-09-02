from datetime import datetime

from slack_sdk import WebClient



class SlackSender:
    def __init__(self, token):
        self.client = WebClient(token=token)
        self.channel = "lab"

    def send_msg(self, status, msg):
        time = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(status, time)
        emoji = ":grin:" if status.strip() == "Accepted" else ":sob:"

        blocks = [
            {"type": "divider"},
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://api.slack.com/img/blocks/bkb_template_images/notificationsWarningIcon.png",
                        "alt_text": "notifications warning icon",
                    },
                    {"type": "mrkdwn", "text": "*Notification*"},
                ],
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Proxy server access detected {emoji}*\n",
                },
            },
            {"type": "divider"},
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Date:* \n {time} \n*Info:* \n" + msg,
                },
            },
        ]
        resp = self.client.chat_postMessage(
            channel=self.channel, blocks=blocks, text=f"SSH monitor: alert",
        )
        return
