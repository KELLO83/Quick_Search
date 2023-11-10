#kakao_token.py
import requests
import json

class token():
    url = "https://kauth.kakao.com/oauth/token"

    data = {
        "grant_type" : "authorization_code",
        "client_id" : "64c65b11be9bb8fa9443e4e6490f6f42",
        "redirect_uri" : "https://example.com/oauth",
        "code" : "uypP1Pj2unTNwQaXfxEV5kg3boUv0ekf3vWFgc-L0sd6vXf_nFFW9NeQKLIKPXSXAAABi2XR2L6BPKUF0hG4dQ"
    }

    response = requests.post(url, data=data)
    tokens = response.json()

    # 토큰을 파일로 저장하기
    if "access_token" in tokens:
        with open("token.json", "w") as fp:
            json.dump(tokens, fp)
            print("토큰 저장 완료")
            print(tokens["access_token"])
    else:
        print(tokens)