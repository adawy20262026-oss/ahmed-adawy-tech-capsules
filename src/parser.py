import mistletoe
from mistletoe.block_token import Heading as MistletoeHeading, Paragraph as MistletoeParagraph, List as MistletoeList, BlockCode, Table as MistletoeTable
from mistletoe.span_token import RawText, Strong, Emphasis, InlineCode, Link as MistletoeLink, Image as MistletoeImage

# Custom Data Classes / Classes for Document Nodes

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
        self.language = language

class Image:
    def __init__(self, src, alt):
        self.src = src
        self.alt = alt

class Table:
    def __init__(self, header, rows):
        self.header = header
        self.rows = rows


def parse_inline(token):
    """Recursively converts inline markdown tokens (Bold, Italic, Links, etc.) to HTML string."""
    if isinstance(token, RawText):
        return token.content
    elif isinstance(token, Strong):
        return f"<strong>{''.join(parse_inline(child) for child in token.children)}</strong>"
    elif isinstance(token, Emphasis):
        return f"<em>{''.join(parse_inline(child) for child in token.children)}</em>"
    elif isinstance(token, InlineCode):
        return f"<code>{''.join(parse_inline(child) for child in token.children)}</code>"
    elif isinstance(token, MistletoeLink):
        target = token.target
        children_text = ''.join(parse_inline(child) for child in token.children)
        return f'<a href="{target}">{children_text}</a>'
    elif hasattr(token, 'children') and token.children:
        return ''.join(parse_inline(child) for child in token.children)
    return getattr(token, 'content', '')


def parse_markdown(markdown_text):
    """Parses markdown string and returns a list of custom node objects."""
    doc = mistletoe.Document(markdown_text)
    nodes = []

    for token in doc.children:
        if isinstance(token, MistletoeHeading):
            text = ''.join(parse_inline(child) for child in token.children)
            nodes.append(Heading(token.level, text))

        elif isinstance(token, MistletoeParagraph):
            # Check if paragraph contains only an image
            if len(token.children) == 1 and isinstance(token.children[0], MistletoeImage):
                img_token = token.children[0]
                alt_text = ''.join(parse_inline(child) for child in img_token.children)
                nodes.append(Image(src=img_token.src, alt=alt_text))
            else:
                text = ''.join(parse_inline(child) for child in token.children)
                nodes.append(Paragraph(text))

        elif isinstance(token, MistletoeList):
            items = []
            for item in token.children:
                # Extract text inside list item
                item_text = ""
                for child in item.children:
                    if hasattr(child, 'children'):
                        item_text += ''.join(parse_inline(c) for c in child.children)
                items.append(item_text)
            nodes.append(BulletList(items))

        elif isinstance(token, BlockCode):
            code_text = ''.join(parse_inline(child) for child in token.children)
            nodes.append(CodeBlock(text=code_text, language=token.language))

        elif isinstance(token, MistletoeTable):
            # Table Header
            header = []
            if hasattr(token, 'header'):
                for cell in token.header.children:
                    header.append(''.join(parse_inline(child) for child in cell.children))
            
            # Table Rows
            rows = []
            for row in token.children:
                row_data = []
                for cell in row.children:
                    row_data.append(''.join(parse_inline(child) for child in cell.children))
                rows.append(row_data)
                
            nodes.append(Table(header=header, rows=rows))

    return nodes
    
# Alias for backward compatibility with build.py
MarkdownParser = parse_markdown
