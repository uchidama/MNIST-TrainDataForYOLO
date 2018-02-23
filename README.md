# MNIST-Train Data For YOLO

[![https://gyazo.com/d9895f31d70a2819e6322e4704c5adb0](https://i.gyazo.com/d9895f31d70a2819e6322e4704c5adb0.png)](https://gyazo.com/d9895f31d70a2819e6322e4704c5adb0)

This software generats MNIST-Train Data For YOLO.  

# Installation

## Install Keras
This software using Keras.
- [Keras installation instructions](https://github.com/keras-team/keras#installation).

If you want to run without to think keras and backend deeplearning frameworks, enter this command.   
```sh
pip install tensorflow
pip install keras
```

## Install Darknet YOLO
```sh
git clone https://github.com/pjreddie/darknet
cd darknet
make
```
- [YOLO: Real-Time Object Detection](https://pjreddie.com/darknet/yolo/).

# How to use
## Generate MNIST Train Data
1. generat MNIST images and labels.

```sh
python mnist_to_jpg_and_label.py
```

2. generate train.txt and test.txt
```sh
python generate_train_txt_and_test_txt.py
```

## Training YOLO on MNIST

3. Copy files to darknet
```sh
cp cfg/tiny-yolo-mnist.cfg <darknet_dir>/cfg
cp cfg/voc-mnist.data <darknet_dir>/cfg
cp data/voc-mnist.names <darknet_dir>/data
```

4. Modify train and test data path. Edit <darknet_dir>/cfg/voc-mnist.data
```
train  = <path-to-mnist-train>/train.txt
valid  = <path-to-mnist-test>/test.txt
```

5. Download Pretrained Convolutional Weights  
```sh
cd <darknet_dir>
wget https://pjreddie.com/media/files/darknet19_448.conv.23
```
6. Make directory to save trained model.
```sh
mkdir backup
```

7. Train The Model
```sh
./darknet detector train cfg/voc-mnist.data cfg/tiny-yolo-mnist.cfg darknet19_448.conv.23
```
## Predict MNIST test data

[![https://gyazo.com/3649c293e3e718aa11af32e59d4897a4](https://i.gyazo.com/3649c293e3e718aa11af32e59d4897a4.png)](https://gyazo.com/3649c293e3e718aa11af32e59d4897a4)

```sh
./darknet detector test <data file> <cfg file> <weights> <predict image>  
```
ex. command.
```sh
./darknet detector test cfg/voc-mnist.data cfg/tiny-yolo-mnist.cfg weights/tiny-yolo-mnist_500000.weights ~/MNIST-TrainDataForYOLO/JPEGImages/60015.jpg
```
## MNIST Trained Weights

[weights/tiny-yolo-mnist_500000.weights](https://github.com/uchidama/MNIST-TrainDataForYOLO/blob/master/weights/tiny-yolo-mnist_500000.weights)

## License

[MIT](LICENSE.md)

## Link

[YOLO: Real-Time Object Detection](https://pjreddie.com/darknet/yolo/)
