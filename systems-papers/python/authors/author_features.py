import utils.data as u_data
import utils.shared_utils as utils
import os

def getAllAuthorFeatures():
    return utils.load_csv_file(u_data.features_directory+"authors.csv")

def getAuthorUName(author, features):
    return utils.author_uname(author, features)

# does full pass through data/conf
def getAllAuthorsAttribute(attr):
    conf_filenames = u_data.getConferenceFilenames()
    values = {}
    for conf_filename in conf_filenames:
        authors = u_data.getAuthors(conf_filename)
        for a_name, a_data in authors.items():
            if isinstance(a_data, str) or not attr in a_data: continue
            val = a_data[attr]
            # update existing entry
            if a_name in values: values[a_name] = max(values[a_name],val)
            # add entry
            else: values[a_name] = val
    return values