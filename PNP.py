import PIL.Image
import requests
import json
import tqdm
import os
import shutil

def is_public_uid(uid, access_token):
    response = requests.get(
        f"https://graph.facebook.com/v13.0/{uid}?fields=is_public",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    json_response = response.json()
    return json_response["is_public"] if "is_public" in json_response else False

def get_image_from_url(image_url):
    response = requests.get(image_url)
    return PIL.Image.open(response.content)

# Display the banner text file.
banner_text_file = open("bs.txt", "r")
banner_text = banner_text_file.read()
print(banner_text)
banner_text_file.close()

# Prompt the user to enter their access token.
access_token = input("Enter your Facebook access token: ")

# Check if the access token is active.
if not is_access_token_active(access_token):
    print("Your access token is not active. Please check your access token at https://developers.facebook.com/tools/explorer/.")
    print("To generate a new access token, please visit https://developers.facebook.com/apps/.")
    exit()

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
        is_public = is_public_uid(uid, access_token)

        if is_public:
            public_uids.append(uid)
        else:
            print(f"{uid} is not public.")

# Save the public UIDs to a file.
with open(public_uids_file_path, "w") as public_uids_file:
    for uid in public_uids:
        public_uids_file.write(uid + "\n")

# If there are no public UIDs, print a message to the user.
if not public_uids:
    print("Sorry man!! None of the uids was public.. try another file")
else:
    print(f"The public UIDs have been saved to the file '{public_uids_file_path}'.")

# Ask the user if they want to follow me on GitHub.
follow_on_github = input("Do you want to follow me on GitHub? (Y/N): ")

if follow_on_github.lower() == "y":
    webbrowser.open("https://github.com/rohitabdullah")
    print("Thanks for following me on GitHub!")
else:
    print("No worries. Thanks for using my tool!")
