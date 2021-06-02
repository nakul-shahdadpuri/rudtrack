import cv2
import requests
import io
import numpy as np
import sys
from stream_reader import *
from config import *
from config import *
from datetime import datetime




def nayanam(LINE_X1,LINE_Y1,LINE_X2,LINE_Y2):
    total_count = 0
    first_frame = True
    mr = MjpegReader(URL_russia)
    for content in mr.iter_content():
        image_data = cv2.imdecode(np.frombuffer(content, dtype=np.uint8), cv2.IMREAD_COLOR)
        #converting to grayscale 
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
        contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        valid_contours = []
        for i,cntr in enumerate(contours):
            x,y,w,h = cv2.boundingRect(cntr)
            if (cv2.contourArea(cntr) >= 25) and validity_condition(LINE_X1,LINE_Y1,LINE_X2,LINE_Y2,x,y):
                valid_contours.append(cntr)
        
        total_count = total_count + len(valid_contours)   
        date = datetime.now()  
        print(str(date) + " count = " +  str(total_count))
        cv2.rectangle(image_dat,(LINE_X1,LINE_Y1),(LINE_X2,LINE_Y2),(255,0,0),2)
        cv2.drawContours(image_dat,valid_contours,-1,(127,200,0),2)


        cv2.imshow("image",image_dat)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()