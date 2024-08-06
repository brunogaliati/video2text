
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
├── .env                   # Example environment variables file
└── sample/                # Directory for downloaded audio files
   └── example.wav
```

## Example Transcription

Here is an example of the transcription output:

"There is significant political activity as Vice President Kamala Harris is anticipated to announce her vice presidential running mate soon. Meanwhile, former President Trump has begun campaigning in Georgia, a key battleground state. An important aspect of the current political landscape is the ongoing discussion about debates; Trump has accepted an invitation to debate Harris on Fox News on September 4th, while Harris has not yet confirmed her participation. This situation reflects a broader perception where both parties are attempting to depict each other as avoiding the debate stage.

Political analyst Steve Swatt highlights that the situation indicates Trump may prefer a debate on Fox News, perceived to be more favorable for him, rather than on ABC, which was initially agreed upon by both Trump and President Biden before Biden withdrew from the race. Despite Trump’s claims that the ABC debate invitation is canceled, it still remains open for both candidates.

As for Harris's selection of a running mate, she is seeking someone who can enhance her chances of winning, with potential candidates including Pennsylvania Governor Josh Shapiro and former astronaut Mark Kelly from Arizona, among others. 

On the campaign trail, Trump, accompanied by his running mate J.D. Vance, expresses confidence and enthusiasm for his audience in Georgia, emphasizing the closeness of the 2020 election in the state. Current polling indicates a very tight race, with Harris enjoying a slight lead over Trump nationally and in several swing states crucial for the upcoming election."

## Contact

For any questions or suggestions, feel free to open an issue or reach out.
