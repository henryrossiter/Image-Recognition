import cv2
import numpy as np

## 'import' files with needed methods
exec(open('./imageManip.py').read())
exec(open('./cornerDetection.py').read())

#if top border isn't black, invert
img = cv2.imread('tri.jpg')
img = blur(img)
if (not np.sum(img[0])==0):
    img = invert(img)

#disp image to check processing
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#trim boders on all sides of image to compress size
img = trim(img)

#disp image to check processing
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(detectCorners(img))
