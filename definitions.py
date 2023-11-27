import json


def load_json():
    f = open('data.json')
    d = json.load(f)
    f.close()
    return d
    

def get_data(id:int=0):
    d = load_json()
    if id != 0:
        return [e for e in d if e["id"] == id]
    else:
        return d


def find_first_free_id():
    d = load_json()
    existing_ids = [item["id"] for item in d]
    free_id = next(i for i in range(1, max(existing_ids) + 2) if i not in existing_ids)
    return free_id

def insert_user(d:dict):
    id = find_first_free_id()
    l = load_json()
    d["id"]=id
    l.append(d)
    with open("data.json", 'w') as json_file:
        json.dump(l, json_file, 
        indent=4,  
        separators=(',',': ')) 
    
   
def remove_user(id:int):
    l = load_json()
    a=[e for e in l if e["id"] == id][0]
    l.remove(a)
    with open("data.json", 'w') as json_file:
        json.dump(l, json_file, 
        indent=4,  
        separators=(',',': '))

def patch_user(id:int,insert_data:dict):
    l=load_json()
    a=[e for e in l if e["id"] == id][0]
    l[l.index(a)].update(insert_data)
    with open("data.json", 'w') as json_file:
        json.dump(l, json_file, 
        indent=4,  
        separators=(',',': '))
