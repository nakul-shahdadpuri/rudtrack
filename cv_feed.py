import cv2
import requests
import io
import numpy as np
import sys
from stream_reader import *
from config import *
from nayanam import *



def main():
    LINE_X1 = int(sys.argv[1])
    LINE_Y1 = int(sys.argv[2])
    LINE_X2 = int(sys.argv[3])
    LINE_Y2 = int(sys.argv[4])
    nayanam(LINE_X1,LINE_Y1,LINE_X2,LINE_Y2)



if __name__ == '__main__':
    main()