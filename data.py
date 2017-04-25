import ntpath
import shutil
import os
import urllib3

# The path root
path_root = 'data/'


# get_data(url): Downloads a file given its URL if the file does not already exist locally.
def get_data(url):
    # Extract the file base name from the URL, and use that to determine the path to any existing file.
    # Does the file not already exist?
    path = '{}{}'.format(path_root, ntpath.basename(url))
    if not os.path.exists(path):

        # The file does not already exist. Request the file using the URL.  Raise an exception if the
        # file was not found.
        my_request = urllib3.PoolManager().request('GET', url, retries=False, preload_content=False)
        if my_request.status != 200:
            raise FileNotFoundError

        # The file was found. Read it into local system.
        with my_request as r, open(path, 'wb') as out_file:
            shutil.copyfileobj(r, out_file)
    return


# remove_data(file): Removes an existing file resource given a name.
def remove_data(file):
    # Determine the path to any existing file. Does the file exist?
    path = '{}{}'.format(path_root, file)
    if os.path.exists(path):
        # The file exists. Remove it.
        os.remove(path)
    return
