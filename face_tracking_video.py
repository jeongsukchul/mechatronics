import cv2
import dlib

hogFaceDetector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")

# Video Capture(Stream) Initialization
cap = cv2.VideoCapture(0)  # 0:from camera

frame_width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # int `width`
frame_height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # int `height`
fps = cap.get(cv2.CAP_PROP_FPS)  # frame rate
    ##

# Video Writer Initialization
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # output video format arguments
vout = cv2.VideoWriter('./recording1.mp4', fourcc, fps, (frame_width, frame_height))
# record
frames = fps * 10  # 10 seconds
while cap.isOpened() and frames > 0:
    ret, frame = cap.read()  # read a frame

    if not ret:
        break
    cv2_im0=frame
    cv2_im90 = cv2.rotate(cv2_im0, cv2.ROTATE_90_CLOCKWISE)  # 시계방향으로 90도 회전
    cv2_im180 = cv2.rotate(cv2_im0, cv2.ROTATE_180)  # 180도 회전
    cv2_im270 = cv2.rotate(cv2_im0, cv2.ROTATE_90_COUNTERCLOCKWISE)  # 반시계방향으로 90도 회전
      # write a frame
    cv2_im = [cv2_im0, cv2_im90, cv2_im180, cv2_im270]
    for i in range(4):
        image = cv2_im[i]
        faces = hogFaceDetector(image)
        for face in faces:
            x = face.left()
            y = face.top()
            w = face.right() - x
            h = face.bottom() - y
            shape = predictor(image, face)

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 10)
            sumx, sumy = [0, 0]
            for k in range(37, 42):
                sumx, sumy = [sumx + shape.part(k).x, sumy + shape.part(k).y]
            leftEye = [sumx // 5, sumy // 5]
            sumx, sumy = [0, 0]
            for k in range(43, 48):
                sumx, sumy = [sumx + shape.part(k).x, sumy + shape.part(k).y]
            rightEye = [sumx // 5, sumy // 5]
            cv2.circle(image, (leftEye[0], leftEye[1]), 1, (0, 0, 255), 50)
            cv2.circle(image, (rightEye[0], rightEye[1]), 1, (0, 0, 255), 50)

        if i == 1:
            image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        elif i == 2:
            image = cv2.rotate(image, cv2.ROTATE_180)
        elif i == 3:
            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        vout.write(image)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # after 1ms, type 'q' => exit
        break

    frames -= 1;

cap.release()

