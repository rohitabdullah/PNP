import webbrowser
import requests
import json
import tqdm
import os

def is_public_uid(uid):
  response = requests.get(
      "https://graph.facebook.com/v13.0/{}/fields=is_public".format(uid))
  json_response = response.json()
  is_public = json_response["is_public"]
  return is_public

#  GitHub profile
webbrowser.open("https://github.com/rohitabdullah")

# Clear 
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Read the banner.
banner_file_path = "bs.txt"
with open(banner_file_path, "r") as banner_file:
  banner_text = banner_file.read()

# banner
print(banner_text)

# Get the path
text_file_path = input("Enter the path to the text file: ")

# where to save
public_uids_file_path = input("Enter the path where to save the public UIDs: ")

# store 
public_uids = []

# Iterate
with open(text_file_path) as text_file:
  for line in text_file:
    uid = line.strip()
    is_public = is_public_uid(uid)

    # Print public or not public.
    if is_public:
      print(f"{uid} is public.")
      public_uids.append(uid)
    else:
      print(f"{uid} is not public.")

# Save UIDs
with open(public_uids_file_path, "w") as public_uids_file:
  for uid in public_uids:
    public_uids_file.write(uid + "\n")

# no public UIDs
if len(public_uids) == 0:
  print("Sorry man!! None of the uids was public.. try another file")
else:
  print("The public UIDs have been saved to the file '{}'.".format(public_uids_file_path))
