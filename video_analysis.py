import cv2
import time
import numpy as np
from datetime import datetime
import time
import sys
from predictor import load_img,init_model,predict

def validity_condition(LINE_X1,LINE_Y1,LINE_X2,LINE_Y2,x,y,w,h,sensitivity):
	x_list = []
	y_list = []
	for i in range(LINE_X1 - w//sensitivity,LINE_X2 + w//sensitivity):
		x_list.append(i)
	for j in range(LINE_Y1 - h//sensitivity ,LINE_Y2):
		y_list.append(j)
	if x + w//2 in x_list and y + h//2 in y_list:
		return True
	else:
		False


def main(LINE_X1,LINE_Y1,LINE_X2,LINE_Y2,sensitivity,area,video_name):
    model = init_model()
    if video_name == "0":
        video_name = 0
    data = cv2.VideoCapture(video_name)
    frame_rate = 0
    frame = 0
    total_count = 0
    increment = 0
    first_frame = True
    start = time.time()
    while (data.isOpened()):
        _,image_data = data.read()
        #converting to grayscale 
        reference_data = cv2.resize(image_data,(800,800))
        image_dat = cv2.resize(image_data,(800,800))
        image_data = cv2.cvtColor(image_dat,cv2.COLOR_BGR2GRAY)

        #frame differncing
        if first_frame:
            previous_frame = image_data
            first_frame = False
            continue
        else:
            diff_image = cv2.absdiff(previous_frame,image_data)
            previous_frame = image_data

        #image thresholding
        ret, thresh = cv2.threshold(diff_image, 30 ,255,cv2.THRESH_BINARY)

        #image di
        kernel = np.ones((3,3), np.uint8)
        dilated = cv2.dilate(thresh,kernel,iterations = 1)

        #getting images
        contours,heirarchy = cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        valid_contours = []
        boxes = []
        confidences = []
        for i,cntr in enumerate(contours):
            x,y,w,h = cv2.boundingRect(cntr)
            boxes.append([x,y,w,h])
            confidences.append(w*h/1000)
        valid_boxes = []
        indexes = cv2.dnn.NMSBoxes(boxes,confidences, 0.45, 0.90)
        for i in boxes:
            x,y,w,h = i
            if w * h > area and validity_condition(LINE_X1,LINE_Y1,LINE_X2,LINE_Y2,x,y,w,h,sensitivity):
                crop_image = reference_data[y :int(y+1.2*h), x:int(x+1.2*w)]
                model_image = load_img(crop_image)
                output = predict(model_image,model)
                if output[2] > 0.8:
                    cv2.rectangle(image_dat,(x,y),(x + w,y + h),(0,0,255),3)
                    image_dat = cv2.putText(image_dat, str(output[1])  +'-'+ str(output[2]), (x +w,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255), 1, cv2.LINE_AA)
                    valid_boxes.append(i)
        
        # if len(valid_boxes) > 3:
        # 	increment  = len(valid_boxes) // 3
        # else:
        # 	increment = len(valid_boxes)
        total_count = total_count + len(valid_boxes)   
        date = datetime.now()
        frame = frame + 1
        frame_rate = frame/ (time.time() - start)

        print(str(date) + " count = " +  str(total_count))
        print(frame_rate)
        cv2.rectangle(image_dat,(LINE_X1,LINE_Y1),(LINE_X2,LINE_Y2),(255,0,0),2)
        
        # cv2.drawContours(image_dat,valid_contours,-1,(127,200,0),2)

        image_dat = cv2.putText(image_dat, 'frame rate = ' + str(frame_rate), (600,780),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255), 1, cv2.LINE_AA)
        image_dat = cv2.putText(image_dat, 'counts = ' + str(total_count), (10,780),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0), 1, cv2.LINE_AA)
        
        f = open("buffer.txt","w")
        f.write(str(total_count) + ',' + str(len(valid_boxes)) + ',' + str(frame_rate) +','+ '1')
        f.close()
        cv2.imshow("image",image_dat)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


#main(LINE_X1 = 153,LINE_Y1 = 573,LINE_X2 = 700,LINE_Y2 = 573,sensitivity = 25)


video_name = sys.argv[1]
x1 = int(sys.argv[2])
y1 = int(sys.argv[3])
x2 = int(sys.argv[4])
y2 = int(sys.argv[5])
s = int(sys.argv[6])
a = int(sys.argv[7])

main(LINE_X1 = x1,LINE_Y1 = y1,LINE_X2 = x2,LINE_Y2 = y2,sensitivity = s,area = a,video_name = video_name)
#j7_1 LINE_X1 = 134,LINE_Y1 = 666,LINE_X2 = 712,LINE_Y2 = 666,sensitivity = 20