"""Main module."""
import data_preprocessing
import yaml


# variables_model
VARIABLES = ["case_study", "days"]
CONFIG_FILE = "local_config.yml"
T = 168


# Load config file with the paths
with open(CONFIG_FILE, "r") as in_file:
    config = yaml.safe_load(in_file)


Xtra, Ytra, Xval, Yval, Xtest, Ytest = data_preprocessing.data_preprocessing(
    VARIABLES, config, lookback=T
)
print(Xtra.shape)
print(Ytra.shape)
print(Xval.shape)
print(Yval.shape)
print(Xtest.shape)
print(Ytest.shape)
