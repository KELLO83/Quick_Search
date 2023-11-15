import os
import Image_process.crop as crop
import cv2
import Image_process.opencv_ration_resize_class as r

class img_controller:

    # 크롭 컨트롤러
    def crop_con(img_path, label_txt):
        
        # crop 폴더에 남아있는 이미지파일 삭제
        if os.path.exists("./crop_dir/"):
            for file in os.scandir("./crop_dir/"):
                os.remove(file.path)
                print("[[ clear crop folder ]]")
        else:
            pass

        #크롭
        crop_object = crop.crop(cv2.imread(img_path), label_txt)
        crop_object.crop()
        print("Crop success!")


    # 이미지 크기 변환 컨트롤러
    # cv2로 이미지를 읽고 200x200보다 작은 경우 1.5배
    def resize_con(crop_folder):
        # 폴더 안의 내용 전부 resize하도록 반복
        for crop_img in os.listdir(crop_folder):
            img_path = "./crop_dir/" + crop_img

            # 이미지 읽고 크기 가져오기 .shape
            img = cv2.imread(img_path, cv2.IMREAD_COLOR)
            height, width, channel = img.shape

            if(height<200 or width<200):
                resize = r.resize_img(img)
                new_image = resize.ration_resize(size = (int(width*1.5), int(height*1.5)))
            else:
                pass

        print("\n\nresize 실행 완료")