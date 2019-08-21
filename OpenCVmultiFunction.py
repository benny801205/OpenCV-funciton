import numpy as np
import cv2
#import matplotlib.pyplot as plt

#灰化
def gray(img):
    image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return image

#二值化  i=0:普通黑白,1:相反黑白
def binary(img,i):
    ret,thresh = cv2.threshold(img,127,255,i)
    return thresh

#普通抓框

#method1:cv2.RETR_CCOMP,cv2.RETR_EXTERNAL  method2:cv2.CHAIN_APPROX_SIMPLE
def findcontours(img,method1,method2):
    contours, hierarchy = cv2.findContours(img,method1,method2)
    return contours,hierarchy

#高斯平滑
def gauss(img):
    blur = cv2.GaussianBlur(img,(5,5),0)
    return blur
#canny ,須先gray
def canny(img):
    cannyimg = cv2.Canny(img, 50, 150)
    return cannyimg
#中值滤波模板 5~25
def median(img,i):
    blur = cv2.medianBlur(img,i)
    return blur

#霍夫直線
def houghline(thresh,img,i,j):
    minLineLength = i
    maxLineGap = j
    lines = cv2.HoughLinesP(thresh,1,np.pi/180,80,minLineLength,maxLineGap)
    for x1,y1,x2,y2 in lines[0]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    return img


#霍夫圓




#腐蝕  黑色被腐蝕 i 影響程度
def erosion(img,i):
    kernel=np.ones((i,i),np.uint8)#生成一个6x6的核
    erosion=cv2.erode(img,kernel,iterations=1)#调用腐蚀算法
    return erosion
#膨脹 黑色被膨脹 i影響程度
def dilate(img,i):
    kernel=np.ones((i,i),np.uint8)#生成一个3x3的核
    dilation=cv2.dilate(thresh,kernel,iterations=4)#调用膨胀算法



#覆蓋外框線，i為覆蓋線寬  img要注意誰黑誰白
def coverexternal(img,outimg,i):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)    
    cv2.drawContours(outimg,contours,-1,(255, 255, 255),i)
    return outimg
#刪除外框線之子類   img要注意誰黑誰白
def CEC(img,outimg,i):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
    area=0
    k=0
#    cv2.drawContours(outimg,contours,-1,[0,0,255],4)
    lengh=(img.shape[0]+img.shape[1])*1.4
    for kk in contours:
        if cv2.arcLength(kk,True) > lengh:
            if cv2.contourArea(kk) > area:
                area = cv2.contourArea(kk)
                maxindex=k
        k=k+1
    number_1=len(contours)
    print maxindex
    for ll in range(number_1)[::-1]:
        if hierarchy[0][ll][3] != maxindex:
            del contours[ll]
    print 'after',len(contours)
    cv2.drawContours(outimg,contours,-1,(0,255,255),i)    
    
    
    
    
    return outimg
#黑白互換
def reverse(img):
    outimg=cv2.bitwise_not(img)
    return outimg

#過濾顏色cv2.inrange()


#作業端
img = cv2.imread(r'C:\Users\6601\.spyder\imread\work.jpg')
img_2=img.copy()
img3=gray(img_2)
output=binary(img3,0)
o2=output.copy()

n1=gray(img)
n2=binary(n1,1)
n3=coverexternal(n2,o2,4)
n3r=reverse(n3)
n3o=n3.copy()
n4=CEC(n3r,n3o,5)








cv2.imwrite('lll2.jpg',n4)
#cv2.imshow('xxx',finial)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.waitKey(1)



