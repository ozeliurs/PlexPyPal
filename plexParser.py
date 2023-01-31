from discordWebhook.webhooks import LibraryOnDeck, LibraryNew, MediaPause, MediaPlay, MediaRate, MediaResume, \
    MediaScrobble, MediaStop, AdminDatabaseBackup, AdminDatabaseCorruption, DeviceNew, PlaybackStarted, UnknownEvent


def parse_plex_json(msg: dict):
    if msg.get("event") == "library.on.deck":
        return LibraryOnDeck(msg)
    elif msg.get("event") == "library.new":
        return LibraryNew(msg)
    elif msg.get("event") == "media.pause":
        return MediaPause(msg)
    elif msg.get("event") == "media.play":
        return MediaPlay(msg)
    elif msg.get("event") == "media.rate":
        return MediaRate(msg)
    elif msg.get("event") == "media.resume":
        return MediaResume(msg)
    elif msg.get("event") == "media.scrobble":
        return MediaScrobble(msg)
    elif msg.get("event") == "media.stop":
        return MediaStop(msg)
    elif msg.get("event") == "admin.database.backup":
        return AdminDatabaseBackup(msg)
    elif msg.get("event") == "admin.database.corruption":
        return AdminDatabaseCorruption(msg)
    elif msg.get("event") == "device.new":
        return DeviceNew(msg)
    elif msg.get("event") == "playback.started":
        return PlaybackStarted(msg)
    else:
        return UnknownEvent(msg)
