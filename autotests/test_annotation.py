from pathlib import Path
from typing import Any, Union, Dict

import pytest

from core.xml_mod import XmlMod, CustomElement
from models import MainModel
from xml_generator import XmlGenerator


def annotation_check(obj: Any, expected_types: dict[str, Any]):
    if not obj.__annotations__:
        raise AssertionError(f'Object "{obj.__name__}" should have annotation.')
    errors = []
    for k, v in obj.__annotations__.items():
        if k not in expected_types:
            errors.append(f'Excess annotation for param "{k}" of function "{obj.__name__}"')
            continue
        expected = expected_types[k]
        if not isinstance(expected, list):
            expected = [expected]
        if v not in expected:
            errors.append(f'Type of {k} should be {expected} but was {v}')
    message = '\n'.join(errors)
    assert len(errors) == 0, f'Annotation to "{obj.__name__}" was not true. Errors:\n{message}'


@pytest.mark.parametrize('func,types', [
    pytest.param(XmlMod.__init__, {'file': [str, Path, Union[str, Path]]}, id=XmlMod.__init__.__name__),
    pytest.param(XmlMod.xml, {'need_save': bool, 'return': None}, id=XmlMod.xml.__name__),
    pytest.param(XmlMod.create_xml,
                 {'file': [str, Path, Union[str, Path]], 'root_name': str, 'return': None}, id=XmlMod.create_xml.__name__),
    pytest.param(XmlMod.insert, {'element': CustomElement, 'xpath': str, 'return': None}, id=XmlMod.insert.__name__)
])
def test_xml_mod(func, types):
    annotation_check(func, types)


@pytest.mark.parametrize('func,types', [
    pytest.param(CustomElement.__init__, {'tag': str, 'attrs': [dict[str, str], Dict[str, str]], 'value': str},
                 id=CustomElement.__init__.__name__)
])
def test_custom_element(func, types):
    annotation_check(func, types)


@pytest.mark.parametrize('func,types', [
    pytest.param(XmlGenerator.__init__, {'file_path': [str, Path, Union[str, Path]], 'root_name': str},
                 id=XmlGenerator.__init__.__name__),
    pytest.param(XmlGenerator.create, {'model': MainModel, 'return': None}, id=XmlGenerator.create.__name__)
])
def test_xml_generator(func, types):
    annotation_check(func, types)

