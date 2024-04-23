import os
import shutil

from copystatic import recursive_copy
from genpage import generate_pages_recursively

dir_path_static = "./static"
dir_path_public = "./public"

dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    recursive_copy(dir_path_static, dir_path_public)
    # generate_page(dir_path_content, template_path, dir_path_public + "/index.html")
    generate_pages_recursively(dir_path_content, template_path, dir_path_public)


main()
