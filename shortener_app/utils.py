import os
import json

# open the file with the specified access and return the handle if the file exists
# return None if it doesn't
def get_file(file_name, access='r'):
    handle = None
    if os.path.isfile(file_name):
        # exists
        handle = open(file_name,access)

    return handle


# get the contents of the json database file, returning it if found, else
# return None
def get_database(file_name):

    handle = get_file(file_name, 'r')

    db = None

    try:

        db = json.load(handle)

    except json.decoder.JSONDecodeError as err:

        db = {}

    handle.close()

    return db


# write the 'contents' to the file_name as json, overwrite the file
def write_database(file_name, contents):

    handle = get_file(file_name, 'w')

    json.dump(contents, handle)

    handle.close()

    return True



