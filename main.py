from textblob import TextBlob
import pyttsx3

# -----------------------------
# Emotion Detection Function
# -----------------------------
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


# -----------------------------
# Emotion → Voice Mapping
# -----------------------------
def get_voice_config(emotion, intensity):
    base_config = {
        "very_positive": {"rate": 220, "volume": 1.0},
        "positive": {"rate": 190, "volume": 0.9},
        "neutral": {"rate": 150, "volume": 0.8},
        "negative": {"rate": 130, "volume": 0.7},
        "very_negative": {"rate": 110, "volume": 0.6},
    }

    config = base_config[emotion]

    # Intensity scaling (BONUS feature 🔥)
    config["rate"] += int(intensity * 30)
    config["volume"] = min(1.0, config["volume"] + intensity * 0.2)

    return config


# -----------------------------
# Main Program
# -----------------------------
def main():
    text = input("Enter text: ")

    emotion, intensity = detect_emotion(text)

    engine = pyttsx3.init()

    # Optional: change voice (better feel)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    config = get_voice_config(emotion, intensity)

    engine.setProperty('rate', config["rate"])
    engine.setProperty('volume', config["volume"])

    # Output file
    output_file = "output.mp3"
    engine.save_to_file(text, output_file)
    engine.runAndWait()

    print("\n--- RESULT ---")
    print("Detected Emotion:", emotion)
    print("Intensity:", round(intensity, 2))
    print("Rate:", config["rate"])
    print("Volume:", round(config["volume"], 2))
    print("Audio saved as:", output_file)


if __name__ == "__main__":
    main()