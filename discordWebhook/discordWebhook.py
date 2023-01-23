import os

import requests


WEBHOOK_URL = os.getenv("WEBHOOK_URL")


class DiscordWebhook:
    def __init__(self):
        self.webhook = {}
        self.url = WEBHOOK_URL

    def set_webhook(self, webhook):
        self.webhook = webhook

    def set_url(self, url):
        self.url = url

    def set_username(self, username):
        self.webhook["username"] = username

    def set_avatar_url(self, avatar_url):
        self.webhook["avatar_url"] = avatar_url

    def set_content(self, content):
        self.webhook["content"] = content

    def set_embed(self, embed):
        self.webhook["embeds"] = [embed.to_dict()]

    def set_components(self, components):
        self.webhook["components"] = components

    def send(self) -> bool:
        return self.debug_send().ok

    def debug_send(self) -> requests.Response:
        req = requests.post(WEBHOOK_URL, json=self.webhook, headers={"Content-Type": "application/json"})

        return req
