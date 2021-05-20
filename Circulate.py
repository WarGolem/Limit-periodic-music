from pydub import AudioSegment

input_music = AudioSegment.from_wav(f"D:\\FYP_Music\\BeatThee.0s.wav")  # Input original music file
input_music_time = len(input_music)  # Save original music length as a parameter

for i in range(7):
    input_music = AudioSegment.from_wav(f"D:\\FYP_Music\\BeatThee.{i}s.wav")
    output_music = input_music + input_music  # Combine two music segments into one
    output_music.export(f"D:\\FYP_Music\\Circulated\\BeatThee.{i}c.wav", format="wav")
    output_music_time = len(output_music)

    while output_music_time < 2*input_music_time:   # To make each music segment have equal length
        output_music += input_music  # Add music segment to itself
        output_music.export(f"D:\\FYP_Music\\Circulated\\BeatThee.{i}c.wav", format="wav")  # Output final music file
        output_music_time = len(output_music)  # Compare the new music length with the assigned music length
