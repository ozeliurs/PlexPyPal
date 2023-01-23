import time
import logging

from pathlib import Path

from flask import Flask, request

from plexParser import parse_plex_json

app = Flask(__name__)
logs = Path("logs")


@app.route('/', methods=['POST'])
def plex_webhook():
    logging.warning(request)
    logging.warning(request.json)
    logging.warning(request.form)
    logging.warning(request.data)
    logging.warning(request.get_data())
    logging.warning(request.get_json())
    logging.warning(request.get_json(force=True))
    logging.warning(request.get_json(silent=True))
    logging.warning(request.get_json(cache=True))
    logging.warning(request.get_json(force=True, silent=True, cache=True))

    data = request.json
    logs.joinpath(f"{time.time()}.json").write_text(str(data))
    embed = parse_plex_json(data)
    embed.send()
    return "OK"


if __name__ == '__main__':
    logs.mkdir(parents=True, exist_ok=True)
    app.run(debug=True)
