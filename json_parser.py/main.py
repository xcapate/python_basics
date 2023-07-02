
import json


def eval_content(content):
    for item in content:
        if isinstance(content[item], dict):
            content[item] = eval_content(content[item])
        elif isinstance(content[item], list):
            temp_list =[];
            for element in content[item]:
                temp_list.append("Get the value for " + element.replace("//","->"))
            content[item]=temp_list
        else:
            content[item] = "get the value of this"
    return content

def parse_content(content):
    json_contents = json.loads(content)

    mapped_data = eval_content(json_contents["mappings"])
    print(mapped_data)
    

    
    

try:
    f= open('payload_briefbox_test.json')
except FileNotFoundError:
    print('File doesn\'t exit')
except Exception:
    print('Undefined variable...')
else:
    content=f.read()
    parse_content(content)
finally:
    print("Closing the file")
    try:
        f.close()
    except NameError:
        print("No need to close the file...")

