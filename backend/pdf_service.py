import os

from reportlab.lib.pagesizes import A4

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)


def create_pdf(comic):

    os.makedirs(
        "generated",
        exist_ok=True
    )

    pdf_path = os.path.join(
        "generated",
        "ComicCraft.pdf"
    )

    document = SimpleDocTemplate(
        pdf_path,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            comic["title"],
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    for panel in comic["panels"]:

        content.append(
            Paragraph(
                f"Panel {panel['panel_number']}",
                styles["Heading2"]
            )
        )

        image_path = panel.get(
            "image_path"
        )

        if image_path and os.path.exists(
            image_path
        ):

            content.append(
                Image(
                    image_path,
                    width=450,
                    height=300
                )
            )

        content.append(
            Spacer(1, 10)
        )

        content.append(
            Paragraph(
                f"<b>Scene:</b> "
                f"{panel['scene']}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Narration:</b> "
                f"{panel['narration']}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Dialogue:</b> "
                f"{panel['dialogue']}",
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 25)
        )

    document.build(content)

    return pdf_path
