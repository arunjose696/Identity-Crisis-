intro_messages=[
    
    """ 
you have entered my haunted mansion, you have to find a way to LEAVE \U0001F4A8 or else you will LIVE here as my GHOST FRIEND FOREVER \U0001F47B.
If you have to escape this mansion you have to crack the door’s secret code of NUMBERS.
I will show some kindness and guide you through.\nTry your best.
Are you ready to explore??.""",
    """
Well that was easy I guess, now you have entered my favorite room, I am living here since my death \U0001FAA6.
Try to escape this room.
Do you want to explore the room?    
    """
    
]

room_setting= [
    """
There is a wall clock \U0001F552, an old diary \U0001F4D6 , and an ancient ROMAN rock \U0001FAA8 . Which object do you want to pick to get the NUMBER Code?\nIf you are stuck you can ask for help/clue. Also there is bag to carry few object which might be helpful later.

    """,
    """
    If you look around the room you can find many SCARY OBJECTS like a spooky little girl mannequin \U0001F9DB, a creepy looking cupboard \U0001F5C4, some hidden skeletons \U0001F480, and a Werewolf mask \U0001F43A ,
and some props like shovel \U000026CF, torch light \U0001F526, and a small bowl filled with water \U0001F963 . 
You have to use the PROPS to explore some OBJECTS. Pick any Scary Object?
    <script> (function() { var imageUrl = 'https://drive.google.com/uc?id=1BOv4W_7KdZ64MdruMMJelMd3p3c9dEDZ'; imageUrl = 'url(' + imageUrl.replace(/[\\']/g, '\\$&') + ')'; document.body.style.backgroundImage = imageUrl; })(); </script>
<audio autoplay> <source src= \"https://drive.google.com/uc?id=1WlnVNbiX4yYnGHFb7ndT5lBGBtrrPwXT \" type= \"audio/ogg \"></audio>
    """,
    """
Almost at the last state.
    """
    
]
no_option_message=[
    "You don't have an option, My room my rules \n",
    "It is funny you still think you have an option.\n",
    "in last few mins"
]


all_objects_global = [{'diary':{'item':'diary','type':'final','question':"Text on the diary reads \n\"Until I am measured I am not known, yet how you miss me when I have flown. The Number you seek is the letters I contain in my word?",'answer':"4",'clue':"Clock measures it. Enter the number of letters in what clock measures.",'completed':False},
               'watch':{'item':'watch','type':'final','question':"The watch from The USA shows 3'o clock, \n and I love New York’s \"TIME'S SQUARE\", the number you want lies in time's square?",'answer':"9",'completed':False, 'clue':"Square the Time." },
               'rock':{'item':'rock','type':'final','question':"You can see letter \U00002164 inscribed on it. Which number it can be?",'answer':"5",'completed':False, 'clue':"I am a Roman numeral indicating a number." },
              },
               {
                   'mannequin':{'item':'mannequin', 'required_prop':None,'type':'final','question':"I have turned her into a mannequin, so be careful!!! A t-shirt on her says, \n“I am present, but also past. I am wrapped, but not a gift. I am named after a parent, but have no children, who am I?”",'answer':"mummy",'clue':"My birth place is Egypt.",'completed':False},
                   'cabinet':{'type':'collection','item':'cabinet','required_prop':'torch', 'pretext':"The doors of the cabinet opens with squeaky sound. \n It is too dark inside, pickup a prop to light things up in cabinet", "action": "With the light you can see a cloth drenched in blood present inside cupboard. Pickup the CLOTH first.",
                               'collection':[{'item':'cloth','type':'final', "pretext":"Hehe I only wiped the blood spilled on the floor, pickup a prop to make the cloth clean and to read the text written on it.",'required_prop':"water",'answer':"Blood",'question':"After cleaning, you can read the text,'I flow through vessels, unseen by the eye, Scarlet and Vital, my hue cannot lie, Life's essence i carry, within me it dwells, A river of secrets, tales no tongue tells, What am I?'","clue":"Vampires favorite drink.",'completed':"It reads"}]},
                    'water':{'type':'prop', 'item':'water','required_prop':None,'description':'something about the glass', 'use':"You pour the liquid on the cloth", 'inoperable':"The {} is not so dirty, no point in using water to clean."},
                    'torch':{"type":'prop', 'item':'torch','required_prop':None,'desciption':'desc about torch','use':'Torch turns on with a yellow beam','inoperable':"The {} is not so dark, the beam does not have much effect."},
                    'shovel':{'type':'collection','item':'shovel', 'required_prop':None,"action" : "Great, you can dig the skeletons. Pick them up to get a clue.", 'collection':[{'item':'skeleton','type':'mechanical','required_prop':None,'answer':None,'pretext':None,'completed':"As soon as you touch the skeleton, you hear a voice saying, \nyou made a mistake of taking me out from my burial, there is nothing I can do \U0001F479, \n pickup next object to escape, fast, time is running out."}]},
                    'werewolf':{'item':'werewolf', 'required_prop':None,'type':'final','question':"This Werewolf mask has some special features, if you wear you can hear a voice giving you a riddle, \n'In depths so still, where evil lurks, a lifeless sea, where darkness works, Ghosts dance upon my shore, Devils prowl, and monsters roar, yet life escapes this eerie bed, with naught but salt, where fear is spread, what am I?'",'answer':"Dead Sea",'clue':"I am a sea named after DEATH.",'completed':False}
              },
               {'vase': {'type':'collection','item':'vase', 'required_prop':None,"action" : "You have to pickup a last object in order to escape, if you see there is a VASE \U0001F3FA and when you try to touch the vase it turns to dust \U0001F4A8 and now you find a scrambled paper \U0001F4C3 fall from it, you have to pick up the PAPER to solve the riddle and escape.", 'collection':[{'item':'paper','type':'final','required_prop':None,'answer':{},'question':"The house surrenders only to the fearless and bold \n to be one you need to survive this last ordeal, behold \n A survivor hides within this room, \n get me his/her name \n and we’ll end this game <h1>{}</h1> \nArrange the alphabets and find the survivor.",'clue':"It's \"YOU\" dummy."}] }}
               ]

