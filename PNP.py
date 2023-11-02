import sys

def main():

  with open("banner.txt", "r") as banner_file:
    banner_text = banner_file.read()

  print(banner_text)

import requests
import json


def is_public_uid(uid):
  """Checks if a Facebook UID is public.

  Args:
    uid: The Facebook UID to check.

  Returns:
    True if the Facebook UID is public, False otherwise.
  """


  response = requests.get(
      "https://graph.facebook.com/v13.0/{}/fields=is_public".format(uid))

 
  if response.status_code == 200:
    
    json_response = response.json()

    
    is_public = json_response["is_public"]

    return is_public
  else:
    
    return False


text_file_path = input("Enter the path to the text file: ")


public_uids = []


with open(text_file_path, "r") as text_file:
  for line in text_file:
    uid = line.strip()

    
    is_public = is_public_uid(uid)

    
    if is_public:
      public_uids.append(uid)


with open("public_uids.txt", "w") as public_uids_file:
  for uid in public_uids:
    public_uids_file.write(uid + "\n")


print("The public UIDs have been saved to the file 'public_uids.txt'.")
