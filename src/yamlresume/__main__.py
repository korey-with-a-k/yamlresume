import argparse

import yaml

from .build import build_html


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-i", "--in-file", default="schema.yml", help="input YAML file")
    parser.add_argument(
        "-o", "--out-file", default="resume.html", help="output HTML file"
    )
    parser.add_argument("--font-awesome-id", help="required for some icons")
    parser.add_argument("--dark", dest="dark_color")
    parser.add_argument("--light", dest="light_color")
    parser.add_argument("--primary", dest="primary_color")
    parser.add_argument("--secondary", dest="secondary_color")
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
