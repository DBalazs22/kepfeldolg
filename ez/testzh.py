import cv2
import numpy
import random

def Elso():
    #A program a felhasználótól bekéri a szerkesztendő kép teljes elérési útvonalát, majd megnyitja ezt a képfájlt.(1p)

    img = cv2.imread("flower.jpg",1)


    #A program elvégzi automatikusan a szükséges képkorrekciós műveleteket.(3p)
    filtered = cv2.GaussianBlur(img,(5,5),1.5)
    filtered = cv2.medianBlur(img,5)
    cv2.imshow("filtered",filtered)
    cv2.waitKey()
    # A program a felhasználó által megadott érték alapján küszöbölést hajt végre. (2p)
    hsv = cv2.cvtColor(filtered,cv2.COLOR_RGB2HSV)
    n =int(input("n="))
    #splitted = cv2.split(hsv)
    mask = cv2.threshold(hsv[:,:,0],n,255,cv2.THRESH_BINARY)

    masked = numpy.zeros(img.shape)
    for i in range(0,3):
        #tempmask[:,:,i]=mask[1]

        masked[:,:,i] = cv2.bitwise_and(hsv[:,:,i],mask[1])

    # A program lehetőséget biztosít a felhasználó számára a kinyert rész színparamétereinek
    # (színezet, színtelítettség és világosság) megadására. (4p)

    hue = input("hue=")
    sat = input("sat=")
    val = input("val=")

    hsv[:,:,0] += numpy.uint8(hue)
    hsv[:,:,1] += numpy.uint8(sat)
    hsv[:,:,2] += numpy.uint8(val)

    # A program eredményként kimenti a felhasználó által megadott elérési útvonalra a
    # szerkesztett képet JPEG formátumban, 92%-os minőségi arányban. (2p)

    result = cv2.cvtColor(hsv,cv2.COLOR_HSV2RGB)

    cv2.imshow("result",result)
    cv2.waitKey()

def Masodik():
    path = input("path= ")
    img = cv2.imread(path,1)
    threshValue = numpy.uint8(input("thresh= "))

    hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    mask = cv2.threshold(hsv[:,:,0],threshValue,255,cv2.THRESH_BINARY)
    mask = mask[1] # csak a tombre van szuksegunk
    masked = numpy.zeros(hsv.shape,dtype=numpy.uint8)
    indexes = list()
    indexes_res = list()

    for i in range(0,hsv.shape[0]):
        for j in range(0,hsv.shape[1]):
            if mask[i,j] ==255 :
                pixelGroup = hsv[i,j,:]

                if (pixelGroup[0] < threshValue*2) and \
                    (pixelGroup[1] >=50 and pixelGroup[1] <=170) and \
                    (pixelGroup[2] >=100 and pixelGroup[2] <=200):
                        indexes.append(tuple((i,j)))
                        masked[i,j,:] = pixelGroup
    for index in indexes:
        n = random.random()
        if n>=0.5:
            indexes_res.append(index)

    mask2 = numpy.zeros(mask.shape,dtype=numpy.uint8)

    for index in indexes_res:
        mask2[index[0],index[1]] = 255

    structElement = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    eroded = cv2.erode(mask2,structElement)
    opened = cv2.dilate(eroded,structElement)

    hsv_result = numpy.zeros(hsv.shape,dtype=numpy.uint8)

    for i in range(0,3):
        hsv_result[:,:,i] = cv2.bitwise_and(hsv[:,:,i],opened)

    hue = numpy.uint8(input("hue="))
    sat = numpy.uint8(input("sat="))
    val = numpy.uint8(input("val="))

    cv2.imshow("opened",opened)

    for i in range(0,hsv_result.shape[0]):
        for j in range(0,hsv_result.shape[1]):
            if numpy.array_equal(hsv_result[i,j,:],numpy.array([0,0,0])):
                hsv_result[i, j, :] = numpy.array([hue,sat,val])

    result = cv2.cvtColor(hsv_result,cv2.COLOR_HSV2RGB)

    cv2.imshow("result",result)
    cv2.waitKey()
Elso()
Masodik()