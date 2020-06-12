from flask import Flask, render_template
from models.greetings import Greetings
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config["DEBUG"] = True
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "IBM - Hello World"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route("/", methods=['GET'])
def hello():
    return render_template("index.html", message=Greetings.get_welcome())


@app.route("/api/v1/hello", methods=['GET'])
def hello_api():
    response = {
        "status": "Ok",
        "message": "Hello World"
    }
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)