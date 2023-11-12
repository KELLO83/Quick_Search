import os.path
import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox

class draw:

    def __init__(self,img : object) -> None:
            self.img = img
            self.save_path = ""
            self.rect_endpoint = []
            self.drawing = False
            self.img_to_show = None
            self.user_draw_location = []

    def user_draw_box(self,event,x,y,flags,param) -> list:

        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.rect_endpoint = [(x,y)]
            
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing is True:
                self.rect_endpoint[1:] = [(x,y)]
                img_temp = np.copy(self.img)
                cv2.rectangle(img_temp,self.rect_endpoint[0],self.rect_endpoint[1],(0,255,0),2)
                self.img_to_show = img_temp
                
        elif event == cv2.EVENT_LBUTTONUP:
            if len(self.rect_endpoint) > 1:  
               print(f"Start point {self.rect_endpoint[0]} , End point {self.rect_endpoint[-1]}")
               cv2.rectangle(self.img,self.rect_endpoint[0],(x,y),(0,255,0),1)
               self.img_to_show = np.copy(self.img)
               self.user_draw_location.append([self.rect_endpoint[0],(x,y)])
               print(f"DEBUG : {self.user_draw_location}")
               self.drawing = False
               
    def draw_run(self):
        self.img_to_show = np.copy(self.img)
        self.orginal_img = np.copy(self.img)
         
        window_name = 'test'
        cv2.namedWindow(window_name)
        cv2.setMouseCallback(window_name, self.user_draw_box)
        
        while True:
            
            try:
                if cv2.getWindowProperty(window_name,0) == -1:
                    pass
            except:
                print("그리기를 종료합니다")
                self.show_exit('q')
                break
            
            cv2.imshow(window_name, self.img_to_show)
            k = cv2.waitKey(1)
            if k == ord('q') :
                print("그리기를 종료합니다")
                self.show_exit('q')
                break
            
            if k == ord('r'):
                print("그림을 초기화 합니다.")
                self.user_draw_location = []
                self.show_exit('r')
                self.img_to_show = np.copy(self.orginal_img)
                self.img = np.copy(self.orginal_img)
                
            if k == ord('s'):
                flag = self.show_exit('s')
                
                if flag == True:
                    cv2.imwrite(self.save_path + "draw_img.jpg",self.img)
                    self.show_exit('q')
                    break
            
        cv2.destroyAllWindows()

        return self.user_draw_location

    def show_exit(self,args) -> bool:
        root = tk.Tk()
        root.withdraw()
        print("args 멈춤확인 {}".format(args))
        if args == 'q':
            messagebox.showinfo("showinfo", "그리기 프로그램을 종료합니다.")
            root.destroy()
            return True
            
        elif  args == 'r':
            messagebox.showinfo("showinfo", "그림을 초기화 합니다.")
            root.destroy()
            return True
            
        elif args == 's':
            response = messagebox.askokcancel("그림을 저장하겠습니까?", "저장하시려면 ok를 눌러주세요")
            if response:
                messagebox.showinfo("showinfo","그림을 저장합니다")
                return True
            else:
                messagebox.showinfo("showinfo", "그림을 저장하지 않습니다.")
                return False
            

                   
"""if __name__ == "__main__":
    PATH = "Image_process/detect_target.jpg"
    draw = draw(cv2.imread(PATH))
    xylist = draw.draw_run()

    print("결과 2차원 리스트 : ",xylist)"""