from metadata import MetadataParser


def test_metadata_parser_creation():

    parser = MetadataParser()

    assert parser is not None


def test_default_metadata():

    parser = MetadataParser()

    metadata, content = parser.parse(
        "# Hello"
    )

    assert metadata["title"] == "Untitled Capsule"
    assert content == "# Hello"


def test_parse_title():

    parser = MetadataParser()

    text = (
        "---\n"
        "title: Python Basics\n"
        "---\n"
        "# Hello"
    )

    metadata, content = parser.parse(text)

    assert metadata["title"] == "Python Basics"
    assert content == "# Hello"


def test_parse_author():

    parser = MetadataParser()

    text = (
        "---\n"
        "author: Ahmed Adawy\n"
        "---\n"
        "Content"
    )

    metadata, _ = parser.parse(text)

    assert metadata["author"] == "Ahmed Adawy"


def test_parse_multiple_fields():

    parser = MetadataParser()

    text = (
        "---\n"
        "title: AI\n"
        "category: Python\n"
        "difficulty: Advanced\n"
        "---\n"
        "Hello"
    )

    metadata, _ = parser.parse(text)

    assert metadata["title"] == "AI"
    assert metadata["category"] == "Python"
    assert metadata["difficulty"] == "Advanced"
