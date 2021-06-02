import cv2
import requests
import io
import numpy as np
import sys


class MjpegReader():
    def __init__(self, url: str):
        self._url = url

    def iter_content(self):
        r = requests.get(self._url, stream=True)
        # parse boundary
        content_type = r.headers['content-type']
        index = content_type.rfind("boundary=")
        assert index != 1
        boundary = content_type[index+len("boundary="):] + "\r\n"
        boundary = boundary.encode('utf-8')

        rd = io.BufferedReader(r.raw)
        while True:
            self._skip_to_boundary(rd, boundary)
            length = self._parse_length(rd)
            yield rd.read(length)

    def _parse_length(self, rd) -> int:
        length = 0
        while True:
            line = rd.readline()
            if line == b'\r\n':
                return length
            try:
            	if line.startswith(b"Content-Length"):
                	length = int(line.decode('utf-8').split(": ")[1])
                	assert length > 0
            except:
            	print("Malformed frame")


    def _skip_to_boundary(self, rd, boundary: bytes):
        for _ in range(10):
            if boundary in rd.readline():
                break
        else:
            pass