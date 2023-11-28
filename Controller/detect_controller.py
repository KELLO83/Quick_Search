import os, cv2
import Image_process.Multi_detect as det
import Image_process.draw as dr

# 객체 탐지 컨트롤러
class detect_con:
    def __init__(self,img_path,productname:str) -> None:
        self.img_path = img_path
        self.productname = productname

    # detect 결과 label_result 폴더에 output.txt 생성(좌표값)
    def detection(self):
        run = det.Multi_detect(self.img_path, self.productname)
        run.detect_run()
        run.save()

    def user_draw(self):
        txt_path = "label_result/output.txt"
        if not os.path.isfile(txt_path):
            print("output.txt가 존재하지 않습니다.")
            raise FileExistsError
        
        draw = dr.draw(cv2.imread(self.img_path))
        xylist = draw.draw_run()
        result_list = []

        h = int(cv2.imread("./Image_process/detect_target.jpg").shape[1])

        # draw 결과값(2차원리스트) 튜플 -> min max 순서에 맞게 리스트화
        for i in range(len(xylist)):
            for j in range(len(xylist[i])):
                xy = str(xylist[i][j])[1:-1]
                xy = xy.replace(", ", " ").split()
                
                if j == 0:
                    xmin = xy[0]
                    ymin = xy[1]
                elif j == 1:
                    xmax = xy[0]
                    ymax = xy[1]

            result_list.append([xmin, ymin, xmax, ymax])
        
        #output.txt에 리스트 내용 추가하기
        with open(txt_path, "a") as file:
            for i in range(len(result_list)):
                for j in range(4):
                    file.write(result_list[i][j])
                    file.write(" ")
                file.write("\n")
                
def call(img_path,category):
    run = detect_con(img_path,category)
    run.detection()
    run.user_draw()
    
if __name__ == "__main__":
    pass