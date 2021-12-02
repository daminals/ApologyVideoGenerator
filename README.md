![github repo badge: Language](https://img.shields.io/badge/GUI-Java-181717?color=orange)  ![github repo badge: Language](https://img.shields.io/badge/Backend-Python-181717?color=blue)  ![github repo badge: Language](https://img.shields.io/badge/Backend-Bash-181717?color=green)  ![github repo badge: Powered By](https://img.shields.io/badge/Powered%20by-FFMPEG-181717?color=Green)  ![github repo badge: Powered By](https://img.shields.io/badge/Powered%20by-gTTS-181717?color=red)  ![github repo badge: Hosted on](https://img.shields.io/badge/Hosted%20on-Heroku-181717?color=purple) ![github repo badge: Powered by](https://img.shields.io/badge/Powered%20by-Discord-181717?color=purple)
# ApologyVideoGenerator

_This branch, master, is the discord bot version, currently hosted on heroku_

A problem our generation faces is the need to apologize for the horrible things we have done.
Youtube sensations do so many horrible things, and apologize in such a generic and uniform way, the apology video has become its own 'unique' genre (I say 'unique' because these videos are all practically the same)

In order to maximize efficiency, a combination of sad videos with a text to speech function could easily generate these videos, saving precious time.

To that end, this program aims to automate the creation of Apology videos, and it achieves its purpose!

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1594592001/video_to_markdown/images/youtube--Cjb45G58kk8-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/Cjb45G58kk8 "")

# Discord Bot

Attaching the generator to a discord bot via heroku server was difficult, but applying the FFmpeg buildpack and google's text to speech API. The discord API routes function calls within discord to the main generator application, runs it, and returns the desired output

# Next Steps

Despite the actual program being finished, there is more I'd like to do with it. Namely, upload it onto a simple website to allow anybody to generate their own apology videos

Add more hosts and possible threads. The bot is not scalable as it only has one worker, and the worker must finish building a video before it can be called to build another video. This means the discord bot engages in blocking, and cannot handle multiple simultaneous requests.

The gTTS module is much slower than pyttsx3, but pyttsx3 does not work through heroku as its installation on my personal device builds differently than on the server. Finding a workaround to help pyttsx3 build on the heroku server would significantly improve runtime and user experience

# Installation
```
$ touch .env
$ echo TOKEN=\'YOUR_DISCORD_BOT_TOKEN\' >> .env
$ ./run
```