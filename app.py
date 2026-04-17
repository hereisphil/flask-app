from flask import Flask, redirect, url_for, render_template, session
from datetime import timedelta
import json

from os import environ as env
from dotenv import load_dotenv
#Followed this guide: https://developer.vonage.com/en/blog/python-environment-variables-a-primer

from authlib.integrations.flask_client import OAuth
from functools import wraps

app = Flask(__name__)
oauth = OAuth(app)
load_dotenv()  #Brings all environment variables from .env into os.environ
app.secret_key = env["RANDOM_APP_KEY"] #Must match .env name exactly
app.debug = True
AUTH0_BASE_URL = env["AUTH0_BASE_URL"]

auth0 = oauth.register(
    "auth0",
    client_id = env["AUTH0_CLIENT_ID"],
    client_secret = env["AUTH0_CLIENT_SECRET"],
    api_base_url = AUTH0_BASE_URL,
    access_token_url = AUTH0_BASE_URL + "/oauth/token",
    authorize_token_url = AUTH0_BASE_URL + "/authorize",
    client_kwargs = {
        "scope": "openid profile email"
        },
    server_metadata_url = env["AUTH0_SERVER_METADATA_URL"]
    #https://dev-eqdktnmkmwc3yxn8.us.auth0.com/.well-known/openid-configuration
    #https://dev-eqdktnmkmwc3yxn8.us.auth0.com/.well-known/oauth-authorization-server
)

app.permanent_session_lifetime = timedelta(minutes=15) #Setup auto session expiration
app.config["SESSION_TYPE"] = "filesystem"

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

#Learned Jinja Templating from this guide:
#https://realpython.com/primer-on-jinja-templating/
@app.route("/")
def home():
    return render_template("index.html", title="Welcome to my Auth0 App")

@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(redirect_uri = url_for("callback", _external=True, _scheme="http"))

@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = auth0.authorize_access_token()
    session["user"] = token
    resp = auth0.get("userinfo")
    print(resp)
    return redirect("/dashboard")

def requires_auth(f):
    @wraps(f)
    def decorated(*arg, **kwargs):
        print(session)
        if "profile" not in str(session):
            return redirect("/")
        return f(*arg, **kwargs)
    return decorated

@app.route("/dashboard")
@requires_auth
def dashboard():
    return render_template("dashboard.html", session=session.get("user"), pretty=json.dumps(session.get("user"), indent=4))

# ---------------------------------------------------------------------------- #
#                          ADDITONAL PROTECTED ROUTE:                          #
# ---------------------------------------------------------------------------- #
@app.route("/settings")
@requires_auth
def settings():
    return render_template("settings.html", session=session.get("user"), pretty=json.dumps(session.get("user"), indent=4))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
