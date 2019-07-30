#from melodyData import data_return
#from play_melody import *
#from music_check import *

#from model import Net
#from detect import hand_detect
#import torch

import cv2
import skeleton

if __name__ == "__main__":
#    midiout = Setting()       #음악 시작하기 위한 세팅

#    model=Net()     #모델 할당
#    model.load_state_dict(torch.load('model/Net.pth'))  # 학습된 모델 로드
    
    hand = skeleton.hand()

    video_path = './media/video.mp4'    
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, image = cap.read()
        result = hand.detection(image)

        if not result:
            cv2.imshow("Pose and Hand", image) 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            continue

        leftX, leftY = hand.get_left_center()
        rightX, rightY = hand.get_right_center()
        distanceX, distanceY = hand.get_distance()

        print('distance X : ', str(distanceX))
        print('distance Y : ', str(distanceY))
        print('')

        #cv2.imshow("Pose and Hand", image)
        #cv2.waitKey(0)
        

        #rand=torch.randint(low=0,high=368,size=(1,42)).float()  # 42개의 손가락 좌표받아오기
        #hand_state=hand_detect(model,rand)  # 0,1로 손가락 상태 받아오기
        
        #num=music(10, 10, 0, 15) #music(num1,num2,num3,num4)
        #onOff, melody = data_return(hand_state,num)         # 첫번째 : 음악 끄기 켜기 , 두번째 음색 고르기
        #melody_start(onOff, melody ,midiout)