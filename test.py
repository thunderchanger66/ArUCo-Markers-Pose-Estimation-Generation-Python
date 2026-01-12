import cv2

# 构建GStreamer管道字符串
pipeline = 'udpsrc port=5600 ! application/x-rtp ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! appsink'

cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

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