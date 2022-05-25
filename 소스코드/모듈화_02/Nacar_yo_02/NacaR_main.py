import cv2
import RPi.GPIO as GPIO
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

### 각종 모듈을 로드 ###
import modules.Drive_Setting as DS     # 베이스보드 단위의 모터 동작
# import modules.Img_Process as IP       # 이미지 조정 및 편집
import modules.Park as PK              # 주차
import modules.LaneCenter as LC        # 차선 중앙 유지
import modules.Intersaction as IS      # 교차로 판단 및 회전
import modules.FrontCar as FC          # 전방 차량 탐색


### RPI 보드 입/출력 설정 ###
PWMA = 18
AIN1   =  22
AIN2   =  27

PWMB = 23
BIN1   = 25
BIN2  =  24

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(PWMA,GPIO.OUT)

GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)
GPIO.setup(PWMB,GPIO.OUT)

L_Motor = GPIO.PWM(PWMA,500)
L_Motor.start(0)

R_Motor = GPIO.PWM(PWMB,500)
R_Motor.start(0)

model_path = './modules/lane_navigation_final2.h5'
LCmodel = load_model(model_path)


### 함수 구현부 ###



### 메인 함수 ###
def main():
    camera = cv2.VideoCapture(-1)
    camera.set(3, 640)
    camera.set(4, 480)
    
    speedSet = 25
    carState = "stop"
    
    ### 키를 입력받아 행동을 결정 ###
    while( camera.isOpened()):
        keValue = cv2.waitKey(1)
        
        if keValue == ord('q') :
            break
        elif keValue == 82 :
            print("work")
            carState = "work"
        elif keValue == 84 :
            print("stop")
            carState = "stop"
        
        ### 카메라 캡쳐 및 이미지 처리 ###
        _, image = camera.read()
        image = cv2.flip(image,-1)
        cv2.imshow('Original', image)
        
        steering_angle = LC.predict_deg(image, LCmodel)
        LC.driving(L_Motor, R_Motor, carState, speedSet, steering_angle)
    
    
        
    ### 종료 시 : 이미지 초기화 ###
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
    GPIO.cleanup()
