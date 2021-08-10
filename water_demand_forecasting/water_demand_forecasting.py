"""Main module."""
import data_preprocessing
import yaml


# variables_model
VARIABLES = ["case_study", "days"]
CONFIG_FILE = r"C:\Users\dcorr\Source\Repos\water_demand_forecasting\water_demand_forecasting\local_config.yml"
T = 168


# Load config file with the paths
with open(CONFIG_FILE, "r") as in_file:
    config = yaml.safe_load(in_file)


Xtra, Ytra, Xval, Yval, Xtest, Ytest, scx, scy = data_preprocessing.data_preprocessing(
    VARIABLES, config, lookback=T
)
print(Xtra.shape)
print(Ytra.shape)
print(Xval.shape)
print(Yval.shape)
print(Xtest.shape)
print(Ytest.shape)
