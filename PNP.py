import os
import requests
import json
import tqdm
import os
import shutil
import webbrowser
import textwrap

def is_access_token_active():
    response = requests.get(
        "https://graph.facebook.com/v13.0/me"
    )
    json_response = response.json()

    if "error" in json_response:
        return False
    else:
        return True

# Get the banner text from the bs.txt file in the repository.
banner_text = requests.get("https://raw.githubusercontent.com/rohitabdullah/pnp/main/bs.txt").text

# Calculate the center of the terminal.
terminal_width = shutil.get_terminal_size()[0]
terminal_height = shutil.get_terminal_size()[1]
center_x = terminal_width // 2
center_y = terminal_height // 2

# Wrap the banner text to fit the terminal width.
banner_text_wrapped = textwrap.fill(banner_text, terminal_width)

# Print the banner text centered in the terminal.
for line in banner_text_wrapped.splitlines():
    print(f"{' ' * center_x}{line}")

# Ask the user if they have an access token.
has_access_token = input("Do you have an access token? (Y/N): ")

if has_access_token.lower() == "y":

    # Check if the access token is active.
    if not is_access_token_active():
        print("Your access token is not active. Please generate a new access token at https://developers.facebook.com/tools/explorer/.")
        exit()

else:

    # Provide the user with a link to generate an access token.
    print("Please generate an access token at https://developers.facebook.com/tools/explorer/.")
    exit()

# Get the path to the text file containing the UIDs.
text_file_path = input("Enter the path to the text file: ")

# Get the path where to save the public UIDs.
public_uids_file_path = input("Enter the path where to save the public UIDs: ")

# Create a list to store the public UIDs.
public_uids = []

# Iterate over the lines in the text file and check if each UID is public.
with open(text_file_path, "r") as text_file:
    for line in tqdm.tqdm(text_file):
        uid = line.strip()
        is_public = is_public_uid()

        if is_public:
            public_uids.append(uid)

# Save the public UIDs to a file.
with open(public_uids_file_path, "w") as public_uids_file:
    for uid in public_uids:
        public_uids_file.write(uid + "\n")

# Inform the user that the public UIDs have been saved.
print("The public UIDs have been saved to the file '{}'.".format(public_uids_file_path))

# Ask the user if they want to follow you on GitHub.
follow_on_github = input("Do you want to follow me on GitHub? (Y/N): ")

if follow_on_github.lower() == "y":
    os.system("open https://github.com/rohitabdullah")
    print("Thanks for following me on GitHub!")
else:
    print("Thank you for using this tool!")

