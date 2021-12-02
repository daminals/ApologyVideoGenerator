# -*- coding: utf-8 -*-
# main.py
# This generates Apology videos
# Daniel Kogan, 6/30/2020

from gtts import gTTS
from moviepy.editor import *
from moviepy.audio.fx.volumex import volumex
import os, random, ffmpy, asyncio, fire,time

# TODO: add subtitles 🥺😳
# TODO: Organize different steps into separate functions (ex: tts to tts function)
# TODO: DEBUG!!! It crashes and is unable to load the video every so often, and that must be fixed

language = 'en'

apology_intros = ["I made a severe and continuous lapse in my judgement, and I don’t expect to be forgiven. I’m "
                  "simply here to apologize. ", "I want to talk to you guys about some mistakes I have made, ",
                  "yeah, I wasn't acting very sexy earlier...   ", "...Long and Deep sigh..."
                  ]

bs = ["My waitress at taco bell got my order wrong three months ago", "I couldn't find my right sock this morning",
      "My mommy took away my PS vita", "My sugar daddy stopped funding my twizzler addiction",
      "scratched my iPhone screen", "I was tried for first degree murder", "I'm a scorpio",
      "I was really hungry at the time"
      "I broke my iPhone by putting it too close to the cutting board, but it's ok my Dad will just buy me a new one"]

middle = ["I don't want your forgiveness, just the open space to be able to say how deeply sorry I am.  ",
          "The goal of my content is always to entertain, I never meant to let it get out of hand.  "
          ]

def gen_ID(char):
    ID = ''
    for i in range(char):
        ID += str(random.randint(0, 9))
    return ID

def clutter():
    for i in os.listdir('Temp-Files'):
        if not i=='.gitkeep':
            os.remove('Temp-Files/' + i)


def compression(input_name, output_name):
    inp = {input_name: None}
    outp = {output_name: '-vcodec libx264 -crf 23'}
    ff = ffmpy.FFmpeg(inputs=inp, outputs=outp)
    print(ff.cmd)
    ff.run()


def main(bool_inp,ID,apolo=''):
    print(bool_inp,ID,apolo)
    ID = str(ID)
    if bool_inp:
        reason = apolo
    else:
        reason = input('Why are you apologizing? ')
    Intro = random.choice(apology_intros)
    Middle_part = f".  I am deeply and truly sorry for {reason.lower()}. It was wrong, disgraceful, and I promise it will never happen again,  .   {reason.lower()} is the worst thing I have ever done in my entire life, no contest. . .  {random.choice(middle)}"
    Conclusion = f' Thank you everyone for giving me this time to apologize for my actions. It\'s just been so so hard for me since {random.choice(bs)}. I love each of you guys so so much. Thank you, and Don\'t forget to SMASH that like button and subscribe for more content!'
    script = Intro + Middle_part + Conclusion
    print('Processing audio...')

    audio = gTTS(script)

    audio.save('Assets/audio.aac')

    audioClip = AudioFileClip("Assets/audio.aac")

    MusicFile = random.choice(os.listdir('./Assets/music'))
    # print(MusicFile)
    try:
        backgroundMusic = AudioFileClip("Assets/music/" + MusicFile)
    except Exception as e:
        print(e)
        print(MusicFile)
        try:
            backgroundMusic = AudioFileClip("Assets/music/" + MusicFile)
        except Exception as e:
            print("Failed loading music")
    backgroundMusic = backgroundMusic.set_duration(audioClip.duration)
    NewaudioClip = CompositeAudioClip([audioClip, backgroundMusic]).set_duration(audioClip.duration)
    print('Audio has been processed....')

    print('Processing video...')

    clip1 = random.choice(os.listdir("./Assets/clips"))
    clip2 = random.choice(os.listdir("./Assets/clips"))
    while clip2 == clip1:
        clip2 = random.choice(os.listdir("./Assets/clips"))
    clip3 = random.choice(os.listdir("./Assets/clips"))
    while clip3 == clip2 or clip3 == clip1:
        clip3 = random.choice(os.listdir("./Assets/clips"))

    clip1 = VideoFileClip("Assets/clips/" + clip1)
    clip2 = VideoFileClip("Assets/clips/" + clip2)
    clip3 = VideoFileClip("Assets/clips/" + clip3)

    # backgroundMusic = volumex(backgroundMusic, 0.1)

    final_clip = concatenate_videoclips([clip1, clip2, clip3])
    final_clip = final_clip.subclip(0, audioClip.duration)

    def Process(final_clip, ID, NewaudioClip):
        try:
            final_clip.set_audio(NewaudioClip).write_videofile("Temp-Files/apology" + ID + ".mov", codec="libx264",
                                                               audio_codec='aac', audio=True,
                                                               temp_audiofile='Temp-Files/temp-audio.m4a',
                                                               fps=30, remove_temp=True)
        except IndexError:
            print(Exception)
            final_clip.subclip(t_end=(final_clip.duration - 1.0 / final_clip.fps)).write_videofile(
                "Temp-Files/apology" + ID + ".mov", codec="libx264", audio_codec='aac',
                audio=True, temp_audiofile='Temp-Files/temp-audio.m4a', fps=30,
                remove_temp=True)

        except Exception as e:
            print(e)
            Process(final_clip, ID, NewaudioClip)

    try:
        Process(final_clip, ID, NewaudioClip)
    except Exception as e:
        print(e)
        clutter()

    print('Video processed...')
    print('Compressing video...')
    compression("Temp-Files/apology" + str(ID) + ".mov", "Finished/apology" + str(ID) + ".mp4")
    os.remove("Temp-Files/apology" + str(ID) + ".mov")
    print('Video compressed...')

    final_clip.close()
    os.remove('Assets/audio.aac')
    clutter()


if __name__ == '__main__':
    ID = gen_ID(4)
    fire.Fire()
