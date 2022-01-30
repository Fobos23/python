from typing import _GenericAlias

from core.xml_mod import XmlMod

if __name__ == '__main__':
    annotations = XmlMod.__init__.__annotations__
    for k, v in annotations.items():
        if isinstance(v,  _GenericAlias):
            a = 0
        else:
            actual_type = v.__mro__

