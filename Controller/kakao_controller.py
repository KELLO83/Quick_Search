import kakao_message.commerce as c

def kakao_message(prod_info):
    # 테스트용 상품 정보 임시설정
    #title = "아디다스 삼바 OG 클라우드 화이트"
    #image_url = "https://kream-phinf.pstatic.net/MjAyMTAzMDVfMjQz/MDAxNjE0OTE0NzIzMTQ4.tsuFUJtHGm4g4KE5EDikVMScORptOQqIB7afi1Nz2Qwg.sftz3YQOuw48xpNSJa1tV4uEsz5iU4mjIvpllgHWEn8g.PNG/p_8f7b72adbc924b5bbf7c670d55865e6b.png?type=m"
    #link = "https://kream.co.kr/products/15251"
    #price = 16900

    title = str(prod_info['brand']) + str(prod_info['product_name'])

    # Commerce 클래스의 인스턴스 생성 시 client_id와 client_secret 전달
    commerce_instance = c.Commerce(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET")

    # Commerce 클래스의 send_kakao_message 메서드 호출
    commerce_instance.send_kakao_message(title, prod_info['image_url'], prod_info['link'], prod_info['price'])
