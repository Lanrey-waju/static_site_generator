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

    with open(dest_path, "w") as html_file:
        html_file.write(template)
