import Drive_Setting as DS
import tensorflow as tf
from tensorflow.keras.models import load_model

model_path = './lane_navigation_final2.h5'
LCmodel = load_model(model_path)
    
### 입력받은 각도를 상수로 계산해주는 함수 ###
def degtoT(degree) :
    T = 1
    if (degree <=0) :
        T = 0
    elif (0 < degree < 10) :
        T = (1 / 10) * degree
    elif (10 <= degree <= 20) :
        T = 1
    elif (20 < degree < 30) :
        T = 0.004 * ((degree-20)**2) + 1
    elif (30 <= degree) :
        T = 1.4
    
    return T

### 모델에서 predict 값을 가져옴 ###
def predict_deg(image) :
    preprocessed = IP.img_preprocess(image)
    cv2.imshow('pre', preprocessed)

    X = np.asarray([preprocessed])
    steering_angle = int(model.predict(X)[0])
    print("predict angle:",steering_angle)
    
    return steering_angle

### 자동차의 상태에 따라 동작 결정 ###
def driving(carState, speedSet, steering_angle) :
    if carState == "work":
        if steering_angle >= 85 and steering_angle <= 95: # 직진 시 오차 : 좌우 5도
            print("working")
            DS.drive_front(speedSet)

        elif steering_angle > 96 : # 96도 이상 : 우회전
            print("right")
        elif steering_angle < 84: #84도 이하 : 좌회전
            print("left")
        DS.drive_turn(speedSet, steering_angle)

    elif carState == "stop":
        DS.drive_stop()
        
