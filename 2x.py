import subprocess
from scipy.io import wavfile
from pydub import AudioSegment


def a_speed(input_file, speed, out_file):  # Define the double speed function
    try:
        cmd = "ffmpeg -y -i %s -filter_complex \"atempo=tempo=%s\" %s" % (input_file, speed, out_file)
        res = subprocess.call(cmd, shell=True)

        if res != 0:
            return False
        return True
    except Exception:
        return False


def halfmusic(srcmusicfile, dstmusicfile):  # Define the half volume function
    data = wavfile.read(srcmusicfile)
    wavfile.write(dstmusicfile, data[0], data[1] // 2)


song = AudioSegment.from_file("D:\\FYP_Music\\BeatThee.mp3")  # Input the original MP3 file
song[0:9*1000].export("D:\\FYP_Music\\BeatThee.0s.wav", format="wav")   # Output wav file

for i in range(6):   # Halve music speed and volume 6 times
    a_speed(f"D:\\FYP_Music\\BeatThee.{i}s.wav", "0.5", f"D:\\FYP_Music\\BeatThee.{i + 1}x.wav")
    halfmusic(f"D:\\FYP_Music\\BeatThee.{i + 1}x.wav", f"D:\\FYP_Music\\BeatThee.{i + 1}s.wav")
