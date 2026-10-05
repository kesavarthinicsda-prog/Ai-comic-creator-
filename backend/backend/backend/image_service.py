import os
import uuid

from dotenv import load_dotenv
from google import genai


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_image(prompt):

    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=prompt
    )

    os.makedirs(
        "generated",
        exist_ok=True
    )

    filename = (
        f"{uuid.uuid4()}.png"
    )

    filepath = os.path.join(
        "generated",
        filename
    )

    for part in response.parts:

        if getattr(
            part,
            "inline_data",
            None
        ):

            image = part.as_image()

            image.save(filepath)

            return filepath

    return None
