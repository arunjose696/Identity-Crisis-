from .utils import add_audio_and_image

fakekey_utterences=[
    """
    The game has started but it looks like a DREAM to you.
    It is chaotic everywhere. The time is 6:15 in the morning. In the dream you are seeing a LITTLE GIRL in front of you. She looks terrified and is trying to tell you something.
    <p style="color:green;">Little girl:The clown is approaching, he will kill us both if you stay still, there is a door with 3 DIGIT LOCK in front of you, try entering any random 3 digit number and please help me.</p>
    
    <p style="color:brown;">Narration:You can try your LUCK and enter a random 3 digit number to unlock the door to escape, try fast, as the scary clown with a shovel is approaching you and the little girl.</p>
    """,
    """
    <p style="color:brown;">The footsteps of the killer are getting closer.</p>
    <p style="color:green;">You can't loose hope with just one try, Please try again, if your luck clicks we both can be escape. The killer is approaching us fast.</p>
    <p style="color:brown;">Try guessing any random 3 digit code again.</p>
    
    """,
    add_audio_and_image("""
    <p style="color:brown;">Narration: The clown is right beside you, he makes a severe blow with a shovel, the girl's head is chopped off brutally and blood sprays on your face.</p>
    <p style="color:green;">Little girl: AAAAAAAHHHHHHHHH, I b...b......b...believed you were my savior.</p>
    <p style="color:brown;">Narration: Little girl is dead now, before the clown chops off your head also, you can quickly give one more try for the lock to save at least yourself. Do a last guess.</p>
    """,audio_id="1WlnVNbiX4yYnGHFb7ndT5lBGBtrrPwXT",image_id="1BOv4W_7KdZ64MdruMMJelMd3p3c9dEDZ")
]
intro_messages=[
    
    """ 
<p style="color:brown;">You have to play the game in a HAUNTED MANSION where you can see only darkness, so practically you wil be blind. As soon as you enter the mansion you hear a voice.</p>
<p style="color:green;">Little girl: Hey....Mate!!!! Do you remember me??? Probably not!!!! You are a person who could see future in dreams, yes you are thinking it right, we both are trapped here by a CLOWN for real this time, he is coming to kill us. He has set up some puzzles. If we solve those problems we will get some 3 digit key to exit a door. Will you please help me?</p>
    """,
    add_audio_and_image("""
Little girl turns to a witch,
<p style="color:red;">Witch:Hehe thank you for letting me escape. I am the witch you, you stupid clown trapped to save the world from me. I blinded you and took away your memories so I can escape from your room of riddles</p>
Now I have escaped you are in my room now. I will let you play a game here,  you will again solve clues, if you solve all my clues I don’t kill you today.
Do you want to explore the room?    
    """,audio_id="1cxR9lUcyYRpdivh9AHXUS0E-Dj7iWb4E",image_id="1kgAnnELo1MPJZLxCNSIhl6E9adpA-loD")
    
]

room_setting= [
    """
<p style="color:green;">Little girl: As you are practically blind I will help you explore the room, there are some objects I can see in the room.There is a wall clock \U0001F552, an old diary \U0001F4D6 , and an ancient ROMAN rock \U0001FAA8 . Which object do you want to pick to get the 3 digit code?\nIf you are stuck you can ask for help/clue.</p>

    """,
    """
    If you look around the room you can find many SCARY OBJECTS like a spooky little girl mannequin \U0001F9DB, a creepy looking cupboard \U0001F5C4, some hidden skeletons \U0001F480, and a Werewolf mask \U0001F43A ,
and some props like shovel \U000026CF, torch light \U0001F526, and a small bowl filled with water \U0001F963 . 
You have to use the PROPS to explore some OBJECTS. Pick any Scary Object?
"""
    
    
    ,
    """
Almost at the last state.
    """
    
]
no_option_message=[
    "You don't have an option, My room my rules \n",
    "It is funny you still think you have an option.\n",
    "in last few mins"
]


all_objects_global = [{'diary':{'item':'diary','type':'final','question':add_audio_and_image("Text on the diary reads \n\"Until I am measured I am not known, yet how you miss me when I have flown. The Number you seek is the letters I contain in my word?",image_id="1Psuf3GLNsZY0SzxMQQuSwLjjwusnYl0n"),'answer':"4",'clue':"Clock measures it. Enter the number of letters in what clock measures.",'completed':False},
               'watch':{'item':'watch','type':'final','question':add_audio_and_image("The watch from The USA shows 3'o clock, \n and I love New York’s \"TIME'S SQUARE\", the number you want lies in time's square?",image_id="17V2oA9aOFGWkFWbsAEwlD15wiz_W_QGi") ,'answer':"9",'completed':False, 'clue':"Square the Time." },
               'rock':{'item':'rock','type':'final','question':add_audio_and_image("You can see letter \U00002164 inscribed on it. Which number it can be?",image_id="1YWdCXvTLI3J38tgYx3LijQpPLlVnhfOc"),'answer':"5",'completed':False, 'clue':"I am a Roman numeral indicating a number." },
              },
               {
                   'mannequin':{'item':'mannequin', 'required_prop':None,'type':'final','question':add_audio_and_image("I have turned her into a mannequin, so be careful!!! A t-shirt on her says, \n“I am present, but also past. I am wrapped, but not a gift. I am named after a parent, but have no children, who am I?",image_id="1kZnRadBhXozTL9X1n7CP7ZEHSWSvJSwd"),'answer':"mummy",'clue':"My birth place is Egypt.",'completed':False},
                   'cabinet':{'type':'collection','item':'cabinet','required_prop':'torch', 'pretext':add_audio_and_image("The doors of the cabinet opens with squeaky sound. \n It is too dark inside, pickup a prop to light things up in cabinet",image_id="1k6nH6FJCdPVYSkQUbLe7D_BRS-ImOChv") , "action": "With the light you can see a cloth drenched in blood present inside cupboard. Pickup the CLOTH first.",
                               'collection':[{'item':'cloth','type':'final', "pretext":"Hehe I only wiped the blood spilled on the floor, pickup a prop to make the cloth clean and to read the text written on it.",'required_prop':"water",'answer':"Blood",'question':"After cleaning, you can read the text,'I flow through vessels, unseen by the eye, Scarlet and Vital, my hue cannot lie, Life's essence i carry, within me it dwells, A river of secrets, tales no tongue tells, What am I?'","clue":"Vampires favorite drink.",'completed':"It reads"}]},
                    'water':{'type':'prop', 'item':'water','required_prop':None,'description':'something about the glass', 'use':"You pour the liquid on the cloth", 'inoperable':"The {} is not so dirty, no point in using water to clean."},
                    'torch':{"type":'prop', 'item':'torch','required_prop':None,'desciption':'desc about torch','use':'Torch turns on with a yellow beam','inoperable':"The {} is not so dark, the beam does not have much effect."},
                    'shovel':{'type':'collection','item':'shovel', 'required_prop':None,"action" : "Great, you can dig the skeletons. Pick them up to get a clue.", 'collection':[{'item':'skeleton','type':'mechanical','required_prop':None,'answer':None,'pretext':None,'completed':"As soon as you touch the skeleton, you hear a voice saying, \nyou made a mistake of taking me out from my burial, there is nothing I can do \U0001F479, \n pickup next object to escape, fast, time is running out."}]},
                    'werewolf mask':{'item':'werewolf mask', 'required_prop':None,'type':'final','question':"This Werewolf mask has some special features, if you wear you can hear a voice giving you a riddle, \n'In depths so still, where evil lurks, a lifeless sea, where darkness works, Ghosts dance upon my shore, Devils prowl, and monsters roar, yet life escapes this eerie bed, with naught but salt, where fear is spread, what am I?'",'answer':"Dead Sea",'clue':"I am a sea named after DEATH.",'completed':False}
              },
               {'vase': {'type':'collection','item':'vase', 'required_prop':None,"action" : add_audio_and_image("You have to pickup a last object in order to escape, if you see there is a VASE \U0001F3FA and when you try to touch the vase it turns to dust \U0001F4A8 and now you find a scrambled paper \U0001F4C3 fall from it, you have to pick up the PAPER to solve the riddle and escape.",image_id="1Ul__dAt1LN0XxEs0qB0tqWlAVLAdHHBE"), 'collection':[{'item':'paper','type':'final','required_prop':None,'answer':{},'question':"The house surrenders only to the fearless and bold \n to be one you need to survive this last ordeal, behold \n A survivor hides within this room, \n get me his/her name \n and we’ll end this game <h1>{}</h1> \nArrange the alphabets and find the survivor.",'clue':"It's \"YOU\" dummy."}] }}
               ]

