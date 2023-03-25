import cv2
import numpy as np
import os

def create_borders(path:str,size = 5):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    print(f"Size before processing: {img.shape}")

    result_img = img.copy()
    half = size // 2

    for i in range(half):
        img = np.insert(img, 0, [(-1,-1,-1) for i in range(img.shape[0])], axis=1)
        img = np.insert(img, img.shape[1], [(-1,-1,-1) for i in range(img.shape[0])], axis=1)

        img = np.insert(img, 0, [(-1,-1,-1) for i in range(img.shape[1])], axis=0)
        img = np.insert(img, img.shape[0], [(-1,-1,-1) for i in range(0, img.shape[1])], axis=0)

    print("Processing..")
    for i in range(half,img.shape[0]-half):
        for j in range(half,img.shape[1]-half):
            crop_img = img[i-half:i+half, j-half:j+half]
            main_color = img[i,j]
            count = 0
            flag = False
            for k in range(crop_img.shape[0]):
                for n in range(crop_img.shape[1]):
                    if not(np.array_equal(crop_img[k,n],main_color)) and not(np.array_equal(crop_img[k,n],(-1,-1,-1))):
                        count += 1
                    if count >= 2:
                        flag = True
                        break
            if flag:
                result_img[i-half,j-half] = (0,0,0)
    print("Done!")
    print(f"Size after processing: {result_img.shape}")


    cv2.imwrite("./out/" + os.path.basename(path).split('.')[0] + ".png", result_img)
    cv2.imshow("AFTER", result_img)

    img_before = cv2.imread(path, cv2.IMREAD_COLOR)
    cv2.imshow("BEFORE", img_before)


    cv2.waitKey(0)

    cv2.destroyAllWindows()


create_borders("./in/00002.png")
