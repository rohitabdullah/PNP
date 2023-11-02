import sys
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

def main():

  with open("banner.txt", "r") as banner_file:
    banner_text = banner_file.read()


  print(banner_text)


  text_file_path = input("Where is the file?: ")

  destination_file_path = input("Where to save the file?: ")


  public_uids = []


  with open(text_file_path, "r") as text_file:
    for line in text_file:
      uid = line.strip()

      is_public = is_public_uid(uid)

      if is_public:
        public_uids.append(uid)

  with open(destination_file_path, "w") as destination_file:
    for uid in public_uids:
      destination_file.write(uid + "\n")

  print("The public UIDs have been saved to the file '{}'.".format(destination_file_path))

if __name__ == "__main__":
  main()
