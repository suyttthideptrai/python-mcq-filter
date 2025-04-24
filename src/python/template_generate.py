import os
from jinja2 import Environment, FileSystemLoader
import utils.file_utils as FU


template_path = os.path.join(os.path.dirname(__file__), '..', 'templates')
abstract_template_path = os.path.join(template_path, 'abstract')

# Load the template
abstract_env = Environment(loader=FileSystemLoader(abstract_template_path))

main_template = abstract_env.get_template('home.html')
navbar_template = FU.get_file_content(os.path.join(abstract_template_path, 'navbar.html'))
sidebar_template = FU.get_file_content(os.path.join(abstract_template_path, 'sidebar.html'))
footer_template = FU.get_file_content(os.path.join(abstract_template_path, 'footer.html'))


# Define content to inject
context = {
    'navbar_here': navbar_template,
    'sidebar_here': sidebar_template,
    'workspace_here': '<p>Yessir</p>',
    'footer_here': footer_template
}

# Render HTML
output_html = main_template.render(context)

target_template_file = os.path.join(template_path, 'home.html')
# Save to file
with open(target_template_file, 'w', encoding='utf-8') as f:
    f.write(output_html)

print("Generated HTML saved to output/home.html")
