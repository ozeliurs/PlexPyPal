import time

from discordWebhook.discordWebhook import DiscordWebhook
from discordWebhook.discordEmbedColor import DiscordEmbedColor


class DiscordWebhookEmbed(DiscordWebhook):
    def __init__(self):
        super().__init__()
        self.webhook["embeds"] = [{}]

    def set_author(self, name, url=None, icon_url=None):
        self.webhook["embeds"][0]["author"] = {"name": name}
        if url is not None:
            self.webhook["embeds"][0]["author"]["url"] = url
        if icon_url is not None:
            self.webhook["embeds"][0]["author"]["icon_url"] = icon_url

    def set_title(self, title, url=None):
        self.webhook["embeds"][0]["title"] = title
        if url is not None:
            self.webhook["embeds"][0]["url"] = url

    def set_description(self, description):
        self.webhook["embeds"][0]["description"] = description

    def set_color(self, color: DiscordEmbedColor):
        self.webhook["embeds"][0]["color"] = color.value

    def set_image(self, url):
        self.webhook["embeds"][0]["image"] = {"url": url}

    def set_thumbnail(self, url):
        self.webhook["embeds"][0]["thumbnail"] = {"url": url}

    def set_footer(self, text, icon_url=None):
        self.webhook["embeds"][0]["footer"]["text"] = text
        if icon_url is not None:
            self.webhook["embeds"][0]["footer"]["icon_url"] = icon_url

    def set_timestamp(self, timestamp=None):
        if timestamp is None:
            timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
        self.webhook["embeds"][0]["timestamp"] = timestamp
