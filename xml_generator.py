from core.decorator import autolog
from core.models_builder import Builder
from core.xml_mod import XmlMod


class XmlGenerator:
    def __init__(self, file_path, root_name):
        self.__xml_mod = XmlMod()
        self.__file_path = file_path
        self.__xml_mod.create_xml(self.__file_path, root_name)

    @autolog
    def create(self, main_model):
        Builder(self.__file_path).build(main_model)