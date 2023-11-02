import requests
import json
import tqdm

def is_public_uid(uid):
  response = requests.get("https://graph.facebook.com/v13.0/{}/fields=is_public".format(uid))
  json_response = response.json()
  is_public = json_response["is_public"]
  return is_public

text_file_path = input("Enter the path to the text file: ")
public_uids_file_path = input("Enter the path where to save the public UIDs: ")
banner_text = open("banner.txt").read()
print(banner_text)
public_uids = []
progress_bar = tqdm.tqdm(total=len(open(text_file_path).readlines()))
with open(text_file_path) as text_file:
  for line in text_file:
    uid = line.strip()
    is_public = is_public_uid(uid)
    if is_public:
      public_uids.append(uid)
    progress_bar.update(1)
progress_bar.close()
with open(public_uids_file_path, "w") as public_uids_file:
  for uid in public_uids:
    public_uids_file.write(uid + "\n")
print("The public UIDs have been saved to the file '{}'.".format(public_uids_file_path))
