import qrcode
from lxml import etree
from qrcode.image.styles.moduledrawers.svg import SvgCircleDrawer
from qrcode.image.svg import SvgPathImage
from scipy.optimize import fsolve


def make_qr_code(data: str) -> bytes:
    qr = qrcode.QRCode(version=7, error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    img = qr.make_image(
        image_factory=SvgPathImage,
        module_drawer=SvgCircleDrawer(),
    )
    svg = img.to_string().replace(b"mm", b"")  # strip units
    return svg


def get_size(element):
    width = element.get("width")
    height = element.get("height")
    if not width or not height:
        viewbox = element.get("viewbox")
        width, height = viewbox.split()[2:]
    return float(width), float(height)


def circle_rect_overlap(circle, rx, ry, rect_width, rect_height, scale=1):
    radius = float(circle.get("r"))
    cx = float(circle.get("cx"))
    cy = float(circle.get("cy"))

    rect_width *= scale
    rect_height *= scale

    # Calculate the distance between the centers
    dx = abs(cx - rx)
    dy = abs(cy - ry)

    # Check if the objects are too far away to overlap
    if dx > (rect_width / 2 + radius):
        return False
    if dy > (rect_height / 2 + radius):
        return False

    # Overlap is possible, check the easy cases
    if dx <= rect_width / 2:
        return True
    if dy <= rect_height / 2:
        return True

    # Calculate the square of the distance between the circle center
    # and the closest corner of the rectangle
    corner_dist_sq = (dx - rect_width / 2) ** 2 + (dy - rect_height / 2) ** 2

    # Check if that distance is less than the circle radius
    return corner_dist_sq <= radius**2


def circle_ellipse_overlap(circle, ex, ey, ellipse_width, ellipse_height, scale=1):
    cr = float(circle.get("r"))
    cx = float(circle.get("cx"))
    cy = float(circle.get("cy"))

    exr = ellipse_width / 2 * scale
    eyr = ellipse_height / 2 * scale

    def equations(vars):
        x, y = vars
        eq1 = (x - ex) ** 2 / exr**2 + (y - ey) ** 2 / eyr**2 - 1
        eq2 = (x - cx) ** 2 + (y - cy) ** 2 - cr**2
        return [eq1, eq2]

    # Check if the circle intersects the ellipse
    root, infodict, ier, mesg = fsolve(equations, (1, 1), full_output=True)
    # print(root, ier, np.isclose(equations(root), [0.0, 0.0]))
    if ier == 1:
        return True

    # Check if the circle is inside the ellipse
    inside_ellipse = (cx - ex) ** 2 / exr**2 + (cy - ey) ** 2 / eyr**2 <= 1
    return inside_ellipse


def embed_svg(bg, fg, shape, fg_scale=4, shape_scale=1.1):
    bg_w, bg_h = get_size(bg)
    ofg_w, ofg_h = get_size(fg)

    fg_w = bg_w / fg_scale
    ratio = fg_w / ofg_w
    fg_h = ofg_h * ratio

    overlap_func = circle_ellipse_overlap if shape == "ellipse" else circle_rect_overlap

    for circle in bg.iter("circle"):
        circle.set("class", "svg-dark")
        if overlap_func(circle, bg_w / 2, bg_h / 2, fg_w, fg_h, scale=shape_scale):
            bg.remove(circle)

    new_x = bg_w / 2 - fg_w / 2
    new_y = bg_h / 2 - fg_h / 2

    for child in fg.iterchildren():
        transform = f"translate({new_x} {new_y}) scale({ratio})"
        original_transform = child.get("transform") or ""
        transform += original_transform
        child.set("transform", transform)
        bg.append(child)


def make_qr_code_svg(
    data,
    embedded_svg_path=None,
    embedded_svg_shape="ellipse",
    scale=4,
    shape_scale=1.1,
):
    qr_svg = make_qr_code(data)
    parser = etree.HTMLParser()
    bg = etree.fromstring(qr_svg, parser).find(".//svg")
    if embedded_svg_path:
        fg = etree.parse(embedded_svg_path, parser).find(".//svg")
        embed_svg(bg, fg, embedded_svg_shape, scale, shape_scale)

    bg.set("viewbox", "4 4 45 45")
    bg.set("width", "130")
    bg.set("height", "130")
    return etree.tostring(bg)
