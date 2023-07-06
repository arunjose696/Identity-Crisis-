
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
            display_rem_item_text = """<link rel=“preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Butcherman&family=Creepster&family=Eater&family=Nosifer&display=swap" rel="stylesheet">you notice you still have to explore <h2 style="font-family: 'Nosifer', cursive; font-size:15px;"> a {0} </h2>. What are you gonna do now ?""".format(remaining_objects_statment)
        print(display_rem_item_text)
        return look_around_setting+display_rem_item_text#+solved_item
    else:
        return "You don't have anything more in the room to solve"

def unwrap(finished_objects, tracker, current_object):
    finished_objects = tracker.get_slot('finished_objects') if tracker.get_slot('finished_objects') else []
    finished_objects.append(current_object)
    
def add_audio_and_image(text, audio_id=None,image_id=None, pos="center"):
    if image_id:
        if pos=="center":
            image = "<script> (function() { var imageUrl = 'https://drive.google.com/uc?id="+ image_id+f"'; imageUrl = 'url(' + imageUrl.replace(/[\\']/g, '\\$&') + ')'; document.body.style.backgroundImage = imageUrl; document.body.style.backgroundSize = '100\% 100\%'; document.body.style.backgroundPosition = '"+pos+"'; document.body.style.backgroundRepeat = 'no-repeat'; document.body.style.height = '100vh'; document.body.style.margin = '0'; document.body.style.padding = '0';})(); </script>"
        else:
            image = "<script> (function() { var imageUrl = 'https://drive.google.com/uc?id="+ image_id+"'; imageUrl = 'url(' + imageUrl.replace(/[\\']/g, '\\$&') + ')'; document.body.style.backgroundImage = imageUrl;document.body.style.backgroundSize = '100\% 100\%'; })(); </script>"
            
    if audio_id:
        audio = "<audio autoplay> <source src= \"https://drive.google.com/uc?id={} \" type= \"audio/ogg \"></audio>".format(audio_id)
    if audio_id and image_id:
        return text + image + audio
    elif image_id:
        return text + image
    elif audio_id:
        return text+audio
    else:
        return
def type_write(text, id):
    output = """ <p id="{id}"></p> <script> const text = "{text}"; const speed = 100; let index = 0; const {id} = document.getElementById("{id}"); function type() {{ if (index < text.length) {{ {id}.innerHTML += text.charAt(index); index++; setTimeout(type, speed); }} }} type(); </script> """.format(id=id,text=text)
    
    return output


def type_write(texts):
    num_instances = len(texts) 
    code_segments = []
    for i in range(1, num_instances + 1):
      code_segments.append(f"<p id=\'abc{i}\'></p>")
    code_segments.append("<script>")
    for i in range(1, num_instances + 1):
        code_segment = f''' const text{i} = \"{texts[i-1]}\"; const speed{i} = 25; let index{i} = 0; const abc{i} = document.getElementById(\"abc{i}\"); function type{i}() {{ if (index{i} < text{i}.length) {{ abc{i}.innerHTML += text{i}.charAt(index{i}); index{i}++; setTimeout(type{i}, speed{i}); }} else {{ setTimeout(() =>type{i+1}(), 1000); }} }} '''
    
        code_segments.append(code_segment)
    
    code_segments.append("type1();")
    code_segments.append("</script>")
    generated_code = '\n'.join(code_segments)
 
    return generated_code