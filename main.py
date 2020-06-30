# main.py
# This does something
# Daniel Kogan, 6/30/2020

from gtts import gTTS
from moviepy.editor import *
from moviepy.audio.fx.volumex import volumex
from moviepy.video.fx.resize import resize
import os, random

# TODO: add subtitles
# TODO: Organize different steps into seperate functions (ex: tts to tts function

language = 'en'

apology_intros = ["I made a severe and continuous lapse in my judgement, and I don’t expect to be forgiven. I’m "
                  "simply here to apologize.", "I want to talk to you guys about some mistakes I have made",
                  "yeah, I wasn't acting very sexy earlier...   "]

bs = ["My waitress at taco bell got my order wrong three months ago", "I couldn't find my right sock this morning",
      "My mommy took away my PS vita", "My sugar daddy stopped funding my twizzler addiction"]


def main():
    reason = input('Why are you apologizing? ')
    Intro = random.choice(apology_intros)
    Middle_part = f"  I am deeply and truly sorry for {reason}. It was wrong, disgraceful, and I promise it will never happen again. {reason} is the worst thing I have ever done in my entire life, no contest. I don't want your forgiveness, just the open space to be able to say how deeply sorry I am for {reason} "
    Conclusion = f' Thank you everyone for giving me this time to apologize for my actions. It\'s just been so so hard for me since {random.choice(bs)}. I love each of you guys so so much. Thank you'

    script = Intro + Middle_part + Conclusion
    print('Processing audio...')

    audio = gTTS(text=script, lang=language, slow=True)

    # audio = audioIntro + audioBridge + audioConc
    audio.save('Assets/audio.aac')

    print('Audio has been processed....')
    print('Processing video...')

    list_num = [1, 2, 3, 4, 5, 6, 7]
    clip1 = random.choice(list_num)
    list_num.remove(clip1)
    clip2 = random.choice(list_num)
    list_num.remove(clip2)
    clip3 = random.choice(list_num)


    clip1 = VideoFileClip("Assets/" + str(clip1) + ".mp4")
    clip2 = VideoFileClip("Assets/" + str(clip2) + ".mp4")
    clip3 = VideoFileClip("Assets/" + str(clip3) + ".mp4")


    audioClip = AudioFileClip("Assets/audio.aac")

    MusicFile = random.choice(os.listdir('./Assets/music'))
    backgroundMusic = AudioFileClip("Assets/music/" + MusicFile)
    #backgroundMusic = volumex(backgroundMusic, 0.1)

    final_clip = concatenate_videoclips([clip1, clip2,clip3])
    final_clip.set_duration(audioClip.duration)
    #final_clip.subclip(0,audioClip.duration)
    #backgroundMusic.subclip(0,audioClip.duration)
    backgroundMusic.set_duration(audioClip.duration)
    NewaudioClip = CompositeAudioClip([audioClip, backgroundMusic])

    final_clip.set_audio(NewaudioClip).subclip(0,audioClip.duration).write_videofile("apology.mov", codec="libx264", audio_codec='aac',
                                                    audio=True,temp_audiofile='temp-audio.m4a',
                                                    remove_temp=True)
    final_clip.close()
    os.remove('Assets/audio.aac')

    """ final_clip.set_audio(new_audioclip).write_videofile(
        'Assets/audio.aac',
        fps=None,
        codec="libx264",
        audio_codec="aac",
        bitrate=None,
        audio=True,
        audio_fps=44100,
        preset='medium',
        audio_nbytes=4,
        audio_bitrate=None,
        audio_bufsize=2000,
        # temp_audiofile="/tmp/temp.m4a",
        # remove_temp=False,
        # write_logfile=True,
        rewrite_audio=True,
        verbose=True,
        threads=None,
    )
    """


if __name__ == '__main__':
    main()
