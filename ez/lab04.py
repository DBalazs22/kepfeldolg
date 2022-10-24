import cv2
import numpy as np

#manual thresh

I = cv2.imread("C:/Users/kapusi/PycharmProjects/prog2/rose_bw.jpg",0)
thresh_value = int(100)

thresholded = cv2.threshold(I,thresh_value,255,cv2.THRESH_BINARY_INV)
thresholded2 = cv2.threshold(I,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

cv2.imshow("rose_mask",thresholded2[1])
cv2.waitKey()

masked = np.bitwise_and(I,thresholded[1])
masked2 = np.bitwise_and(I,thresholded2[1])

cv2.imshow("rose_masked",masked2)
cv2.waitKey()
#
# #adaptive thresh
#
I2 = cv2.imread("C:/Users/kapusi/PycharmProjects/prog2/text.png",0)
blockSize = int(5)
adaptive = cv2.adaptiveThreshold(I, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize, 2);

cv2.imshow("adaptive",adaptive)
cv2.waitKey()

###----------------
Img = cv2.imread("morp_test.png", 0);
kernel = np.ones((5, 5), dtype=np.uint8)
dilated = cv2.dilate(Img, kernel)
eroded = cv2.erode(Img, kernel)

cv2.imshow("test",Img)
cv2.imshow("dilated",dilated)
cv2.imshow("eroded",eroded)
cv2.waitKey()

img = cv2.imread("morp_test_open.png",0)
img2 = cv2.imread("morp_test_closed.png",0)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
kernel2= cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

eroded = cv2.erode(img,kernel)
opened = cv2.dilate(eroded,kernel)

dilated = cv2.dilate(img2,kernel2)
closed  = cv2.erode(dilated,kernel2)

cv2.imshow("img",img)
cv2.imshow("img2",img2)
cv2.imshow("eroded",eroded)
cv2.imshow("opened",opened)
cv2.imshow("dilated",dilated)
cv2.imshow("closed",closed)
cv2.waitKey()

img = cv2.imread("kacsa.jpg", 1)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
hsv[:,:,2] = hsv[:,:,2]*0.5
hsv[:,:,0] = hsv[:,:,0]*0.8

shapeofHsv = hsv.shape
for i in range(0,shapeofHsv[0]):
    for j in range(0,shapeofHsv[1]):
        if hsv[i,j,0] > 30 and hsv[i,j,0] < 120:
            hsv[i, j, :] = (0,0,0)

result = cv2.cvtColor(hsv,cv2.COLOR_HSV2RGB)

cv2.imshow("res",result)
cv2.waitKey()