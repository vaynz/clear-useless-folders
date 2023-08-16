import os

def delete_empty_folders(directory):
	for root, dirs, files in os.walk(directory, topdown=False):
		for folder in dirs:
			folder_path = os.path.join(root, folder)
			if not os.listdir(folder_path): ## Check if is not used
				print(f"Deleting empty folder: {folder_path}")
				os.rmdir(folder_path)

if __name__ == "__main__":
	target_directory = r"F:\Development\Packer - Dev\Client"
	delete_empty_folders(target_directory)
