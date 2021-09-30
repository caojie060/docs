## YAML转JSON

> 使用yaml模块中的load函数将yaml转换为dict格式
> 使用json模块中的dumps函数将dict转换为json格式

```python
import json,yaml


test_file = open(test_yaml_file,"r")
#先将yaml转换为dict格式
generate_dict = yaml.load(test_file,Loader=yaml.FullLoader)
generate_json = json.dumps(generate_dict,sort_keys=False,indent=4,separators=(',',': '))
print(generate_json)
```



## JSON转YAML

> 使用json模块中的loads模块将json转换为dict
> 使用yaml模块中的dump函数将dict转换为yaml格式

```python
import yaml,json


test_file = open(test_json_file,"r")
test_json = json.loads(test_file)
test_dict = test_json
test_yaml = yaml.dump(test_dict)
#或者直接转换为文件
new_yaml_file = open("new_file","w")
yaml.safe_dump(test_dict,stream=new_yaml_file,default_flow_style=False)
```

