import sys, os, cv2
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append("C/Users/user/Quick_Search/Image_process")
import Image_process.Multi_detect as det
import Image_process.draw as dr

# 객체 탐지 컨트롤러
class detect_con:
    def __init__(self,img_path,productname:str) -> None:
        self.img_path = img_path
        self.productname = productname

    # detect 결과 label_result 폴더에 output.txt 생성(좌표값)
    def detection(img_path, classname):
        run = det.Multi_detect(img_path, classname)
        run.detect_run()
        run.save()

    def user_draw(img_path, txt_path):
        draw = dr.draw(cv2.imread(img_path))
        xylist = draw.draw_run()
        result_list = []

        # draw 결과값(2차원리스트) 튜플 -> min max 순서에 맞게 리스트화
        for i in range(len(xylist)):
            for j in range(len(xylist[i])):
                xy = str(xylist[i][j])[1:-1]
                xy = xy.replace(", ", " ").split()
                
                # xmin ymax xmax ymin -> xmin ymin xmax ymax
                if j == 0:
                    xmin = xy[0]
                    ymax = xy[1]
                elif j == 1:
                    xmax = xy[0]
                    ymin = xy[1]

            result_list.append([xmin, ymin, xmax, ymax])
        
        #output.txt에 리스트 내용 추가하기
        with open(txt_path, "a") as file:
            for i in range(len(result_list)):
                for j in range(4):
                    file.write(result_list[i][j])
                    file.write(" ")
                file.write("\n")

if __name__ == "__main__":
    pass