import cognitive_face as CF
import numpy as np
import cv2, time, serial
import logging
import subprocess




logging.basicConfig(filename='data/data.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

logging.info("Logging Air Particulate Concentration")

logger = logging.getLogger('concentration')


ser = serial.Serial('/dev/tty.usbmodem1411', 9600) # Establish the connection on a specific port

while True:
    data = ser.readline()
    if (data):
        string = subprocess.check_output(['./whereami'])
        string.splitlines()[0].replace("Latitude: ", "")
        print data.rstrip() + " " + string.splitlines()[0].replace("Latitude: ", "") + " " + string.splitlines()[1].replace("Longitude: ", "")
        logger.info(data.rstrip() + " " + string.splitlines()[0].replace("Latitude: ", "") + " " + string.splitlines()[1].replace("Longitude: ", ""))
