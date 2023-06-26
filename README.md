# 2022_PBL-competition

2022년 겨울학기 **인천대학교 PBL 공모전** - **교차로 사고 예방을 위한 스마트 가로등**

> 인천대학교 융합형 PBL 프로그램 대상 수상

> 2022년도 PBL 프로그램 우수작 인천시장상 수상

|파일명|설명|
|---|---|
|cam_1.py|카메라 1대를 통해 Object Detection 하는 코드(SSD-MobileNet 사용)|
|cam_2.py|카메라 2대를 통해 Object Detecton 하는 코드(SSD-MobileNet 사용)|
|car_detection|카메라 1대와 YoloV3를 사용하여 Object Detection 하는 코드|
|led_test.py|실제로 공모전에서 사용한 코드이며 차량의 앞,뒤 모습을 학습시킨 모델을 사용하여 차량을 인식하고, 그에 따라 아두이노에 신호를 보내는 코드|

## 프로젝트 기간
2022.12.15~2023.02.03

## 프로젝트에서 해결하고자한 문제점
![image](https://github.com/Taebee00/2023_PBL-competition/assets/104549849/14a43560-2405-4504-bd88-a05e5b8203a1)
- 교통사고 중 **폭 13m 미만**의 좁은 골목 도로, 그 중에서도 **교차로**에서의 사고 비율과 사망자 비율이 높다는 것을 파악
- 즉 폭이 좁고, 불법 주정차 차량이 많은 **교차로**에서의 잦은 사고율과 높은 사망률을 문제점으로 제시

## 문제 원인
![image](https://github.com/Taebee00/2023_PBL-competition/assets/104549849/c353dd37-c5d1-47eb-8364-b438d7f5975c)
- 교차로의 진입 시에 운전자의 **시각부하량** 증가
- 좁은 골목 교차로 특성상 **신호등**의 부재
- 다수의 **주/정차 차량** 등으로 인한 운전자의 시야각 제한

## 해결 방법
![image](https://github.com/Taebee00/2023_PBL-competition/assets/104549849/7c7f8e2f-e436-488e-bd09-324afa24fec1)
- 교차로에 진입하는 차량이 있다면 **카메라를 통해 교차로에 진입하는 차량을 감지하고, LED를 통해 진입 차량의 유무와 방향을 알려줌**

## HW 구성
![image](https://github.com/Taebee00/2023_PBL-competition/assets/104549849/d2948fd4-3bf1-436d-8cbb-5a65f2508698)
![image](https://github.com/Taebee00/2023_PBL-competition/assets/104549849/2f3d80a9-0829-49c4-86df-bec764fc6db9)
- 메인보드로는 **Jetson Nano**, GPIO 컨트롤을 위해 **Arduino Uno**를 사용하였고, 차량 인식을 위한 **Webcam**, 그리고 차량 진입 여부 신호는 **NeoPixel**을 사용하였음
- 모든 부품이 들어갈 모듈 박스는 3D 프린팅을 통해 제작하였음

## SW 구성
![image](https://github.com/Taebee00/2023_PBL-competition/assets/104549849/3cefcbe0-7fcb-446a-a84c-d2bd949fcba2)
![image](https://github.com/Taebee00/2023_PBL-competition/assets/104549849/e6bd76cd-725c-42f0-aa7b-3092c62a6cc4)
- 차량의 앞, 뒤 모습을 다른 객체로 학습시킨 후, 차량의 앞모습이 일정시간 이상 감지된다면 진입 차량, 뒷모습이 일정시간 이상 감지되면 진출 차량으로 판단하도록 함
- 학습된 모델이 진입 차량을 감지하면 아두이노에 신호를 전달하여, 진입 차량의 방향에 맞는 LED를 점등하여 다른 진입 차량에게 시각적 신호를 보내줌
- 임베디드 기기에 특화된 학습 모델인 **SSD-MobileNet** 모델을 사용

## 최종 결과
![image](https://github.com/Taebee00/2023_PBL-competition/assets/104549849/bf6a5e9f-6d93-4305-9a88-e50bfb0ccd63) | ![image](https://github.com/Taebee00/2023_PBL-competition/assets/104549849/32f6fb52-ea19-4fad-9564-f65560d32103) | ![image](https://github.com/Taebee00/2023_PBL-competition/assets/104549849/2db0db3a-ec3f-4d85-be55-156489b4e5ff)
|---|---|---|
|최종조립 사진|진입 차량 인식 화면|진출 차량 인식 화면|

### 시연 영상
https://github.com/Taebee00/2023_PBL-competition/assets/104549849/4aaaf011-507c-4510-b188-06c9852639ef | https://github.com/Taebee00/2023_PBL-competition/assets/104549849/2b98c7d4-26d3-4c9d-a600-04be2c2f928e
|---|---|
|빨간 선 안의 범위에 차량의 앞모습을 일정 시간동안 인식하여 진입차량으로 판단 후, 차량 진입 방향의 수직 방향의 LED가 진입 차량의 유무와 방향을 표시해주는 것을 알 수 있음|차량이 교차로를 진입했을 때 LED가 켜지고, 진출할 때는 LED가 다시 꺼지는 것을 알 수 있음|

> 기타 시연영상 모음: https://youtu.be/AagYl6HYg5w

### 수상
> 인천대학교 융합형 PBL 프로그램 대상

> 2022년도 PBL 프로그램 우수작 인천시장상

