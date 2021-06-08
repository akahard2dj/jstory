from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

import requests
import json

app = FastAPI()


@app.get("/")
def read_root():
    client_id = ''
    redirect_uri = 'http://localhost:8000/oauth'
    kakao_oauthurl = 'https://kauth.kakao.com/oauth/authorize?client_id={}&redirect_uri={}&response_type=code&scope=talk_message'.format(
        client_id, redirect_uri
    )
    return RedirectResponse(kakao_oauthurl)


@app.get("/oauth")
def oauth_kakao(request: Request):
    code = request.query_params.get('code')
    client_id = ''
    redirect_uri = 'http://localhost:8000/oauth'

    token_request_url = "https://kauth.kakao.com/oauth/token"
    payload = "grant_type=authorization_code"
    payload += "&client_id=" + client_id
    payload += "&redirect_url" + redirect_uri
    payload += "&code=" + code
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cache-Control': 'no-cache'
    }
    res = requests.request('POST', token_request_url, data=payload, headers=headers)
    access_token = json.loads(((res.text).encode('utf-8')))

    return access_token
