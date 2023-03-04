import cv2
import dlib

hogFaceDetector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")

# Video Capture(Stream) Initialization
cap = cv2.VideoCapture('./video2.mp4')  # 0:from camera

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
    cv2_im=frame
      # write a frame

    faces = hogFaceDetector(cv2_im)
    for face in faces:
        x = face.left()
        y = face.top()
        w = face.right() - x
        h = face.bottom() - y
        shape = predictor(cv2_im, face)
    
        cv2.rectangle(cv2_im, (x, y), (x + w, y + h), (0, 255, 0), 10)
        sumx, sumy = [0, 0]
        for i in range(37, 42):
            sumx, sumy = [sumx + shape.part(i).x, sumy + shape.part(i).y]
        leftEye = [sumx // 5, sumy // 5]
        sumx, sumy = [0, 0]
        for i in range(43, 48):
            sumx, sumy = [sumx + shape.part(i).x, sumy + shape.part(i).y]
        rightEye = [sumx // 5, sumy // 5]
        cv2.circle(cv2_im, (leftEye[0], leftEye[1]), 1, (0, 0, 255), 50)
        cv2.circle(cv2_im, (rightEye[0], rightEye[1]), 1, (0, 0, 255), 50)

    vout.write(cv2_im)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # after 1ms, type 'q' => exit
        break

    frames -= 1;

cap.release()

