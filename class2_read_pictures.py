import cv2
import random

#change color on part of img

>>> img = cv2.imread("testM.tif",-1)
>>> print(img.shape)
(893, 1600, 3)
>>> print(img[0]) #read the first row of img
>>> print(img[130][350:600])
>>> for i in range(100):
          for j in range(img.shape[1]):
                img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
>>> cv2.imshow("image",img)
>>> cv2.waitKey(50)
>>> cv2.destroyAllWindows()



#copy/paste logo on part of img
>>> img = cv2.imread("testM.tif",-1)
>>> tag = img[500:700, 600:900]  #move this square
>>> img[100:300, 650:950] = tag  #same size as range we set above

>>> cv2.imshow("image",img)
>>> cv2.waitKey(50)
>>> cv2.destroyAllWindows()
