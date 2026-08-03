import mistletoe

from mistletoe.block_token import (
    Heading as MistletoeHeading,
    Paragraph as MistletoeParagraph,
    List as MistletoeList,
    CodeFence,
    Table as MistletoeTable,
)

from mistletoe.span_token import (
    RawText,
    Strong,
    Emphasis,
    InlineCode,
    Link as MistletoeLink,
    Image as MistletoeImage,
)


class Heading:

    def __init__(self, level, text):

        self.level = level
        self.text = text


class Paragraph:

    def __init__(self, text):

        self.text = text


class BulletList:

    def __init__(self, items):

        self.items = items


class CodeBlock:

    def __init__(self, text, language=""):

        self.text = text
        self.language = language or ""


class Image:

    def __init__(self, src, alt):

        self.src = src
        self.alt = alt


class Table:

    def __init__(self, header, rows):

        self.header = header
        self.rows = rows


def parse_inline(token):
    """
    Convert inline markdown tokens into HTML.
    """

    if isinstance(token, RawText):
        return token.content

    if isinstance(token, Strong):
        return (
            "<strong>"
            + "".join(
                parse_inline(child)
                for child in token.children
            )
            + "</strong>"
        )

    if isinstance(token, Emphasis):
        return (
            "<em>"
            + "".join(
                parse_inline(child)
                for child in token.children
            )
            + "</em>"
        )

    if isinstance(token, InlineCode):
        return (
            "<code>"
            + "".join(
                parse_inline(child)
                for child in token.children
            )
            + "</code>"
        )

    if isinstance(token, MistletoeLink):

        text = "".join(
            parse_inline(child)
            for child in token.children
        )

        return (
            f'<a href="{token.target}">'
            f"{text}"
            "</a>"
        )

    if hasattr(token, "children") and token.children:

        return "".join(
            parse_inline(child)
            for child in token.children
        )

    return getattr(token, "content", "")

def parse_markdown(markdown_text):
    """
    Parse markdown into internal nodes.
    """

    document = mistletoe.Document(markdown_text)

    nodes = []

    for token in document.children:
        print(type(token))
        
        if isinstance(token, MistletoeHeading):

            text = "".join(
                parse_inline(child)
                for child in token.children
            )

            nodes.append(
                Heading(
                    token.level,
                    text,
                )
            )

        elif isinstance(
            token,
            MistletoeParagraph,
        ):

            if (
                len(token.children) == 1
                and isinstance(
                    token.children[0],
                    MistletoeImage,
                )
            ):

                image = token.children[0]

                alt = "".join(
                    parse_inline(child)
                    for child in image.children
                )

                nodes.append(
                    Image(
                        image.src,
                        alt,
                    )
                )

            else:

                text = "".join(
                    parse_inline(child)
                    for child in token.children
                )

                nodes.append(
                    Paragraph(text)
                )

        elif isinstance(
            token,
            MistletoeList,
        ):

            items = []

            for item in token.children:

                value = ""

                for child in item.children:

                    if hasattr(
                        child,
                        "children",
                    ):

                        value += "".join(
                            parse_inline(c)
                            for c in child.children
                        )

                items.append(value)
            nodes.append(
                BulletList(items)
            )

        elif isinstance(
            token,
            CodeFence,
        ):

            code = getattr(
                token,
                "content", 
                "",
            )

            if (
                not code
                and hasattr(
                    token, 
                    "children",
                )
            ):
                
                code = "".join(
                    getattr(
                        child, 
                        "content", 
                        "",
                    )
                    for child in token.children
                )

            nodes.append(
                CodeBlock(
                    code,
                    token.language or "",
                )
            )

        elif isinstance(
            token,
            MistletoeTable,
        ):

            header = []

            if hasattr(token, "header"):

                for cell in token.header.children:

                    header.append(
                        "".join(
                            parse_inline(child)
                            for child in cell.children
                        )
                    )

            rows = []

            for row in token.children:

                current = []

                for cell in row.children:

                    current.append(
                        "".join(
                            parse_inline(child)
                            for child in cell.children
                        )
                    )

                rows.append(current)
            nodes.append(
                Table(
                    header,
                    rows,
                )
            )

    return nodes


class MarkdownParser:
    """
    Compatibility wrapper.
    """

    def parse(self, markdown_text):

        return parse_markdown(
            markdown_text
        )

    def __call__(self, markdown_text):

        return self.parse(
            markdown_text
        )
