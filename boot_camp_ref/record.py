import cv2


def main():
    # Video Capture(Stream) Initialization
    cap = cv2.VideoCapture(0)  # 0:from camera

    if cap.isOpened():  # Check the capture object is opened
        ##
        frame_width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # int `width`
        frame_height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # int `height`
        fps = cap.get(cv2.CAP_PROP_FPS)  # frame rate
        ##

    # Video Writer Initialization
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # output video format arguments
    vout = cv2.VideoWriter('recording.mp4', fourcc, fps, (frame_width, frame_height))

    # record
    frames = fps * 10  # 10 seconds
    while cap.isOpened() and frames > 0:
        ret, frame = cap.read()  # read a frame

        if not ret:
            break

        vout.write(frame)  # write a frame

        if cv2.waitKey(1) & 0xFF == ord('q'):  # after 1ms, type 'q' => exit
            break

        frames -= 1;

    cap.release()


if __name__ == '__main__':
    main()
