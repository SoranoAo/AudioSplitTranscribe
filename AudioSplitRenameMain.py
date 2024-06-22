from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
import os

def split_audio_on_silence(audio_path, min_silence_len=3000, silence_thresh=-80, keep_silence=1000):
    # Load audio file
    audio = AudioSegment.from_wav(audio_path)
    
    # Split audio based on silence
    chunks = split_on_silence(audio, 
                              min_silence_len=min_silence_len, 
                              silence_thresh=silence_thresh, 
                              keep_silence=keep_silence)
    
    return chunks

def transcribe_audio(audio_chunk):
    recognizer = sr.Recognizer()
    with audio_chunk.export(format="wav") as audio_file:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
            try:
                # Transcribe audio
                text = recognizer.recognize_google(audio, language='ja-JP')
                return text
            except sr.UnknownValueError:
                return "Unintelligible"
            except sr.RequestError as e:
                return f"API request error: {e}"

def save_chunks_with_transcriptions(chunks, output_dir, original_filename):
    for i, chunk in enumerate(chunks):
        transcription = transcribe_audio(chunk)
        filename = f"{transcription[:30].replace(' ', '_')}_{i}.wav"
        output_path = os.path.join(output_dir, filename)
        chunk.export(output_path, format="wav")
        print(f"Saved {output_path}")


def process_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".wav"):
            input_audio_path = os.path.join(input_dir, filename)
            print(f"Processing {input_audio_path}...")
            chunks = split_audio_on_silence(input_audio_path)
            save_chunks_with_transcriptions(chunks, output_dir, os.path.splitext(filename)[0])

if __name__ == "__main__":
    current_dir = os.getcwd()
    input_dir = os.path.join(current_dir,"input_wav")
    output_dir = os.path.join(current_dir,"output_wav")
    process_directory(input_dir, output_dir)