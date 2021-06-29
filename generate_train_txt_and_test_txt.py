import glob
import os


def write_list_file(listfile, jpg_file):
    wd = os.getcwd()
    with open(listfile, "w") as f:
        for filename in glob.glob(f"{wd}/JPEGImages/{jpg_file}"):
            print(filename)
            f.write(filename + "\n")


if __name__ == "__main__":
    write_list_file("train.txt", "[0-5]*.jpg")
    write_list_file("test.txt", "6*.jpg")
