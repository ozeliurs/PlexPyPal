import time

from pathlib import Path

from flask import Flask, request

from plexParser import parse_plex_json

app = Flask(__name__)
logs = Path("logs")


@app.route('/', methods=['POST'])
def plex_webhook():
    print(request)
    print(request.json)
    print(request.form)
    print(request.data)
    print(request.get_data())
    print(request.get_json())
    print(request.get_json(force=True))
    print(request.get_json(silent=True))
    print(request.get_json(cache=True))
    print(request.get_json(force=True, silent=True, cache=True))

    data = request.json
    logs.joinpath(f"{time.time()}.json").write_text(str(data))
    embed = parse_plex_json(data)
    embed.send()
    return "OK"


if __name__ == '__main__':
    logs.mkdir(parents=True, exist_ok=True)
    app.run(debug=True)
