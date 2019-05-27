from enum import Enum, auto

class Message:
    def __init__(self, text=None, resource=None, ui=None):
        assert text or resource or ui, 'Provide content for message'
        self.text = text
        self.resource = resource
        self.ui = ui


class ResourceType(Enum):
    PICTURE = auto()
    VIDEO = auto()
    GIF = auto()
    DOCUMENT = auto()   # TODO: send method in bot


class Resource:
    def __init__(self, path, resource_type=ResourceType.PICTURE):
        self.path = path
        self.type = resource_type
