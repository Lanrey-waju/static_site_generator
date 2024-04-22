import os
import shutil

from copystatic import recursive_copy
from genpage import generate_page

source_path = "./static"
destination_path = "./public"

from_path = "./content/index.md"
template_path = "template.html"
dest_path = "./public/index.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
    recursive_copy(source_path, destination_path)
    generate_page(from_path, template_path, dest_path)


main()
