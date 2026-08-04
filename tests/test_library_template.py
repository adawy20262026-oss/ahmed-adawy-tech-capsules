from library_template import LibraryTemplate


def test_render_header():

    html = LibraryTemplate.render_header(10)

    assert "Ahmed Adawy Tech Capsules" in html
    assert "Total Capsules: 10" in html
    assert "<html" in html
    assert "</head>" in html
    assert '<div class="library">' in html


def test_render_card():

    capsule = {
        "title": "Python Basics",
        "subtitle": "Learn Python",
        "category": "Python",
        "difficulty": "Beginner",
        "language": "en",
        "version": "1.0",
        "file": "python-basics",
    }

    html = LibraryTemplate.render_card(capsule)

    assert "Python Basics" in html
    assert "Learn Python" in html
    assert "Beginner" in html
    assert "Version 1.0" in html
    assert "python-basics.html" in html
    assert "python-basics.pdf" in html
    assert "#198754" in html


def test_render_card_default_values():

    html = LibraryTemplate.render_card({})

    assert "Untitled Capsule" in html
    assert "General" in html
    assert "Beginner" in html
    assert "Version 1.0" in html
    assert "unknown.html" in html
    assert "unknown.pdf" in html


def test_render_footer():

    html = LibraryTemplate.render_footer()

    assert "searchCapsules" in html
    assert "</html>" in html
    assert "Ahmed Adawy Tech Capsules" in html
