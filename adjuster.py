import re

def timestampToSeconds(timestamp):
    hours, minutes, seconds = timestamp.split(":")
    seconds = int(seconds)
    seconds += 60 * int(minutes) + (60*60*int(hours))
    return seconds
    
    
def secondsToTimestamp(seconds):
    seconds = max(int(seconds), 0)
    
    hours = seconds // (60*60)
    seconds = seconds % (60*60)
    minutes = seconds // (60)
    seconds = seconds % 60
    
    hours = str(hours)
    minutes = str(minutes)
    seconds = str(seconds)
    
    while len(hours) < 2: 
        hours = "0" + hours
    while len(minutes) < 2: 
        minutes = "0" + minutes
    while len(seconds) < 2: 
        seconds = "0" + seconds
    
    return f"{hours}:{minutes}:{seconds}"


assert timestampToSeconds("01:00:00") == 60*60
assert timestampToSeconds("00:01:00") == 60
assert timestampToSeconds("00:00:23") == 23

assert secondsToTimestamp(23) == "00:00:23"
assert secondsToTimestamp(60) == "00:01:00"
assert secondsToTimestamp(60*60+12) == "01:00:12"


input_filepath = input("INPUT FILEPATH: Please enter the filepath of the .srt file you'd like to offset: ").strip('"')



with open(input_filepath, "r") as file:
    testInput = "".join(file.readlines())

timestampRE = "\d\d\:\d\d\:\d\d"

timestamps = re.findall(timestampRE, testInput)
splitText = re.split(timestampRE, testInput)

print("Input Successful")

offset = int(input("OFFSET: Please enter the number of seconds you'd like to offset the .srt file: "))

fixedText = ""
for i, timestamp in enumerate(timestamps):
    fixedText += splitText[i]
    fixedText += secondsToTimestamp(timestampToSeconds(timestamp) + offset)
fixedText += splitText[-1]

print("Process Complete.")
output_filepath = input("OUTPUT FILEPATH: Please enter the filepath of the .srt file you'd like to output to: ").strip('"')
with open(output_filepath, "w") as file:
    file.write(fixedText)

print("Output Successful.")

