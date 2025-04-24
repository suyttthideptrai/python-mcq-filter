from jinja2 import Template
from components.abstract_form_input import AbstractFormInput
import utils.file_utils as FU


class TextInput(AbstractFormInput):

    def __init__(self, id: str, label: str, default_value: str = None, placeholder: str = None):
        super().__init__(classname="text_input", id=id, label=label, type="text")
        self.id = id
        self.context = {
            'id': id,
            'label': label,
            'placeholder': placeholder,
            'value': default_value
        }
    
    
    def get_html(self) -> str:
        html_path = FU.get_component_html_path(self.classname)
        html_content = FU.get_file_content(html_path)
        template = Template(html_content)
        return template.render(self.context)
    
    def get_value_js_function(self) -> str:
        """
        Get the JavaScript function for the component.
        :return: JavaScript function string.
        """
        return f"""
function get_data_{self.type}_{self.id}() {{
    var input = document.getElementById("{self.id}");
    if (input) {{
        return input.value;
    }} else {{
        console.error("Element with ID '{self.id}' not found.");
        return null;
    }}
}}
        """
