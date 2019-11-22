dict1={1:"usama",2:"Ali",3:"usama",4:"zara",5:"Ali"}
dict2={}
for key, value in dict1.items():
    dict2.setdefault(value, set()).add(key)
list1=[values for key, values in dict2.items() if len(values) > 1]
print("Duplicate keys are:" ,list1)
    
