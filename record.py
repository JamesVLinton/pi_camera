import os 
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import CircularOutput
import ffmpeg

picam2 = Picamera2()
fps = 30
dur = 5 # how long the buffer should be, this is how long the saved clips will be as well
micro = int((1 / fps) * 1000000)
file_directory = "video_files/"
if not os.path.isdir(file_directory):
    os.mkdir(file_directory, exist_ok=True)
video_num = 0

vconfig = picam2.create_video_configuration()
vconfig['controls']['FrameDurationLimits'] = (micro, micro)
picam2.configure(vconfig)
encoder = H264Encoder()
output = CircularOutput(buffersize=int(fps * (dur + 0.2)), outputtofile=False)
picam2.start_recording(encoder, output)

print("camera started...")
stop = ""
while stop.upper() != "Q":
    output.fileoutput = f"{file_directory}file{video_num}.h264"
    output.start()
    input(f"Press enter to capture the last {dur} seconds.")
    output.stop()
    video_num += 1
    stop = input("Press enter to capture another video or Q and enter to quit.")

# convert files from h264 to mp4
for i in range(video_num):
    ffmpeg.input(f"{file_directory}file{i}.h264").output(f"{file_directory}file{i}.mp4").run()
