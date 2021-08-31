
import json
fobj = open(r'data.csv', 'r')
keys = ["label", "id", "link", "children"]

complete_dic = {}
parent = True
for row in fobj.readlines()[1:]:
    fchild = True
    row = row.rstrip(',\n ')
    if row.strip():
        if parent:
            dic = dict(zip(keys, row.split(',')[1:4] + [list()]))
            complete_dic.update(dic)
            parent = False
        else:
            firstchild = complete_dic["children"]
            line = row.split(',')[1:]
            i=0
            while i<len(line):
                dic = dict(zip(keys, line[i:i+3]+[list()]))
                i+=3
                if dic["id"] == complete_dic["id"]:
                    continue
                firstchild.append(dic)
                firstchild = dic.get('children')


#print(complete_dic)
json_encode = json.dumps(complete_dic)
#print(json_encode)
json_object = json.loads(json_encode)
#print(json_object)
print(json.dumps(json_object, indent = 4))
fobj.close()

