import Controller.detect_controller as det
import copy
def get_imageinformation(img_path,category):
    """ GUI 로부터 선택한 사진의 경로와 카테고리를 받아옵니다. """

    
    # names: ['long-pants', 'long-sleeve', 'short-pants', 'short-sleeve', 'sleeveless'] ---> 상하의 인공지능이 구별하는것.. <메모>
    top = ['long-sleeve','short-sleeve','sleeveless']
    bottom = ['long-pants','short-pants']
    
    target = None
    
    if category == "top":
        target = copy.deepcopy(top)
    elif category == "bottom":
        target = copy.deepcopy(bottom)
        
    print(f"detect_controller 전달전 검사.. 실행 사진경로 {img_path} 사용자 검색 카테고리 {target}")
    det.call(img_path,target)
    
    
    
    
    
    
    
    