# main.py
# This does something
# Daniel Kogan, 6/30/2020

from gtts import gTTS
from moviepy.editor import *
import os,random

language = 'en'

apology_intros = ["I made a severe and continuous lapse in my judgement, and I don’t expect to be forgiven. I’m "
                  "simply here to apologize.","I want to talk to you guys about some mistakes I have made",
                  "... ... ... yeah I wasn't acting very sexy earlier",""]

bs = ["My waitress at taco bell got my order wrong three months ago","I couldn't find my right sock this morning","My mommy took away my PS vita", "My sugar daddy stopped funding my twizzler addiction"]


def main():
    reason = input('Why are you apologizing? ')
    Intro = random.choice(apology_intros)
    Middle_part = f"  I am deeply and truly sorry for {reason}. It was wrong, disgraceful, and I promise it will never happen again. {reason} is the worst thing I have ever done in my entire life, no contest. I don't want your forgiveness, just the open space to be able to say how deeply sorry I am for {reason} "
    Conclusion = f' Thank you everyone for giving me this time to apologize for my actions. It\'s just been so so hard for me since {random.choice(bs)}. I love each of you guys so so much. Thank you'

    script = Intro + Middle_part + Conclusion
    audio = gTTS(text=script, lang=language, slow=False)
    audio.save('Assets/audio.mp3')

    os.system("mpg321 audio.mp3")

if __name__ == '__main__':
    main()