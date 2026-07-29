"""
Ahmed Adawy Tech Capsules
Build Engine v0.1.0
"""

from parser import read_capsule
from html_generator import generate_html

from pathlib import Path


def main():

    capsule = Path("../capsules/linux-cli.md")

    print("=" * 50)
    print("Ahmed Adawy Tech Capsules")
    print("=" * 50)

    print("\nReading capsule...")

    markdown = read_capsule(capsule)

    print("Done.")

    print("\nGenerating HTML...")

    html = generate_html(markdown)

    print("Done.")

    print("\nPreview:\n")

    print(html[:600])

    print("\nBuild completed successfully.")


if __name__ == "__main__":
    main()            print(f"[Missing] {folder}")


def main():
    print_banner()
    check_structure()
    print("\nBuilder is ready.")
    print("PDF generation will be added soon.")


if __name__ == "__main__":
    main()
