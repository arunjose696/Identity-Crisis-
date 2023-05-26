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
Here is bag for you, which will come handy later. There is a clock on the wall with time 3:00 with USA flag as background , you can have a look at my old diary, an antique vase, goggles with yellow shades and an ancient roman rock. Which one do you want to pick up first
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
                   'vase': {'type':'collection',"action" : "When you try to pick the vase it turns to dust and now you find a crumbled paper fall from it", 'collection':[{'item':'paper','type':'mechanical','requiredSlot':"lens",'answer':"4",'clue':"The letters seem to be very small not possible to read them with naked eye, try looking ",'completed':"It reads"}] }                  
              }
               ]
