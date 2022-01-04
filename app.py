from flask import Flask


server = Flask(__name__)


@server.get("/version")
def get_version() -> str:
    return "1.0"


server.run()
