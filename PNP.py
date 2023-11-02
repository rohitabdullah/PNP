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


import os
os.system('cls' if os.name == 'nt' else 'clear')


with open("banner.txt", "r") as banner_file:
  banner_text = banner_file.read()


print(banner_text)


text_file_path = input("Where is the text file (path): ")


public_uids_file_path = input("Where to save the public UIDs (path): ")


public_uids = []


with open(text_file_path) as text_file:
  for line in text_file:
    uid = line.strip()
    is_public = is_public_uid(uid)


    if is_public:
      print(f"{uid} is public.")
      public_uids.append(uid)
    else:
      print(f"{uid} is not public.")


with open(public_uids_file_path, "w") as public_uids_file:
  for uid in public_uids:
    public_uids_file.write(uid + "\n")


if len(public_uids) == 0:
  print("Sorry man!! None of the UIDs were public.. Try another file")
else:
  print("The public UIDs have been saved to the file '{}'.".format(public_uids_file_path))
