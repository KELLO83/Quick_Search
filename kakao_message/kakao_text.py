import requests
import json

#발행한 토큰 불러오기
with open("token.json","r") as kakao:
    tokens = json.load(kakao)

url="https://kapi.kakao.com/vs/api/talk/memo/default/send"

headers={
    "Authorization" : "Bearer" + tokens["access_token"]
}

data = {
    'object_type' : 'text',
    'text' : '테스트입니다.',
    'link' : {
        'web_url': 'https://naver.com',
        'mobile_web_url': 'https://developers.kakao.com'
    },
    'button_title': '키워드'
}

data={'template_object':json.dumps(data)}
response=requests.post(url,headers=headers, data=data)
response.status_code