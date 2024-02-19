### Getting started
1. Plug in raspberry pi to power and internet (via ethernet)
2. Open terminal and run `ssh slimy@raspberrypi` when prompted enter `bastard` as the password
3. Once in the shell navigate to `/home/slimy/Projects/pi_camera`
4. To start the video buffer run `python record.py` and follow the prompts to save videos.
5. Once you are finished recording the videos will be output to the `video_files` directory and to watch them from a new terminal you can transfer them to your computer using the following command `scp -r slimy@raspberrypi:/home/slimy/Projects/pi_camera/video_files .` (both the .h264 and .mp4 files will be included)

### Development
1. To make changes to the `record.py` script I would recommend making the changes locally and then moving them onto the pi with the command `scp ./record.py slimy@raspberrypi:/home/slimy/Projects/pi_camera/record.py`
2. When you are ready to turn the pi off run the command `sudo shutdown -h now`
3. `setup.sh` has been created to assist if the program needs to be run on different hardware with all of the configurations and dependencies needed


