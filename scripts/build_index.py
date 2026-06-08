#!/usr/bin/env python3
"""Build the static homepage from section partials."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / "templates" / "index.html"
SECTIONS_DIR = ROOT / "sections"
OUTPUT_PATH = ROOT / "index.html"
SECTION_PATTERN = re.compile(r"\{\{section:([a-z0-9_-]+)\}\}")


def load_section(match):
    name = match.group(1)
    path = SECTIONS_DIR / f"{name}.html"
    if not path.exists():
        raise FileNotFoundError(f"Missing section partial: {path}")
    return path.read_text(encoding="utf-8").rstrip()


def main():
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    rendered = SECTION_PATTERN.sub(load_section, template)
    if SECTION_PATTERN.search(rendered):
        raise ValueError("Unresolved section placeholder in rendered index.html")
    OUTPUT_PATH.write_text(f"{rendered.rstrip()}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
