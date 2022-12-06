import cv2

def callback(value):
    pass

def setup_trackbars(range_filter):
    cv2.namedWindow("Trackbars")

    for i in ["Min","Max"]:
        v = 0 if i == "Min" else 255

        for j in range_filter:
            cv2.createTrackbar("%s_%s" % (j,i), "Trackbars", v, 255, callback)

def get_trackbar_values(range_filter):
    values = []

    for i in ["Min", "Max"]:
        for j in range_filter:
            v = cv2.getTrackbarPos("%s_%s" % (j,i), "Trackbars")
            values.append(v)

    return values

def main():

    range_filter = "HSV"

    cap = cv2.VideoCapture(0)
    setup_trackbars(range_filter)

    while(True):

        _, frame = cap.read()

        frame_to_thresh = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = get_trackbar_values(range_filter)

        thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))


        cv2.imshow("Frame", frame)
        cv2.imshow("Thres", thresh)

        if cv2.waitKey(1) & 0xFF is ord('q'):
            break

if __name__ == '__main__':
    main()