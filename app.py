from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec


server = Flask(__name__)
spec = FlaskPydanticSpec("flask", title="Fist API")
spec.register(server)


@server.get("/version")
def get_version() -> str:
    return "1.0"


server.run()
