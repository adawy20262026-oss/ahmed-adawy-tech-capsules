"""
Metadata Parser
Ahmed Adawy Tech Capsules
"""


class MetadataParser:

    def parse(self, text: str):

        if not text.startswith("---"):
            return {}, text

        parts = text.split("---", 2)

        if len(parts) < 3:
            return {}, text

        metadata_text = parts[1].strip()
        content = parts[2].strip()

        metadata = {}

        for line in metadata_text.splitlines():

            if ":" not in line:
                continue

            key, value = line.split(":", 1)

            metadata[key.strip()] = value.strip()

        return metadata, content
