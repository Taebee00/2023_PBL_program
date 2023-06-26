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






