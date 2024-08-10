import ollama
from time import sleep
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
# 'content': 'Describe thoroughly of the image.',

llavastatement = response['message']['content']
theprompt = r'''
From this short story: 

'''+llavastatement+r''' 



Make a title for this short story. Just write the title, don't recommend me anything.
'''
# Extract as many keywords from the passage, separated by commas. Do not write in bullet points

# print('\n\n',theprompt)





# response2 = ollama.generate(model='gemma2:2b', prompt = theprompt)



# print('\n\n','====================\n', response2['response'], '====================\n')
clear_terminal()
print(llavastatement)
print('\n=========== THE END ===========')