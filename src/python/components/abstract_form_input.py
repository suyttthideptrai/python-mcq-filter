from abc import abstractmethod

from components.abstract_component import AbstractComponent



class AbstractFormInput(AbstractComponent):
    
    TYPES = ["text", "file", "textarea", "checkbox", "dropdown"]
    
    def __init__(self, classname: str, id: str, label: str, type: str):
        super().__init__(classname)
        self.id = id
        self.label = label
        self.type = type
        if type not in self.TYPES:
            raise ValueError(f"Invalid type: {type}. Must be one of {self.TYPES}.")
    
    
    def get_input_id(self) -> str:
        """
        Get the input ID.
        :return: Input ID string.
        """
        return self.id
    
    @abstractmethod
    def get_html(self) -> str:
        """
        Get the HTML representation of the component.
        :return: HTML string.
        """
        return f"<div classname=\"{self.classname}\">abstract html</div>"
    
    def get_value_js_function(self) -> str:
        """
        Get the JavaScript function for the component.
        :return: JavaScript function string.
        """
        return f"function get_data_{self.id}() {{}}"