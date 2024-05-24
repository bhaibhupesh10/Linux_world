import cv2
cap = cv2.VideoCapture(0)
while True:
   status, photo = cap.read()
   cv2.imwrite("nikita.png",photo)
   cv2.imshow("meri photo", photo)
   if cv2.waitKey(100) ==13:
       break


cv2.destroyAllWindows()


