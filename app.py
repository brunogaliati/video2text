import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from openai import OpenAI

client = OpenAI(api_key="YOUR OPENAI API KEY")

# YouTube video URL
url = "https://www.youtube.com/watch?v=aI3HcoU99qY"

# Initialize YouTube object with progress callback
yt = YouTube(url, on_progress_callback=on_progress)

# Print the video title
print(f"Downloading audio from: {yt.title}")

# Get audio-only stream
audio_stream = yt.streams.get_audio_only()

# Create the directory if it doesn't exist
os.makedirs('sample', exist_ok=True)

# Create a safe filename by removing invalid characters
safe_title = "".join(c for c in yt.title if c.isalnum() or c in (' ', '_')).rstrip()
filename = os.path.join('sample', f"{safe_title}.wav")

# Download the audio and save it as a WAV file in the 'sample' directory
audio_stream.download(output_path='sample', filename=f"{safe_title}.wav")

# Load audio file for transcription
with open(filename, 'rb') as audio_file:
    # Transcribe audio using OpenAI API
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )

# Print the transcribed text
print("Transcription: ")
print(transcription.text)

# Store transcribed quotes
quotes = transcription.text

def format_message(role, content):
    """Format a message for the OpenAI API."""
    return {"role": role, "content": content}

def get_response(messages):
    """Send a message to the OpenAI API and return the response."""
    completion = client.chat.completions.create(
        model='gpt-4o-mini',  # newest, cheapest model
        messages=messages,
    )
    return completion.choices[0].message.content

# Instructions for summarization
instructions = f"""
You are an investment manager who uses several communication channels to convey information to clients regarding political and economic news, reports, and articles. 
Please take the text below and create a summary for this purpose. 
Use simple yet professional language. The idea is to summarize the central points of the text using different phrasing, always in the third person, referring to the person speaking in the text, not the manager themselves. 
For example: I want to give an update based on a video I recently watched. The idea is that the recent changes...
Avoid phrases like "the presenter said" or "the presenter concluded." Instead, use more direct expressions like: "The central idea is that the improvement..."
Always respond in Portuguese, even if the base text is in another language.
Do not omit any points or arguments from the text. The goal is to summarize efficiently without losing content.
Quotes: {quotes}
"""

# Prepare message and get response
message = format_message("system", instructions)
messages = [message]
response = get_response(messages)

# Print the summarized response
print("Summary: ")
print(response)
