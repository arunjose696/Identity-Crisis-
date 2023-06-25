
def look_around(all_objects=[], finished_objects=[]):
    remaining_objects = list((set(all_objects.keys())) - set(finished_objects))
    if len(remaining_objects) > 0:
        remaining_objects_statment = ", a ".join(remaining_objects)
        finished_objects_statment = ", ".join(finished_objects)
        solved_item=""
        display_rem_item_text=""
        look_around_setting = "\n\nWhen you glance around the room, "
        if finished_objects:
            solved_item = "\nYou have already solved clues from <h3> {0} </h3>!!".format(finished_objects_statment)
        if remaining_objects_statment:
            display_rem_item_text = "you notice you still have to explore <h2> a {0} </h2>. What are you gonna do now ?".format(remaining_objects_statment)
        return look_around_setting+display_rem_item_text#+solved_item
    else:
        return "You don't have anything more in the room to solve"

def unwrap(finished_objects, tracker, current_object):
    finished_objects = tracker.get_slot('finished_objects') if tracker.get_slot('finished_objects') else []
    finished_objects.append(current_object)
    
def add_audio_and_image(text, audio_id=None,image_id=None):
    image = "<script> (function() { var imageUrl = 'https://drive.google.com/uc?id="+ image_id+"'; imageUrl = 'url(' + imageUrl.replace(/[\\']/g, '\\$&') + ')'; document.body.style.backgroundImage = imageUrl; })(); </script>"
    audio = "<audio autoplay> <source src= \"https://drive.google.com/uc?id={} \" type= \"audio/ogg \"></audio>".format(audio_id)
    if audio_id and image_id:
        return text + image + audio
    elif image_id:
        return text + image
    elif audio_id:
        return text+audio
    else:
        return
    
    