from json.tool import main
from tabnanny import check
import wave
import simpleaudio
import random


class Sound:
    filePath = ""
    soundName = ""
    waveObj = None

    def __init__(self, filePath, soundName):
        self.filePath = filePath
        self.soundName = soundName

    def setPlay(self):
        self.waveObj = simpleaudio.WaveObject.from_wave_file(self.filePath)

    def playSound(self):
        self.playObj = self.waveObj.play()
        self.playObj.wait_done()


def settingSounds():
    soundDirPath = "./sounds/"

    soundList = []
    soundList.append(Sound(soundDirPath + "c.wav", "C"))
    soundList.append(Sound(soundDirPath + "d.wav", "D"))
    soundList.append(Sound(soundDirPath + "e.wav", "E"))
    soundList.append(Sound(soundDirPath + "f.wav", "F"))
    soundList.append(Sound(soundDirPath + "g.wav", "G"))
    soundList.append(Sound(soundDirPath + "a.wav", "A"))
    soundList.append(Sound(soundDirPath + "b.wav", "B"))
    return soundList


def main():

    soundList = settingSounds()

    while True:
        print("Playing")
        sound = random.choice(soundList)
        sound.setPlay()
        sound.playSound()

        while True:
            print("select code: C,D,E,F,G,A,B")
            yourAnswer = input("? >> ")

            # check
            for sound_ in soundList:
                if yourAnswer == sound_.soundName:
                    break
            else:
                continue
            break

        if yourAnswer == sound.soundName:
            print("correct!!")
        else:
            print("wrong... Answer is {}".format(sound.soundName))
        print()


def isPlaying(waveObj):
    if waveObj.is_playing():
        return True
    return False


if __name__ == "__main__":
    main()
