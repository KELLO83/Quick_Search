import os
import Image_process.Multi_detect as det

# 객체 탐지 컨트롤러
class detect_controller:

    def detection(img_path):
        detect = det.detect_class(img_path)
        detect.detect_run()
        print(detect.get_object_all_locatin)
        print(detect.get_vulnerability)

        for key,value in detect.object_location_dict.items():
            print("key : {} , value : {}".format(key,value))

        detect.get_bound_box()
        detect.draw_run()
        detect.get_label_location()
