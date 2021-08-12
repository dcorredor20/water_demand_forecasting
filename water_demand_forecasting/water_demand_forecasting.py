"""Main module."""
from data_preprocessing import Model
from config_files.load_config_file import load_config_file
import yaml


# variables_model
VARIABLES = ["case_study", "days"]
config = load_config_file(r"local_config.yml")
T = 168


Xtra, Ytra, Xval, Yval, Xtest, Ytest, scx, scy = Model.data_preprocessing(
    VARIABLES, config, lookback=T
)
print(Xtra.shape)
print(Ytra.shape)
print(Xval.shape)
print(Yval.shape)
print(Xtest.shape)
print(Ytest.shape)
