import argparse

import webcolors
import yaml

from .build import build_html


def to_color(value):
    if value in webcolors.CSS3_NAMES_TO_HEX:
        return value

    if "," in value:
        return f"rgb({value})"

    return f"#{value}" if not value.startswith("#") else value


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-i", "--in-file", default="schema.yml", help="input YAML file")
    parser.add_argument(
        "-o", "--out-file", default="resume.html", help="output HTML file"
    )
    parser.add_argument("--font-awesome-id", help="required for some icons")
    parser.add_argument("--dark", type=to_color, dest="dark_color")
    parser.add_argument("--light", type=to_color, dest="light_color")
    parser.add_argument(
        "--primary",
        type=to_color,
        dest="primary_color",
    )
    parser.add_argument(
        "--secondary",
        type=to_color,
        dest="secondary_color",
    )
    args = parser.parse_args()

    with open(args.in_file) as f:
        data = yaml.safe_load(f)

    if args.font_awesome_id:
        data["font_awesome_id"] = args.font_awesome_id

    html = build_html(data, **vars(args))

    with open(args.out_file, "w") as f:
        f.write(html)


if __name__ == "__main__":
    main()
