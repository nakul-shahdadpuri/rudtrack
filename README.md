<div align="center">
  <img src="https://user-images.githubusercontent.com/43999912/123759092-35633c00-d8dd-11eb-9289-a0d3a42068d5.png">
</div>

# Introduction

Rudtrack provides a new approach to object detection and classification in video/live feeds. Rudtrack aims to be faster and lighter than other models in the market and strives to provide a faster way to detect moving objects in a video feed. Rudtrack is desinged for systems with low computational ability and thus uses MobileNet for its classification in the backend.

# Installation

```sh
git clone https://github.com/nakul-shahdadpuri/rudtrack.git
conda env create -f setup.yml
conda activate rudtrack
pip install -r setup.txt
```

# Usage

## For Live Feeds
```sh
python live_analysis [IP] [LINE_X1] [LINE_Y1] [LINE_X2] [LINE_Y2] [Sensitivity] [Area]
```
Here the IP refers to the IP address of the live feed camera. Currently we only use HTTP protocol.

## For Videos
```sh
python video_analysis [VIDEO PATH] [LINE_X1] [LINE_Y1] [LINE_X2] [LINE_Y2] [Sensitivity] [Area]
```

Here X1, X2, Y1, Y2 corresbond to the rectangle coordinates in which the desired object is to be detected. The Sensitivity Parameter is used so that an object lying outside the rectangle zone also gets detected if a certain section of the object is in the zone. 

The area parameter decided the minimum box area an object should be to be detected by the classifier.
 ```
 A = 1000 and sensitivity = 4 
 ```
 could be set normally and changed upon user.
 
 
 If you want to analyse for the entire video feed, 
 set 
 ```sh
 X1=0  X2=800  Y1=0  Y2=800
```
## Architecture Pipeline 
![Blank diagram (1)](https://user-images.githubusercontent.com/43999912/123781378-cba15d00-d8f1-11eb-84cd-b5eec779d2ce.png)




## Dependencies

```sh
tensorflow==2.5.0
OpenCV==4.1.1
```

## References
https://www.tensorflow.org/api_docs/python/tf/keras/applications/mobilenet/MobileNet

https://www.kasperkamperman.com/blog/computer-vision/computervision-framedifferencing/

