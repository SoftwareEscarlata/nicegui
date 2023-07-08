from pathlib import Path
from typing import Union

from nicegui.dependencies import register_vue_component

from .mixins.source_element import SourceElement

component = register_vue_component(Path('image.js'))


class Image(SourceElement):

    def __init__(self, source: Union[str, Path] = '') -> None:
        """Image

        Displays an image.

        :param source: the source of the image; can be a URL, local file path or a base64 string
        """
        super().__init__(tag=component.tag, source=source)
        self.use_component(component)
