import os
import Image_process.crop as crop
import cv2
import Image_process.pytorch_resize as torch_resize

class img_controller:


    def __init__(self , img_path , crop_folder,label_txt) -> None:
        self.img_path = img_path
        self.crop_folder = crop_folder
        self.label_txt = label_txt
        
        
    # 크롭 컨트롤러
    def crop_con(self):
        
        # crop 폴더에 남아있는 이미지파일 삭제
        if os.path.exists("./crop_dir/"):  # Hard coding
            for file in os.scandir("./crop_dir/"):
                os.remove(file.path)
                print("[[ clear crop folder ]]")
        else:
            pass

        #크롭
        crop_object = crop.crop(cv2.imread(self.img_path), self.label_txt)
        crop_object.crop()
        print("Crop success!")


    # 이미지 크기 변환 컨트롤러
    # cv2로 이미지를 읽고 200x200보다 작은 경우 width/height 중 하나를 400px에 맞춰 키움
    def resize_con(self):
        # 폴더 안의 내용 전부 resize하도록 반복
        for crop_img in os.listdir(self.crop_folder):
            img_path = "./crop_dir/" +  crop_img

            # 이미지 읽고 크기 가져오기 .shape
            img = cv2.imread(img_path, cv2.IMREAD_COLOR)
            height, width , _  = img.shape
            # print("\n\n w,h확인 >> height : ", height, "\twidth : ", width, "\n\n")

            if(height<100 or width<100):
                new_img = torch_resize.resize(img,width,height)
                # print("\n\n 변환된 w,h 확인 >> height : ", new_image.shape[0], "\twidth : ", new_image.shape[1], "\n\n")
                cv2.imwrite(img_path, new_img)
            else:
                pass

        print("\n\nresize 실행 완료")   