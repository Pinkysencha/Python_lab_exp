import re

#1. resplit
text = "Temp:24 Humidity:60 Pressure:1012"
print("re.split()")
sensors = "Temp, Humidity, Pressure"
split_result = re.split(",", sensors)
print(split_result)

#2. resub
sentence = "The network will upgrade from 5G soon"
print("\n=re.sub()")
sub_result = re.sub("5G", "6G", sentence)
print(sub_result)

#3. rematch
device = "IoT_4589"
print("\nre.match()")
match_result = re.match("IoT", device)
if match_result:
    print("Valid IoT Device ID")
else:
    print("Invalid Device")

#4. research
msg = "Device connected to 5G network"
print("\nre.search()")
search_result = re.search("5G", msg)
if search_result:
    print("5G Network Found")
else:
    print("Not Found")

#5. refindall
print("\nre.findall()")
findall_result = re.findall("[0-9]+", text)
print(findall_result)

#7. refinditer

words = "cat bat mat cat rat"
print("\nre.finditer()")
pattern = "cat"
matches = re.finditer(pattern, words)
for m in matches:
    print("Match:", m.group(), 
          "Start:", m.start(), 
          "End:", m.end())

#8. full match
print("\nDate Validation (DD/MM/YYYY)")
date = input("Enter date (DD/MM/YYYY): ")
pattern1 = r'^\d{2}/\d{2}/\d{4}$'
if re.fullmatch(pattern1, date):
    print("Valid Date Format")
else:
    print("Invalid Date Format")

