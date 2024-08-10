import ollama
from filesIngest import filesIngest
from raw import convert2raw






def clear_terminal():
    """
    Clears the terminal screen.

    This function uses the `os` module to determine the operating system and
    then uses the appropriate command to clear the screen.

    Parameters:
    None

    Returns:
    None
    """
    # Check the operating system
    import os
    os_name = os.name

    # Clear the screen based on the operating system
    if os_name == 'posix':
        # Unix/Linux/MacOS/BSD/etc.
        os.system('clear')
    elif os_name == 'nt':
        # Windows
        os.system('cls')
    else:
        # Fallback for other operating systems
        print('\n' * 100)

clear_terminal()

selectFiles = filesIngest.select_files()
getFiles = filesIngest.getFileList()
getFiles = [convert2raw(filepath) for filepath in getFiles]

for file in getFiles:
  response = ollama.chat(model='llava:13b', messages=[
    {
      'role': 'user',
      'content': 'From the image, write twenty (20) keywords present in this photo, separated by commas.',
      'images': [file],
    },
  ])

  llavastatement = response['message']['content']

  print('\n=========== '+ file +' ===========')
  print(llavastatement)