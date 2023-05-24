from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.nlu import utils
from rasa.shared.nlu.training_data.message import Message
from typing import Any, List, Optional, Text
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from typing import Dict, Text, Any, List
from rasa.shared.nlu.training_data.training_data import TrainingData
from rasa.engine.storage.resource import Resource
import truecase
from rasa.engine.storage.storage import ModelStorage
@DefaultV1Recipe.register(

   [DefaultV1Recipe.ComponentType.INTENT_CLASSIFIER], is_trainable=True

)
class TruecaserPreprocessor(GraphComponent):
    name = "Truecaser"
    provides = []
    requires = []
    defaults = {}
    language_list = ["en"]
    @classmethod

    def create(

       cls,

       config: Dict[Text, Any],

       model_storage: ModelStorage,

       resource: Resource,

       execution_context: ExecutionContext,

   ) -> GraphComponent:

       # TODO: Implement this

       ...

    def train(self, training_data: TrainingData) -> Resource:

       # TODO: Implement this if our component requires training

       ...

    def process_training_data(self, training_data: TrainingData) -> TrainingData:

       # TODO: Implement this if our component augments the training data with

       #       tokens or message features which are used by other components

       #       during training.

       ...

       return training_data

    def process(self, messages: List[Message]) -> List[Message]:
        #print(messages[0])
        message =messages[0]
        text = truecase.get_true_case(message.get("text"))
        message.set("text", text)
        messages[0] = message
        #print(messages[0].get("text"))
        # Perform truecasing on the text
        
        

       # TODO: This is the method which Rasa Open Source will call during inference.

    

        return messages

    