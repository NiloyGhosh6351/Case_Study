import json
import os 
from pprint import pprint
formattedDirectoryPath = "./formattedData"
if not os.path.exists(formattedDirectoryPath):
    os.makedirs(formattedDirectoryPath)

totalFile=os.listdir('./data')
totalFormatted=[]
for fileName in totalFile:
    file=open('data/'+fileName)
    data=json.load(file)

    formated_String={ "dataset_name":fileName,
            "image_link": "",
            "annotation_type": "image",
            "annotation_objects": {
                "vehicle": {
                    "presence": 0,
                    "bbox": []
                },
                "license_plate": {
                    "presence": 0,
                    "bbox": []
                }
            },
            "annotation_attributes": {
                "vehicle": {
                    "Type": None,
                    "Pose": None,
                    "Model": None,
                    "Make": None,
                    "Color": None
                },
                "license_plate": {
                    "Difficulty Score": None,
                    "Value": None,
                    "Occlusion": None
                }
            }}
    if len(data['objects'])>0:
        for j in range(2):
            for i in data['objects'][0]['points']['exterior'][j]:
                formated_String['annotation_objects']['vehicle']['bbox'].append(i)
        for i in data['objects'][0]['tags']:
            formated_String['annotation_attributes']['vehicle'][i['name']]=i['value']
    
    if len(data['objects'])>1:
        for j in range(2):
            for i in data['objects'][1]['points']['exterior'][j]:
                formated_String['annotation_objects']['license_plate']['bbox'].append(i)
        for i in data['objects'][1]['tags']:
            formated_String['annotation_attributes']['license_plate'][i['name']]=i['value']
    vehicleFlag=False
    licensePlateFlag=False
    for i in data['objects']:
        if i['classTitle']=='Vehicle':
            vehicleFlag=True
        if i['classTitle']=='License Plate':
            licensePlateFlag=True
    if vehicleFlag:
        formated_String['annotation_objects']['vehicle']['presence']=1
    if licensePlateFlag:
        formated_String['annotation_objects']['license_plate']['presence']=1
    file_path = os.path.join(formattedDirectoryPath, 'formatted_'+fileName)
    with open(file_path, "w") as file:
        json.dump(formated_String,file)
    #totalFormatted.append(formated_String)