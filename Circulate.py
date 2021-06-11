from pydub import AudioSegment

input_longest_music = AudioSegment.from_wav(f"D:\\FYP_Music\\BeatThee.6s.wav") # Input the longest music file
music_period = len(input_longest_music)  # Save the longest music length as a parameter

for i in range(7):
    input_music = AudioSegment.from_wav(f"D:\\FYP_Music\\BeatThee.{i}s.wav") # Input each music file
    output_music = input_music
    output_music_time = len(output_music)

    while output_music_time < music_period:   # To make each music segment have equal length
        output_music += input_music  # Add music segment to itself
        output_music.export(f"D:\\FYP_Music\\Circulated\\BeatThee.{i}c.wav", format="wav")  # Output final music file
        output_music_time = len(output_music)  # Compare the new music length with the assigned music length

    output_music.export(f"D:\\FYP_Music\\Circulated\\BeatThee.{i}c.wav", format="wav")
