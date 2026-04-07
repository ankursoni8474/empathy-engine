from flask import Flask, render_template, request, send_file
from textblob import TextBlob
import pyttsx3
import os

app = Flask(__name__)

def detect_emotion(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.6:
        return "very_positive", abs(polarity)
    elif polarity > 0.2:
        return "positive", abs(polarity)
    elif polarity < -0.6:
        return "very_negative", abs(polarity)
    elif polarity < -0.2:
        return "negative", abs(polarity)
    else:
        return "neutral", abs(polarity)

def get_voice_config(emotion, intensity):
    base_config = {
        "very_positive": {"rate": 220, "volume": 1.0},
        "positive": {"rate": 190, "volume": 0.9},
        "neutral": {"rate": 150, "volume": 0.8},
        "negative": {"rate": 130, "volume": 0.7},
        "very_negative": {"rate": 110, "volume": 0.6},
    }

    config = base_config[emotion]
    config["rate"] += int(intensity * 30)
    config["volume"] = min(1.0, config["volume"] + intensity * 0.2)

    return config

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']

        emotion, intensity = detect_emotion(text)
        config = get_voice_config(emotion, intensity)

        engine = pyttsx3.init()
        engine.setProperty('rate', config["rate"])
        engine.setProperty('volume', config["volume"])

        output_file = os.path.join("static", "output.mp3")
        engine.save_to_file(text, output_file)
        engine.runAndWait()

        return render_template('index.html', audio=True, emotion=emotion)

    return render_template('index.html', audio=False)

if __name__ == '__main__':
    app.run(debug=True)