# ApologyVideoGenerator

A problem our generation faces is the need to apologize for the horrible things we have done.
Youtube sensations do so many horrible things, and apologize in such a generic and uniform way, the apology video has become its own 'unqiue' genre (I say 'unque' because these videos are all practically the same)

In order to maximize efficiency, a combination of sad videos with a text to speech function could easily generate these videos, saving precious time.

To that end, this program aims to automate the creation of Apology vidoes, and it achieves its purpose!

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1594592001/video_to_markdown/images/youtube--Cjb45G58kk8-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/Cjb45G58kk8 "")

# Discord Bot
Discord bot functionality has been attached!

SorryBot now generates videos on a heroku backend, and sends them to your discord server after just  2 minutes!

<img src="https://github.com/daminals/ApologyVideoGenerator/blob/master/Assets/demonstration/worked.png" width="600">

# Next Steps

Despite the actual program being finished, there is more I'd like to do with it. Namely, upload it onto a simple website to allow anybody to generate their own apology videos

Implement a Java GUI to make video generation significantly nicer

Improve discord bot functionality-- Current method of operation engages in blocking, which is not ideal for a discord bot.

In addition, there are more bugs than I would like in the program, and they cause it to crash every so often. These bugs are typically within writing videos to file, and mixing the audio

# Installation

In addition to requirements.txt, ffmpeg must be installed on your computer for this program to function