import cv2
image = cv2.imread("krishna.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("title",image)

#percent the which image is resize
scale_percent =50

new_width = int(image.shape[1] * scale_percent /100)
new_height =int(image.shape[0] * scale_percent /100)


#resize image it give
output = cv2.resize(image,(new_width,new_height))

cv2.imwrite('newimage.png',output)
cv2.waitKey(0)
