import cv2
import numpy as np

vid = cv2.VideoCapture('videos/virat_pothole_test.mp4')

while(True):
    ret, frame = vid.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey, (5, 5), 0)
    mask = cv2.inRange(grey,230,250)
    edges = cv2.Canny(mask, 190, 200)
    mask = (255 - mask)
    image = mask

    # Set our filtering parameters
    # Initialize parameter setting using cv2.SimpleBlobDetector
    params = cv2.SimpleBlobDetector_Params()

    params.filterByArea = True
    params.minArea = 600

    '''# Set Circularity filtering parameters
    params.filterByCircularity = True
    params.maxCircularity = 0.7
    #params.minCircularity = 0.5'''

    '''# Set Convexity filtering parameters
    params.filterByConvexity = True
    params.minConvexity = 0.99'''

    params.filterByInertia = True
    params.minInertiaRatio = 0.00001
    detector = cv2.SimpleBlobDetector_create(params)

    keypoints = detector.detect(image)

    blank = np.zeros((1, 1))
    blobs = cv2.drawKeypoints(frame, keypoints, blank, (0, 0, 255),
                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    pts = cv2.KeyPoint_convert(keypoints)
    if len(keypoints)>0:
        x1=(int(pts[0][0] -50), int(pts[0][1] -50))
        x2=(int(pts[0][0] +50), int(pts[0][1] +50))
        print(x1)
        frame = cv2.rectangle(frame, x1, x2, (60,255,60), 5)
    
    #cv2.imshow("Filtering Circular Blobs Only", blobs)
    #cv2.imshow('mask', mask)
    cv2.imshow('frame', frame)
    #cv2.imshow('edges', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



vid.release()
cv2.destroyAllWindows()