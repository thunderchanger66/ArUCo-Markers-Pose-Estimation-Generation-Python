# 运行GStreamer命令，将UDP流重新编码为MJPEG并通过TCP发送：  
gst-launch-1.0 udpsrc port=5600 ! application/x-rtp,encoding-name=H264 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! jpegenc ! tcpserversink host=127.0.0.1 port=8080

# 转发到虚拟摄像头
- sudo modprobe v4l2loopback exclusive_caps=1 max_buffers=2 video_nr=10
- gst-launch-1.0 udpsrc port=5600 ! application/x-rtp,encoding-name=H264 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! v4l2sink device=/dev/video10

# 或者重新编译OpenCV源码，使能Gstreamer