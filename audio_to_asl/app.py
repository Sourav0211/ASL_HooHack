import os
from flask import Flask, request, jsonify
from scripts.speech_to_text import speech_to_text
from scripts.text_to_sign import convert_to_sign_grammar
# from scripts.sign_mapping import get_sign_videos

app = Flask(__name__)

os.makedirs("audio_to_text", exist_ok=True)
os.makedirs("text_to_sign", exist_ok=True)

@app.route("/convert", methods=["POST"])
def convert():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files["audio"]
    audio_path = "mic_to_audio/temp_audio.wav"
    audio_file.save(audio_path)

    print(f"✅ Audio file saved at: {audio_path}")

    # Step 1: Convert speech to text
    text = speech_to_text(audio_path)
    # Save the transcribed text in a file
    text_filename = f"audio_to_text/transcription.txt"
    with open(text_filename, "w") as f:
        f.write(text)

    print(f"📝 Recognized Text: {text}")
    
    # Step 2: Convert text to sign language grammar
    sign_sentence = convert_to_sign_grammar(text)

    # Save the transcribed sign text in a file
    sign_text_filename = f"text_to_sign/sign_transcription.txt"
    with open(sign_text_filename, "w") as f:
        f.write(sign_sentence)
    
    # Step 3: Map to sign videos
    # video_paths = get_sign_videos(sign_sentence)
    print(f"📝 Recognized Text: {text}")
    print(f"📝 Recognized Text: {sign_sentence}")
    
    # return jsonify({"text": text, "sign_sentence": sign_sentence, "videos": video_paths})

if __name__ == "__main__":
    app.run(debug=True)