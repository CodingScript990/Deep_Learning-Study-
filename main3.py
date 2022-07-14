import cv2

img = cv2.imread('bg.jpg')
overlay_img = cv2.imread('ipadpro.webp', cv2.IMREAD_UNCHANGED)

# imread(변수, 이미지 합성시 투명도)

# img 사이즈 변환

overlay_img = cv2.resize(overlay_img, dsize=(150,150))

overlay_alpha = overlay_img[:, :, 3:] / 255.0
# alpha(투명도) : 각 픽셀이 얼마나 투명한지 나타내는 값
# 첫번째는 높이, 두번째는 너비, 세번째는 채널

background_alpha = 1.0 - overlay_alpha
# 1.0 - alpha는 반전 값

x1 = 450 # x좌표
y1 = 200 # y좌표
x2 = x1 + 150 # x좌표 + 크기
y2 = y1 + 150 # y좌표 + 크기

img[y1:y2, x1:x2] = overlay_alpha * overlay_img[:, :, :3] + background_alpha * img[y1:y2, x1:x2]
# 이미지의 위치를 지정 => 오버레이 이미지의 크기를 지정 => 원래 이미지를 자른 부분

cv2.imshow('img', img)
cv2.waitKey(0)