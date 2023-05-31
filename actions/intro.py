intro_messages=[
    
    """ 
you have entered my haunted mansion, now you have to find a way to leave or else you will become my ghost friend forever.
I am a smart spirit, you know, if you have to escape this mansion you have to crack the door’s secret code.
I was a kind human when I was alive, so I will show some kindness and guide you through my super dark mansion and help you get out of this place.
Hehehehehe, rack your brains and have fun, Good luck!!!!
Are you ready to explore my deadly mansion??.""",
    """
Well that was easy, you seem to be a remarkable person to have unlocked the door so fast. 
But do you think I will let you go this easily?? Never!!! 
Now you have entered my favorite room, after my death i started living here.
I promise this is the last test I'll put you through, escape this room and you’ll be free to go.

Do you want to explore the room?    
    """
    
]

room_setting= [
    """
There is a clock on the wall pointing at 3 with the USA flag as a background, an old diary and an ancient roman rock.
Also, here is a bag for you which will be helpful to carry my legacy.

    """,
    """
As your eyes get adjusted you start looking around, There are many scary things in this dark room you notice \n
a spooky little girl mannequine, a yellow shaded goggles which you can put on if you want, a shovel, a magnifying lens, a torch light, \n
a chinese vase, a creepy looking cupboard and a small bowl filled with water beside it.


Also there are lot of skeletons burried in this room. If you could dig them up, there might be a clue for you.

    """
    
]
no_option_message=[
    "You don't have an option., My room my rules \n",
    "It is funny you still think you have an option \n"
]


all_objects = [{'diary':{'item':'diary','type':'final','question':"You open the diary and find this written on the first page \nUntil I am measured I am not known, Yet how you miss me when I have flown. The Number you seek is the letters I contain",'answer':"4",'clue':"I wait for none",'completed':False},
               'watch':{'item':'watch','type':'final','question':"It was a gift from a very special American friend, turn it around, you should find a text saying, \nI love New York’s Times Square, that is the second digit of the door lock.",'answer':"9",'completed':False, 'clue':"Think mathematically" },
               'rock':{'item':'rock','type':'final','question':"You can see letter V inscribed on it. What could it mean?",'answer':"5",'completed':False, 'clue':"Capital of Italy" },
              },
               {
                   'mannequin':{'item':'mannequin', 'required_prop':None,'type':'final','question':"She also came here and couldn’t escape so I turned her into a mannequin, so be careful!!! A t-shirt on her says, \n“I am present, but also past. I am wrapped, but not a gift. I am named after a parent, but have no children”",'answer':"mummy",'clue':"Egypt",'completed':False},
                   
                   'vase': {'type':'collection','item':'vase', 'required_prop':None,"action" : "When you try to pick the vase it turns to dust and now you find a crumbled paper fall from it", 'collection':[{'item':'paper','type':'mechanical','required_prop':"magnifying_lens",'answer':"4",'pretext':"The letters seem to be very small not possible to read them with naked eye, \ntry looking for something to make text appear bigger ",'completed':"It reads"}] } ,
                   'cabinet':{'type':'collection','item':'cabinet','required_prop':'torch', 'pretext':"The doors of the cabinet open with squeky sound \n It is too dark inside, find something to light things up", "action": "With the light in the cupboard you see a cloth,\n A cloth drenced in blood ",
                               'collection':[{'item':'cloth','type':'final', "pretext":"Hehe i only wiped the blood spilled on the floor, you can use some other prop to make the cloth clean and read the text written on it",'required_prop':"water",'answer':"Blood",'question':"When cleaned up the cloth becomes clear and now you can read   'From the head down to toes, through every living being I flow. Some people might faint when they see me though! What am I?'","clue":"What vampires drink",'completed':"It reads"}]},
                    'water':{'type':'prop', 'item':'water','required_prop':None,'description':'something about the glass', 'use':"You pour the liquid on the cloth", 'inoperable':"The {} is not so dirty, no point in using water to clean"},
                    'magnifying_lens':{'type':'prop', 'item':'magnifying_lens','required_prop':None,'description':'something about the glass', 'use':"now things look enlarged", "inoperable": "Dont see a benefit of using a magnifier on {}, dont see any text that could be enlarged"},
                    'torch':{"type":'prop', 'item':'torch','required_prop':None,'desciption':'desc about torch','use':'Torch turns on with a yellow beam','inoperable':"The {} is not so dark, the beam does not have much effect"},
                    'shovel':{'type':'collection','item':'shovel', 'required_prop':None,"action" : "Great, you found an equipment to find your future friends, Now they are visible to you. You can ask them for clue by picking them", 'collection':[{'item':'skeleton','type':'mechanical','required_prop':None,'answer':None,'pretext':None,'completed':"As soon as you touch the skeleton, you hear a voice saying, \nyou made the mistake of taking me out from my burial, there is nothing I can do, \nLooks like that was a no show, try another prop to escape, try it out fast, time is running out."}]},
                    'goggles':{'item':'goggles', 'required_prop':None,'type':'final','question':"After you wear this goggles, you notice a text written on the wall \n'Where do ghosts, mummies, and devils love to swim?'",'answer':"Dead Sea",'clue':"Birth opposite",'completed':False}
              },
               {'final_wall':{'item':'Wall','type':'final','question':" The house surrenders only to the fearless and bold to be one you need to survive this last ordeal, behold  A survivor hides within this room, get me his name and we’ll end this game.{}",'answer':"name",'clue':"its you",'completed':False}}
               ]

