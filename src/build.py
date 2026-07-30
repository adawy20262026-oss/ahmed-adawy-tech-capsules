from pathlib import Path
import sys

from builder import CapsuleBuilder


def main():

    if len(sys.argv) > 1:
        source = Path(sys.argv[1])
    else:
        source = Path("capsules/linux-cli-essentials.md")

    builder = CapsuleBuilder()

    builder.build(source)

    print("Capsule built successfully.")


if __name__ == "__main__":
    main()
