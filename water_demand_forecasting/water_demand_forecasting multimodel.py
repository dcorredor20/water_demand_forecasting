"""Main module."""
from wdf_model import WDF_Model
from config_files.load_config_file import load_config_file
import yaml


# variables_model
VARIABLES = ["case_study", "days"]
config = load_config_file(r"local_config.yml")
T = 168

case_studies = dict()
case_studies[2] = {
    "train": r"C:\Users\dcorr\Desktop\TU thesis\DataThesis\DATI\Ferrara\Qh_CS2_14.txt",
    "test": r"C:\Users\dcorr\Desktop\TU thesis\DataThesis\DATI\Ferrara\Qh_CS2_15.txt",
}
case_studies[3] = {
    "train": r"C:\Users\dcorr\Desktop\TU thesis\DataThesis\DATI\Ferrara\Qh_CS3_14.txt",
    "test": r"C:\Users\dcorr\Desktop\TU thesis\DataThesis\DATI\Ferrara\Qh_CS3_15.txt",
}
case_studies[4] = {
    "train": r"C:\Users\dcorr\Desktop\TU thesis\DataThesis\DATI\Ferrara\Qh_CS4_14.txt",
    "test": r"C:\Users\dcorr\Desktop\TU thesis\DataThesis\DATI\Ferrara\Qh_CS4_15.txt",
}
case_studies[5] = {
    "train": r"C:\Users\dcorr\Desktop\TU thesis\DataThesis\DATI\Ferrara\Qh_CS5_14.txt",
    "test": r"C:\Users\dcorr\Desktop\TU thesis\DataThesis\DATI\Ferrara\Qh_CS5_15.txt",
}
case_studies[6] = {
    "train": r"C:\Users\dcorr\Desktop\TU thesis\DataThesis\DATI\Ferrara\Qh_CS6_14.txt",
    "test": r"C:\Users\dcorr\Desktop\TU thesis\DataThesis\DATI\Ferrara\Qh_CS6_15.txt",
}


for c in case_studies.keys():
    config_temp = dict()
    config_temp["case_study"] = dict()
    config_temp["days"] = dict()
    config_temp["case_study"]["train"] = case_studies[c]["train"]
    config_temp["case_study"]["test"] = case_studies[c]["test"]
    config_temp["days"] = {
        "train": r"C:\Users\dcorr\Desktop\TU thesis\DataThesis\Models\days2014.csv",
        "test": r"C:\Users\dcorr\Desktop\TU thesis\DataThesis\Models\days2015.csv",
    }
    Xtra, Ytra, Xval, Yval, Xtest, Ytest, scx, scy = WDF_Model.data_preprocessing(
        VARIABLES, config_temp, lookback=T, type_scaler="Standard"
    )
    case_studies[c]["Xtra"] = Xtra
    case_studies[c]["Ytra"] = Ytra
    case_studies[c]["Xval"] = Xval
    case_studies[c]["Yval"] = Yval
    case_studies[c]["Xtest"] = Xtest
    case_studies[c]["Ytest"] = Ytest
    case_studies[c]["scx"] = scx
    case_studies[c]["scy"] = scy
    print(Xtra.shape)
    print(Ytra.shape)
    print(Xval.shape)
    print(Yval.shape)
    print(Xtest.shape)
    print(Ytest.shape)
    print(config_temp)

print(config_temp)
