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
from .intro import intro_messages,room_setting,all_objects,no_option_message
from .utils import look_around
from rasa_sdk.events import UserUtteranceReverted, ActionExecuted
import spacy
nlp = spacy.load("en_core_web_md")

FIRST_ROOM_KEY="459"


collections_list = []
bag = {}
diary = []
helps_remaining = 5
level = 0

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
        
        
        print("HELOO","interest_in_game")
        
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
        message = "Hello {0}".format(name)+intro_messages[level]
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
        print("action_give_clue") 
        if current_object is None:
            dispatcher.utter_message(text="Pick up something first")
            return
        
        global helps_remaining
        if helps_remaining>0:
            current_object = tracker.get_slot('current_object')
            current_object_details = all_objects[level][current_object]
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
                finished_objects = tracker.get_slot('finished_objects') if tracker.get_slot('finished_objects') else []
                current_object = current_object.lower()
                if current_object.lower() in collections_list:                    
                    finished_objects.append(current_object)
                    dispatcher.utter_message(text="You have kept Paper in the bag")
                    dispatcher.utter_message(text=look_around(all_objects[level], finished_objects=finished_objects))
                    return [SlotSet("finished_objects", list(set(finished_objects)))]
                else:
                    if current_object not in all_objects[level]:
                        if current_object in finished_objects:
                            dispatcher.utter_message(text="You had already cracked the puzzle I had in  {}".format(current_object))                       
                        else:  
                            dispatcher.utter_message(text="You dont have a {} in the room".format(current_object))                       
                        dispatcher.utter_message(text=look_around(all_objects[level]))
                        print("-------------")
                        return 
                        
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
                        
                        return [SlotSet("finished_objects", list(set(finished_objects)))]
                        
                    return [SlotSet("current_object", current_object)]  
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
                            display_rem_item_text = "As you have already solved {0}, you are left with {1}. What are you gonna do now ?".format(finished_objects_statment,remaining_objects_statment)
                            dispatcher.utter_message(text=display_rem_item_text)
                            return [SlotSet("finished_objects", list(set(finished_objects))), SlotSet("current_object", None)]
                        else:
                            dispatcher.utter_message(text="Now you have found all the important number of my life. Arrange it an order of birth to death to escape this room")
                            return [SlotSet("first_room_clues_done", True),FollowupAction("key_form"), SlotSet("current_object", None)]
                        # return [ConversationPaused()]
                    else:
                        dispatcher.utter_message(text="The Answer you entered is wrong, You have {} helps pending may be use one or try something else".format(helps_remaining))
                    break
        dispatcher.utter_message(text="ROOM ONE Answer")
        return 


class RoomTwoInteract(Action):
    def name(self) -> Text:
        return "action_room_two_interact"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action_room_two_interact")
        print(tracker.latest_message["entities"])
        global all_objects
        events=[]
        finished_objects = tracker.get_slot('finished_objects') if tracker.get_slot('finished_objects') else []
        for entity in tracker.latest_message["entities"]:
            if entity["entity"] == "current_object":
                object = entity["value"]
                object.lower()
                object = object.lower()
                
                if object not in all_objects[level] and object not in bag:
                    dispatcher.utter_message(text="You dont have a {} in the room".format(object))                       
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
                        dispatcher.utter_message(text=object_data['pretext'])
                        return [SlotSet("current_object", object)]
                    else :
                        dispatcher.utter_message(text=object_data['pretext'])
                        dispatcher.utter_message(text="something in your bag would help")
                        return [SlotSet("current_object", object)]
            
                if object_data['type']=='prop':
                    current_object = tracker.get_slot("current_object")
                    if current_object:
                        if all_objects[level][current_object]['required_prop']==object:
                            dispatcher.utter_message(text=object_data['use'])
                            object_data=all_objects[level][current_object]
                            events.append(SlotSet("current_prop", None))
                            if object in all_objects[level]:
                                bag[object]= all_objects[level].pop(object)        
                        else:
                            dispatcher.utter_message(text=object_data["inoperable"].format(current_object))
                            
                    elif object_data['item'] not in  bag:
                        object_data = all_objects[level].pop(object)
                        bag[object] = object_data
                        dispatcher.utter_message(text="You have kept the {} in your bag it may come in handy later".format(object))
                        events.append(SlotSet("current_prop", object))
                        return events
                    else:
                        dispatcher.utter_message(text=object_data["inoperable"].format("room"))
                        events.append(SlotSet("current_prop", object))
                        return events

                if object_data['type'] == "final":
                    dispatcher.utter_message(text=object_data['question'])
                    print("-----------") 
                    events.append(SlotSet("current_object", current_object)) 
                    events.append(FollowupAction("answer_form")   )   
                elif object_data['type'] == "mechanical":
                    dispatcher.utter_message(text=object_data['completed'])
                    finished_objects.append(current_object)
                    dispatcher.utter_message(text=look_around(all_objects[level], finished_objects=finished_objects))
                    events.append(SlotSet("current_object", None))
                    events.append(SlotSet("finished_objects", list(set(finished_objects))))
                elif object_data['type'] == "collection":
                    for item in object_data["collection"]:
                        all_objects[level][item["item"]] = item                    
                    finished_objects.append(current_object)
                    dispatcher.utter_message(text=object_data['action'])
                    dispatcher.utter_message(text=look_around(all_objects[level], finished_objects=finished_objects))
                    events.append(SlotSet("finished_objects", list(set(finished_objects))))
                    return [SlotSet("finished_objects", list(set(finished_objects)))]
                   
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
        finished_objects = tracker.get_slot('finished_objects') if tracker.get_slot('finished_objects') else []
        dispatcher.utter_message(text=look_around(all_objects[level], finished_objects=finished_objects))


class RoomTwoAnswerInteract(Action):
    def name(self) -> Text:
        return "test_action"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("test_action")
        print("current_object {}".format(tracker.get_slot('current_object')))
        print("current_prop {}".format(tracker.get_slot('current_prop')))
        print("current_prop {}".format(bag))
        print("all_objects {}".format(all_objects))
        print("=================================================")
        print(tracker.latest_message)
        print("=================================================")
        global level
        level=1
        
        dispatcher.utter_message(text="test_action")
        return  [SlotSet("first_room_clues_done", True),SlotSet("current_object", None), SlotSet("current_prop", None) ]



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
        if len(tracker.latest_message["text"])>2:
            text = tracker.latest_message["text"]
            name =''.join(e for e in text if e.isalnum())
            return {"name":name}
                      
        
        return {"name":None}

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
        form_exit_intents = ["current_object","look_around_room"]
        user_answer= nlp(tracker.latest_message["text"])
        
        current_object = tracker.get_slot('current_object')
        finished_objects = tracker.get_slot('finished_objects')
        current_object_details = all_objects[level][current_object]
        correct_answer = nlp(current_object_details['answer'])
        similarity = correct_answer.similarity(user_answer)
        
        if similarity>0.7:
            dispatcher.utter_message(text="You got it right")
            finished_objects.append(current_object)
            finished_objects_statment = ", ".join(finished_objects)
            remaining_objects = list((set(all_objects[level].keys())) - set(finished_objects))
            if len(remaining_objects) > 0:
                remaining_objects_statment = ", ".join(remaining_objects)
                display_rem_item_text = "As you have already solved {0}, you are left with {1}. What are you gonna do now ?".format(finished_objects_statment,remaining_objects_statment)
                dispatcher.utter_message(text=display_rem_item_text)
                return {"answer":current_object_details['answer']} 
            else:
                dispatcher.utter_message(text="You have solved all clues")
                return {"answer":current_object_details['answer']} 
        else:
            dispatcher.utter_message(text="Not exactly what I have in mind try again")
        return {"answer":None} 
             
        
class ActionAskCarVersion(Action):
    def name(self):
        return "action_ask_answer"

    def run(self, dispatcher, tracker, domain):
        print( "action_ask_answer")
        
        current_object = tracker.get_slot('current_object')
        dispatcher.utter_message(text="The {} awaits an answer".format(current_object))

        return []           
         
        
        

    
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
            global level, finished_objects
            level = level+1
            finished_objects =[]
            return {"key":FIRST_ROOM_KEY} 


            
        
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
        dispatcher.utter_message(template="my_custom_fallback_template")

        # Revert user message which led to fallback.
        return [UserUtteranceReverted()]