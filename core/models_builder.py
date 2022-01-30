from core.decorator import autolog
from core.xml_mod import XmlMod, CustomElement


class Builder:
    def __init__(self, file):
        self.xml_mod = XmlMod(file)
        self.xpath = ['.']

    @staticmethod
    def __create_xpath(xpath):
        return '\\'.join(xpath)

    @autolog
    def build(self, model):

        for attr in [attr for attr in dir(model) if not attr.startswith('_') and attr not in ['tag', 'attrs', 'value']]:
            value = getattr(model, attr)
            if isinstance(value, CustomElement):
                self.xml_mod.insert(value, self.__create_xpath(self.xpath))
                continue
            if isinstance(value, list):
                self.xpath.append(attr)
                for item in value:
                    self.build(item)
                self.xpath.pop()
