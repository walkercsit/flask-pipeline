from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello Test Application!"

# run the app.
if __name__ == "__main__":
    application.run()