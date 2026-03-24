import cv2
import matplotlib.pyplot as plt


# display pic
cat = cv2.imread("cat.jpeg")
cv2.imshow("cat",cat)
cv2.waitKey(0);
h,w,c = cat.shape
print("height :{} Width:{} Channels: {}".format(h,w,c))
cat_copy = cat.copy()
cat_copy_resize = cv2.resize(cat_copy,(400,400))
cv2.imshow("copied cat",cat_copy_resize)
cv2.waitKey(0)
cv2.rectangle(cat_copy, (550, 100), (900, 350), (255, 0, 0), 2)
cv2.imshow("copied cat",cat_copy)
cv2.waitKey(0)
