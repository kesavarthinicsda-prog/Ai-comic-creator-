const API_URL =
    "http://127.0.0.1:8000";


async function generateComic() {

    const data = {

        story_prompt:
            document.getElementById(
                "story_prompt"
            ).value,

        character_name:
            document.getElementById(
                "character_name"
            ).value,

        setting:
            document.getElementById(
                "setting"
            ).value,

        tone:
            document.getElementById(
                "tone"
            ).value,

        art_style:
            document.getElementById(
                "art_style"
            ).value,

        panels:
            Number(
                document.getElementById(
                    "panels"
                ).value
            )
    };


    document.getElementById(
        "loading"
    ).style.display = "block";


    try {

        const response =
            await fetch(
                `${API_URL}/generate`,
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                        "application/json"
                    },

                    body:
                    JSON.stringify(data)

                }
            );


        const result =
            await response.json();


        showComic(result);


    } catch (error) {

        document.getElementById(
            "result"
        ).innerHTML =
        `<div class="panel">
        ❌ Error generating comic
        </div>`;

    }


    document.getElementById(
        "loading"
    ).style.display = "none";
}


function showComic(data) {

    const result =
        document.getElementById(
            "result"
        );


    result.innerHTML =
        `<h1>${data.title}</h1>`;


    data.panels.forEach(
        panel => {

            const div =
                document.createElement(
                    "div"
                );


            div.className =
                "panel";


            let image = "";


            if (panel.image_path) {

                image =
                `<img src="${API_URL}/${panel.image_path}">`;

            }


            div.innerHTML = `

                <h2>
                    Panel
                    ${panel.panel_number}
                </h2>

                ${image}

                <p>
                    <b>Scene:</b>
                    ${panel.scene}
                </p>

                <p>
                    <b>Narration:</b>
                    ${panel.narration}
                </p>

                <p>
                    <b>Dialogue:</b>
                    ${panel.dialogue}
                </p>

            `;


            result.appendChild(div);

        }
    );


    result.innerHTML += `

        <a
        class="download"
        href="${API_URL}/${data.pdf}"
        target="_blank"
        >
        📄 Download Comic PDF
        </a>

    `;
}
