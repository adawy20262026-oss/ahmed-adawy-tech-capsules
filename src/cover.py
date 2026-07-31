"""
Cover Renderer
Ahmed Adawy Tech Capsules
"""


class CoverRenderer:

    def render(self, metadata):

        title = metadata.get(
            "title",
            "Ahmed Adawy Tech Capsules"
        )

        subtitle = metadata.get(
            "subtitle",
            ""
        )

        author = metadata.get(
            "author",
            "Ahmed Adawy"
        )

        version = metadata.get(
            "version",
            "1.0"
        )

        return f"""
<div class="cover">

<p>Ahmed Adawy Tech Capsules</p>

<h1>{title}</h1>

<h2>{subtitle}</h2>

<p>

<b>Author</b><br>

{author}

</p>

<p>

Version {version}

</p>

</div>
"""
