import cv2

cap = cv2.VideoCapture('tcp://127.0.0.1:8080')

if not cap.isOpened():
    print("无法打开视频流")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # 在这里处理你的frame，例如显示、检测等
        cv2.imshow('Gazebo Camera Stream', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()