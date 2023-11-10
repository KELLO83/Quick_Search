import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append("C/Users/user/Quick_Search/Image_process")
print(sys.path)
#from Image_process import Multi_detect as det
import Image_process.Multi_detect
# 객체 탐지 컨트롤러
# class detect_con:

#     def test2_detection(img_path, classname):
#         run = det.Multi_detect(img_path, classname)
#         run.detect_run()
#         run.save()


# run = det.Multi_detect("Image_process/detect_target.jpg", "shoes")
# run.detect_run()
# run.save()

run = Image_process.Multi_detect.Multi_detect("Image_process/detect_target.jpg",'shoes')
run.detect_run()
run.save()