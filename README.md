# 2022_PBL-competition

2022년 겨울학기 인천대학교 PBL 공모전 - 교차로 사고 예방을 위한 스마트 가로등

## 프로젝트 기간
2022.12.15~2023.02.03

## 문제점 
![image](https://github.com/Taebee00/2023_PBL-competition/assets/104549849/14a43560-2405-4504-bd88-a05e5b8203a1)

## 문제 원인
![image](https://github.com/Taebee00/2023_PBL-competition/assets/104549849/c353dd37-c5d1-47eb-8364-b438d7f5975c)

## 해결 방법
![image](https://github.com/Taebee00/2023_PBL-competition/assets/104549849/7c7f8e2f-e436-488e-bd09-324afa24fec1)
- 교차로에 진입하는 차량이 있다면 카메라를 통해 교차로에 진입하는 차량을 감지하고, LED를 통해 진입 차량의 유무와 방향을 알려줌

## HW 구성
![image](https://github.com/Taebee00/2023_PBL-competition/assets/104549849/d2948fd4-3bf1-436d-8cbb-5a65f2508698)
![image](https://github.com/Taebee00/2023_PBL-competition/assets/104549849/2f3d80a9-0829-49c4-86df-bec764fc6db9)


## 개발 환경
### HW
- Jeston Nano
- Speaker
- I2C LCD
- USB Webcam
- Amp
### SW
- Python
- OpenCV
- Dlib library

## Detection
### Face Detection
- Dlib library 에서 제공하는 `get_frontal_face_detector`함수를 이용하여 이미지 속 얼굴의 위치를 detect
- `shape_predictor`함수를 이용하여 detect된 얼굴을 68개의 landmark로 변환

![image](https://github.com/Taebee00/sleep-detection-system/assets/104549849/a8d12e17-0f28-4d23-9dc4-b51d683f8103)

### Eye Blink Detection
- Eye Aspect Ratio(EAR) Algorithm

  눈의 종횡 비 변화를 이용해 눈 감김을 판단하는 알고리즘
  
  ![image](https://github.com/Taebee00/sleep-detection-system/assets/104549849/50a3af23-f12e-4373-a9cb-432633a210e4)
  
- Face Detection을 통해 얻은 68개의 landmark 중 눈에 해당하는 36~47번 landmark를 이용하여 EAR rate를 계산
- EAR rate가 감소하며 눈의 종횡 비가 감소한 것이므로 '눈 감김'으로 판단
- '눈 감김'의 빈도를 count 하여 졸음을 감지

![image](https://github.com/Taebee00/sleep-detection-system/assets/104549849/5df815f4-9d9b-41ca-ac85-fee027cfcc9b)

## Warning
- I2C LCD에 경고 메세지 출력
`lcd.writ_string('Careful\r\nAre you sleepy?)`
- espeak를 통해 경고 메시지를 TTS 방식으로 출력
`os.system("espeak -a 200 -p 20 -s 240 -v en-us+f5" + " " +text)`

## 기대 효과 및 장점
- 단순히 눈을 감았다 뜨는 것이 아닌, 일정한 시간 안에 몇 번 감았는지를 계산해 운전자의 졸음 여부를 확실하고 체계적으로 감시하고 감지할 수 있음
- 졸음을 감지하면 운전자에게 시각적으로, 청각적으로 신호를 전달하여 운전자가 즉각적인 피드백을 받을 수 있도록 함
- 운전 관련 분야가 아닌 거짓말 탐지 등, 눈을 깜빡임을 인식하는 다른 다양한 분야에도 쓰일 수 있음


