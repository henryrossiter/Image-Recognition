import cv2
import numpy as np

def detectCorners(img):
    #filename = imgName
    #img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #change image to grayscale in order to run corner detection
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)


    # Threshold for an optimal value, it may vary depending on the image.
    # makes detected corners red
    img[dst>0.1*dst.max()]=[0,0,255]

    #find coordinates of corners and zip into iterator
    coord = np.where(np.all(img == (0, 0, 255), axis=-1))
    coorarray = zip(coord[0], coord[1])

    #show image with detected corners marked in red
    cv2.imshow('dst',img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

    #returns list of tuples containing points of corners
    return list(coorarray)
