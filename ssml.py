from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()
ssml = "<speak>Hello, <emphasis level='strong'>world!</emphasis></speak>"

input_text = texttospeech.SynthesisInput(ssml=ssml)
voice = texttospeech.VoiceSelectionParams(language_code="en-US")
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

response = client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)

with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
