import requests
import json

def is_public_uid(uid):
  """Checks if a Facebook UID is public.

  Args:
    uid: The Facebook UID to check.

  Returns:
    True if the Facebook UID is public, False otherwise.
  """

  # Make a GET request to the Facebook Graph API.
  response = requests.get(
      "https://graph.facebook.com/v13.0/{}/fields=is_public".format(uid))

  # Check the response status code.
  if response.status_code == 200:
    # The response is successful.
    json_response = response.json()

    # Check the is_public field.
    is_public = json_response["is_public"]

    return is_public
  else:
    # The response was not successful.
    return False

# Get the path to the text file.
text_file_path = input("Enter the path to the text file: ")

# Get the name of the output file.
output_file_name = input("Enter the name of the output file: ")

# Create a list to store the public UIDs.
public_uids = []

# Read the text file line by line.
with open(text_file_path, "r") as text_file:
  for line in text_file:
    uid = line.strip()

    # Check if the UID is public.
    is_public = is_public_uid(uid)

    # If the UID is public, add it to the list.
    if is_public:
      public_uids.append(uid)

# Write the public UIDs to the output file.
with open(output_file_name, "w") as output_file:
  for uid in public_uids:
    output_file.write(uid + "\n")

# Print a message to the user.
print(f"The public UIDs have been saved to the file '{output_file_name}'.")
