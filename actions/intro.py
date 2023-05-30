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
Here is bag for you, which will come handy later. There is a clock on the wall with time 3:00 with USA flag as background , you can have a look at my old diary, and an ancient roman rock. Which one do you want to pick up first
    """,
    """
As your eyes get adjusted you start looking around, There are many scary things in this dark room you notice a spooky little girl mannequine, 
A warewolf mask which you can put on if you want, a shovel, a magnifying lens, a torch light, a chinese vase, a creepy looking cupboard, 
you also spot a yellow shaded goggles on the ground and a small bowl filled with water beside it.

Start with one of the objects and find your way out.
    """,
    """Still didn’t find the exit?? That is because I don’t want you to leave this mansion. 
    There is one more riddle for you inscribed on the wall, it will be visible if you wear yellow shaded goggles, want to try it out as a last option??
""",
"""I am worried that you will leave me. I want to have one final play with you. Here is a vase. Lift and see what is waiting for you.""",

"""When you tried to lift the vase, the vase dusted out and a paper fell from it. There is something on it but everything is so small to naked eye.
You were so smart from start. I have awareded you with a magnifying lens. You can use it to read it"""
    
]
no_option_message=[
    "You don't have an option., My room my rules \n",
    "It is funny you still think you have an option \n"
]


all_objects = [{'diary':{'item':'diary','type':'final','question':"You open the diary and find this written on the first page  -Until I am measured I am not known, Yet how you miss me when I have flown. The Number you seek is the letters I contain",'answer':"4",'clue':"I wait for none",'completed':False},
               'watch':{'item':'watch','type':'final','question':"If you turn it around you find a text saying, I love New York’s Times Square, that is the second digit of the door lock.",'answer':"9",'completed':False, 'clue':"Think mathematically" },
               'rock':{'item':'rock','type':'final','question':"You can see letter V inscribed on it.",'answer':"5",'completed':False, 'clue':"Capital of Italy" },
              },
               {'mannequin':{'item':'mannequin','type':'final','question':"She also came here and couldn’t escape so I turned her into a mannequin, so be careful!!! A t-shirt on her says, “I am present, but also past. I am wrapped, but not a gift. I am named after a parent, but have no children”",'answer':"mummy",'clue':"Egypt",'completed':False},
               'magnifying_lens':{'item':'magnifying_lens','type':'final','question':"Great work, the text reads “ I have a body, arms, legs and a head, but I’m heartless and have no guts. What am I?",'answer':"skeleton",'completed':False, 'clue':"body",'weiter_prompt': 'Lens will be useful in ur journey so let it be in ur bag'},
               'cupboard':{'item':'cupboard','type':'prop','question':"It looks like a chinese vase, you can find scrambled paper in it. The text is not clear, use another prop from around here.",'answer':None,'completed':False, 'clue':"Think mathematically",'connected_prop':[{'torch':'primary','bowl_water':'secondary'}],'fall_back':None },
               'torch_light':{'item':'torch_light','type':'prop','question':"The torch light lights up a small part of the cupboard,inside the cupboard you can see a cloth filled in fresh blood, you might have to use some other prop to make the cloth clean and read the text written on it.",'answer':None,'completed':False, 'clue':"yet to put torch",'connected_prop':[{'cupboard':'primary','bowl_water':'secondary'}],'fall_back':"Will be useful later"},
               'bowl_water':{'item':'bowl_water','type':'prop','question':"Now you can see the text inscribed on the cloth, It reads: “From the head down to toes, through every living being I flow. Some people might faint when they see me though! What am I?” ",'answer':"blood",'completed':False, 'clue':"bowl clue",'connected_prop':[{'cupboard':'primary','torch':'secondary'}],'fall_back':"use some other things to use this"},
               'werewolf_mask':{'item':'werewolf_mask','type':'final','question':"After you wear this mask, you notice a text written on the wall  \n“Where do ghosts, mummies, and devils love to swim?””",'answer':"dead sea",'completed':False, 'clue':"birth opposite"}
               },
               {'mirror':{'item':'mirror','type':'final','question':"Wear them and look up, you can see the text “Look in my face, I am somebody. Look in my back, I am nobody. What am I?”",'answer':"mirror",'clue':"mirror clue",'completed':False}},
               {'final_paper':{'item':'mirror','type':'final','question':" The house surrenders only to the fearless and bold to be one you need to survive this last ordeal, behold  A survivor hides within this room, get me his name and we’ll end this game.",'answer':"name",'clue':"its you",'completed':False}}
            #    ,
            #    {
            #        'vase': {'type':'collection','item':'vase', 'required_prop':None,"action" : "When you try to pick the vase it turns to dust and now you find a crumbled paper fall from it", 'collection':[{'item':'paper','type':'mechanical','required_prop':"lens",'answer':"4",'clue':"The letters seem to be very small not possible to read them with naked eye, \ntry looking for something to make text appear bigger ",'completed':False}] } ,
            #        'cabinet':{'type':'collection','item':'cabinet','required_prop':'torch', 'clue':"The doors of the cabinet open with squeky sound \n It is too dark inside, find something to light things up", "action": "With the light  you see a cloth,\n A cloth drenced in blood ",
            #                    'collection':[{'item':'cloth','type':'mechanical', "clue":"Hehe i only wiped the blood spilled on the floor, you can use some other prop to make the cloth clean and read the text written on it",'required_prop':"water",'answer':"blood",'question':"From the head down to toes, through every living being I flow. Some people might faint when they see me though! What am I",'completed':False}]},
            #         'lens':{'type':'prop', 'item':'lens','required_prop':None,'description':'something about the glass', 'use':"now things look enlarged"},
            #         'torch':{"type":'prop', 'item':'torch','required_prop':None,'desciption':'sesc about torch','use':'Torch turns on with a yellow beam','inoperable':"The {} is not so dark, the beam does not have much effect"}
            #   }
               ]
