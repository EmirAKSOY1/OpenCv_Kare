import cv2
import math
import numpy as np

# lower_red=np.array([161,155,84])
# upper_red = np.array([179,255,255])

lower_red=np.array([149,100,100])
upper_red = np.array([189,255,255])

video=cv2.VideoCapture(0)
i=True
while i:
    success, img=video.read()
    img=cv2.flip(img,1)
    image=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(image,lower_red,upper_red)
    
    contours,hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    mask=cv2.bitwise_and(img,img,mask=mask)
    #yan çizgiler
    img=cv2.line(img,(50,20),(50,460),(64,255,255),2)#sol
    img=cv2.line(img,(590,20),(590,460),(64,255,255),2)#sag
    #/yan çizgiler

    img=cv2.line(img,(40,20),(60,20),(39,237,250),2)
    cv2.putText(img,"+50",(0,25),cv2.FONT_HERSHEY_DUPLEX,0.5,(39,237,250),1,cv2.LINE_4)

    img=cv2.line(img,(40,230),(60,230),(39,237,250),2)
    cv2.putText(img,"0",(15,233),cv2.FONT_HERSHEY_DUPLEX,0.5,(39,237,250),1,cv2.LINE_4)

    img=cv2.line(img,(40,460),(60,460),(39,237,250),2)
    cv2.putText(img,"+50",(0,462),cv2.FONT_HERSHEY_DUPLEX,0.5,(39,237,250),1,cv2.LINE_4)

    img=cv2.line(img,(580,20),(600,20),(39,237,250),2)
    cv2.putText(img,"-50",(605,25),cv2.FONT_HERSHEY_DUPLEX,0.5,(39,237,250),1,cv2.LINE_4)
    
    img=cv2.line(img,(580,230),(600,230),(39,237,250),2)
    cv2.putText(img,"0",(615,235),cv2.FONT_HERSHEY_DUPLEX,0.5,(39,237,250),1,cv2.LINE_4)
    
    img=cv2.line(img,(580,460),(600,460),(39,237,250),2)
    cv2.putText(img,"+50",(605,462),cv2.FONT_HERSHEY_DUPLEX,0.5,(39,237,250),1,cv2.LINE_4)

    #aim
    img=cv2.line(img, (300,250),(320,250),(0,0,0),1)
    img=cv2.line(img, (310,240),(310,260),(0,0,0),1)
    #/aim
    if len(contours)!=0:
        for contour in contours:
            if cv2.contourArea(contour)>1000:
                img=cv2.line(img,(50,10),(50,450),(39,237,250),2)
                x,y,w,h=cv2.boundingRect(contour)
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                # img=cv2.line(img, (300,250),(320,250),(0,0,0),1)
                # img=cv2.line(img, (310,240),(310,260),(0,0,0),1)
                img=cv2.line(img,(x,y),(x+w,y+h),(0,255,0),1)
                img=cv2.line(img,(x+w,y),(x,h+y),(0,255,0),1)
                yariw=w/2
                yarix=int(x+yariw)
                yarih=h/2
                yariy=int(y+yarih)
                cv2.circle(img,(yarix,yariy),6,(255,255,255),-1)
                img=cv2.line(img, (310,250),(yarix,yariy),(255,255,255),1)
                x=math.pow((310-yarix),2)+math.pow((250-yariy),2)
                x=math.sqrt(x)
                # if(x<10):
                #     i=False
                #     print("Mekanizma Çalıştı")
    cv2.imshow("mask",mask)
    cv2.imshow("cam",img)
    k=cv2.waitKey(5)
    if k==27:
        break

video.release()
cv2.destroyAllWindows()  