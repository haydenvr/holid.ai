import base64
import requests
import base64
import os

api_key = "UPDATE-KEY"
def generate_image(text, api_key, test = True, engine_id="stable-diffusion-v1-6", api_host="https://api.stability.ai"):
        if test:
            return open("./imagegen/out/v1_txt2img_0.png", "r")
        
        print("Generating image")
        response = requests.post(
            f"{api_host}/v1/generation/{engine_id}/text-to-image",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {api_key}"
            },
            json={
                "text_prompts": [
                    {
                        "text": text
                    }
                ],
                "cfg_scale": 7,
                "height": 1024,
                "width": 1024,
                "samples": 1,
                "steps": 30,
            },
        )

        if response.status_code != 200:
            raise Exception("Non-200 response: " + str(response.text))

        data = response.json()

        return base64.b64decode(data["artifacts"][0]["base64"])

if __name__ == "__main__":
    print(generate_image("A cute cat", api_key))
