intro_messages=[
    
    """ 
you have entered my haunted mansion, now you have to find a way to leave or else you will become my ghost friend forever.
I am a smart spirit, you know, if you have to escape this mansion you have to crack the door’s secret code.
I was a kind human when I was alive, so I will show some kindness and guide you through my super dark mansion and help you get out of this place.
Hehehehehe, rack your brains and have fun, Good luck!!!!
Are you ready to explore my deadly mansion??.""",
    """
But do you think I will  let you go this easily??
Never!!! Now you have entered my favorite room, 
Where I am actually living after my death. Do you want to explore the room??
    
    """
    
]

room_setting= [
    """
Here is bag for you, which will come handy later. There is a clock on the wall with time 3:00 with USA flag as background , you can have a look at my old diary, an antique vase, and an ancient roman rock. Which one do you want to pick up first
    """,
    """
There are many scary things in this dark room,
there is a spooky little girl mannequine with a t-shirt and something is written on it, 
There are many skeletons hidden in the room, I ate them up casually and buried when I was bored, hehehehe, 

    """
    
]
no_option_message=[
    "You don't have an option., My room my rules \n",
    "It is funny you still think you have an option \n"
]


all_objects = [{'diary':{'item':'diary','type':'final','question':"You open the diary and find this written on the first page  -Until I am measured I am not known, Yet how you miss me when I have flown. The Number you seek is the letters I contain",'answer':"4",'clue':"I wait for none",'completed':False},
               'watch':{'item':'watch','type':'final','question':"If you turn it around you find a text saying, I love New York’s Times Square, that is the second digit of the door lock.",'answer':"9",'completed':False, 'clue':"Think mathematically" },
               'rock':{'item':'rock','type':'final','question':"You can see letter V inscribed on it.",'answer':"5",'completed':False, 'clue':"Capital of Italy" },
              # 
              },
               {
                   'mannequin':{'item':'mannequin', 'required_prop':None,'type':'final','question':"She also came here and couldn’t escape so I turned her into a mannequin, so be careful!!! A t-shirt on her says, “I am present, but also past. I am wrapped, but not a gift. I am named after a parent, but have no children”",'answer':"mummy",'clue':"Egypt",'completed':False},
                   
                   'vase': {'type':'collection','item':'vase', 'required_prop':None,"action" : "When you try to pick the vase it turns to dust and now you find a crumbled paper fall from it", 'collection':[{'item':'paper','type':'mechanical','required_prop':"magnifying_lens",'answer':"4",'pretext':"The letters seem to be very small not possible to read them with naked eye, \ntry looking for something to make text appear bigger ",'completed':"It reads"}] } ,
                   'cabinet':{'type':'collection','item':'cabinet','required_prop':'torch', 'pretext':"The doors of the cabinet open with squeky sound \n It is too dark inside, find something to light things up", "action": "With the light  you see a cloth,\n A cloth drenced in blood ",
                               'collection':[{'item':'cloth','type':'final', "pretext":"Hehe i only wiped the blood spilled on the floor, you can use some other prop to make the cloth clean and read the text written on it",'required_prop':"water",'answer':"blood",'question':"From the head down to toes, through every living being I flow. Some people might faint when they see me though! What am I",'completed':"It reads"}]},
                    'water':{'type':'prop', 'item':'water','required_prop':None,'description':'something about the glass', 'use':"You can use this to clean", 'inoperable':"The {} is not so dirty, no point in using water to clean"},
                    'magnifying_lens':{'type':'prop', 'item':'magnifying_lens','required_prop':None,'description':'something about the glass', 'use':"now things look enlarged"},
                    'torch':{"type":'prop', 'item':'torch','required_prop':None,'desciption':'sesc about torch','use':'Torch turns on with a yellow beam','inoperable':"The {} is not so dark, the beam does not have much effect"}
              },
               {'mirror':{'item':'mirror','type':'final','question':"Wear them and look up, you can see the text “Look in my face, I am somebody. Look in my back, I am nobody. What am I?”",'answer':"mirror",'clue':"mirror clue",'completed':False}},
               {'final_paper':{'item':'mirror','type':'final','question':" The house surrenders only to the fearless and bold to be one you need to survive this last ordeal, behold  A survivor hides within this room, get me his name and we’ll end this game.",'answer':"name",'clue':"its you",'completed':False}}
               
               ]

