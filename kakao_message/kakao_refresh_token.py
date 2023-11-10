# kakao_refresh_token.py
import requests
import json
from datetime import datetime, timedelta

class KakaoTokenManager:
    def __init__(self, client_id, client_secret):
        self.client_id = "64c65b11be9bb8fa9443e4e6490f6f42"
        self.client_secret = "cYbX3wr8vVcsmqFS1AhGnd8qs9pI0dyTQ"
        self.base_url = "https://kauth.kakao.com/oauth/token"
        self.token_file = "token.json"
        self.tokens = self.load_tokens()

    def load_tokens(self):
        try:
            with open(self.token_file, "r") as file:
                tokens = json.load(file)
                return tokens
        except FileNotFoundError:
            return {"access_token": None, "refresh_token": None, "expires_at": None}

    def save_tokens(self, access_token, refresh_token, expires_in):
        expires_at = datetime.now() + timedelta(seconds=expires_in)
        tokens = {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expires_at": expires_at.isoformat(),
        }
        with open(self.token_file, "w") as file:
            json.dump(tokens, file)

    def is_token_expired(self):
        expires_at_iso = self.tokens.get("expires_at")
        if expires_at_iso:
            expires_at = datetime.fromisoformat(expires_at_iso)
            return datetime.now() > expires_at
        else:
            return False

    def refresh_access_token(self):
        if self.tokens["refresh_token"] and not self.is_token_expired():
            print("액세스 토큰이 유효합니다.")
            return self.tokens["access_token"]

        print("액세스 토큰이 만료되었거나 유효하지 않습니다. 토큰을 갱신합니다.")

        data = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.tokens["refresh_token"],
        }

        response = requests.post(self.base_url, data=data)
        result = response.json()

        if response.status_code == 200:
            new_access_token = result.get("access_token")
            new_refresh_token = result.get("refresh_token")
            expires_in = result.get("expires_in")

            self.save_tokens(new_access_token, new_refresh_token, expires_in)

            print("새로운 액세스 토큰이 발급되었습니다.")
            print("리프레시 토큰이 갱신되었습니다.")

            return new_access_token
        else:
            print("토큰 갱신 실패. 상태 코드:", response.status_code)
            try:
                error_message = result.get("error_description")
                print("에러 메시지:", error_message)
            except Exception as e:
                print("에러 메시지를 가져오는 중 오류 발생")

            return None

