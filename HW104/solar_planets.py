import cv2
img=cv2.imread("solar-system.jpg")
cv2.putText(img,"The Sun",(100,50),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255))
cv2.putText(img,"Mercury",(110,180),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))
cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.imwrite("Solar_System.jpg", img)

