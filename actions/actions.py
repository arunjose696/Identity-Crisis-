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
from rasa_sdk.events import SlotSet, FollowupAction
import json
import time

all_objects = {'diary':{'item':'diary','question':"You open the diary and find this written on the first page  -Until I am measured I am not known, Yet how you miss me when I have flown. The Number you seek is the letters I contain",'answer':"4",'completed':False},
               'watch':{'item':'watch','question':"You look at the watch and it has 12 cities on it instead of numbers, there’s only one hand and it points at London. You flip the clock and find some wordings. The time is the number you seek",'answer':"7",'completed':False}}
class IntroAction(Action):
    def name(self) -> Text:
        return "action_intro"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("7")
        name = tracker.get_slot('name')
        message = "Hello {0}, You entered the escape room and the door slammed behind you.You find yourself in a dark dusty room, you notice big flashing screen on the wall and before you have time to look around you hear a voice coming from the screen, saying:".format(name) + \
            "\n\nWelcome to my mansion, my dear guests. I'm sorry to inform you that you have been invited for a very special party. I have been lonely for a long time, ever since I died in this mansion many years ago. I have been looking for some company, but no one ever comes to visit me. That's why I had to resort to more...creative methods. That's where you come in. You have one hour to find the exit of my mansion, or else you will join me as my permanent guests. Don't worry, it will be fun...for me. Good luck!" +\
            "\nYou look at your watch and it shows 8:00. As your eyes get adjusted to the darkness you go around the room exploring and looking for any clues to breakout. You notice An old diary, a watch with names fo 12 countries instead of numbers, A antique vase, a goggles with yellow shades and a Ancient roman rock." +\
    "\nIn front of you there is a hugeTreasure box with a lock that takes 3 digits in ascending order as its code."+\
    "\nyou look around the room and you spot a green door at the end of the room, you assume this is the exit and try to open the door. The door is locked firmly, and needs a key to open it." + \
        "\n Try to find key for the door."

        # for char in message:
        #     dispatcher.utter_message(text=char, typing=True)
        #     time.sleep(0.1)
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
class StoreNameAction(Action):
    def name(self) -> Text:
        return "action_store_name"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 

        name = tracker.get_slot('name')
        if name is None:
            for entity in tracker.latest_message["entities"]:
                if entity["entity"] == "name":
                    name = entity["value"]
            return [SlotSet("name", name)]
        else:
            dispatcher.utter_message("The Answer you entered is wrong")
            return [FollowupAction('action_room_one_interact')]


class RoomOneInteract(Action):
    def name(self) -> Text:
        return "action_room_one_interact"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        print (tracker.latest_message)
        for entity in tracker.latest_message["entities"]:
            if entity["entity"] == "current_object":
                current_object = entity["value"]
                object_data = all_objects[current_object]
                dispatcher.utter_message(text=object_data['question'])        
                return [SlotSet("current_object", current_object)]
class RoomOneAnswerInteract(Action):
    def name(self) -> Text:
        return "action_room_one_answer_interact"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        current_object = tracker.get_slot('current_object')
        finished_objects = tracker.get_slot('finished_objects')
        if current_object in all_objects:
            current_object_details = all_objects[current_object]
            answer = current_object_details['answer']
            
            for entity in tracker.latest_message["entities"]:
                if entity["entity"] == "number_answer":
                    user_answer = entity["value"]
                    if user_answer == answer:
                        finished_objects.append(current_object)
                        finished_objects_statment = ", ".join(finished_objects)
                        remaining_objects = list((set(all_objects.keys())) - set(finished_objects))
                        remaining_objects_statment = ", ".join(remaining_objects)
                        display_rem_item_text = "As you have already solved {0}, you are left with {1}. What are you gonna do now ?".format(finished_objects_statment,remaining_objects_statment)
                        dispatcher.utter_message(text=display_rem_item_text)
                        return [SlotSet("finished_objects", finished_objects)]
                    else:
                        dispatcher.utter_message(text="The Answer you entered is wrong")
                    break
        dispatcher.utter_message(text="ROOM ONE Answer")
        return 

    
class ActionInteract(Action):

    def name(self) -> Text:
        return "action_interact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if tracker.get_slot('data') is None or tracker.get_slot('data') == "null":
            data = {}
            with open('story.json') as f:
                data["objects"] = json.load(f)
        else: data = tracker.get_slot('data')

        print(tracker.latest_message["entities"])
        existing_object = False
        for entity in tracker.latest_message["entities"]:
            if entity["value"] in data["objects"].keys():
                interacted_object = data["objects"][entity["value"]]
                existing_object = True
                if entity["group"] in interacted_object:
                    action = entity["group"]
                    required_objects = []
                    if "need" in interacted_object[action]:
                        for need in interacted_object[action]["need"]:
                            if need not in data["objects"].keys():
                                required_objects.append(need)
                    if len(required_objects) > 0:
                        dispatcher.utter_message(
                            f"You can't {entity['group']} the {entity['value']}. You need: {', '.join(required_objects)}"
                        )
                        continue
                    dispatcher.utter_message(interacted_object[action]["utter"])
                    if not "objects" in interacted_object[action]: continue
                    dispatcher.utter_message(f"You find: {', '.join(interacted_object[action]['objects'].keys())}")
                    for object in interacted_object[action]["objects"].keys():
                        data["objects"][object] = interacted_object[action]["objects"][object]
                else:
                    if entity['group'] == "search":
                        dispatcher.utter_message(f"You can't find anything interesting when searching the {entity['value']}.")
                    else:
                        dispatcher.utter_message(f"You can't {entity['group']} the {entity['value']}.")
            else:
                dispatcher.utter_message(f"There is no {entity['value']}.")
        if not existing_object:
            dispatcher.utter_message(f"You can interact \U0001F4D4 with: {', '.join(data['objects'].keys())}")

        return [SlotSet("data", data)]
