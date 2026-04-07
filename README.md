# Empathy Engine 🎙️

## Overview
This project implements an AI-based Empathy Engine that converts input text into emotionally expressive speech.

Unlike standard text-to-speech systems, this model adjusts vocal characteristics such as rate and volume based on detected emotion, making the output sound more human-like.

---

## Features
- Detects 5 emotion categories:
  - Very Positive
  - Positive
  - Neutral
  - Negative
  - Very Negative
- Uses sentiment polarity to determine emotion intensity
- Dynamically modifies speech parameters (rate, volume)
- Implements clear emotion-to-voice mapping logic
- Generates audio output (.mp3 file)

---

## How It Works
1. Input text is provided by the user
2. Sentiment analysis is performed using TextBlob
3. Emotion and intensity are calculated
4. Voice parameters are adjusted accordingly
5. Audio is generated using pyttsx3

---

## Tech Stack
- Python
- TextBlob (Sentiment Analysis)
- pyttsx3 (Text-to-Speech)

---

## How to Run

### 1. Install dependencies

## Example
Input:

Output:
- Emotion: Very Positive
- Audio file generated: output.mp3

---

## Design Logic (Important)
The system maps detected emotion to speech parameters:

- Very Positive → Fast rate, high volume  
- Positive → Moderately fast, slightly high volume  
- Neutral → Normal rate and volume  
- Negative → Slower rate, lower volume  
- Very Negative → Very slow rate, very low volume  

Additionally, emotion intensity further scales these parameters dynamically.

---

## Future Improvements
- Add pitch control
- Use advanced emotion models (HuggingFace)
- Build a web interface using Flask