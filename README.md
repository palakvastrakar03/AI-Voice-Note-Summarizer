# AI Voice Note Summarizer
An end-to-end AI-powered web application that converts voice notes into concise summaries, key bullet points, and important keywords.
Designed to help users quickly understand long audio recordings without listening to the entire file.
This project integrates speech-to-text, natural language processing, and a modern animated frontend.
---

## Features: 
-  Upload any voice note (audio file)
-  Automatic speech-to-text transcription using **OpenAI Whisper**
-  AI-generated summary of the spoken content
-  Bullet-point key highlights
-  Keyword extraction for quick understanding
-  Modern animated UI with smooth transitions
-  Frontend–backend integration using REST APIs

---
## Tech Stack:
### Frontend
HTML5
CSS3 (animations, gradients, glassmorphism)
JavaScript (Vanilla JS)

### Backend
Python
FastAPI
Uvicorn

### AI / ML
Whisper (Speech-to-Text)
Hugging Face Transformers
BART Large CNN (Summarization)
KeyBERT (Keyword Extraction)

### Utilities
FFmpeg – audio conversion
Git & GitHub – version control

---

## How the Project Works:
1. User uploads an audio file through the web interface  
2. Backend converts audio to text using **Whisper**
3. Transcribed text is processed using **NLP summarization models**
4. The system generates:
   - Summary
   - Key points
   - Keywords
5. Results are displayed with animated UI elements

---

## System Architecture:
```
User Audio Upload
        ↓
 Audio Normalization (FFmpeg)
        ↓
 Speech-to-Text (Whisper)
        ↓
 Text Processing
   ├── Summary Generation
   ├── Bullet Point Extraction
   └── Keyword Extraction
        ↓
 Frontend Visualization
```
---

## Project Structure:
```
VoiceSummarizer/
│
├── backend/
│ ├── main.py
│ ├── transcribe.py
│ ├── summarize.py
│ ├── ai_features.py
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── uploads/
├── requirements.txt
└── README.md
```

---

## Example Output:
-Summary:
 A concise explanation of the main idea spoken in the audio.
-Key Points:
 Important statements extracted from the content
 Structured for quick reading
-Keywords:
 AI-extracted relevant terms from the speech

---

## How to Run the Project:
1. Clone the Repository
2. Create Virtual Environment:
   ```
      python -m venv venv source venv/bin/activate
      venv\Scripts\activate
   ```
3. Install Dependencies: pip install -r requirements.txt
4. Run the Backend: uvicorn backend.main:app --reload
5. Open Frontend: Open frontend/index.html directly in your browser.

---

## Example Use Case:
Summarizing lecture recordings
Quickly reviewing meeting notes
Extracting key ideas from voice journals
Converting long voice notes into readable content

---

## Performance Notes:
Runs completely on CPU
Best suited for short to medium audio files
No internet or paid API dependency after setup

---

## Limitations:
Not deployed (runs locally)
Long audio files may take more processing time
English language focused

---

## Project Status:
- Completed
- Working Locally


---

## Author:
Palak Vastrakar 

---

## Acknowledgements:
OpenAI Whisper
Hugging Face Transformers
FastAPI Community
