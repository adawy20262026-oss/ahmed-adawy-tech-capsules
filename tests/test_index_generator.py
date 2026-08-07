from index_generator import IndexGenerator
import index_generator


def test_generate_creates_index(tmp_path, monkeypatch):

    monkeypatch.setattr(index_generator, "OUTPUT_DIR", tmp_path)

    generator = IndexGenerator()

    capsules = [
        {
            "title": "Python Basics",
            "subtitle": "Learn Python",
            "category": "Python",
            "difficulty": "Beginner",
            "language": "en",
            "version": "1.0",
            "file": "python-basics",
        }
    ]

    generator.generate(capsules)

    assert (tmp_path / "index.html").exists()


def test_generate_contains_title(tmp_path, monkeypatch):

    monkeypatch.setattr(index_generator, "OUTPUT_DIR", tmp_path)

    generator = IndexGenerator()

    capsules = [
        {
            "title": "Python Basics",
            "file": "python-basics",
        }
    ]

    generator.generate(capsules)

    html = (tmp_path / "index.html").read_text()

    assert "Python Basics" in html
    assert "Ahmed Adawy Tech Capsules" in html


def test_generate_empty_library(tmp_path, monkeypatch):

    monkeypatch.setattr(index_generator, "OUTPUT_DIR", tmp_path)

    generator = IndexGenerator()

    generator.generate([])

    html = (tmp_path / "index.html").read_text()

    assert "<html" in html
    assert "</html>" in html
