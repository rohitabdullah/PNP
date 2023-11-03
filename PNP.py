import requests
import json
import tqdm
import os

#logo 
logo=(""
`7MM"""Mq.`7MN.   `7MF'`7MM"""Mq. 
  MM   `MM. MMN.    M    MM   `MM.
  MM   ,M9  M YMb   M    MM   ,M9 
  MMmmdM9   M  `MN. M    MMmmdM9  
  MM        M   `MM.M    MM       
  MM        M     YMM    MM       
.JMML.    .JML.    YM  .JMML."")

def clear():
  os.system('clear')
print(logo)
print(42*'-')
print("▌│█║▌║▌║ 𝚁.𝙰 𝙶𝚛𝚘𝚞𝚙. ║▌║▌║█│▌")
print(42*'-')

#uid check
def is_public_uid(uid):
  response = requests.get(
      "https://graph.facebook.com/v13.0/{}/fields=is_public".format(uid))
  json_response = response.json()
  is_public = json_response["is_public"]
  return is_public

# Clear the console.
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Get the path to the text file.
text_file_path = input("Enter the path to the text file: ")

# Get the path where to save the public UIDs.
public_uids_file_path = input("Enter the path where to save the public UIDs: ")

# Create a list to store the public UIDs.
public_uids = []

# Iterate over the lines in the text file and check if each UID is public.
with open(text_file_path) as text_file:
  for line in text_file:
    uid = line.strip()
    is_public = is_public_uid(uid)

    # Print the UID and indicate whether it is public or not public.
    if is_public:
      print(f"{uid} is public.")
      public_uids.append(uid)
    else:
      print(f"{uid} is not public.")

# Save the public UIDs to a file.
with open(public_uids_file_path, "w") as public_uids_file:
  for uid in public_uids:
    public_uids_file.write(uid + "\n")

# If there are no public UIDs, print a message to the user.
if len(public_uids) == 0:
  print("Sorry man!! None of the uids was public.. try another file")
else:
  print("The public UIDs have been saved to the file '{}'.".format(public_uids_file_path))
