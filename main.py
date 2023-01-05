import cv2
import os
import time
import uuid

img_path= os.path.join('data','images')
num_images=20
camera = cv2.VideoCapture(0)
for imgnum in range(num_images):
    
    print('collecting image{}'.format(imgnum))
    ret, frame = camera.read()
    imgname=os.path.join(img_path,f'{str(uuid.uuid1())}.jpg')
    cv2.imwrite(imgname,frame)
    cv2.imshow('image',frame)
    time.sleep(0.5)
    
    if cv2.waitKey(1) & 0xFF==32:
        break
camera.release()
cv2.destroyAllWindows()