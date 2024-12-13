import re

def timestampToSeconds(timestamp):
    hours, minutes, seconds = timestamp.split(":")
    seconds = int(seconds)
    seconds += 60 * int(minutes) + (60*60*int(hours))
    return seconds
    
    
def secondsToTimestamp(seconds):
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





with open("raw_captions.txt", "r") as file:
    testInput = "".join(file.readlines())



timestampRE = "\d\d\:\d\d\:\d\d"

timestamps = re.findall(timestampRE, testInput)
print(f"{timestamps=}")
splitText = re.split(timestampRE, testInput)
print(f"{splitText}")


fixedText = ""
for i, timestamp in enumerate(timestamps):
    fixedText += splitText[i]
    fixedText += secondsToTimestamp(timestampToSeconds(timestamp) + 25)
fixedText += splitText[-1]

print(f"{fixedText=}")

with open("PK.srt", "w") as file:
    file.write(fixedText)
    

