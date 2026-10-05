import os

from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from fastapi.staticfiles import (
    StaticFiles
)

from .models import ComicRequest

from .gemini_service import (
    generate_story
)

from .image_service import (
    generate_image
)

from .pdf_service import (
    create_pdf
)


app = FastAPI(
    title="ComicCraft",
    description="AI Comic Story Creator",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


os.makedirs(
    "generated",
    exist_ok=True
)


app.mount(
    "/generated",
    StaticFiles(
        directory="generated"
    ),
    name="generated"
)


@app.get("/")
def home():

    return {
        "message":
        "ComicCraft API is running"
    }


@app.post("/generate")
def generate_comic(
    data: ComicRequest
):

    comic = generate_story(data)

    for panel in comic["panels"]:

        prompt = f"""
Create a high quality comic illustration.

Character:
{data.character_name}

Setting:
{data.setting}

Art Style:
{data.art_style}

Tone:
{data.tone}

Scene:
{panel["scene"]}

Image details:
{panel["image_prompt"]}

Keep the character appearance
consistent.

Do not add text inside the image.
"""

        image_path = generate_image(
            prompt
        )

        panel["image_path"] = (
            image_path
        )

    pdf_path = create_pdf(
        comic
    )

    return {
        "success": True,
        "title": comic["title"],
        "panels": comic["panels"],
        "pdf": pdf_path
    }
