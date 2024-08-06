
# YouTube Audio Transcription and Summarization

This project provides a script to download audio from a YouTube video, transcribe the audio using OpenAI's Whisper model, and generate a concise summary of the transcribed text.

## Features

- **Download YouTube Audio**: Extracts and downloads audio from a specified YouTube video URL.
- **Transcription**: Uses OpenAI's Whisper model to transcribe the downloaded audio into text.
- **Summarization**: Generates a professional summary of the transcribed text, tailored for communication in the field of investment management.

## Prerequisites

- Python 3.x
- An OpenAI API key

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Environment Variables**:
   - Create a `.env` file in the root of your project.
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

1. **Edit the Script**:
   - Open `app.py` and set the `url` variable to the desired YouTube video URL.

2. **Run the Script**:
   ```bash
   python app.py
   ```

   The script will:
   - Download the audio from the specified YouTube video.
   - Transcribe the audio using OpenAI's Whisper model.
   - Generate a summary of the transcription.

## Project Structure

```
my-project/
│
├── app.py                 # Main script
├── README.md              # Project documentation
├── requirements.txt       # List of dependencies
├── .env.example           # Example environment variables file
└── sample/                # Directory for downloaded audio files
   └── example.wav
```


## Contact

For any questions or suggestions, feel free to open an issue or reach out.
