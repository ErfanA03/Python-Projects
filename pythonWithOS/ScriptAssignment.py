import os
import time

directory_path = 'C:\\Users\\bluep\\Documents\\GitHub\\Python-Projects\\ScriptAssignment'

def main():
    # Iterate through all files in the directory
    for filename in os.listdir(directory_path):
        # Create an absolute path for the file
        file_path = os.path.join(directory_path, filename)
        # Check if the file ends with '.txt'
        if filename.lower().endswith('.txt') and os.path.isfile(file_path):
            # Get the modified timestamp of the file
            mtime = os.path.getmtime(file_path)
            # Convert the timestamp to a readable format
            modified_time = format_timestamp(mtime)
            # Print the filename and its modified timestamp
            print('File: {}, Modified Time: {}'.format(filename, modified_time))




def format_timestamp(timestamp):
    # Convert timestamp to a human-readable format
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))





if __name__ == "__main__":
    main()
