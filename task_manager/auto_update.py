import os
import time
import shutil

# Directory where the project files are located
target_directory = "/Users/sebastienkneppert/Downloads/TASK_MANAGER_PROJECT/task_manager"
# Directory where downloaded files are placed
downloads_directory = "/Users/sebastienkneppert/Downloads"

# List of project files to monitor and update automatically
FILES_TO_MONITOR = [
    "display_helpers.py",
    "main.py",
    "progress_tracking.py"
]

def update_files():
    updated = False
    for filename in FILES_TO_MONITOR:
        source_file = os.path.join(downloads_directory, filename)
        target_file = os.path.join(target_directory, filename)

        # If a new version of the file exists in the /Downloads folder, copy it to the project directory
        if os.path.exists(source_file):
            # Update the target file if it's different from the source file
            if not os.path.exists(target_file) or open(source_file).read() != open(target_file).read():
                shutil.copy2(source_file, target_file)
                print(f"{filename} has been updated in the project directory.")
                updated = True

            # Remove the downloaded file after updating the project
            os.remove(source_file)

    return updated

def auto_update(interval=30):
    try:
        while True:
            print("Checking for updates in the /Downloads folder...")
            if update_files():
                print("Project files have been updated.")
            else:
                print("No updates detected.")
            print("Waiting for the next check...")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Auto-update stopped manually.")

if __name__ == "__main__":
    auto_update(30)
