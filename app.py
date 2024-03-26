import os
import time
from dotenv import load_dotenv
from deepgram import (
    DeepgramClient,
    SpeakOptions,
)
from flask import Flask, render_template, request, redirect, url_for
from pydub import AudioSegment
from pydub.playback import play

app = Flask(__name__, template_folder="templates")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

load_dotenv()
SPEAK_OPTIONS = {"text": "Hello!"}
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/speak", methods=["POST"])
def speak():
    audio_str = request.form['content']
    SPEAK_OPTIONS = {"text":audio_str}

    try:
        deepgram = DeepgramClient(DEEPGRAM_API_KEY)
        options = SpeakOptions(
            model="aura-luna-en", encoding="linear16", container="wav"
        )
        response = deepgram.speak.v("1").save(
            STATIC_DIR + "/speakup_output.wav", SPEAK_OPTIONS, options
        )
        print(response.to_json(indent=4))
    except Exception as e:
        print(f"Exception: {e}")

    song = AudioSegment.from_wav(STATIC_DIR + "/speakup_output.wav")
    play(song)

    return render_template("audio.html")

if __name__ == "__main__":
    app.run(debug=True)