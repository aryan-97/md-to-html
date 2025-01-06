import os
import shutil

from src.markdown.markdown_parser import extract_title, markdown_to_html

def generate_page(from_path: str, template_path: str, to_path: str):
    with open(template_path, "r") as templateFile:
        template = templateFile.read()

    with open(from_path, "r") as contentFile:
        content = contentFile.read()

    title = extract_title(content)
    content = markdown_to_html(content)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    with open(to_path, "w") as outputFile:
        outputFile.write(template)

def process_dir(path: str, target: str, template_path: str):
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            print("Generating page: ", file.replace(".md", ".html"))
            generate_page(os.path.join(path, file), template_path, os.path.join(target, file.replace(".md", ".html")))
        else:
            print("Creating directory: ", file)
            os.mkdir(os.path.join(target, file))
            process_dir(os.path.join(path, file), os.path.join(target, file), template_path)

def generate_pages(from_path: str, template_path: str, to_path: str):
    process_dir(from_path, to_path, template_path)


if __name__ == '__main__':
    shutil.rmtree("public", ignore_errors=True)
    shutil.copytree("static", "public")
    generate_pages("content", "template.html", "public")
