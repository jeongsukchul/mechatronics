import dlib
import cv2


# step3: get HOG face detector and faces
hogFaceDetector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")


image = cv2.imread("./image2.jpg")

# step2: converts to gray image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = hogFaceDetector(gray, 1)
x = faces[0].left()
y = faces[0].top()
w = faces[0].right() - x
h = faces[0].bottom() - y
shape = predictor(gray,faces[0])

cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 10)
sumx, sumy = [0,0]
for i in range(37,42):
    sumx, sumy = [sumx + shape.part(i).x, sumy+shape.part(i).y]
leftEye = [sumx//5,sumy//5]
sumx, sumy = [0,0]
for i in range(43, 48):
    sumx, sumy = [sumx + shape.part(i).x, sumy+shape.part(i).y]
rightEye = [sumx//5, sumy//5]
print(leftEye)
print(rightEye)
print(image.shape)
cv2.circle(image, (leftEye[0], leftEye[1]), 1, (0, 0, 255), 50)
cv2.circle(image, (rightEye[0], rightEye[1]), 1, (0, 0, 255), 50)
# step5: display the resulted image
cv2.imshow("Image", image)
cv2.imwrite('result2.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()