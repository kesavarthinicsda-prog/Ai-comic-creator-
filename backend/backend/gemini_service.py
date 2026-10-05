import os
import json

from dotenv import load_dotenv
from google import genai


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_story(data):

    prompt = f"""
You are a professional comic book writer.

Create a short comic story based on the following information.

Story idea:
{data.story_prompt}

Main character:
{data.character_name}

Setting:
{data.setting}

Tone:
{data.tone}

Art style:
{data.art_style}

Number of panels:
{data.panels}

Return ONLY valid JSON.

Format:

{{
    "title": "Comic Title",
    "panels": [
        {{
            "panel_number": 1,
            "scene": "Scene description",
            "narration": "Narration",
            "dialogue": "Dialogue",
            "image_prompt": "Image generation prompt"
        }}
    ]
}}

Create exactly {data.panels} panels.
Keep the character consistent throughout the story.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```"):

        text = text.replace(
            "```json",
            ""
        )

        text = text.replace(
            "```",
            ""
        )

        text = text.strip()

    return json.loads(text)
