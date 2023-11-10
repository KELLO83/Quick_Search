from detect_controller import detect_con as det


img_path = "Image_process/detect_target.jpg"
txt_path = "label_result/output.txt"

#det.detection(img_path, "shoes")

det.user_draw(img_path, txt_path)