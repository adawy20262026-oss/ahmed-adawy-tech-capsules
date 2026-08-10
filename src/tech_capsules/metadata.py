"""
Metadata Parser
Ahmed Adawy Tech Capsules
"""


class MetadataParser:

    DEFAULTS = {
        "project": "Ahmed Adawy Tech Capsules",
        "title": "Untitled Capsule",
        "subtitle": "",
        "author": "Ahmed Adawy",
        "category": "General",
        "difficulty": "Beginner",
        "language": "English",
        "version": "1.0",
    }

    def parse(self, text: str):

        if not text.startswith("---"):
            return self.DEFAULTS.copy(), text

        parts = text.split("---", 2)

        if len(parts) < 3:
            return self.DEFAULTS.copy(), text

        metadata_text = parts[1].strip()
        content = parts[2].strip()

        metadata = self.DEFAULTS.copy()

        for line in metadata_text.splitlines():

            line = line.strip()

            if not line:
                continue

            if ":" not in line:
                continue

            key, value = line.split(":", 1)

            key = key.strip().lower()
            value = value.strip()

            if value:
                metadata[key] = value

        return metadata, content
