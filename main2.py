import cv2 # OpenCV Modul

img = cv2.imread('iphone.jpg') # img를 Read...

print(img) # print!
print(img.shape) # img 형태를 보고 싶을때! (높이, 너비, 채널) / img는 픽셀로 이루어져 있음

# 직사각형 그리기

cv2.rectangle(img, pt1=(50, 35), pt2=(525, 830), color=(255,0,0), thickness=2)

# rectangle(변수, pt1=>왼쪽 위 좌표[x,y], pt2=>오른쪽 아래 좌표[x,y], color=>선 색깔, thickness=>선 두께)

# 동그라미 그리기

cv2.circle(img, center=(345, 460), radius=60, color=(0,0,255), thickness=3)

# circle(변수, center=>원의 중심, radius=>원의 반지름, color=>원의 색상, thickness=>선 두께)

# img 자르기

cropped_img = img[35:830, 50:525]

# y,x 순서로 img size를 cut한다.

# img size 재정의

img_resized = cv2.resize(img, (600, 900))

# resize(변수, (y,x))

# rgb color system을 바꿀때
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# cvtColor(변수, RGB)

cv2.imshow('result', img_rgb) # img color를 보여주기 위함!
cv2.waitKey(0) # 컬러 시스템을 사용하는 경우는 흑백인데 다른 흑백으로 바꾸고자 할때 설정한다.

# img를 window로 띄울때

cv2.imshow('resize', img_resized) # img size를 재정의한 것을 보여줌
cv2.imshow('crop', cropped_img) # 자른 img를 보여줄때!
cv2.imshow('img', img) # img를 보여줄거다
cv2.waitKey(0) # 무한정으로 key를 입력하기 전까지 img를 띄워준다