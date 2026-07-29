"""
Ahmed Adawy Tech Capsules
Build Script

Author: Ahmed Adawy
Version: 0.1.0
"""

from pathlib import Path


PROJECT_NAME = "Ahmed Adawy Tech Capsules"
VERSION = "0.1.0"


def print_banner():
    print("=" * 50)
    print(PROJECT_NAME)
    print(f"Version {VERSION}")
    print("=" * 50)


def check_structure():
    folders = [
        "assets",
        "capsules",
        "templates",
        "output",
    ]

    print("\nChecking project structure...\n")

    for folder in folders:
        if Path(folder).exists():
            print(f"[OK] {folder}")
        else:
            print(f"[Missing] {folder}")


def main():
    print_banner()
    check_structure()
    print("\nBuilder is ready.")
    print("PDF generation will be added soon.")


if __name__ == "__main__":
    main()
