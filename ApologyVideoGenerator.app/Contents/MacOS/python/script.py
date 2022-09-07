# script.py
# Daniel Kogan
# 12.24.2021
# this is a library
import os, random

apology_intros = ["I made a severe and continuous lapse in my judgement, and I don’t expect to be forgiven. I’m "
                  "simply here to apologize. ", "I want to talk to you guys about some mistakes I have made, ",
                  "yeah, I wasn't acting very sexy earlier...   ", "...Long and Deep sigh...",
                  "Hey crewmates! SORRY for being sus earlier... ", 
                  ]

bs = ["My waitress at taco bell got my order wrong three months ago", "I couldn't find my right sock this morning",
      "My mommy took away my PS vita", "My sugar daddy stopped funding my twizzler addiction",
      "I scratched my iPhone screen", "I was tried for first degree murder", "I was born a scorpio",
      "I was really hungry at the time"
      "I broke my iPhone by putting it too close to the cutting board, but it's ok my Dad will just buy me a new one",
      "My brita filter cracked", 
      "Mercury was in retrograde",
      "My stock portfolio dropped two cents",
      "Bitcoin went down", 
      ]

middle = ["I don't want your forgiveness, just the open space to be able to say how deeply sorry I am.  ",
          "The goal of my content is always to entertain, I never meant to let it get out of hand.  ",
          "The inhumane actions that I have done were truly despicable.  ",
          "It was once I lost one thousand insta followers that I understood the error of my ways.   "
          f'When I lost my sponsorship with {random.choice(["Manscaped","NordVPN", "Among Us", "Audible","skill share"])}, I realized how wrong I was.  '
          ]

challenge = ["It's just been so hard for me since ",
             "Life has always been difficult for me, for instance ",
             "Life for me has been like that tiktok taylor swift audio: Screaming! Crying! ever since ",
             "I've been feeling so not epic gamer because "
             ]

wrongness_list = ["is the worst thing I have ever done in my entire life, no contest",
                  "is the lowest of lows, and it should not have been me",
                ]

thank_u = ["Thank you everyone for giving me this time to apologize for my actions",
           "Thanks for listening to this video, follow for more content like this"
           ]

def create_script(reason):
    script = random.choice(apology_intros)
    script += f".  I am deeply and truly sorry for {reason.lower()}. It was wrong, disgraceful, and I promise it will never happen again,  .   {reason.lower()} {random.choice(wrongness_list)}. . .  {random.choice(middle)}"
    script += f' {random.choice(thank_u)}. {random.choice(challenge)} {random.choice(bs)}. I love each of you guys so   so much. Thank you, and Don\'t forget to SMASH that like button and subscribe for more content!       .    '
    return script