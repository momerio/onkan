import simpleaudio

wav_obj = simpleaudio.WaveObject.from_wave_file("./sounds/c.wav")
play_obj = wav_obj.play()
play_obj.wait_done()
