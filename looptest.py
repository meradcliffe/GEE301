# References Used: https://github.com/lihuang3/ur5_ROS-Gazebo
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
#https://stackoverflow.com/questions/23398926/drawing-bounding-box-around-given-size-area-contour
import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)
timeout = time.time() + 60*2  # 30 seconds from now
while(1):

    # Take each frame
    _, frame = cap.read()
    
    
    
    for i2 in range(6): 
    
    # define range of blue color in HSV
        if i2==0: #blue
            blueimage=frame.copy()
            hsvblue = cv2.cvtColor(blueimage, cv2.COLOR_BGR2HSV)
            blurblue=cv2.GaussianBlur(hsvblue,(5,5),0)
            lower_blue = np.array([102,100,100])
            upper_blue = np.array([110,250,250])
            maskblue = cv2.inRange(blurblue, lower_blue, upper_blue)
            res = cv2.bitwise_and(blueimage,blueimage, mask= maskblue)
            cnts,hierarchy = cv2.findContours(maskblue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
            Mblue=cv2.moments(maskblue)
            if Mblue['m00']> 0:
                cx = int(Mblue['m10']/Mblue['m00'])
                cy = int(Mblue['m01']/Mblue['m00'])
                for i, c in enumerate(cnts):
                    area = cv2.contourArea(c)
                    if area > 9000:
                      cv2.circle(res, (cx, cy), 10, (0,0,0), -1)
                      rectangle = cv2.boundingRect(c) 
                      x,y,w,h = rectangle
                      print('width is',w)
                      print('height is ',h)
                      apparent_area=(h/42.7)*(w/42.7)
                      real_area=45
                      area_constant=real_area/apparent_area
                      corrected_area=area_constant*apparent_area
                      if real_area-5<corrected_area<real_area+5:
                          print('Correct Area Detected')
                      Distance=9*526.7/w
                      print('Distance is',Distance)
                      if rectangle[2] < 50 or rectangle[3] < 50: continue
                      cv2.rectangle(res,(x,y),(x+w,y+h),(0,255,0),2)
                      cv2.putText(res, "({}, {})".format(int(cx), int(cy)), (int(cx-5), int(cy+15)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                      cv2.putText(res, "Distance:" + str(float(Distance)) .format(int(cx), int(cy+50)), (int(cx-50), int(cy+50)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                      cv2.putText(res, "Area Constant:" + str(float(area_constant)) .format(int(cx+5), int(cy-50)), (int(cx+50), int(cy-50)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                      cv2.drawContours(res, cnts, 0, (255, 255, 255),1)
                      print('Blue Object Detected')
        if i2==1:#green
            greenimage=frame.copy()
            hsvgreen=cv2.cvtColor(greenimage,cv2.COLOR_BGR2HSV)
            blurgreen=cv2.GaussianBlur(hsvgreen,(5,5),0)
            lower_green=np.array([40,50,50])
            upper_green=np.array([80,255,255])
            maskgreen = cv2.inRange(blurgreen, lower_green, upper_green)
            resg= cv2.bitwise_and(greenimage,greenimage, mask= maskgreen)
            cnts1,hierarchy = cv2.findContours(maskgreen.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]#need to clone these stuff
            Mgreen=cv2.moments(maskgreen)
            if Mgreen['m00']> 0:
                cx1 = int(Mgreen['m10']/Mgreen['m00'])
                cy1 = int(Mgreen['m01']/Mgreen['m00'])
                contour_sizes1 = [(cv2.contourArea(contour1), contour1) for contour1 in cnts1]
                biggest_contour1 = max(contour_sizes1, key=lambda x1: x1[0])[1]
                for ig, s in enumerate(cnts1):
                    area1 = cv2.contourArea(s)
                    if area1 > 12000:
                      cv2.circle(resg, (cx1, cy1), 10, (0,0,0), -1)
                      rectangle1 = cv2.boundingRect(s) 
                      print(area1)
                      x,y,w,h = rectangle1
                      if rectangle1[2] < 50 or rectangle1[3] < 50: continue
                      cv2.rectangle(resg,(x,y),(x+w,y+h),(0,255,0),2)
                     
                      cv2.putText(resg, "({}, {})".format(int(cx1), int(cy1)), (int(cx1-5), int(cy1+15)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                      cv2.putText(resg, "Area:" + str(int(area1)) .format(int(cx1), int(cy1+50)), (int(cx1-50), int(cy1+50)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                      cv2.drawContours(resg, cnts1, 0, (255, 255, 255),1)
                      print('Green Object Detected')
        if i2==2:
            purpimg=frame.copy()
            hsvpurple=cv2.cvtColor(purpimg,cv2.COLOR_BGR2HSV)
            blurp=cv2.GaussianBlur(hsvpurple,(5,5),0)
            lower_purp=np.array([110,50,50])
            upper_purp=np.array([140,255,255])
            maskp = cv2.inRange(blurp, lower_purp, upper_purp)
            resp= cv2.bitwise_and(purpimg,purpimg, mask= maskp)
            cnts2,hierarchy = cv2.findContours(maskp.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]#need to clone these stuff
            Mpurp=cv2.moments(maskp)
            if Mpurp['m00']> 0: #purple
                cxp = int(Mpurp['m10']/Mpurp['m00'])
                cyp = int(Mpurp['m01']/Mpurp['m00'])
                contour_sizes2 = [(cv2.contourArea(contour2), contour2) for contour2 in cnts2]
                biggest_contour2 = max(contour_sizes2, key=lambda x1: x1[0])[1]
                for ip, s2 in enumerate(cnts2):
                    area2 = cv2.contourArea(s2)
                    if area2 > 12000:
                      cv2.circle(resp, (cxp, cyp), 10, (0,0,0), -1)
                      rectangle2 = cv2.boundingRect(s2) 
                      x2,y2,w2,h2 = rectangle2
                      if rectangle2[2] < 50 or rectangle2[3] < 50: continue
                      cv2.rectangle(resp,(x2,y2),(x2+w2,y2+h2),(0,255,0),2)
                     
                      cv2.putText(resp, "({}, {})".format(int(cxp), int(cyp)), (int(cxp-5), int(cyp+15)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                      cv2.putText(resp, "Area:" + str(int(area2)) .format(int(cxp), int(cyp+50)), (int(cxp-50), int(cyp+50)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                      cv2.drawContours(resp, cnts2, 0, (255, 255, 255),1)
                      print('Purple Object Detected')
            
        if i2==3:
            rimg=frame.copy()
            hsvr=cv2.cvtColor(rimg,cv2.COLOR_BGR2HSV)
            blurr=cv2.GaussianBlur(hsvr,(5,5),0)
            lower_r=np.array([0,90,90])
            upper_r=np.array([10,255,255])
            maskr = cv2.inRange(blurr, lower_r, upper_r)
            resr= cv2.bitwise_and(rimg,rimg, mask= maskr)
            cnts3,hierarchy = cv2.findContours(maskr.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]#need to clone these stuff
            Mr=cv2.moments(maskr)
            if Mr['m00']> 0: #purple
                cxr = int(Mr['m10']/Mr['m00'])
                cyr = int(Mr['m01']/Mr['m00'])
                contour_sizes3 = [(cv2.contourArea(contour2), contour2) for contour2 in cnts3]
                biggest_contour3 = max(contour_sizes2, key=lambda x1: x1[0])[1]
                for ir, s3 in enumerate(cnts3):
                    area3 = cv2.contourArea(s3)
                    if area3 > 12000:
                      cv2.circle(resr, (cxr, cyr), 10, (0,0,0), -1)
                      rectangle3 = cv2.boundingRect(s3) 
                      x3,y3,w3,h3 = rectangle3
                      if rectangle3[2] < 50 or rectangle3[3] < 50: continue
                      cv2.rectangle(resr,(x3,y3),(x3+w3,y3+h3),(0,255,0),2)
                      cv2.putText(resr, "({}, {})".format(int(cxr), int(cyr)), (int(cxr-5), int(cyr+15)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                      cv2.putText(resr, "Area:" + str(int(area3)) .format(int(cxr), int(cyr+50)), (int(cxr-50), int(cyr+50)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                      cv2.drawContours(resr, cnts3, 0, (255, 255, 255),1)
                      print('Red Object Detected')
        if i2==4:
            yimg=frame.copy()
            hsvy=cv2.cvtColor(yimg,cv2.COLOR_BGR2HSV)
            blury=cv2.GaussianBlur(hsvy,(5,5),0)
            lower_y=np.array([20,80,100])
            upper_y=np.array([45,255,255])
            masky = cv2.inRange(blury, lower_y, upper_y)
            resy= cv2.bitwise_and(yimg,yimg, mask= masky)
            cnts4,hierarchy = cv2.findContours(masky.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]#need to clone these stuff
            My=cv2.moments(masky)
            if My['m00']> 0: 
                cxy = int(My['m10']/My['m00'])
                cyy = int(My['m01']/My['m00'])
                contour_sizes4 = [(cv2.contourArea(contour3), contour3) for contour3 in cnts4]
                biggest_contour4 = max(contour_sizes2, key=lambda x1: x1[0])[1]
                for iy, s4 in enumerate(cnts4):
                    area4 = cv2.contourArea(s4)
                    if area4 > 12000:
                      cv2.circle(resy, (cxy, cyy), 10, (0,0,0), -1)
                      rectangle4 = cv2.boundingRect(s4) 
                      x4,y4,w4,h4 = rectangle4
                      if rectangle4[2] < 50 or rectangle4[3] < 50: continue
                      cv2.rectangle(resy,(x4,y4),(x4+w4,y4+h4),(0,255,0),2)
                      cv2.putText(resy, "({}, {})".format(int(cxy), int(cyy)), (int(cxy-5), int(cyy+15)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                      cv2.putText(resy, "Area:" + str(int(area4)) .format(int(cxy), int(cyy+50)), (int(cxy-50), int(cyy+50)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                      cv2.drawContours(resy, cnts4, 0, (255, 255, 255),1)
                      print('Yellow Object Detected')
            
        if i2==5:
            oimg=frame.copy()
            hsvo=cv2.cvtColor(oimg,cv2.COLOR_BGR2HSV)
            bluro=cv2.GaussianBlur(hsvo,(5,5),0)
            lower_o=np.array([9,100,100])
            upper_o=np.array([29,255,255])
            masko = cv2.inRange(bluro, lower_o, upper_o)
            reso= cv2.bitwise_and(oimg,oimg, mask= masko)
            cnts5,hierarchy = cv2.findContours(masko.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]#need to clone these stuff
            Mo=cv2.moments(masko)
            if Mo['m00']> 0: 
                cxo = int(Mo['m10']/Mo['m00'])
                cyo = int(Mo['m01']/Mo['m00'])
                contour_sizes5 = [(cv2.contourArea(contour4), contour4) for contour4 in cnts5]
                biggest_contour5 = max(contour_sizes2, key=lambda x1: x1[0])[1]
                for io, s5 in enumerate(cnts5):
                    area5 = cv2.contourArea(s5)
                    if area5 > 12000:
                      cv2.circle(reso, (cxo, cyo), 10, (0,0,0), -1)
                      rectangle5 = cv2.boundingRect(s5) 
                      x5,y5,w5,h5 = rectangle5
                      if rectangle5[2] < 50 or rectangle5[3] < 50: continue
                      cv2.rectangle(reso,(x5,y5),(x5+w5,y5+h5),(0,255,0),2)
                      cv2.putText(reso, "({}, {})".format(int(cxo), int(cyy)), (int(cxo-5), int(cyo+15)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                      cv2.putText(reso, "Area:" + str(int(area5)) .format(int(cxo), int(cyo+50)), (int(cxo-50), int(cyo+50)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                      cv2.drawContours(reso, cnts5, 0, (255, 255, 255),1)
                      print('Orange Object Detected')     
                       
         
    cv2.imshow('Blue',res)
    cv2.imshow('Green',resg)
    cv2.imshow('Purple',resp)
    cv2.imshow('Red',resr)
    cv2.imshow('Yellow',resy)
    cv2.imshow('Orange',reso)
    hor=np.hstack((res,resg))
    hor2=np.hstack((resr,reso))
    cv2.imshow('Video',hor2)
    cv2.imshow('Video2',hor2)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()