#This script automates the process of adding, committing, and pushing changes to a Git repository.

#The script first prints the status of the repository using the "git status" command. It then prompts the user for confirmation before proceeding. If the user chooses not to proceed, the script ends.

#Next, the script asks the user to specify which files to add to the repository. The files are entered as a space-separated list, and the script uses the "git add" command to add them.

#The script then prompts the user for a commit message, which is entered as a string. It uses the "git commit" command to commit the changes with the specified message.

#The script then asks the user for confirmation before pushing the changes to the remote repository. If the user chooses not to push, the script ends. Otherwise, it uses the "git push" command to push the changes.

#The "confirm_action" and "prompt_files" functions are helper functions that prompt the user for confirmation and file names, respectively.

#The "if name == 'main':" block ensures that the "main" function is only called when the script is run directly, and not when it is imported as a module.

import os
import subprocess

def main():
    #print status
    subprocess.run(['git', 'status'])
	
    # Ask the user for confirmation before proceeding
    if not confirm_action("Are you sure you want to add, commit, and push?"):
        return
    
    # Ask the user which files to add
    files = prompt_files("Enter the files you want to add (separated by spaces): ")
    
    # Add the specified files to the Git repository
    subprocess.run(["git", "add"] + files)
    
    # Ask the user for the commit message
    message = input("Enter a commit message: ")
    
    # Commit the changes with the specified message
    subprocess.run(["git", "commit", "-m", message])
    
    # Ask the user for confirmation before pushing
    if not confirm_action("Are you sure you want to push?"):
        return
    
    # Push the changes to the remote repository
    subprocess.run(["git", "push"])

def confirm_action(prompt):
    """Ask the user for confirmation before proceeding."""
    response = input(f"{prompt} (y/n): ")
    return response.lower() == "y"

def prompt_files(prompt):
    """Prompt the user for a list of files to add."""
    files = input(prompt)
    return files.split()

if __name__ == "__main__":
    main()
    

