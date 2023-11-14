import os
import Image_process.crop as crop
import cv2
import Image_process.opencv_ration_resize_class as r

class img_controller:

    # 크롭 컨트롤러
    # 11/15 문제 발생 - 사용자 크롭을 통해 추가된 좌표값은 crop하지 못하고 오류가 남
    def crop_con(img_path, label_txt):
        crop_object = crop.crop(cv2.imread(img_path), label_txt)
        crop_object.crop()
        print("Crop success!")


    # 이미지 크기 변환 컨트롤러
    # cv2로 이미지를 읽고, 1.3배 200x200보다 작은 경우
    def resize_con(crop_folder):
        # 폴더 안의 내용 전부 resize하도록 반복
        for crop_img in os.listdir(crop_folder):
            img_path = "./crop_dir/" + crop_img

            # 이미지 읽고 크기 가져오기 .shape
            img = cv2.imread(img_path, cv2.IMREAD_COLOR)
            height, width, channel = img.shape

            if(height<200 or width<200):
                resize = r.resize_img(img)
                new_image = resize.ration_resize(size = (200,200))  # (width*1.3, height*1.3) 넣으면 오류 size 값이 바꾸고 싶은 크기인지?
                cv2.imshow("new_image",new_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                pass

        print("\n\nresize 실행 완료")