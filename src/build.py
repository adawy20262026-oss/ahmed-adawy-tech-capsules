"""
Build Entry Point
Ahmed Adawy Tech Capsules
"""

from pathlib import Path
import sys

from builder import CapsuleBuilder


def main():

    builder = CapsuleBuilder()

    # لو المستخدم كتب اسم ملف
    if len(sys.argv) > 1:

        source = Path(sys.argv[1])

        builder.build(source)

    # لو مفيش Arguments
    # ابني كل الكبسولات
    else:

        builder.build_all()

    print("Build completed successfully.")


if __name__ == "__main__":
    main()
