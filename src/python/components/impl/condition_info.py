from components.abstract_component import AbstractComponent
from jinja2 import Template
import utils.file_utils as FU


class ConditionInfo(AbstractComponent):
    
    def __init__(self, text: str):
        super().__init__("condition_info")
        self.text = text
    
    def get_html(self):
        html_path = FU.get_component_html_path(self.classname)
        html_content = FU.get_file_content(html_path)
        template = Template(html_content)
        return template.render(text=self.text)