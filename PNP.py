import os
import requests
import textwrap
import shutil
import webbrowser
import tqdm

def is_access_token_active(access_token):
    response = requests.get(
        f"https://graph.facebook.com/v13.0/me?access_token={access_token}"
    )
    json_response = response.json()

    if "error" in json_response:
        return False
    else:
        return True

# Function to check if a UID is public. You need to implement the actual logic.
def is_public_uid(uid, access_token):
    # Replace this with the actual logic to check if a UID is public.
    pass

def main():
    # Get the banner text from the "bs.txt" file.
    with open("bs.txt", "r") as banner_file:
        banner_text = banner_file.read()

    # Calculate the center of the terminal.
    terminal_width = shutil.get_terminal_size().columns
    center_x = terminal_width // 2

    # Wrap the banner text to fit the terminal width.
    banner_text_wrapped = textwrap.fill(banner_text, terminal_width)

    # Print the banner text centered in the terminal.
    for line in banner_text_wrapped.splitlines():
        print(f"{' ' * center_x}{line}")

    # Ask the user for their access token.
    access_token = input("Enter your access token: ")

    # Check if the access token is active.
    if not is_access_token_active(access_token):
        print("Your access token is not active. Please generate a new access token at https://developers.facebook.com/tools/explorer/")
        exit()

    # Prompt the user for the path to the text file containing UIDs.
    text_file_path = input("Enter the path to the text file: ")

    # Prompt the user for the path to save the public UIDs.
    public_uids_file_path = input("Enter the path where to save the public UIDs: ")

    # Create a list to store the public UIDs.
    public_uids = []

    # Iterate over the lines in the text file and check if each UID is public.
    with open(text_file_path, "r") as text_file:
        for line in tqdm.tqdm(text_file):
            uid = line.strip()
            is_public = is_public_uid(uid, access_token)  # You need to implement this function.

            if is_public:
                public_uids.append(uid)

    # Save the public UIDs to a file.
    with open(public_uids_file_path, "w") as public_uids_file:
        for uid in public_uids:
            public_uids_file.write(uid + "\n")

    # Inform the user that the public UIDs have been saved.
    print(f"The public UIDs have been saved to the file '{public_uids_file_path}'.")

    # Ask the user if they want to follow the author on GitHub.
    follow_on_github = input("Do you want to follow the author on GitHub? (Y/N): ")

    if follow_on_github.lower() == "y":
        webbrowser.open("https://github.com/rohitabdullah")
        print("Thanks for following the author on GitHub!")
    else:
        print("Thank you for using this tool!")

if __name__ == "__main__":
    main()
