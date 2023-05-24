from pathlib import Path
from typing import Optional, Union

from bottle import SimpleTemplate
from lxml import etree

from .defaults import default_icons, default_styles
from .qr import make_qr_code_svg


class Container(dict):
    """
    Allows lookup by attribute (dot notation) as well as by
    key (square bracket notation). Returns None if an
    attribute is not found

    Intended to make JSON/YAML data easier to use with the
    SimpleTemplate engine
    """

    def __init__(self, **kwargs) -> None:
        super().__init__({k: self._recurse(v) for k, v in kwargs.items()})

    @classmethod
    def _recurse(cls, v):
        if isinstance(v, dict):
            return cls(**v)
        if isinstance(v, list):
            return [cls._recurse(i) for i in v]
        return v

    def __getattr__(self, name):
        return self.get(name)


def apply_styles(data: Container, **kwargs) -> None:
    data["style"] = data.style or Container()
    for name, default in default_styles.items():
        value = kwargs.get(name)
        if value is not None:
            data.style[name] = value
        else:
            data.style.setdefault(name, default)


def load_svg(path: str) -> str:
    parser = etree.HTMLParser()
    svg = etree.parse(path, parser).find(".//svg")
    viewbox = svg.get("viewbox")
    if not viewbox:
        width = svg.get("width")
        height = svg.get("height")
        svg.set("viewbox", f"0 0 {width} {height}")
    return etree.tostring(svg)


def expand_item_with_icon(
    item: Union[str, Container], name: Optional[str] = None
) -> Container:
    if isinstance(item, str):
        item = Container(value=item)

    if item.path:
        item["svg"] = load_svg(item.path)
    elif "icon" not in item:
        name = name or item.value
        icon = default_icons.get(name.lower())
        if icon:
            item["icon"] = icon

    return item


def build_html(data: dict, **style_kwargs) -> str:
    parent_dir = Path(__file__).resolve().parent
    tpl = SimpleTemplate(name="index.tpl", lookup=[parent_dir / "templates"])

    data = Container(**data)

    apply_styles(data, **style_kwargs)

    for name, item in data.contact_info.items():
        data.contact_info[name] = expand_item_with_icon(item, name=name)

    for section, items in data.sidebar.items():
        data.sidebar[section] = [expand_item_with_icon(i) for i in items]

    if data.qr_code:
        data["qr_code_svg"] = make_qr_code_svg(**data.qr_code)

    return tpl.render(data)
