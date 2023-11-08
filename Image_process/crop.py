# Image crop class
import cv2
import os

class crop : 

    def __init__(self,img : str, label_txt_path : str) -> None:
        self.img = img # 원본이미지경로
        self.label_txt_path = label_txt_path
        self.path = self.confirmation_dir()
        self.crop_image = []
        self.location = []

        # txt 파일 내용 존재 여부 확인 후 location 리스트에 좌표값 추가(2차원 리스트) # 수정필요..... 10/27 txt파일형식 xmin ymin xmax ymax 이후 그런 값들이 차례로 행으로 출력됨...
        if (os.path.isfile(self.label_txt_path)):
            with open(label_txt_path,'r') as txt:
                n = 0
                for line in txt:
                    self.location.append(line.split())
                    del self.location[n][0]  # 라벨번호 빼고 좌표값만 저장
                    n += 1
        
        
    def crop(self) -> object :
        " Image crop   return  Image Obejct"
        """ xmin , xmax , ymin , ymax 값으로 이미지를 자르세요"""
    
        for i, value in enumerate(self.location):
            xmin, ymin, xmax, ymax = map(lambda x: int(float(x)), value)
            print(xmin, ymin, xmax, ymax)
            cv2.imwrite(self.path + str(i) + ".jpg", self.img[ymin:ymax, xmin:xmax])
        
        print(f"Save Image path : {self.path}")

    def confirmation_dir(self) -> str:
        count = 1
        if os.path.isdir("./crop_dir"):
            pass
        else:
            os.mkdir("./crop_dir")

        while True:
            if os.path.isdir("./crop_dir/{}".format(count)):
                count += 1
            else:
                print("Generate Folder : ./crop_dir/{}".format(count))
                os.makedirs("./crop_dir/{}".format(count))
                save_path = "./crop_dir/{}/".format(count)
                return  save_path

    def __str__ (self) ->None:
        for key,value in self.dict_location.items():
            print("key : {} , value : {}".format(key,value))

if __name__ == "__main__":
    "test code"
    # key : 0 , value : [208.87770080566406, 336.2223815917969, 922.2138061523438, 1004.7623901367188]
    #key : 1 , value : [348.85107421875, 425.29705810546875, 877.2025146484375, 971.7975463867188]
    # n[0, 0.581, 0.3489795918367347, 0.53, 0.2108843537414966]
    crop_object = crop(cv2.imread("C:/Users/user/Destop/test/testimg.jpg"), "C:/Users/user/Quick_Search/label_result/0/output.txt")
    crop_object.crop()

    print("Crop success!")


    