import os.path
import pandas as pd
import torch
import traceback
import sys
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt
import Image_process.filter as filter

class Multi_detect():
    def __init__(self,img,productname:str) -> None:
        self.img = img 
        self.model_path  = ["Model/Cap.pt",
                            "Model/Shoes.pt",
                            "Model/Clothes.pt"]

        for i in range(len(self.model_path)):
            if not os.path.isfile(self.model_path[i]):
                print("Model {} 존재하지않습니다".format(self.model_path[i]))
                raise FileExistsError
            
        self.model = []
        init_start = time.time()
        for i in range(len(self.model_path)):
            start = time.time()
            print("model_path 추가중.... {}".format(self.model_path[i]))
            self.model.append(torch.hub.load('ultralytics/yolov5','custom',path=self.model_path[i]))
            end = time.time()
            print("소요시간 ...{}".format(abs(end-start)))
            
        print("전체 소요시간 ...{}".format(abs(end-init_start)))

        self.DataFrame = pd.DataFrame(columns=['xmin', 'ymin', 'xmax', 'ymax', 'confidence', 'class', 'name'])
        self.object_location  = []
        self.object_location_dict ={}
        self.classification = []
        self.confidence_vulnerability = []
        self.productname = productname
        
           
    def detect_run(self) :
        for i in range(len(self.model_path)):
            if self.img == None:
                print("detect_run  실행중... 이미지가 존재하지않습니다")
                raise FileNotFoundError
            
            result = self.model[i](self.img , size=640)
            
            result.print()
            # result.show()

            locate = result.pandas().xyxy[0]
            print("locate .... {}".format(locate))
            print("locate type {}".format(type(locate)))
            
            self.DataFrame = pd.concat([self.DataFrame,locate]).reset_index(drop=True)

        print("필터링 수행전 DataFrame결과출력...... :",self.DataFrame)
        # 필터링
        self.DataFrame = filter.filter_run(self.productname, self.DataFrame)
        
        print("DataFrame결과출력......")
        print(self.DataFrame)
        self.get_object_location()
        return self.DataFrame
    
    def get_object_location(self):
        try:
            for i in range(len(self.DataFrame)):
                product_number = i
                self.object_location.append([self.DataFrame['xmin'][i],self.DataFrame['xmax'][i],
                                            self.DataFrame['ymin'][i],self.DataFrame['ymax'][i]])

                self.object_location_dict[product_number] = [self.DataFrame['xmin'][i],self.DataFrame['xmax'][i],
                                            self.DataFrame['ymin'][i],self.DataFrame['ymax'][i]]

                if self.DataFrame['confidence'][i] <= 0.5:
                    self.confidence_vulnerability.append(i)
                    
                          
                for i in range(len(self.DataFrame)): # 식별 상품 이름 저장
                    self.classification.append(self.DataFrame['name'][i])
        except:
            print("Error sys.exc_info[0]: {}".format(sys.exc_info()[0]))
            print("Error sys.exc_info[2]: {}".format(sys.exc_info()[2]))
            print("Error : {}".format(traceback.print_exc()))
            return False

    def save(self):
        print("csv파일로 저장합니다....")
        self.DataFrame.to_csv('output.csv')
        buffer = self.DataFrame[['xmin','ymin','xmax','ymax']]
        
        if os.path.isdir("./label_result"):
            pass
        else:
            os.mkdir("./label_result")

        save_path = "./label_result/"      
        
        buffer.to_csv("{}/output.txt".format(save_path),index=False,header=False,sep=" ")
        
        # self.bound_box() # Test용 코드입니다 시각화박스가 잘그렸졌는지확인 실제 적용시 주석처리해주세요
        print("DEBUG")
        
    def bound_box(self):
        img = cv2.imread(self.img)
        convert_type = []
        for i in range(len(self.object_location)):
            buffer = list(map(lambda x : int(float(x)), self.object_location[i]))
            convert_type.append(buffer)
        
        for i in range(len(convert_type)):
            cv2.rectangle(img,(convert_type[i][0],convert_type[i][2]),(convert_type[i][1],convert_type[i][3]),(0,0,255),2) 
            cv2.putText(img,self.classification[i],(convert_type[i][0],convert_type[i][2]-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,color=(0,0,255),thickness=2)

        img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        plt.imshow(img_rgb) 
        plt.show()
        
if __name__ == "__main__":
    print("Testing.......")
    img = "Image_process/detect_target.jpg"

    run = Multi_detect(img,'shoes') # 찾고자하는 상품명도 인자로 받아서 DataFrame에서 Name으로 필터링해주면됨
    run.detect_run()
    run.save()