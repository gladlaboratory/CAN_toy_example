# CAN_toy_example
Toy example for car control by CAN





1. 필수 라이브러리
    1.1 CAN 메시지 송수신, Encode & Decode 관련 라이브러리
       Cantools : pip3 install cantools
       Can-utils : sudo apt-get install can-utils

    1.2 Keyboard 제어를 위한 상호작용 라이브러리
       Keyboard : pip3 install keyboard

    1.3 설치 권장(Optional)
       Terminator : sudo apt-get install terminator

2. CAN FD 통신 설정
     sudo ip link set down can0
     sudo ip link set can0 type can bitrate 500000 dbitrated 2000000 berr-reporting on fd on
     sudo ip link set can0 up

4. control_by_keyboard.py를 실행하여 키보드로 차량제어 실tl


