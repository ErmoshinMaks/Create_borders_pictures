import cv2
import numpy as np

def create_borders(size = 3):
    img = cv2.imread('./in/00002.png', cv2.IMREAD_COLOR)
    half = size//2
    for i in range(size,img.shape[0]-size):
        for j in range(size,img.shape[1]-size):
            crop_img = img[i-half:i+half, j-half:j+half]
            main_color = img[i,j]
            count = 0
            flag = False
            for k in range(crop_img.shape[0]):
                for n in range(crop_img.shape[1]):
                    if not(np.array_equal(crop_img[k,n],main_color)) and not(np.array_equal(crop_img[k,n],(0,0,0))):
                        count += 1
                    if count >= 2:
                        flag = True
                        break
            if flag:
                img[i,j] = (0,0,0)

    cv2.imwrite("result.png", img)

create_borders()
