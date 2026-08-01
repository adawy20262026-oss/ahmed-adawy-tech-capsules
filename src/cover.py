"""
Cover Renderer
Ahmed Adawy Tech Capsules
"""


class CoverRenderer:

    def render(self, metadata):

        project = metadata.get(
            "project",
            "Ahmed Adawy Tech Capsules"
        )

        title = metadata.get(
            "title",
            "Untitled Capsule"
        )

        subtitle = metadata.get(
            "subtitle",
            ""
        )

        author = metadata.get(
            "author",
            "Ahmed Adawy"
        )

        category = metadata.get(
            "category",
            "General"
        )

        difficulty = metadata.get(
            "difficulty",
            "Beginner"
        )

        language = metadata.get(
            "language",
            "English"
        )

        version = metadata.get(
            "version",
            "1.0"
        )

        return f"""
<div class="cover">

<div class="cover-brand">
{project}
</div>

<h1>{title}</h1>

<h2>{subtitle}</h2>

<div class="cover-divider"></div>

<table class="cover-meta">

<tr>
<td><strong>Author</strong></td>
<td>{author}</td>
</tr>

<tr>
<td><strong>Category</strong></td>
<td>{category}</td>
</tr>

<tr>
<td><strong>Difficulty</strong></td>
<td>{difficulty}</td>
</tr>

<tr>
<td><strong>Language</strong></td>
<td>{language}</td>
</tr>

<tr>
<td><strong>Version</strong></td>
<td>{version}</td>
</tr>

</table>

<div class="cover-footer">

Professional Technical Capsule

</div>

</div>
"""
