import utils.data as u_data
import utils.shared_utils as utils
import os

def getPersonsFeatures():
    return utils.load_csv_file(u_data.persons_directory+"persons.csv")

if __name__ == "__main__":
    persons_features = getPersonsFeatures()
    print(type(persons_features))
    if type(persons_features) == list:
      print(persons_features[0])
