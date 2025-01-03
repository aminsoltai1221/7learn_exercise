import xmltodict
import json


class Adapter:
    def __init__(self):
        pass 
    
    def XMLtoJSON(self, file):
        dictionary = self.readXML(file)
        json_string = json.dumps(dictionary, indent=4)
        return json_string
    
    def readXML(self, file):
        with open(file=file, mode="r") as f:
            data = xmltodict.parse(f.read())
            return data




# مثال استفاده:
adapter = Adapter()
file_path = "example.xml"  # مسیر فایل XML
json_output = adapter.XMLtoJSON(file_path)
print(json_output)
