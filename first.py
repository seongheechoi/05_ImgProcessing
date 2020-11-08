import cv2

img_file = "./img/1.jpg"
img = cv2.imread(img_file, cv2.IMREAD_REDUCED_COLOR_2)

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No image file.')