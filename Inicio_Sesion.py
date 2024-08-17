
from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from pymongo import *
import os

app = Flask(__name__)

# Credenciales de Facebook
facebook = oauth.register(
    name="facebook",
    client_id="TU_CLIENT_ID",
    client_secret="TU_SECRETO_CLIENTE",
    access_token_url="https://graph.facebook.com/v10.0/oauth/access_token",
    access_token_params=None,
    authorize_url="https://www.facebook.com/v10.0/dialog/oauth",
    authorize_params=None,
    redirect_uri="http://localhost:5000/login/callback/facebook",
    client_kwargs={"scope": "email public_profile"},
)

# Credenciales de Google para el login
google = oauth.register(
    name="google",
    client_id=os.getenv(GOOGLE_ID_CLIENTE),
    client_secret=os.getenv(GOOGLE_CLIENTE_SECRETO),
    access_token_url="https://accounts.google.com/o/oauth2/token",
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    authorize_params=None,
    redirect_uri="http://localhost:5000/login/callback/google",
    client_kwargs={"scope": "openid profile email"},
)

# Credenciales de GitHub
github = oauth.register(
    name="github",
    client_id=os.getenv(GITHUB_ID_CLIENTE),
    client_secret=os.getenv(GITHUB_CLIENTE_SECRETO),
    access_token_url="https://github.com/login/oauth/access_token",
    access_token_params=None,
    authorize_url="https://github.com/login/oauth/authorize",
    authorize_params=None,
    redirect_uri="http://localhost:5000/login/callback/github",
    client_kwargs={"scope": "user:email"},
)





# if __name__ == "__main__":
# 	app.run()