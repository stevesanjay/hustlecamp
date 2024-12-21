

file_path = "word.txt"
# print(file_path)

try:
    with open(file_path ,'r') as file:
        result = file.read()
        print(result)
    # for line in file:
    #     print(line.strip())
            
            
except FileNotFoundError:
    print("file name is wrong ")
        
    