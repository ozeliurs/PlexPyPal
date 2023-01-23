import json
import time
import logging

from pathlib import Path

from flask import Flask, request

from plexParser import parse_plex_json

app = Flask(__name__)
logs = Path("logs")


@app.route('/', methods=['POST'])
def plex_webhook():
    data = json.loads(request.form['payload'])
    logs.joinpath(f"{time.time()}.json").write_text(json.dumps(data, indent=4))
    embed = parse_plex_json(data)
    embed.send()
    return "OK"


if __name__ == '__main__':
    logs.mkdir(parents=True, exist_ok=True)
    app.run(debug=True)
