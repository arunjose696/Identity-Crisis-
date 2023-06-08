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
If you look around the room you can find many SCARY OBJECTS like a spooky little girl mannequin \U0001F9DB, a creepy looking cupboard \U0001F5C4, some hidden skeletons \U0001F480, and yellow shaded goggles \U0001F97D ,
and some props like shovel \U000026CF, torch light \U0001F526, and a small bowl filled with water \U0001F963 . 
You have to use the PROPS to explore some OBJECTS. Pick any Scary Object?
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
                   'cabinet':{'type':'collection','item':'cabinet','required_prop':'torch', 'pretext':"The doors of the cabinet opens with squeaky sound. \n It is too dark inside, pickup a prop to light things up in cabinet", "action": "With the light you can see a cloth drenched in blood present inside cupboard. Pickup the cloth and use a prop for the text on the cloth to be visible.",
                               'collection':[{'item':'cloth','type':'final', "pretext":"Hehe I only wiped the blood spilled on the floor, pickup a prop to make the cloth clean and read the text written on it.",'required_prop':"water",'answer':"Blood",'question':"After cleaning, you can read the text,'From the head down to toes, through every living being I flow. Some people might faint when they see me though! What am I?'","clue":"Vampires favorite drink.",'completed':"It reads"}]},
                    'water':{'type':'prop', 'item':'water','required_prop':None,'description':'something about the glass', 'use':"You pour the liquid on the cloth", 'inoperable':"The {} is not so dirty, no point in using water to clean."},
                    'torch':{"type":'prop', 'item':'torch','required_prop':None,'desciption':'desc about torch','use':'Torch turns on with a yellow beam','inoperable':"The {} is not so dark, the beam does not have much effect."},
                    'shovel':{'type':'collection','item':'shovel', 'required_prop':None,"action" : "Great, you can dig the skeletons. Pick them up to get a clue.", 'collection':[{'item':'skeleton','type':'mechanical','required_prop':None,'answer':None,'pretext':None,'completed':"As soon as you touch the skeleton, you hear a voice saying, \nyou made a mistake of taking me out from my burial, there is nothing I can do \U0001F479, \n pickup next object to escape, fast, time is running out."}]},
                    'goggles':{'item':'goggles', 'required_prop':None,'type':'final','question':"After you wear the goggles, you notice text written on the wall \n'In which sea do ghosts, mummies, and devils love to swim?'",'answer':"Dead Sea",'clue':"I am a sea named after DEATH.",'completed':False}
              },
               {'vase': {'type':'collection','item':'vase', 'required_prop':None,"action" : "When you try to pick the vase it turns to dust and now you find a scrambled paper fall from it", 'collection':[{'item':'paper','type':'final','required_prop':None,'answer':{},'question':"The house surrenders only to the fearless and bold \n to be one you need to survive this last ordeal, behold \n A survivor hides within this room, \n get me his/her name \n and we’ll end this game <h1>{}</h1> \nArrange the alphabets and find the survivor.",'clue':"It's \"YOU\" dummy."}] }}
               ]

