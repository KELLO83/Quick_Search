from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import time

class ProductCrawler:
    def __init__(self):
        # 브라우저 창 없이 실행
        self.firefox_options = Options()
        self.firefox_options.add_argument("--headless")

        # Firefox 웹 드라이버 초기화
        self.driver = webdriver.Firefox(options=self.firefox_options)
        
        # 사이트별 정보 및 요소 이름 정의
        self.websites_data = {
            "크림": {
                "url": "https://kream.co.kr/search?keyword= &tab=products",
                "search_selector": "input.input_search.show_placeholder_on_focus",
                "brand_selector": "p.product_info_brand.brand",
                "product_name_selector": "p.translated_name",
                "price_selector": "p.amount",
                "link_selector": "a.item_inner",
                "imgurl_selector": "img.image.full_width",
                "no_result_selector": "div.product_list.recently_viewed",
            },
            "무신사": {
                "url": "https://www.musinsa.com/app/",
                "search_selector": "input#commonLayoutSearchForm.sc-1ppcy5v-3.ljHcMG",
                "brand_selector": "p.item_title",
                "product_name_selector": "p.list_info",
                "price_selector": "p.price",
                "imgurl_selector": "img.lazyload.lazy",
                "link_selector": "a.img-block",
                "no_result_selector": "div.search-nr-case",
            },
            "11번가": {
                "url": "https://www.11st.co.kr/",
                "search_selector": "input.search_text",
                "brand_selector": "dd.c-seller__name",
                "product_name_selector": "div.c-card-item__name > dd",
                "price_selector": "dd.c-card-item__price",
                "imgurl_selector": "img",
                "link_selector": "a.c-card-item__anchor",
                "no_result_selector": "section#section_noSearchData.search_section",
            },
        }
        # 상품을 찾았는지 나타내는 변수
        self.product_found = False

        self.target = None

    def crawl_product(self, search_keyword) -> dict:
        """ 키워드 str 상품명을 입력받고 성공시 target dict 반환 실패시 None 반환 target = 상품정보  dict"""

        for site, data in self.websites_data.items():
            url = data["url"]
            search_selector = data["search_selector"]
            product_name_selector = data["product_name_selector"]
            price_selector = data["price_selector"]
            brand_selector = data["brand_selector"]
            link_selector = data["link_selector"]
            imgurl_selector = data["imgurl_selector"]
            no_result_selector = data["no_result_selector"]

            # 사이트 방문
            self.driver.get(url)

            try:
                # 검색창 찾기
                search_element = self.driver.find_element(By.CSS_SELECTOR, search_selector)
                # 검색 키워드 입력
                search_element.send_keys(search_keyword)
                search_element.send_keys(Keys.RETURN)
                time.sleep(1)

                no_result_elements = self.driver.find_elements(By.CSS_SELECTOR, no_result_selector)

                if no_result_elements:
                    print(f"{site} 사이트에서 상품을 찾을 수 없습니다.")
                    continue  # 상품을 찾을 수 없음 다음 사이트로 이동

                # 상품 정보 추출
                product_name = self.driver.find_element(By.CSS_SELECTOR, product_name_selector).text.strip()
                price = self.driver.find_element(By.CSS_SELECTOR, price_selector).text.strip().split()[0]
                brand = self.driver.find_element(By.CSS_SELECTOR, brand_selector).text.strip()
                link = self.driver.find_element(By.CSS_SELECTOR, link_selector)
                imgurl = self.driver.find_element(By.CSS_SELECTOR, imgurl_selector)

                print("사이트명:", site)
                print("브랜드명:", brand)
                print("상품 이름:", product_name)
                print("가격:", price)
                print("구매페이지 URL:", link.get_attribute("href"))
                print("상품 이미지 URL:", imgurl.get_attribute("src"))
                print('-' * 40)
                self.product_found = True

                target = {
                    "site": site,
                    "brand": brand,
                    "product_name": product_name,
                    "price": price,
                    "link": link.get_attribute("href"),
                    "imgurl": imgurl.get_attribute("src"),
                }

                # 상품을 찾으면 크롤링 중단
                break
            except Exception as e:
                print(f"오류 발생: {str(e)}")

        if not self.product_found:
            print("모든 사이트에서 상품을 찾을 수 없습니다.")
            return self.target # None 반환

        return target

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    print("TEST CODE 입니다 ....")
    crawler = ProductCrawler()
    search_keyword = input("검색할 키워드를 입력하세요: ")
    res = crawler.crawl_product(search_keyword)   # crawl_product 메서드 호출 매개변수 : 키워드 str // 반환값 : dict 형태
    """ 만약 target = None 이라면 정보를 찾지못한거입니다//....
     target = {
                    "site": site,
                    "brand": brand,
                    "product_name": product_name,
                    "price": price,
                    "link": link.get_attribute("href"),
                    "imgurl": imgurl.get_attribute("src"),
                }    
    """
    crawler.close()

    print(res)