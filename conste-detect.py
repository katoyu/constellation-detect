import cv2
import numpy as np
#本画像
img = cv2.imread("image1.png").astype(np.float32)
#一部切り抜き画像
img2 = cv2.imread("image2.png").astype(np.float32)

H ,W, C = img.shape
Ht, Wt, Ct = img2.shape


#ラスタライズ走査を行う

i, j = -1, -1
v = 255 * H * W * C
for y in range(H-Ht):
    for x in range(W-Wt):
        _v = np.sum((img[y:y+Ht, x:x+Wt] - img2) ** 2)
        if _v < v:
            v = _v
            i, j = x, y


out = img.copy()
cv2.rectangle(out, pt1=(i, j), pt2=(i+Wt, j+Ht), color=(0,0,255), thickness=1)
out = out.astype(np.uint8)

cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
