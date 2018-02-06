import cv2
import sys
import numpy as np

#blur image to remove noise and convert to 32-bit to improve corner detection
def blur(img):

    # Otsu's thresholding after Gaussian filtering
    blur = cv2.GaussianBlur(img,(15,15),0)

        # to do - test performance with different image manipulations / sizes / thresholding
        #ret, th = cv2.threshold(blur2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        #to do - test performance change with image inversion
        #th = invert(th)
    return(blur)

#inverts image, so that shape will be white outlined by black
def invert(image):
    imagem = cv2.bitwise_not(image)
    return(imagem)

#crops black rows from top of image
def trimFromTop(image):
    croppedImg = image
    while np.sum(croppedImg[0])==0:
        croppedImg = np.delete(croppedImg,0,0)
    print("size is now + "+str(croppedImg.size))
    return(croppedImg)

#crops out black space around each axis of image, returns cropped image
def trim(image):
    img = image
    for x in range(3):
        img = trimFromTop(img)
        img = np.rot90(img)
    img = trimFromTop(img)
    return img
