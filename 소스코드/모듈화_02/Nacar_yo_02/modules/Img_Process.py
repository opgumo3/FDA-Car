import cv2

### 이미지 해상도 및 크기 수정 ###
def img_preprocess(image):
    height, _, _ = image.shape
    image = image[int(height/2):,:,:]
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    image = cv2.GaussianBlur(image, (3,3), 0)
    image = cv2.resize(image, (200,66)) 
    image = image / 255
    return image

