import os
import json


def get_file(file_name, access='r'):
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


# write the 'contents' to the file_name as json
def write_database(file_name, contents):

    handle = get_file(file_name, 'w')

    json.dump(contents, handle)

    handle.close()

    return True



