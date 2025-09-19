import os
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__)

# Zenék mappája (tegyél ide MP3 fájlokat Renderen)
MUSIC_DIR = "."

@app.route("/songs")
def list_songs():
    files = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]
    return jsonify(files)

@app.route("/play/<filename>")
def get_song(filename):
    return send_from_directory(MUSIC_DIR, filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render által adott port
    app.run(host="0.0.0.0", port=port)
