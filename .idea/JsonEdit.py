import json

json_path = 'D:/00.MIGRATION/01.JsonEditTest/test2.json'

with open(json_path,'r',encoding='utf-8') as json_file:
    json_data = json.load(json_file)

    for patient_item in json_data["data"]:
        if patient_item['workspaceId'] in ['ef9966c2b5c911ea900651b8a822af09']:
            patient_item['id'] = "__CENACLE__환자" + str(patient_item['chartNumber'])




with open('D:/00.MIGRATION/01.JsonEditTest/test6.json','w',encoding='utf-8') as json_write:
    json.dump(json_data, json_write, indent=2)

print(json_data)
    # print(jsonData[workspaceId])
