# Image crop class
import cv2
import os

xmin = 100
ymin = 156
xmax = 469
ymax = 337

path = "./crop_dir/"
img = cv2.imread("C:/Users/user/Quick_Search/Image_process/detect_target.jpg")

cv2.imshow(img)

txt_file = "./label_result/output.txt"
location = []
"""
if (os.path.isfile(txt_file)):
    with open(txt_file,'r') as txt:
        n = 0
        for line in txt:
            location.append(line.split())
            #del self.location[n][0]  # 라벨번호 빼고 좌표값만 저장
            n += 1

for i, value in enumerate(location):
    xmin, ymin, xmax, ymax = map(lambda x: int(float(x)), value)
    print(xmin, ymin, xmax, ymax)
    print(path+str(i)+".jpg")
    cv2.imwrite(path + str(i) + ".jpg", img[ymin:ymax, xmin:xmax])"""

"""for i in range(3):
    print(xmin, ymin, xmax, ymax)
    cv2.imwrite(path + str(i) + ".jpg", img[156:337, 100:156])"""