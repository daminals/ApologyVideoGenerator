# main.py
# This does something
# Daniel Kogan, 6/30/2020

from gtts import gTTS
from moviepy.editor import *
from moviepy.audio.fx.volumex import volumex
from moviepy.video.fx.resize import resize
import os, random

# TODO: add subtitles
# TODO: Organize different steps into seperate functions (ex: tts to tts function)

language = 'en'

apology_intros = ["I made a severe and continuous lapse in my judgement, and I don’t expect to be forgiven. I’m "
                  "simply here to apologize. ", "I want to talk to you guys about some mistakes I have made, ",
                  "yeah, I wasn't acting very sexy earlier...   "]

bs = ["My waitress at taco bell got my order wrong three months ago", "I couldn't find my right sock this morning",
      "My mommy took away my PS vita", "My sugar daddy stopped funding my twizzler addiction"]


def main():
    reason = input('Why are you apologizing? ')
    Intro = random.choice(apology_intros)
    Middle_part = f".  I am deeply and truly sorry for {reason.lower()}. It was wrong, disgraceful, and I promise it will never happen again,  .   {reason.lower()} is the worst thing I have ever done in my entire life, no contest. . . I don't want your forgiveness, just the open space to be able to say how deeply sorry I am for {reason.lower()}. "
    Conclusion = f' Thank you everyone for giving me this time to apologize for my actions. It\'s just been so so hard for me since {random.choice(bs)}. I love each of you guys so so much. Thank you, and Don\'t forget to like and subscribe!'
    script = Intro + Middle_part + Conclusion
    print('Processing audio...')

    audio = gTTS(text=script, lang=language, slow=True)

    audio.save('Assets/audio.aac')

    audioClip = AudioFileClip("Assets/audio.aac")

    MusicFile = random.choice(os.listdir('./Assets/music'))
    #print(MusicFile)
    backgroundMusic = AudioFileClip("Assets/music/" + MusicFile)
    backgroundMusic = backgroundMusic.set_duration(audioClip.duration)
    NewaudioClip = CompositeAudioClip([audioClip, backgroundMusic]).set_duration(audioClip.duration)
    print('Audio has been processed....')


    print('Processing video...')

    list_num = [1, 2, 3, 4, 5, 6, 7]
    clip1 = random.choice(list_num)
    list_num.remove(clip1)
    clip2 = random.choice(list_num)
    list_num.remove(clip2)
    clip3 = random.choice(list_num)
    #print(clip1,clip2,clip3)


    clip1 = VideoFileClip("Assets/" + str(clip1) + ".mp4")
    clip2 = VideoFileClip("Assets/" + str(clip2) + ".mp4")
    clip3 = VideoFileClip("Assets/" + str(clip3) + ".mp4")

    #backgroundMusic = volumex(backgroundMusic, 0.1)

    final_clip = concatenate_videoclips([clip1, clip2,clip3])
    #final_clip.subclip(0,audioClip.duration)
    #backgroundMusic.subclip(0,audioClip.duration)

    final_clip = final_clip.subclip(0,audioClip.duration)
    try:
        final_clip.set_audio(NewaudioClip).write_videofile("apology.mov", codec="libx264", audio_codec='aac',
                                                        audio=True,temp_audiofile='temp-audio.m4a',fps=30,
                                                        remove_temp=True)
    except IndexError:
        final_clip.set_audio(NewaudioClip).subclip(t_end=(final_clip.duration - 1.0/final_clip.fps)).write_videofile("apology.mov", codec="libx264", audio_codec='aac',audio=True, temp_audiofile='temp-audio.m4a', fps=30, remove_temp=True)


    final_clip.close()
    os.remove('Assets/audio.aac')


if __name__ == '__main__':
    main()
