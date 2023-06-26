import jetson.inference
import jetson.utils

net_1=jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera_1=jetson.utils.videoSource("csi://0")
display_1 = jetson.utils.videoOutput()

net_2=jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera_2=jetson.utils.videoSource("/dev/video1")
display_2=jetson.utils.videoOutput()


while True:
	img_1 = camera_1.Capture()
	detection_1=net_1.Detect(img_1)
	display_1.Render(img_1)
	display_1.SetStatus("Object Detection | Network {:.0f} FPS".format(net_1.GetNetworkFPS()))
	
	img_2 = camera_2.Capture()
	detection_2=net_2.Detect(img_2)
	display_2.Render(img_2)
	if detection_2!=NULL:
		for i in detection:
			print(i)
	display_2.SetStatus("Object Detection | Network {:.0f} FPS".format(net_2.GetNetworkFPS()))