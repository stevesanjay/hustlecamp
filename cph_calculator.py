'''
Created on 

@author: Raja CSP Raman

source:
    

business:
CPH Calculator

CPH - Collection Per Hour

Sample:
s: 06:48
e: 07:03
c: 112

s - started
e - ended
c - collected

CPH:
	took 15 minutes to collect 112 items

	1m = 112/15 = 7.466666667
	60m = 7.466666667 * 60 = 448

	Per Hour = Collected_items_count * 60 / minutes_taken

source:
    https://pythonspot.com/read-file/
'''
from datetime import datetime


# import pdb


#def get_cph(input_text):
def calculate_time_difference(start_time, end_time):

    fmt     = '%H:%M'
    start   = datetime.strptime(start_time, fmt)
    end     = datetime.strptime(end_time, fmt)
    difference = end - start
    
    return difference.total_seconds() / 60  # Convert to minutes

def calculate_output(input_data):

    lines       = input_data.split('\n')
    print(f"lines : {lines}")
    # print(type(lines))

    print(f"lines(0) : {lines[0]}")

    start_time  = lines[0].split(': ')[1]

    end_time    = lines[1].split(': ')[1]
    collected_items_count       = int(lines[2].split(': ')[1])

    print(f"start_time : {start_time}")
    print(f"end_time : {end_time}")
    
    
    minutes_taken    = calculate_time_difference(start_time, end_time)
    print(f"minutes_taken : {minutes_taken}")
    output           = collected_items_count * 60 / minutes_taken

    return int(output)

def read_custom_file():
    f = open("data.txt", "r")
    line = f.read()
    print(line)

    return line

def startpy():

    # print("Tact101")

    # Sample input
#     sample_input = """s: 06:18
# e: 07:03
# c: 712
# """

    sample_input = read_custom_file()

    print("Output:", calculate_output(sample_input))
        

if __name__ == '__main__':
    startpy()