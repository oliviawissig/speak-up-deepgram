import os
from dotenv import load_dotenv
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)
# from flask import Flask, render_template

load_dotenv()
AUDIO_FILE = "no_sleep_podcast.mp3"
DEEPGRAM_API_KEY = os.getenv('DEEPGRAM_API_KEY')

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return render_template('index.html')

def main():
    try:
        deepgram = DeepgramClient(DEEPGRAM_API_KEY)

        with open(AUDIO_FILE, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        options = PrerecordedOptions(model="nova-2", smart_format=True)
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        print(response.to_json(indent=4))

    except Exception as e:
        print(f"Exception: {e}")

if __name__ == '__main__':
	main()