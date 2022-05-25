import RPi.GPIO as GPIO
import modules.LaneCenter as LC

PWMA = 18
AIN1   =  22
AIN2   =  27

PWMB = 23
BIN1   = 25
BIN2  =  24
'''
def driver_setting():

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
'''
    

def drive_stop(L_Motor, R_Motor):
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(AIN2,False)
    GPIO.output(AIN1,False)
    R_Motor.ChangeDutyCycle(0)
    GPIO.output(BIN2,False)
    GPIO.output(BIN1,False)

def drive_front(L_Motor, R_Motor, speed):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2,True)
    GPIO.output(AIN1,False)
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2,True)
    GPIO.output(BIN1,False)

'''
def drive_back(speed, degree): ### 뒤로 가는 동작 제거
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2,False)
    GPIO.output(AIN1,True)
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2,False)
    GPIO.output(BIN1,True)
'''

def drive_turn(L_Motor, R_Motor, speed, degree):
    Tl = degree - 80
    Tr = 100 - degree

    spdL = LC.degtoT(Tl) * speed
    spdR = LC.degtoT(Tr) * speed

    L_Motor.ChangeDutyCycle(spdL)
    GPIO.output(AIN2,True)
    GPIO.output(AIN1,False)
    R_Motor.ChangeDutyCycle(spdR)
    GPIO.output(BIN2,True)
    GPIO.output(BIN1,False)


'''
def drive_left(speed, degree):
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(AIN2,False)
    GPIO.output(AIN1,True)
    R_Motor.ChangeDutyCycle(spdR)
    GPIO.output(BIN2,True)
    GPIO.output(BIN1,False)
'''



