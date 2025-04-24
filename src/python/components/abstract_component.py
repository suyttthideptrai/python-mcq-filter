from abc import ABC, abstractmethod


class AbstractComponent(ABC):
    
    def __init__(self, classname: str):
        self.classname = classname
        
    
    @abstractmethod
    def get_html(self) -> str:
        """
        Get the HTML representation of the component.
        :return: HTML string.
        """
        return f"<div classname=\"{self.classname}\">abstract html</div>"