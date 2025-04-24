from jinja2 import Template
from components.abstract_form_input import AbstractFormInput
import utils.file_utils as FU
from typing import List

class DropDown(AbstractFormInput):

    def __init__(self, id: str, label: str, values: List[str], default_value: str):
        super().__init__(classname="dropdown", id=id, label=label, type="dropdown")
        if default_value not in values:
            raise ValueError(f"Default value '{default_value}' is not in the list of values.")
        self.id = id
        self.values = values
        self.context = {
            'id': id,
            'label': label,
            'values': values,
            'default_value': default_value,
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


a = DropDown("id_dropdown_1", "Test", ["option1", "option2"], "option1")
print(a.get_html())
print(a.get_value_js_function())