import whisper
from stable_whisper import modify_model
import json

# model = whisper.load_model("large")
#
# # load audio and pad/trim it to fit 30 seconds
# audio = whisper.load_audio("audio/First_Audio_test_no_numbers.mp3")
# audio = whisper.pad_or_trim(audio)
#
# # make log-Mel spectrogram and move to the same device as the model
# mel = whisper.log_mel_spectrogram(audio).to(model.device)
#
# # detect the spoken language
# _, probs = model.detect_language(mel)
# print(f"Detected language: {max(probs, key=probs.get)}")
#
# # decode the audio
# options = whisper.DecodingOptions(max_initial_timestamp=0.0, fp16=False)
# result = whisper.decode(model, mel, options)
#
# # print the recognized text
# print(result)
filename = "First_Audio_test_no_numbers.mp3"

model = whisper.load_model("large")
modify_model(model)
result1 = model.transcribe("audio/" + filename, language='da', suppress_silence=False, ts_num=16)
print(result1)

with open("transcriptions/" + filename + ".json", "w") as f:
    json_data = json.dumps(result1)

    # Write the JSON string to the file
    f.write(json_data)
