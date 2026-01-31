import os
import shutil
import re

source_folder = "source_files"  
image_folder = "images_moved"
os.makedirs(image_folder, exist_ok=True)

print("Moving image files...")
for file_name in os.listdir(source_folder):
    if file_name.endswith(".jpg") or file_name.endswith(".png"):
        shutil.move(os.path.join(source_folder, file_name),
                    os.path.join(image_folder, file_name))
        print(f"Moved: {file_name}")
print("Image files moved successfully.\n")

text_file = os.path.join(source_folder, "emails.txt") 
output_file = "extracted_emails.txt"

if os.path.exists(text_file):
    with open(text_file, "r") as file:
        content = file.read()

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", content)

    with open(output_file, "w") as file:
        for email in emails:
            file.write(email + "\n")

    print(f"Extracted {len(emails)} emails to {output_file}")
else:
    print("emails.txt not found in source_files folder")
