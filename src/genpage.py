import pathlib
from markdown_blocks import markdown_to_html_node, extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as md_file:
        md = md_file.read()

    html = markdown_to_html_node(md).to_html()
    title = extract_title(md)

    with open(template_path, "r") as tp_file:
        template = tp_file.read()

    template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    dest_path = pathlib.Path(dest_path)
    print(dest_path)
    if dest_path != "":
        dest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "w") as html_file:
        html_file.write(template)


def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    content_path = pathlib.Path(dir_path_content)
    dest_path = pathlib.Path(dest_dir_path)
    for file in content_path.iterdir():
        if file.is_file() and file.suffix == ".md":
            # print(f"markdown file: {file}")
            dest_dir_path = dest_path.joinpath(f"{file.stem}.html")

            print(f"Destination: {dest_dir_path}")

            generate_page(file, template_path, dest_dir_path)

        elif file.is_dir():
            dest_dir_path = dest_path.joinpath(file.name)
            generate_pages_recursively(file, template_path, dest_dir_path)
