

file_name = "fruits.txt"

lines = ["apple","dates","banana","cherry"]

data = {
    "name":"steve",
    "city":"coimbatore"
}

    
def write_list_values(file_name, lines ):
    
    with open(file_name ,'w') as file:
        for line in lines:
            file.write(line+ "\n")
            
def write_dict_data(file_name, data):
    with open(file_name ,'w') as file:
        for key, value in data.items():
            # file.write(line+ "\n")
            file.write(f"{key}:{value} \n")
    
    
write_dict_data(file_name, data)
    