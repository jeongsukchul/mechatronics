import cv2

# Create a background subtractor object
fgbg = cv2.createBackgroundSubtractorMOG2()

# Open the default camera (usually 0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Apply thresholding to remove noise
    thresh = cv2.threshold(fgmask, 128, 255, cv2.THRESH_BINARY)[1]

    # Find contours in the thresholded image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw a rectangle around each contour
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting image
    cv2.imshow('frame', frame)

    # Exit if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()