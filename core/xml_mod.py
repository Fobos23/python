import xml.etree.ElementTree as ET
from contextlib import contextmanager

from core import log
from core.decorator import autolog


class CustomElement:
    def __init__(self, tag, attrs=None, value=None):
        self.tag = tag
        self.attrs = attrs
        self.value = value


class XmlMod:
    def __init__(self, file=None):
        self.file = file

    @contextmanager
    def xml(self, need_save=True):
        try:
            tree = ET.parse(self.file)
            yield tree.getroot()
            if need_save:
                tree.write(self.file)
        except Exception as e:
            log.error(e)

    @autolog
    def create_xml(self, file, root_name):
        with open(file, 'w') as f:
            f.write(f'<{root_name}></{root_name}>')
            self.file = file
        log.info(f'Create file: {file.name}')

    @autolog
    def insert(self, element, xpath):
        with self.xml() as root:
            parent = root.find(xpath)
            sub_elem = ET.SubElement(parent, element.tag)
            if element.attrs:
                sub_elem.attrib = element.attrs
            if element.value:
                sub_elem.text = element.value
            log.info(f'Add element {sub_elem.tag} with value: {sub_elem.text} attrs: {sub_elem.attrib}')
