"""
Syntax Highlighting Engine
Ahmed Adawy Tech Capsules
"""

from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound


class SyntaxHighlighter:
    """
    Converts source code into syntax-highlighted HTML.
    """

    def __init__(self):

        self.formatter = HtmlFormatter(
            nowrap=False,
            cssclass="highlight"
        )

    def highlight(self, code: str, language: str = "") -> str:

        if not language:
            lexer = TextLexer()

        else:
            try:
                lexer = get_lexer_by_name(language)

            except ClassNotFound:
                lexer = TextLexer()

        return highlight(
            code,
            lexer,
            self.formatter
        )

    def css(self):

        return self.formatter.get_style_defs(".highlight")
