import cv2
import numpy as np

class resize_img:
    def __init__(self,img:object) -> None:
        self.img = img
        self.height , self.width , self.channel = img.shape
        
    def ration_resize(self,size = None,padColor = 0) -> object:
        h , w = self.height , self.width
        
        sh , sw = size
  
        if h > sh or w > sw: # 이미지가 size보다 크면 h w 초과
            print("Debug h > sh or w > sw")
            """ CV2.Inter_AREA"""
            interp = None # cv2.INTER_AREA (영역 보간법) 영역축소 -> 영영축소 필요성 x
        else:  # 하나라도 작거나 둘다 작으면
            interp = cv2.INTER_LANCZOS4 # Lanczoz 보간법 8*8 픽셀 참조
            
        aspect = h / w # Image Ratio
        
        if aspect > 1 : #  h > w  Exceed height
            new_w = sw 
            new_h = np.round(new_w / aspect).astype(int) 
            pad_vert = (sh - new_h) / 2
            pad_top , pad_bot = np.floor(pad_vert).astype(int) , np.ceil(pad_vert).astype(int)
            pad_left , pad_right = 0 , 0
        
        elif aspect < 1 : # h < w  Exceed width w가 더 크다
            new_h = sh 
            new_w = np.round(new_h * aspect).astype(int)
            pad_horz = (sw - new_w) / 2
            pad_left , pad_right = np.floor(pad_horz).astype(int) , np.ceil(pad_horz).astype(int)
            pad_top , pad_bot = 0 , 0
            
        else: # 비율 1 : 1 조정 x
            new_h , new_w = sh , sw
            pad_left , pad_right , pad_top , pad_bot = 0 , 0 , 0 , 0
            
        print("===========================================")
        print(f"IMG TYPE {type(self.img)}")
        print("===========================================")
        if self.img.shape[2] != 3 and not isinstance(padColor , (list,tuple,np.ndarray)): # RGB가 아니라면
            """ RGB변형"""
            padColor = [padColor] * 3 
        
        
        res_img = cv2.resize(self.img, (new_w , new_h) , interpolation = interp) # interpolation = 보간법
        # res_img = cv2.copyMakeBorder(res_img , pad_top , pad_bot , pad_left , pad_right 
        #                              , borderType = cv2.BORDER_CONSTANT , value = padColor)  # cv2.BODER_CONSTANT : 테두리 색상을 일정하게 유지
                                        
        return res_img # 변환결과 반환
                    
if __name__ == "__main__":
    rs = resize_img(cv2.imread("crop_dir/3/0.jpg"))
    new_image = rs.ration_resize(size = (200,200))
    cv2.imshow("new_image",new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    