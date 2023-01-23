import time

from pathlib import Path

from flask import Flask, request

from plexParser import parse_plex_json

app = Flask(__name__)
logs = Path("logs")


@app.route('/', methods=['POST'])
def plex_webhook():
    data = request.json
    logs.joinpath(f"{time.time()}.json").write_text(str(data))
    embed = parse_plex_json(data)
    embed.send()
    return "OK"


if __name__ == '__main__':
    logs.mkdir(parents=True, exist_ok=True)
    app.run(debug=True)
