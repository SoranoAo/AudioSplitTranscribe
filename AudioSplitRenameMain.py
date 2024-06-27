from faster_whisper import WhisperModel
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
import os
import re
import json

def convert_to_fullwidth(input_string):
    # 半角文字を全角文字に変換する辞書
    conversion_dict = {
        '!': '！',
        '-': 'ー',
        '?': '？'
    }
    
    # 変換結果を格納するリスト
    converted_string = []

    # 入力文字列を一文字ずつ処理
    for char in input_string:
        if char in conversion_dict:
            converted_string.append(conversion_dict[char])
        else:
            converted_string.append(char)

    # リストを文字列に変換して返す
    return ''.join(converted_string)

def clean_filename(filename: str) -> str:
    # Windowsでファイル名に使えない文字を削除する
    invalid_chars = r'[<>:"/\\|?*]'
    cleaned_filename = re.sub(invalid_chars, '', filename)
    return cleaned_filename

def split_audio_on_silence(audio_path, min_silence_len, silence_thresh, keep_silence):
    # Load audio file
    audio = AudioSegment.from_wav(audio_path)
    
    # Split audio based on silence
    chunks = split_on_silence(audio, 
                              min_silence_len=min_silence_len, 
                              silence_thresh=silence_thresh, 
                              keep_silence=keep_silence)
    
    return chunks


def transcribe_audio_offline_whisper(audio_chunk,model):
       
    with audio_chunk.export(format="wav") as audio_file:
        transcribeList, _ = model.transcribe(audio_file, beam_size=5)
        
        result = ''
        for segment in transcribeList:
            result = result + str(segment.text)
            #print(str(segment.text))
        print("transcribe result: "+str(result))
        
        zenkakuChange = convert_to_fullwidth(result)

        return clean_filename(zenkakuChange)
    

def transcribe_audio_online(audio_chunk):
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


def save_chunks_with_transcriptions(chunks, output_dir, original_filename,model):
    for i, chunk in enumerate(chunks):
        #transcription = transcribe_audio_online(chunk)
        transcription = transcribe_audio_offline_whisper(chunk,model)
        filename = f"{transcription[:30].replace(' ', '_')}_{i}.wav"
        output_path = os.path.join(output_dir, filename)
        chunk.export(output_path, format="wav")
        print(f"Saved {output_path}")


def process_directory(input_dir, output_dir, model,min_silence_len,silence_thresh,keep_silence):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".wav"):
            input_audio_path = os.path.join(input_dir, filename)
            print(f"Processing {input_audio_path}...")
            chunks = split_audio_on_silence(input_audio_path,min_silence_len,silence_thresh,keep_silence)
            save_chunks_with_transcriptions(chunks, output_dir, os.path.splitext(filename)[0],model)

if __name__ == "__main__":
    current_dir = os.getcwd()
    input_dir = os.path.join(current_dir,"input_wav")
    output_dir = os.path.join(current_dir,"output_wav")

    model_size = "large-v3"
    model = WhisperModel(model_size, device="cpu", compute_type="int8")


    # JSONファイルのパスを指定
    json_file_path = 'settings.json'

    # JSONファイルを読み込む
    with open(json_file_path, 'r') as file:
        settings = json.load(file)

    # 設定値を変数に格納
    min_silence_len = settings['min_silence_len']
    silence_thresh = settings['silence_thresh']
    keep_silence = settings['keep_silence']

    # 設定値を表示
    print(f"Minimum Silence Length: {min_silence_len}")
    print(f"Silence Threshold: {silence_thresh}")
    print(f"Keep Silence: {keep_silence}")


    process_directory(input_dir, output_dir,model,min_silence_len,silence_thresh,keep_silence)