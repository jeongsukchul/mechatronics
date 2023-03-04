import RPi.GPIO as GPIO #RPi.GPIO 라이브러리를 GPIO로 사용
from time import sleep  #time 라이브러리의 sleep함수 사용

servoPin1          = 12   # 서보 핀
servoPin2          = 13   # 서보 핀
servoPin3          = 14   # 서보 핀
SERVO_MAX_DUTY    = 12   # 서보의 최대(180도) 위치의 주기
SERVO_MIN_DUTY    = 3    # 서보의 최소(0도) 위치의 주기

GPIO.setmode(GPIO.BOARD)        # GPIO 설정
GPIO.setup(servoPin1, GPIO.OUT)  # 서보핀 출력으로 설정
GPIO.setup(servoPin2, GPIO.OUT)  # 서보핀 출력으로 설정
GPIO.setup(servoPin3, GPIO.OUT)  # 서보핀 출력으로 설정

servo1 = GPIO.PWM(servoPin1, 50)  # 서보핀을 PWM 모드 50Hz로 사용하기 (50Hz > 20ms)
servo2 = GPIO.PWM(servoPin2, 50)  # 서보핀을 PWM 모드 50Hz로 사용하기 (50Hz > 20ms)
servo3 = GPIO.PWM(servoPin3, 50)  # 서보핀을 PWM 모드 50Hz로 사용하기 (50Hz > 20ms)
servo1.start(0)  # 서보 PWM 시작 duty = 0, duty가 0이면 서보는 동작하지 않는다.
servo2.start(0)  # 서보 PWM 시작 duty = 0, duty가 0이면 서보는 동작하지 않는다.
servo3.start(0)  # 서보 PWM 시작 duty = 0, duty가 0이면 서보는 동작하지 않는다.

servo = {1: servo1, 2: servo2, 3: servo3}
'''
서보 위치 제어 함수
degree에 각도를 입력하면 duty로 변환후 서보 제어(ChangeDutyCycle)
'''
def setServoPos(axis,degree):
  # 각도는 180도를 넘을 수 없다.
  if degree > 180:
    degree = 180

  # 각도(degree)를 duty로 변경한다.
  duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
  # duty 값 출력
  print("Degree: {} to {}(Duty)".format(degree, duty))

  # 변경된 duty값을 서보 pwm에 적용
  servo[axis].ChangeDutyCycle(duty)


if __name__ == "__main__":
  # 서보 0도에 위치
  setServoPos(0)
  sleep(1) # 1초 대기
  # 90도에 위치
  setServoPos(90)
  sleep(1)
  # 50도..
  setServoPos(50)
  sleep(1)

  # 120도..
  setServoPos(120)
  sleep(1)

  # 180도에 위치
  setServoPos(180)
  sleep(1)

  # 서보 PWM 정지
  servo.stop()
  # GPIO 모드 초기화
  GPIO.cleanup()