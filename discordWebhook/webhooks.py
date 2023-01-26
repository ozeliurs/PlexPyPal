from discordWebhook.discordWebhookEmbed import DiscordWebhookEmbed
from discordWebhook.discordEmbedColor import DiscordEmbedColor


class BaseEmbed(DiscordWebhookEmbed):
    def __init__(self, msg):
        super().__init__()
        self.set_username("PlexPyPal")
        self.set_timestamp()

        if msg.get("Metadata").get("grandparentTitle"):
            title = msg.get("Metadata").get("grandparentTitle")

            if msg.get("Metadata").get("index") and msg.get("Metadata").get("parentIndex"):
                title += f" S{msg.get('Metadata').get('parentIndex')}E{msg.get('Metadata').get('index')} - {msg.get('Metadata').get('title')}"

        else:
            title = msg.get("Metadata").get("title")

        if msg.get("Metadata").get("year"):
            title += f" ({msg.get('Metadata').get('year')})"

        self.set_title(title)


class LibraryOnDeck(BaseEmbed):
    def __init__(self, msg):
        super().__init__(msg)
        self.set_author("New media on deck")
        self.set_description(f"{msg.get('Account').get('title')}")
        self.set_color(DiscordEmbedColor.BLUE)


class LibraryNew(BaseEmbed):
    def __init__(self, msg):
        super().__init__(msg)
        self.set_author("New media added")
        self.set_description(f"{msg.get('Account').get('title')}")
        self.set_color(DiscordEmbedColor.BLUE)


class MediaPause(BaseEmbed):
    def __init__(self, msg):
        super().__init__(msg)
        self.set_author("Media paused")
        self.set_description(f"{msg.get('Account').get('title')}")
        self.set_color(DiscordEmbedColor.YELLOW)


class MediaPlay(BaseEmbed):
    def __init__(self, msg):
        super().__init__(msg)
        self.set_author("Media playing")
        self.set_description(f"{msg.get('Account').get('title')}")
        self.set_color(DiscordEmbedColor.GREEN)


class MediaRate(BaseEmbed):
    def __init__(self, msg):
        super().__init__(msg)
        self.set_author("Media rated")
        self.set_description(f"{msg.get('Account').get('title')}")
        self.set_color(DiscordEmbedColor.WHITE)


class MediaResume(BaseEmbed):
    def __init__(self, msg):
        super().__init__(msg)
        self.set_author("Media resumed")
        self.set_description(f"{msg.get('Account').get('title')}")
        self.set_color(DiscordEmbedColor.GREEN)


class MediaScrobble(BaseEmbed):
    def __init__(self, msg):
        super().__init__(msg)
        self.set_author("Media scrobbled")
        self.set_description(f"{msg.get('Account').get('title')}")
        self.set_color(DiscordEmbedColor.WHITE)


class MediaStop(BaseEmbed):
    def __init__(self, msg):
        super().__init__(msg)
        self.set_author("Media stopped")
        self.set_description(f"{msg.get('Account').get('title')}")
        self.set_color(DiscordEmbedColor.RED)


class AdminDatabaseBackup(BaseEmbed):
    def __init__(self, msg):
        super().__init__(msg)
        self.set_author("Database backup")
        self.set_color(DiscordEmbedColor.GREEN)


class AdminDatabaseCorruption(BaseEmbed):
    def __init__(self, msg):
        super().__init__(msg)
        self.set_author("Database corruption")
        self.set_color(DiscordEmbedColor.RED)


class DeviceNew(BaseEmbed):
    def __init__(self, msg):
        super().__init__(msg)
        self.set_author("New device")
        self.set_color(DiscordEmbedColor.YELLOW)


class PlaybackStarted(BaseEmbed):
    def __init__(self, msg):
        super().__init__(msg)
        self.set_author("Playback started")
        self.set_color(DiscordEmbedColor.GREEN)


class UnknownEvent(BaseEmbed):
    def __init__(self, msg):
        super().__init__(msg)
        self.set_author("Unknown event")
        self.set_color(DiscordEmbedColor.MAGENTA)
