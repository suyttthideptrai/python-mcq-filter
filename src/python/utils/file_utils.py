import os
from path import HTML_ASSET_DIR


def get_component_html_path(component_name: str):
    return os.path.join(HTML_ASSET_DIR, "components", f"{component_name}.html")

def get_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()