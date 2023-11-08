import os
import class_detect as det

import crop
import cv2

import resize

class Controller:

    # 객체 탐지 컨트롤러
    def detect_con(img_path):
        detect = det.detect_class(img_path)
        detect.detect_run()
        print(detect.get_object_all_locatin)
        print(detect.get_vulnerability)

        for key,value in detect.object_location_dict.items():
            print("key : {} , value : {}".format(key,value))

        detect.get_bound_box()
        detect.draw_run()
        detect.get_label_location()

    # 크롭 컨트롤러
    def crop_con(img_path, label_txt):
        crop_object = crop.crop(cv2.imread(img_path), label_txt)
        crop_object.crop()
        print("Crop success!")


    # 이미지 크기 변환 컨트롤러
    # cv2로 이미지를 읽고, 1.3배 200x200보다 작은 경우
    def resize_con(crop_folder):
        
        # 폴더 안의 내용 전부 resize하도록 반복
        for inner_folder in os.listdir(crop_folder):
            folder_path = os.path.join(crop_folder, inner_folder)
            for img_path in os.listdir(folder_path):
                img = cv2.imread(img_path, cv2.IMREAD_COLOR)
                height, width, channels = img.shape

        rs = resize.resize_img(cv2.imread("crop_dir/3/0.jpg"))
        new_image = rs.ration_resize(size = (200,200))
        cv2.imshow("new_image",new_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()