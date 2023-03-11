pip3 install opencv-python
pip install opencv-python
python -m pip install opencv-python
python3 -m pip install opencv-python

/ludc/Tools/Software/Python/versions/3.6.10/bin/python3
>>> import cv2
>>> print(cv2.__version__)
4.5.1

>>> img = cv2.imread("logo.png",0)  #-1,color; 0,grey; 1,unchage
>>> cv2.imshow("Image",img)
>>> img = cv2.resize(img,(400,400))
>>> cv2.waitKey(0)
>>> cv2.destroyAllWindows()

>>> img = cv2.imread("logo.png",0)  #-1,color; 0,grey; 1,unchage
>>> cv2.imshow("Image",img)
>>> img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)  #half size set
>>> cv2.waitKey(0)
>>> cv2.destroyAllWindows()

>>> img = cv2.imread("logo.png",0)  #-1,color; 0,grey; 1,unchage
>>> cv2.imshow("Image",img)
>>> img = cv2.rotate(img,cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
>>> img = cv2.rotate(img,cv2.cv2.ROTATE_90_CLOCKWISE)
>>> CV2.imwrite("new_img.jpg",img)  #write a new file
>>> cv2.waitKey(0)
>>> cv2.destroyAllWindows()
