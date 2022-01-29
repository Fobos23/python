import xml.etree.ElementTree as ET
from contextlib import contextmanager

from core import log


class XmlMod:
    def __init__(self, file):
        self.file_path = file

    @contextmanager
    def xml(self):
        try:
            root = ET.parse(self.file_path)
        except Exception as e:
            log.info()

