import os

import numpy as np
from PIL import Image, ImageOps
from keras.datasets import mnist


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def save_image(filename: str, data_array: np.ndarray):
    bg_color = (0x00, 0x00, 0xff)
    screen = (500, 375)

    img = Image.new("RGB", screen, bg_color)

    mnist_img = Image.fromarray(data_array.astype(np.uint8))
    mnist_img_invert = ImageOps.invert(mnist_img)

    w = int(mnist_img.width * 10)
    mnist_img_invert = mnist_img_invert.resize((w, w))

    x = int((img.width - w) / 2)
    y = int((img.height - w) / 2)
    img.paste(mnist_img_invert, (x, y))
    img.save(filename)

    return convert((img.width, img.height), (float(x), float(x + w), float(y), float(y + w)))


DIR_NAME = "JPEGImages"
LABEL_DIR_NAME = "labels"


def main():
    global DIR_NAME, LABEL_DIR_NAME

    # the data, shuffled and split between train and test sets
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    if not os.path.exists(DIR_NAME):
        os.mkdir(DIR_NAME)

    if not os.path.exists(LABEL_DIR_NAME):
        os.mkdir(LABEL_DIR_NAME)

    no = 0
    for j, li in enumerate([x_train, x_test]):
        print("[---------------------------------------------------------------]")
        for i, x in enumerate(li):
            # Write Image file
            filename = f"{DIR_NAME}/{no:05d}.jpg"
            print(filename)

            ret = save_image(filename, x)
            print(ret)

            # Write label file
            label_filename = f"{LABEL_DIR_NAME}/{no:05d}.txt"
            print(label_filename)

            y = y_train[i] if j == 0 else y_test[i]

            with open(label_filename, "w") as f:
                f.write(f"{y:d} {ret[0]:f} {ret[1]:f} {ret[2]:f} {ret[3]:f}")

            no += 1


if __name__ == "__main__":
    main()
