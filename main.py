import cv2
import numpy as np
import os
def create_borders(path:str,size = 5):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    half = size//2
    result_img = img.copy()[half:img.shape[0]-half, half:img.shape[1]-half]
    print("Processing..")
    for i in range(half,img.shape[0]-half):
        for j in range(half,img.shape[1]-half):
            crop_img = img[i-half:i+half, j-half:j+half]
            main_color = img[i,j]
            count = 0
            flag = False
            for k in range(crop_img.shape[0]):
                for n in range(crop_img.shape[1]):
                    if not(np.array_equal(crop_img[k,n],main_color)):
                        count += 1
                    if count >= 2:
                        flag = True
                        break
            if flag:
                result_img[i-half,j-half] = (0,0,0)
    print("Done!")

    cv2.imwrite("./out/" + os.path.basename(path).split('.')[0] + ".png", result_img)
    cv2.imshow("AFTER", result_img)
    cv2.imshow("BEFORE", img)


    cv2.waitKey(0)

    cv2.destroyAllWindows()


create_borders("./in/00001.png")
