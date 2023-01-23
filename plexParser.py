from discordWebhook.discordWebhookEmbed import DiscordWebhookEmbed
from discordWebhook.discordEmbedColor import DiscordEmbedColor


def base_embed(msg: dict):
    embed = DiscordWebhookEmbed()
    embed.set_username("PlexPyPal")
    embed.set_description(msg.get("Metadata").get("title"))
    # embed.set_thumbnail(msg.get("Metadata").get("thumb"))
    embed.set_timestamp()
    return embed


def library_on_deck(msg: dict):
    embed = base_embed(msg)
    embed.set_author("New media on deck")
    return embed


def library_new(msg: dict):
    embed = base_embed(msg)
    embed.set_author("New media added")
    return embed


def media_pause(msg: dict):
    embed = base_embed(msg)
    embed.set_author("Media paused")
    embed.set_title(msg.get('Metadata').get('title'))
    return embed


def media_play(msg: dict):
    embed = base_embed(msg)
    embed.set_author("Media playing")
    embed.set_title(msg.get('Metadata').get('title'))
    embed.set_description(f"{msg.get('Account').get('title')} has started playing {msg.get('Metadata').get('title')}")
    embed.set_color(DiscordEmbedColor.GREEN)
    return embed


def media_rate(msg: dict):
    embed = base_embed(msg)
    embed.set_author("Media rated")
    embed.set_title(msg.get('Metadata').get('title'))
    return embed


def media_resume(msg: dict):
    embed = base_embed(msg)
    embed.set_author("Media resumed")
    embed.set_title(msg.get('Metadata').get('title'))
    return embed


def media_scrobble(msg: dict):
    embed = base_embed(msg)
    embed.set_author("Media scrobbled")
    embed.set_title(msg.get('Metadata').get('title'))
    return embed


def media_stop(msg: dict):
    embed = base_embed(msg)
    embed.set_author("Media stopped")
    return embed



def admin_database_backup(msg: dict):
    embed = base_embed(msg)
    embed.set_author("Database backup")
    return embed


def admin_database_corruption(msg: dict):
    embed = base_embed(msg)
    embed.set_author("Database corruption")
    return embed


def device_new(msg: dict):
    embed = base_embed(msg)
    embed.set_author("New device")
    return embed


def playback_started(msg: dict):
    embed = base_embed(msg)
    embed.set_author("Playback started")
    return embed


def unknown_event(msg: dict):
    embed = base_embed(msg)
    embed.set_author("Unknown event")
    embed.set_description(msg.get("event"))
    return embed


def parse_plex_json(msg: dict):
    if msg.get("event") == "library.on.deck":
        return library_on_deck(msg)
    elif msg.get("event") == "library.new":
        return library_new(msg)
    elif msg.get("event") == "media.pause":
        return media_pause(msg)
    elif msg.get("event") == "media.play":
        return media_play(msg)
    elif msg.get("event") == "media.rate":
        return media_rate(msg)
    elif msg.get("event") == "media.resume":
        return media_resume(msg)
    elif msg.get("event") == "media.scrobble":
        return media_scrobble(msg)
    elif msg.get("event") == "media.stop":
        return media_stop(msg)
    elif msg.get("event") == "admin.database.backup":
        return admin_database_backup(msg)
    elif msg.get("event") == "admin.database.corruption":
        return admin_database_corruption(msg)
    elif msg.get("event") == "device.new":
        return device_new(msg)
    elif msg.get("event") == "playback.started":
        return playback_started(msg)
    else:
        return unknown_event(msg)
