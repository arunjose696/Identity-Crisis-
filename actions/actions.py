# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from email import message
from tkinter.messagebox import NO
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction, ConversationPaused
from rasa_sdk import Tracker, FormValidationAction
import json
import time
from typing import Text, List, Any, Dict
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from word2number import w2n
import re

FIRST_ROOM_KEY="459"
all_objects = {'diary':{'item':'diary','type':'final','question':"You open the diary and find this written on the first page  -Until I am measured I am not known, Yet how you miss me when I have flown. The Number you seek is the letters I contain",'answer':"4",'clue':"I wait for none",'completed':False},
               'watch':{'item':'watch','type':'final','question':"If you turn it around you find a text saying, I love New York’s Times Square, that is the second digit of the door lock.",'answer':"9",'completed':False, 'clue':"Think mathematically" },
               'rock':{'item':'rock','type':'final','question':"You can see letter V inscribed on it.",'answer':"5",'completed':False, 'clue':"Capital of Italy" },
              # 'vase': {'type':'collection',"action" : "When you try to pick the vase it turns to dust and now you find a crumbled paper fall from it", 'collection':[{'item':'paper','type':'mechanical','requiredSlot':"lens",'answer':"4",'clue':"The letters seem to be very small not possible to read them with naked eye, try looking ",'completed':"It reads"}] }
              }
props ={'lens':{'description':'something about the glass', 'pick':"now things look enlarged", "slot":"lens"}}
collections_list = ['paper']
bag = {}
diary = []
helps_remaining = 5

def create_box(text):
    lines = text.split('\n')
    max_line_length = max(len(line) for line in lines)
    box_width = max_line_length + 4
    box_height = len(lines) + 2
    horizontal_line = '─' * box_width
    box = '┌' + horizontal_line + '┐\n'
    for line in lines:
        padding = ' ' * (max_line_length - len(line))
        box += '│  ' + line + padding + '  │\n'
    box += '└' + horizontal_line + '┘\n'
    return box

def numberlock(text):
    lines = text.split('\n')
    max_line_length = max(len(line) for line in lines)
    box_width = max_line_length + 11
    box_height = len(lines) + 2
    horizontal_line = '─' * box_width
    box = '┌' + horizontal_line + '┐\n'
    for line in lines:
        padding = ' ' * (max_line_length - len(line))
        box += '│    ' + line + padding + '    │\n'
    box += '└' + horizontal_line + '┘\n'
    return box
class GameInterest(Action):
    def name(self) -> Text:
        return "action_game_interest"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        interest_in_game = tracker.get_slot('interest_in_game')
        
        
        print("HELOO",interest_in_game)
        
        if interest_in_game.lower() in ['yes','ya','yeah','ja','okay']:
            dispatcher.utter_message(text="Here is bag for you, which will come handy later. There is a clock on the wall with time 3:00 with USA flag as background , you can have a look at my old diary, an antique vase, goggles with yellow shades and an ancient roman rock. Which one do you want to pick up first?")
        else:
            dispatcher.utter_message(text="You don't have an option. You have to explore to exit. Here is bag for you, which will come handy later. There is a clock on the wall with time 3:00 with USA flag as background , you can have a look at my old diary, an antique vase, goggles with yellow shades and an ancient roman rock. Which one do you want to pick up first?")
            
        return []
class IntroAction(Action):
    def name(self) -> Text:
        return "action_intro"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        message = "Hello {0}, you have entered my haunted mansion, now you have to find a way to leave or else you will become my ghost friend forever.".format(name) +\
        "\nI am a smart spirit, you know, if you have to escape this mansion you have to crack the door’s secret code. "+\
        "\nI was a kind human when I was alive, so I will show some kindness and guide you through my super dark mansion and help you get out of this place."+\
        "\n Hehehehehe, rack your brains and have fun, Good luck!!!!"+\
        "\n Are you ready to explore my deadly mansion??."
        dispatcher.utter_message(text=message)
        return []
class AskName(Action):
    def name(self) -> Text:
        return "action_ask_name"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
    
        dispatcher.utter_message(text="Welcome to Escape Room Challenge!. To Start the challenge please enter your name.")
    
        return


class RoomOneGiveClue(Action):
    def name(self) -> Text:
        return "action_give_clue"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        current_object = tracker.get_slot('current_object')
        finished_objects = tracker.get_slot('finished_objects')
        print(tracker.latest_message["entities"]) 
        if current_object is None:
            dispatcher.utter_message(text="Pick up something first")
            return
        
        global helps_remaining
        if helps_remaining>0:
            current_object = tracker.get_slot('current_object')
            current_object_details = all_objects[current_object]
            clue = current_object_details['clue']
            dispatcher.utter_message(text = "The screen gets tuned on and you see")
            dispatcher.utter_message(text=create_box(clue))     
            helps_remaining -= 1
            if helps_remaining == 0:
                 dispatcher.utter_message(text="You have no more clues left")  
            else:
                dispatcher.utter_message(text="Be cautius you have just {} more clues!!!".format(helps_remaining))        
        else:
            dispatcher.utter_message(text="You have exhausted your helps")
            

class RoomOneInteract(Action):
    def name(self) -> Text:
        return "action_room_one_interact"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        print (tracker.latest_message)
        print(tracker.get_slot("first_room_clues_done"))
        print("RoomOneInteract")
        print(tracker.latest_message)
        for entity in tracker.latest_message["entities"]:
            if entity["entity"] == "current_object":
                current_object = entity["value"]
                current_object.lower()
                current_object = current_object.lower()
                if current_object.lower() in collections_list:
                    finished_objects = tracker.get_slot('finished_objects') if tracker.get_slot('finished_objects') else []
                    finished_objects.append(current_object)
                    dispatcher.utter_message(text="You have kept Paper in the bag")
                    dispatcher.utter_message(text=look_around(all_objects, finished_objects=finished_objects))
                    return [SlotSet("finished_objects", list(set(finished_objects)))]
                else:
                    if current_object not in all_objects:
                        dispatcher.utter_message(text="You dont have a {} in the room".format(current_object))                       
                        dispatcher.utter_message(text=look_around(all_objects))
                        print("-------------")
                        return 
                        
                    object_data = all_objects[current_object]
                    print(object_data)
                    if object_data['type'] == "final":
                        dispatcher.utter_message(text=object_data['question'])        
                    elif object_data['type'] == "mechanical":
                        dispatcher.utter_message(text=object_data['clue'])
                    elif object_data['type'] == "collection":
                        for item in object_data["collection"]:
                            all_objects[item["item"]] = item
                        finished_objects = tracker.get_slot('finished_objects') if tracker.get_slot('finished_objects') else []
                        finished_objects.append(current_object)
                        dispatcher.utter_message(text=object_data['action'])
                        dispatcher.utter_message(text=look_around(all_objects, finished_objects=finished_objects))
                        
                        return [SlotSet("finished_objects", list(set(finished_objects)))]
                        
                    return [SlotSet("current_object", current_object)]  
        dispatcher.utter_message(text=look_around(all_objects))

def look_around(all_objects=all_objects, finished_objects=[]):
    remaining_objects = list((set(all_objects.keys())) - set(finished_objects))
    if len(remaining_objects) > 0:
        remaining_objects_statment = ", a ".join(remaining_objects)
        finished_objects_statment = ", ".join(finished_objects)
        solved_item=""
        display_rem_item_text=""
        look_around_setting = "\n\nWhen you glance around the room, "
        if finished_objects:
            solved_item = "\nYou have already solved {0}!!".format(finished_objects_statment)
        if remaining_objects_statment:
            display_rem_item_text = "Now you  see a {0}. What are you gonna do now ?".format(remaining_objects_statment)
        return look_around_setting+display_rem_item_text#+solved_item
    else:
        return "You dont have anything more in the room to solve"
                    
class RoomOneAnswerInteract(Action):
    def name(self) -> Text:
        return "action_room_one_answer_interact"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("RoomOneAnswerInteract") 
        current_object = tracker.get_slot('current_object')
        finished_objects = tracker.get_slot('finished_objects')
        if current_object is None:
            dispatcher.utter_message(text="Pick up something first")
            return
            
        if current_object in all_objects:
            current_object_details = all_objects[current_object]
            answer = current_object_details['answer']
            
            
            for entity in tracker.latest_message["entities"]:
                if entity["entity"] == "number_answer":
                    user_answer = str(w2n.word_to_num(entity["value"]))
                    if user_answer == answer:
                        finished_objects.append(current_object)
                        finished_objects_statment = ", ".join(finished_objects)
                        remaining_objects = list((set(all_objects.keys())) - set(finished_objects))
                        if len(remaining_objects) > 0:
                            remaining_objects_statment = ", ".join(remaining_objects)
                            display_rem_item_text = "As you have already solved {0}, you are left with {1}. What are you gonna do now ?".format(finished_objects_statment,remaining_objects_statment)
                            dispatcher.utter_message(text=display_rem_item_text)
                            return [SlotSet("finished_objects", list(set(finished_objects)))]
                        else:
                            dispatcher.utter_message(text="Now you have found all the important number of my life. Arrange it an order of birth to death to escape this room")
                            return [SlotSet("first_room_clues_done", True),FollowupAction("key_form")]
                        # return [ConversationPaused()]
                    else:
                        dispatcher.utter_message(text="The Answer you entered is wrong, You have {} helps pending may be use one or try something else".format(helps_remaining))
                    break
        dispatcher.utter_message(text="ROOM ONE Answer")
        return 

####################Forms###########################

class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""
        print(tracker.latest_message["entities"]) 
        for entity in tracker.latest_message["entities"]:
            if entity["entity"] == "PERSON" or entity["entity"]=="name":
                name = entity["value"] 
                return {"name":name}       
        
        return {"name":None}
    
class ValidateKeyForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_key_form"

    def validate_key(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `key` value."""
        print("validate action")
        numbers=re.findall(r"\d+", slot_value)
        
        if not numbers or len(numbers[0]) !=3:
            dispatcher.utter_message(text="The door lock only accepts one number which should be 3 digits")
            return {"key":None}
        user_entry=numbers[0]
        status=""
        mistakes = 0
        for i in range(3):
            if user_entry[i] == FIRST_ROOM_KEY[i]:
                status+="\U00002705 "
            else:
                status+= "\U0000274C "
                mistakes += 1
        print("validate action")
        #todo add validations to handle different type of numbers
        if mistakes>0:
            print("inside if")
            dispatcher.utter_message(text="Looks like the key is wrong, the number lock shows\n")
            dispatcher.utter_message(text=numberlock(status))
            dispatcher.utter_message(text="\n")
            
            return {"key":None}
        else:
            dispatcher.utter_message(text="The number lock clicks")
            dispatcher.utter_message(text=numberlock(status))
            dispatcher.utter_message(text="\n")
            dispatcher.utter_message(text="Good the door opens for you  \U00002705")
            return {"key":FIRST_ROOM_KEY} 
            
        
