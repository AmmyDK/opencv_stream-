import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  
  image = np.zero(frame.shape, np.unit8)
  smaller_frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
  cv2.imshow('frame',frame)
  
  if cv2.waitKey(1) == ord('d'):
      break
      
cap.release()
cv2.destroyAllWindows()