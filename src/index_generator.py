"""
Library Index Generator
Ahmed Adawy Tech Capsules
"""

from config import (
    OUTPUT_DIR,
    DEFAULT_ENCODING,
)

from library_template import (
    LibraryTemplate,
)


class IndexGenerator:

    def generate(self, capsules):

        OUTPUT_DIR.mkdir(
            exist_ok=True
        )

        html = [

            LibraryTemplate.render_header(
                len(capsules)
            )

        ]

        for capsule in capsules:

            html.append(

                LibraryTemplate.render_card(
                    capsule
                )

            )

        html.append(

            LibraryTemplate.render_footer()

        )

        (
            OUTPUT_DIR
            / "index.html"
        ).write_text(

            "\n".join(html),

            encoding=DEFAULT_ENCODING,

        )

        print(
            "Library index generated."
        )
