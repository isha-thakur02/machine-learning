import cv2

# Read an Image
img = cv2.imread("image1.jpg")
print(type(img))
print(img.shape)
# Show Image
cv2.imshow("Image",img)
cv2.waitKey(0)

# resizing
resized_img = cv2.resize(img,(300,300))
cv2.imshow("Image",resized_img)

# rotate the image
rotate_img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Image",rotate_img)

#Change Image to gray scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image",img_gray)

# to save image
cv2.imwrite("grey_img.png", img_gray)


# create image
import numpy as np
# create blank image
i = np.zeros((512,512,3))

# draw line in the blank image
cv2.line(i, (50, 50), (150, 150), (255, 0, 0), thickness = 5)

# draw rectangle
cv2.rectangle(i, (50, 50), (150, 150), (0, 255, 0), thickness = 5)

# # draw a circle
cv2.circle(i, (100, 100), 80, (0, 0, 255), thickness = 5)

# Add text
cv2.putText(i, 'First class', (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 250, 300), 2)
cv2.imshow("Image",i)



# if you want to stop seeing you image then press x
import numpy as np
i = np.zeros((512,512,3))
while True:
    cv2.imshow("windows", i)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break
cv2.destroyAllWindows()


cv2.waitKey(0)


