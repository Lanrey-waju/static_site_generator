import os
import shutil


source_path = "./static"
destination_path = "./public"


def main():
    recursive_copy(source_path, destination_path)


def recursive_copy(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    if not os.path.exists(destination):
        os.mkdir(destination)
    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(destination, item)
        print(f"from {s} to {d}")
        if os.path.isdir(s):
            recursive_copy(s, d)
        else:
            shutil.copy(s, d)


main()
