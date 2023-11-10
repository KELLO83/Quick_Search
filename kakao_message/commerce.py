# commerce.py
import json
import requests
from kakao_refresh_token import KakaoTokenManager

class Commerce:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_kakao_token(self):
        token_manager = KakaoTokenManager(self.client_id, self.client_secret)
        tokens = token_manager.load_tokens()

        # 토큰의 유효기간이 60초 미만이면 refresh 토큰 갱신
        if tokens["expires_in"] < 60:
            token_manager.refresh_access_token()
            tokens = token_manager.load_tokens()

        return tokens["access_token"]

    # 메시지 전송
    def send_kakao_message(self, title, image_url, link, price):
        url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
        access_token = self.get_kakao_token()

        headers = {
            "Authorization": "Bearer " + access_token
        }

        # commerce template message
        template_object = {
            "object_type": "commerce",
            "content": {
                "title": title,
                "image_url": image_url,
                "image_width": 640,
                "image_height": 640,
                "link": {
                    "web_url": link,
                    "mobile_web_url": link,
                    "android_execution_params": "contentId=100",
                    "ios_execution_params": "contentId=100"
                }
            },
            "commerce": {
                "regular_price": price
            },
            "buttons": [
                {
                    "title": "구매하기",
                    "link": {
                        "web_url": link,
                        "mobile_web_url": link,
                        "android_execution_params": "contentId=100&buy=true",
                        "ios_execution_params": "contentId=100&buy=true"
                    }
                },
                {
                    "title": "공유하기",
                    "link": {
                        "web_url": "https://style.kakao.com/main/women/contentId=100/share",
                        "mobile_web_url": "https://style.kakao.com/main/women/contentId=100/share",
                        "android_execution_params": "contentId=100&share=true",
                        "ios_execution_params": "contentId=100&share=true"
                    }
                }
            ]
        }

        data = {
            "template_object": json.dumps(template_object)
        }

        res = requests.post(url, data=data, headers=headers)

        # 전송 여부 확인 및 에러 메시지 출력
        if res.json().get('result_code') == 0:
            print('메시지 전송 완료')
        else:
            print('메시지 전송 중 오류가 발생했습니다. 오류메시지 : ' + str(res.json()))

        print("응답 코드:", res.status_code)
        print("응답 내용:", res.text)