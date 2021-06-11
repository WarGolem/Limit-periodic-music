from pydub import AudioSegment

audio1 = AudioSegment.from_wav("D:\\FYP_Music\\Circulated\\BeatThee.0c.wav")  # Your first audio file
audio2 = AudioSegment.from_wav("D:\\FYP_Music\\Circulated\\BeatThee.1c.wav")  # Your second audio file
mixed1 = audio1.overlay(audio2)  # Mix the first file with the second file
for i in range(5):
    audio3 = AudioSegment.from_wav(f"D:\\FYP_Music\\Circulated\\BeatThee.{i + 2}c.wav")
    mixed1 = mixed1.overlay(audio3)  # Mix it with the rest audio files
    mixed1.export("D:\\FYP_Music\\BeatThee.mixed.wav", format='wav')  # Export final mixed audio file
