"""
Cover Renderer
Ahmed Adawy Tech Capsules
"""


class CoverRenderer:
    """
    Renders the cover page for a Tech Capsule.
    """

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
            "Professional Technical Publication"
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

        release = metadata.get(
            "release",
            "2026"
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
            <td>Author</td>
            <td>{author}</td>
        </tr>

        <tr>
            <td>Category</td>
            <td>{category}</td>
        </tr>

        <tr>
            <td>Difficulty</td>
            <td>{difficulty}</td>
        </tr>

        <tr>
            <td>Language</td>
            <td>{language}</td>
        </tr>

        <tr>
            <td>Version</td>
            <td>{version}</td>
        </tr>

        <tr>
            <td>Release</td>
            <td>{release}</td>
        </tr>

    </table>

    <div class="cover-footer">
        Professional Technical Capsule
        <br><br>
        © Ahmed Adawy
    </div>

</div>
"""
