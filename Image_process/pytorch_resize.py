import torchvision.transforms as T # import torchvision 
import os
import PIL
import matplotlib.pyplot as plt

def resize(img_path , widht , height):
    img =  PIL.Image.open(img_path)
    
    preprocess = T.Compose([
        T.Resize((widht,height))
    ])
    
    img_resized = preprocess(img)
    return img_resized



if __name__ == "__main__":
    img_path = "Image_process/detect_target.jpg"
    if not os.path.isfile(img_path):
        raise Exception("Image not found")
    width = 300
    height = 300
    
    res = resize(img_path,width, height)
    
    plt.imshow(res)
    plt.show()
    
    res.save("Image_process/detect_target_resized.jpg")
    
    
