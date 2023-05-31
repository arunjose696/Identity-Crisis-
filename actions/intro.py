intro_messages=[
    
    """ 
you have entered my haunted mansion, you have to find a way to leave or else you will become my ghost friend forever.
If you have to escape this mansion you have to crack the door’s secret code of numbers.
I will show some kindness and guide you through my super dark mansion.\n Try your best.
Are you ready to explore my deadly mansion??.""",
    """
Well that was easy I guess, 
Now you have entered my favorite room, after my death i started living here.
I promise this is the last test I'll put you through, escape this room and you’ll be free to go.

Do you want to explore the room?    
    """
    
]

room_setting= [
    """
There is a clock on the wall, an old diary and an ancient ROMAN rock. Which one do you want to pick? 

    """,
    """
In this room there are many SCARY OBJECTS  and some PROPS to explore those objects. \n
a spooky little girl mannequine \U0001F9DB, a creepy looking cupboard \U0001F5C4, some hidden skeletons \U0001F480, chinese vase \U0001F3FA, \n yellow shaded goggles \U0001F97D, shovel \U00013B49, torch light \U0001F526, \n
and a small bowl filled with water.


Also there are lot of skeletons burried in this room. If you could dig them up, there might be a clue for you.

    """
    
]
no_option_message=[
    "You don't have an option., My room my rules \n",
    "It is funny you still think you have an option \n"
]


all_objects = [{'diary':{'item':'diary','type':'final','question':"Text on the diary reads \nUntil I am measured I am not known, Yet how you miss me when I have flown. The Number you seek is the letters I contain",'answer':"4",'clue':"Clock measures it.",'completed':False},
               'watch':{'item':'watch','type':'final','question':"The time is 3'o clock, it's a watch from The USA, \n and I love New York’s \"TIME'S SQUARE\", the number you want lies in time's square",'answer':"9",'completed':False, 'clue':"Square the Time" },
               'rock':{'item':'rock','type':'final','question':"You can see letter 'V' inscribed on it. Which number it can be?",'answer':"5",'completed':False, 'clue':"I am a Roman numberal indicating a number" },
              },
               {
                   'mannequin':{'item':'mannequin', 'required_prop':None,'type':'final','question':"I only turned her into a mannequin, so be careful!!! A t-shirt on her says, \n“I am present, but also past. I am wrapped, but not a gift. I am named after a parent, but have no children”",'answer':"mummy",'clue':"Egypt",'completed':False},
                   'cabinet':{'type':'collection','item':'cabinet','required_prop':'torch', 'pretext':"The doors of the cabinet open with squeky sound \n It is too dark inside, find something to light things up", "action": "With the light in the cupboard you see a cloth,\n A cloth drenced in blood ",
                               'collection':[{'item':'cloth','type':'final', "pretext":"Hehe i only wiped the blood spilled on the floor, you can use some other prop to make the cloth clean and read the text written on it",'required_prop':"water",'answer':"Blood",'question':"When cleaned up the cloth becomes clear and now you can read   'From the head down to toes, through every living being I flow. Some people might faint when they see me though! What am I?'","clue":"What vampires drink",'completed':"It reads"}]},
                    'water':{'type':'prop', 'item':'water','required_prop':None,'description':'something about the glass', 'use':"You pour the liquid on the cloth", 'inoperable':"The {} is not so dirty, no point in using water to clean"},
                    'torch':{"type":'prop', 'item':'torch','required_prop':None,'desciption':'desc about torch','use':'Torch turns on with a yellow beam','inoperable':"The {} is not so dark, the beam does not have much effect"},
                    'shovel':{'type':'collection','item':'shovel', 'required_prop':None,"action" : "Great, you found an equipment to find your future friends, Now they are visible to you. You can ask them for clue by picking them", 'collection':[{'item':'skeleton','type':'mechanical','required_prop':None,'answer':None,'pretext':None,'completed':"As soon as you touch the skeleton, you hear a voice saying, \nyou made the mistake of taking me out from my burial, there is nothing I can do, \nLooks like that was a no show, try another prop to escape, try it out fast, time is running out."}]},
                    'goggles':{'item':'goggles', 'required_prop':None,'type':'final','question':"After you wear this goggles, you notice a text written on the wall \n'Where do ghosts, mummies, and devils love to swim?'",'answer':"Dead Sea",'clue':"Birth opposite",'completed':False}
              },
               {'vase': {'type':'collection','item':'vase', 'required_prop':None,"action" : "When you try to pick the vase it turns to dust and now you find a crumbled paper fall from it", 'collection':[{'item':'paper','type':'final','required_prop':None,'answer':{},'question':"The house surrenders only to the fearless and bold \n to be one you need to survive this last ordeal, behold \n A survivor hides within this room, \n get me his name \n and we’ll end this game {} \nArrange and find the survivor",'clue':"It's you"}] }}
               ]

