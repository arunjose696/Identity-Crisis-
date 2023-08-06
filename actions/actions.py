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
from .intro import intro_messages,room_setting,all_objects_global,no_option_message,fakekey_utterences
from .utils import look_around,type_write
from rasa_sdk.events import UserUtteranceReverted, ActionExecuted
import spacy
from random import shuffle
import nltk
nltk.download('popular')
nlp = spacy.load("en_core_web_md")
import uuid
from .utils import add_audio_and_image


FIRST_ROOM_KEY="459"


collections_list = []
diary = []


def get_jumbled_name(name):
    word = list(name)
    shuffle(word)
    word = " ".join(word)
    if word==name:
        return get_jumbled_name(word)        
    return word.lower()
    

def create_box(text):
    return text

def numberlock(text):
    return text
class GameInterest(Action):
    def name(self) -> Text:
        return "action_game_interest"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        interest_in_game = tracker.get_slot('interest_in_game')
        
        
        print("HELOO","interest_in_game")
        level =tracker.get_slot('level')
        if interest_in_game.lower() in ['yes','ya','yeah','ja','okay']:
            dispatcher.utter_message(text=room_setting[level])
        else:
            dispatcher.utter_message(text=no_option_message[level]+room_setting[level])
            
        return []
class IntroAction(Action):
    def name(self) -> Text:
        return "action_intro"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action_intro")
        name = tracker.get_slot('name')
        level =tracker.get_slot('level')
        if level == 1:
            message = intro_messages[level]
        else:
            message = "Hello {0} !!!".format(name)+intro_messages[level]
        dispatcher.utter_message(text=message)
        return []
class AskName(Action):
    def name(self) -> Text:
        return "action_ask_name"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:     
        dispatcher.utter_message(text="""Welcome to Trap for Dummies!. To Start the challenge please enter your name.    <head><link rel="preload" href="https://drive.google.com/uc?id=18w_boFKDWwOVsc0g12CZBMWhKVQJQc_-" as="image"></head>""")
    
        return


class RoomOneGiveClue(Action):
    def name(self) -> Text:
        return "action_give_clue"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        current_object = tracker.get_slot('current_object')
        finished_objects = tracker.get_slot('finished_objects')
        all_objects = tracker.get_slot('all_objects')
        level =tracker.get_slot('level')
        print("action_give_clue") 
        if current_object is None:
            dispatcher.utter_message(text="Pick up something first")
            return
        
        events = []        
        help_remaining = tracker.get_slot("helps_remaining")
        if True and help_remaining and help_remaining > 0:
            current_object = tracker.get_slot('current_object')
            current_object_details = all_objects[level][current_object]
            if "clue" not in current_object_details: 
                if "use" in current_object_details:
                    dispatcher.utter_message(text = "If you try to use, {}".format(current_object_details["use"]))
                dispatcher.utter_message(text = "There are no clues I can give you for the {}".format(current_object)) 
                return 
            clue = current_object_details['clue']
            if type(clue) == str:
                dispatcher.utter_message(text=create_box(clue))    
            elif type(clue) == list:
                clue_level = tracker.get_slot("clue_level")
                if int(clue_level) + 1 <= len(clue):
                    dispatcher.utter_message(text=create_box(clue[clue_level]))
                    events.append(SlotSet("clue_level", clue_level + 1))
                else:
                    dispatcher.utter_message(text=create_box("THE CLUES FOR THIS RIDDLE HAS EXHAUSTED"))
            
            events.append(SlotSet("helps_remaining", help_remaining - 1))
            return events
        else:
            dispatcher.utter_message(text="You have used all your clues")

class RoomOneInteract(Action):
    def name(self) -> Text:
        return "action_room_one_interact"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        print (tracker.latest_message)
        print(tracker.get_slot("first_room_clues_done"))
        level =tracker.get_slot('level')
        print("RoomOneInteract")
        print(tracker.latest_message)
        all_objects = tracker.get_slot('all_objects')
        events = []
        for entity in tracker.latest_message["entities"]:
            if entity["entity"] == "current_object":
                current_object = entity["value"]
                current_object.lower()
                finished_objects = tracker.get_slot('finished_objects') if tracker.get_slot('finished_objects') else []
                current_object = current_object.lower()
                if current_object.lower() in collections_list:                    
                    finished_objects.append(current_object)
                    dispatcher.utter_message(text="You have kept Paper in the bag")
                    dispatcher.utter_message(text=look_around(all_objects[level], finished_objects=finished_objects))
                    return [SlotSet("finished_objects", list(set(finished_objects)))]
                else:
                    if current_object in finished_objects:
                        dispatcher.utter_message(text="You had already cracked the puzzle I had in  {}".format(current_object))
                        dispatcher.utter_message(text=look_around(all_objects[level],finished_objects))
                        print("-------------")
                        return
                    elif current_object not in all_objects[level]: 
                        
                        dispatcher.utter_message(text="You don't have a {} in this room".format(current_object))                       
                        dispatcher.utter_message(text=look_around(all_objects[level],finished_objects))
                        print("-------------")
                        return 
                    else:
                        object_data = all_objects[level][current_object]
                        print(object_data)
                        if object_data['type'] == "final":
                            dispatcher.utter_message(text=object_data['question'])        
                        elif object_data['type'] == "mechanical":
                            dispatcher.utter_message(text=object_data['clue'])
                        elif object_data['type'] == "collection":
                            for item in object_data["collection"]:
                                all_objects[level][item["item"]] = item
                            finished_objects = tracker.get_slot('finished_objects') if tracker.get_slot('finished_objects') else []
                            finished_objects.append(current_object)
                            dispatcher.utter_message(text=object_data['action'])
                            dispatcher.utter_message(text=look_around(all_objects[level], finished_objects=finished_objects))
                            events.append(SlotSet("clue_level", 0))
                            events.append(SlotSet("finished_objects", list(set(finished_objects))))
                            return events
                        events.append(SlotSet("clue_level", 0))
                        events.append(SlotSet("current_object", current_object))
                        return events 
        dispatcher.utter_message(text=look_around(all_objects[level]))



                    
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
        level =tracker.get_slot('level')
        all_objects = tracker.get_slot('all_objects')
        print(current_object)
        print(all_objects)
        print(level)
        print(all_objects[level])
        if current_object in all_objects[level]:
            current_object_details = all_objects[level][current_object]
            answer = current_object_details['answer']
            
            
            for entity in tracker.latest_message["entities"]:
                if entity["entity"] == "number_answer":
                    user_answer = str(w2n.word_to_num(entity["value"]))
                    if user_answer == answer:
                        finished_objects.append(current_object)
                        finished_objects_statment = ", ".join(finished_objects)
                        remaining_objects = list((set(all_objects[level].keys())) - set(finished_objects))
                        if len(remaining_objects) > 0:
                            remaining_objects_statment = ", ".join(remaining_objects)
                            display_rem_item_text = """<link rel=“preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Butcherman&family=Creepster&family=Eater&family=Nosifer&display=swap" rel="stylesheet"><h3>Fantastic !!! You got it right!! </h3>As you have already solved {0}, you are left with <h2 style="font-family: 'Nosifer', cursive; font-size:17pxpx;"> {1} </h2> Pick the next object.""".format(finished_objects_statment,remaining_objects_statment)
                            
                            dispatcher.utter_message(text=display_rem_item_text)
                            return [SlotSet("finished_objects", list(set(finished_objects))), SlotSet("current_object", None)]
                        else:
                            dispatcher.utter_message(text="""<link rel=“preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Butcherman&family=Creepster&family=Eater&family=Nosifer&display=swap" rel="stylesheet"> <p style="color:green;font-family: 'Nosifier', cursive; font-size:30px;">Great, you got the digits. I love arranging everything in “order”, same can go with the digits. \nArrange it in the order of small to big.</p>""")
                            return [SlotSet("first_room_clues_done", True),FollowupAction("key_form"), SlotSet("current_object", None)]
                        # return [ConversationPaused()]
                    else:
                        help_remaining = tracker.get_slot("helps_remaining")
                        dispatcher.utter_message(text="The Answer you entered is wrong, You have {} helps pending may be use one or try something else".format(help_remaining))
                    break
        return 

class RoomTwoInteract(Action):
    def name(self) -> Text:
        return "action_room_two_interact"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action_room_two_interact")
        # print(tracker.slots)
        print(tracker.latest_message["text"])
        all_objects = tracker.get_slot('all_objects')
        level =tracker.get_slot('level')
        events=[]
        finished_objects = tracker.get_slot('finished_objects') if tracker.get_slot('finished_objects') else []
        bag = tracker.get_slot('bag')
        for entity in tracker.latest_message["entities"]:
            if entity["entity"] == "current_object":
                object = entity["value"]
                object.lower()
                object = object.lower()
                
                if object not in all_objects[level] and object not in bag:
                    print(f"---{object}---{level}------")
                    dispatcher.utter_message(text="You don't have a {} in this room".format(object))                       
                    dispatcher.utter_message(text=look_around(all_objects[level]))
                    return 
                if object in  all_objects[level]:
                    object_data = all_objects[level][object]
                    current_object = object_data["item"]
                else:
                    object_data = bag[object]
                if object_data['required_prop']:
                    if object_data['required_prop'] ==  tracker.get_slot("current_prop"):
                        pass
                    elif object_data['required_prop'] not in bag:
                        print(f"not in bag here {object}")
                        dispatcher.utter_message(text=object_data['pretext'])
                        events.append(SlotSet("clue_level", 0))
                        events.append(SlotSet("current_object", object))
                        return events
                    else :
                        dispatcher.utter_message(text=object_data['pretext'])
                        dispatcher.utter_message(text="something in your bag would help")
                        print(f"matched here {object}")
                        events.append(SlotSet("clue_level", 0))
                        events.append(SlotSet("current_object", object))
                        return events
            
                if object_data['type']=='prop':
                    current_object = tracker.get_slot("current_object")
                    print(f"CURRENT 345 {current_object}")
                    if current_object:
                        if all_objects[level][current_object]['required_prop']==object:
                            dispatcher.utter_message(text=object_data['use'])
                            object_data=all_objects[level][current_object]
                            events.append(SlotSet("current_prop", None))
                            if object in all_objects[level]:
                                bag[object]= all_objects[level].pop(object) 
                                events.append(SlotSet("bag", bag)) 
                                events.append(SlotSet("all_objects", all_objects)) 
                                 
                                     
                        else:
                            dispatcher.utter_message(text=object_data["inoperable"].format(current_object))
                            
                    elif object_data['item'] not in  bag:
                        object_data = all_objects[level].pop(object)
                        bag[object] = object_data
                        events.append(SlotSet("bag", bag))   
                        dispatcher.utter_message(text="You have kept the {} in your bag it may come in handy later".format(object))
                        events.append(SlotSet("current_prop", object))
                        events.append(SlotSet("all_objects", all_objects)) 
                        return events
                    else:
                        dispatcher.utter_message(text=object_data["inoperable"].format("room"))
                        events.append(SlotSet("current_prop", object))
                        return events

                if object_data['type'] == "final":
                    if object_data['item'] == 'paper':
                        name = tracker.get_slot('name')
                        jumbled_name = get_jumbled_name(name)
                        dispatcher.utter_message(text=object_data['question'].format(jumbled_name))
                        events.append(FollowupAction("finalanswer_form")   )
                    else:
                        dispatcher.utter_message(text=object_data['question'])
                        events.append(FollowupAction("answer_form")   )
                    print("-----------") 
                    events.append(SlotSet("current_object", current_object)) 
                    
                    events.append(SlotSet("clue_level", 0))
                elif object_data['type'] == "mechanical":
                    dispatcher.utter_message(text=object_data['completed'])
                    finished_objects.append(current_object)
                    dispatcher.utter_message(text=look_around(all_objects[level], finished_objects=finished_objects))
                    events.append(SlotSet("current_object", None))
                    events.append(SlotSet("clue_level", 0))
                    events.append(SlotSet("finished_objects", list(set(finished_objects))))
                elif object_data['type'] == "collection":
                    for item in object_data["collection"]:
                        
                        all_objects[level][item["item"]] = item
                        print(f"all_objects is {all_objects}")
                        events.append(SlotSet("all_objects", all_objects))                    
                    finished_objects.append(current_object)
                    dispatcher.utter_message(text=object_data['action'])
                    #dispatcher.utter_message(text=look_around(all_objects[level], finished_objects=finished_objects))
                    events.append(SlotSet("finished_objects", list(set(finished_objects))))
                    return events
                remaining_objects = list((set(all_objects[level].keys())) - set(finished_objects))
                if len(remaining_objects)==0:
                    level=level+1
                    events.append(SlotSet("level", level))
                    dispatcher.utter_message(text=add_audio_and_image("You see door infront of you. When you to try to approach the door A big VASE appears infront of you. Let's see how you get past it, (try to pick it up)",image_id="16hTtS9bKQJUZX1RcHjEX4qv8g9il0hk2"))
                    events.append(SlotSet("finished_objects", []))
                return events
        dispatcher.utter_message(text="pick up something in the room")
        return events



class RoomTwoAnswerInteract(Action):
    def name(self) -> Text:
        return "action_room_two_answer_interact"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action_room_two_answer_interact")
        dispatcher.utter_message(text="action_room_two_answer_interact")
        
class RoomTwoAnswerInteract(Action):
    def name(self) -> Text:
        return "look_around"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        all_objects = tracker.get_slot('all_objects')
        level = tracker.get_slot('level')
        finished_objects = tracker.get_slot('finished_objects') if tracker.get_slot('finished_objects') else []
        dispatcher.utter_message(text=look_around(all_objects[level], finished_objects=finished_objects))

class BagInteract(Action):
    def name(self) -> Text:
        return "look_bag"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        bag = tracker.get_slot('bag')
        if len(bag) > 0:
            bag_items = bag.keys()
            bag_items_statment = ", a".join(bag_items)
            dispatcher.utter_message(text="In Bag you can find {}. Things in bag will be used automatically when its needed".format(bag_items_statment))
        else:
            dispatcher.utter_message(text="No Things in bag")


class StartFakeKeyForm(Action):
    def name(self) -> Text:
        return "action_start_fakekey_form"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action_start_fakekey_form")
        return [FollowupAction("fakekey_form")]


class RoomTwoAnswerInteract(Action):
    def name(self) -> Text:
        return "test_action"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        all_objects = tracker.get_slot('all_objects')
        print("test_action")
        print("current_object {}".format(tracker.get_slot('current_object')))
        print("current_prop {}".format(tracker.get_slot('current_prop')))
        print("current_prop {}".format(tracker.get_slot('bag')))
        print("all_objects {}".format(all_objects))
        print("=================================================")
        print(tracker.latest_message)
        print("=================================================")
        level=1
        
        dispatcher.utter_message(text="test_action")
        
        return  [SlotSet("first_room_clues_done", True),SlotSet("current_object", None), SlotSet("current_prop", None),  SlotSet("level", level)]



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
                return {"name":name,"all_objects":all_objects_global} 
        if len(tracker.latest_message["text"])>2:
            text = tracker.latest_message["text"]
            name =''.join(e for e in text if e.isalnum())
            return {"name":name,"all_objects":all_objects_global}
                      
        
        return {"name":None,"key":None,"all_objects":all_objects_global}

class ValidateAnswerForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_answer_form"

    def validate_answer(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `key` value."""
        print("validate action")
        print(tracker.latest_message)
        level = tracker.get_slot('level')
        form_exit_intents = ["current_object","look_around_room"]
        user_answer= nlp(tracker.latest_message["text"])
        all_objects = tracker.get_slot('all_objects')
        current_object = tracker.get_slot('current_object')
        finished_objects = tracker.get_slot('finished_objects')
        current_object_details = all_objects[level][current_object]
        print("level {} current_object{}".format(level,current_object))
        if level == 2 and current_object == 'paper':
            print("user_answer {} correct_answer{}".format(user_answer,tracker.get_slot('name')))
            correct_answer = tracker.get_slot('name')
            user_answer = str(user_answer)
            if correct_answer.strip().lower() == user_answer.strip().lower():
                print("inside if user_answer {} correct_answer{}".format(user_answer,tracker.get_slot('name')))
                dispatcher.utter_message(text="Yes, you were the survivor afterall and now that you revealed the name yourself .I am letting you free this time.")
                return {"answer":user_answer} 
            else:
                print("inside else user_answer {} correct_answer{}".format(user_answer,tracker.get_slot('name')))
                dispatcher.utter_message(text="Try to solve the  jumbled letters")
                return {"answer":None} 
        else:
            correct_answer = nlp(current_object_details['answer'])
            similarity = correct_answer.similarity(user_answer)
        
            if similarity>0.7:
                # dispatcher.utter_message(text="Fantastic !!! You are one hurdle less from escaping!!")
                finished_objects.append(current_object)
                current_prop = tracker.get_slot("current_prop")
                if current_prop is not None:
                    finished_objects.append(current_prop)
                finished_objects_statment = ", ".join(finished_objects)
                remaining_objects = list((set(all_objects[level].keys())) - set(finished_objects))
                if len(remaining_objects) > 0:
                    remaining_objects_statment = ", ".join(remaining_objects)
                    display_rem_item_text = """<link rel=“preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Butcherman&family=Creepster&family=Eater&family=Nosifer&display=swap" rel="stylesheet"><h3>Fantastic !!! You are one hurdle less from escaping!!</h3> As you have already solved {0}, you are left with <h2 style="font-family: 'Nosifer', cursive; font-size:17px;"> {1} </h2> Pickup the next object.""".format(finished_objects_statment,remaining_objects_statment)
                    dispatcher.utter_message(text=display_rem_item_text)
                    return {"answer":current_object_details['answer'],"finished_objects":finished_objects} 
                else:
                    # dispatcher.utter_message(text="You have solved all clues in this room")
                    level = level+1
                    dispatcher.utter_message(text="""<link rel=“preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Butcherman&family=Creepster&family=Eater&family=Nosifer&display=swap" rel="stylesheet"><h3>Faboulous !!! You almost escaped from me, but I can't leave you that easy !!</h3> <p style="color:green; font-family: 'Nosifier', cursive;font-size:17px"> A door appears infront of you. When you to try to approach the door A big VASE appears infront of you. Let's see how you get past it , (try to pick up the VASE)</p>""")
                    return {"answer":current_object_details['answer'],"finished_objects":[],"level":level} 
            else:
                help_remaining = tracker.get_slot("helps_remaining")
                dispatcher.utter_message(text="The Answer you entered is wrong, You have {} helps pending may be use one or try something else".format(help_remaining))
            return {"answer":None} 


class ValidateAnswerForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_finalanswer_form"

    def validate_finalanswer(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `key` value."""
        print("validate final answer action")
        print(tracker.latest_message)
        level = tracker.get_slot('level')
        form_exit_intents = ["current_object","look_around_room"]
        user_answer= nlp(tracker.latest_message["text"])
        all_objects = tracker.get_slot('all_objects')
        current_object = tracker.get_slot('current_object')
        finished_objects = tracker.get_slot('finished_objects')
        current_object_details = all_objects[level][current_object]
        print("level {} current_object{}".format(level,current_object))
        if level == 2 and current_object == 'paper':
            print("user_answer {} correct_answer{}".format(user_answer,tracker.get_slot('name')))
            correct_answer = tracker.get_slot('name')
            user_answer = str(user_answer)
            if correct_answer.strip().lower() == user_answer.strip().lower():
                print("inside if user_answer {} correct_answer{}".format(user_answer,tracker.get_slot('name')))
                dispatcher.utter_message(text="<h2>Congratulations!!!! You've managed to escape the confining room</h2> but beware, for an eerie presence lingers ever so close behind you. Like a haunting shadow, it stalks your every move, patiently waiting for the perfect opportunity to become your lifelong companion, whether in friendship or something much darker.")
                return [ConversationPaused()]
            else:
                print("inside else user_answer {} correct_answer{}".format(user_answer,tracker.get_slot('name')))
                dispatcher.utter_message(text="Try to solve the  jumbled letters")
                return {"answer":None} 
              
        
class ActionAskCarVersion(Action):
    def name(self):
        return "action_ask_answer"

    def run(self, dispatcher, tracker, domain):
        print( "action_ask_answer")
        
        current_object = tracker.get_slot('current_object')
        dispatcher.utter_message(text="The {} awaits an answer. You can use HELP to get clues from the girl.".format(current_object))

        return []           
         
class ActionResetAnswerSlot(Action):
    def name(self) -> Text:
        return "action_reset_answer"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("answer", None)]     
        
class ValidateKeyForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_fakekey_form"

    def validate_fakekey(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `key` value."""
        print("validate fake_key action")
        attempt = tracker.get_slot('attempt')
        
        numbers=re.findall(r"\d+", slot_value)
        if not numbers:
            dispatcher.utter_message(text="Let us deal with all that later, now try to guess a 3 digit key")
            return {"fakekey":None}
        if  len(numbers[0]) !=3:
            dispatcher.utter_message(text="Lock takes a 3 digit key")
            return {"fakekey":None}
        attempt=attempt+1
        if attempt >= 3:
            #dispatcher.utter_message(text=type_write(text="Password is wrong the clown laughs viciously and stabs you right in your throat. You look at the clock it is 6:15, 6:15 the time of your death.", id="abc"))
            texts=["Password is wrong, the clown laughs viciously and stabs you right in your throat and you lie dead there, 6:15 the time of your death",
                   "Suddenly you hear the alarm ringing at 6 am, you realise that it was all a deadly dream afterall, now you have to actually WAKE UP to play the actual game. Type WAKEUP to start the game."]
            dispatcher.utter_message(text=type_write(texts))
            return {"fakekey":"value"}
            
        status=""
        mistakes = 0
        user_entry=numbers[0]
        for i in range(3):
            if user_entry[i] == FIRST_ROOM_KEY[i]:
                status+="\U00002705 "
            else:
                status+= "\U0000274C "
                mistakes += 1
        
        #todo add validations to handle different type of numbers
        if mistakes>0:
            print("inside if")
            dispatcher.utter_message(text="Looks like the key is wrong, the number lock shows \n{}".format(status))
            
            
            return {"fakekey":None,"attempt":attempt}
        else:
            dispatcher.utter_message(text="Looks like the key is right, but the door does not open\n{}".format(status))
            return {"fakekey":None,"attempt":attempt}
    
    def validate_wakeup(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        intent = tracker.latest_message.get('intent', {}).get('name')
        if intent== "wake_up":
            return {"wakeup":"Done"}
        else:
            dispatcher.utter_message(text="Try waking up first")
            return  {"wakeup":None}
            
            
        
class ActionAskFakeKey(Action):
    def name(self):
        return "action_ask_fakekey"

    def run(self, dispatcher, tracker, domain):
        print( "action_ask_fakekey")
        attempt = tracker.get_slot('attempt')
        previousattempt = tracker.get_slot('previousattempt')
        if attempt != previousattempt:
            dispatcher.utter_message(text="{}".format(fakekey_utterences[attempt]))
        
        previousattempt = attempt

        return [SlotSet("previousattempt", previousattempt)] 

class ActionAskWakeUp(Action):
    def name(self):
        return "action_ask_wakeup"

    def run(self, dispatcher, tracker, domain):
        print( "action_ask_wakeup")
        
        level=tracker.get_slot('level')
        if level==-1:
            level+=1
            dispatcher.utter_message(text=add_audio_and_image("",audio_id="1kCz1eAoJB1dh_i7qFN-H-G3tZz7eN9Nz"))
            return [SlotSet("level",level)]
        else:
            dispatcher.utter_message(text="Wake up to start the game")
            
        
        
    
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
        level = tracker.get_slot('level')
        finished_objects = tracker.get_slot('finished_objects')
        
        if not numbers or len(numbers[0]) !=3:
            dispatcher.utter_message(text="The door lock only accepts one number which should be 3 digits.")
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
            dispatcher.utter_message(text="Looks like the key is wrong, the number lock shows.\n Arrange the numbers in ascending order.")
            dispatcher.utter_message(text=numberlock(status))
            
            return {"key":None}
        else:
            dispatcher.utter_message(text=("The number lock clicks."))
            dispatcher.utter_message(text=numberlock(status))
            
            level = level+1
            finished_objects =[]
            return {"key":FIRST_ROOM_KEY,"level":level, "finished_objects":finished_objects} 


            
        
class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_default_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        print("fallback")
        print(tracker.latest_message)
        dispatcher.utter_message(text=f"An unexpected error, We are sorry this occured. Could you reload the window and play the game again, this time it would be great if you dont type in <h2>{tracker.latest_message['text']}</h2> we will keep a note of this and fix this soon so the issue does not occur anymore")

        # Revert user message which led to fallback.
        return []