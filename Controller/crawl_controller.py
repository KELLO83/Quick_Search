import os
import Site_crawling.object_name as co
import Site_crawling.site_name as cs

def crawl_objectname(img_path):
    keyword = co.upload_image_and_extract_keyword(img_path) # Site_crawling/target.jpg
    print("\nobject_name 크롤링 결과 : ", keyword)
    return keyword


def crawl_sitename(name_list):
    crawler = cs.ProductCrawler()

    for name in name_list:    
        result = crawler.crawl_product(name)
        if result!= None:
            break;

    #search_keyword = input("검색할 키워드를 입력하세요: ")
    #res = crawler.crawl_product(search_keyword)   # crawl_product 메서드 호출 매개변수 : 키워드 str // 반환값 : dict 형태
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
    print("\n[[크롤링 결과]]\n", result)
    return result

# 메인에서 이 함수만 실행하면 됨
def crawling(img_path):
    # 크롭 이미지 존재 여부 확인
    if os.path.isfile(img_path):
        pass
    else:
        print("Image File Not Exist")
        raise  FileNotFoundError

    product_name = crawl_objectname(img_path)
    prod_info = crawl_sitename(product_name)
    return prod_info
