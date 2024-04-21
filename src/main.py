import os
import shutil

from copystatic import recursive_copy


source_path = "./static"
destination_path = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
    recursive_copy(source_path, destination_path)


main()
