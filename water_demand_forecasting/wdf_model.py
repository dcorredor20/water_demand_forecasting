import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from typing import Dict, List, Tuple


class WDF_Model:
    """
    Class to define all the steps in for a model.

    """
    @staticmethod
    def read_datasets(
        variables: List[str], config: Dict[str, str], mode: str
    ) -> Dict[str, pd.DataFrame]:
        assert mode in ["train", "test"], "Mode not in train, test"
        dict_files = dict()
        for v in variables:
            assert v in config.keys(), "Variable not in config"
            # Read data
            dict_files[v] = pd.read_csv(config[v][mode], header=None, sep=r"\s+")
        return dict_files

    @staticmethod
    def create_sequences(
        series: np.array, lookback: int, horizon: int = 24
    ) -> Tuple[np.array, np.array]:
        """Return X and Y sequences."""
        X = []
        Y = []
        for t in range(len(series) - lookback - horizon):
            x = series[t : t + lookback]
            X.append(x)
            y = series[t + lookback : t + lookback + horizon]
            Y.append(y)

        X = np.array(X)
        Y = np.array(Y)
        return X, Y

    @staticmethod
    def build_datasets(
        variables: List[str], dict_files: Dict[str, pd.DataFrame], lookback: int,
    ) -> Tuple[np.array, np.array]:
        """Load data and return X and Y."""
        assert "case_study" in variables, "case_study must be in variables"
        X_all = list()
        for v in variables:
            # Reshape data
            if v == "case_study":
                X = dict_files[v].values.reshape(-1)
                X, Y = WDF_Model.create_sequences(X, lookback)
            else:
                X = np.array(dict_files[v])
                X, _ = WDF_Model.create_sequences(X, lookback)

            # If more than one variable reshape
            if len(variables) > 1 and v == "case_study":
                X = np.expand_dims(X, axis=2)

            X_all.append(X)

        X_all = np.concatenate(X_all, axis=-1)

        return X_all, Y

    @staticmethod
    def scaler(
        Xtra:np.array, Ytra:np.array, Xval:np.array, Yval:np.array, Xtest:np.array, Ytest:np.array, type_scaler:str,
        variables:List[str]
    ):
        assert type_scaler in ["MinMax", "Standard"], "Scaler must be MinMax or Standard"
        # Scalers
        if type_scaler == "MinMax":
            scx = MinMaxScaler([0, 1])
            scy = MinMaxScaler([0, 1])
        if type_scaler == "Standard":
            scx = StandardScaler()
            scy = StandardScaler()

        # For train
        Xtra_shape = Xtra.shape
        Ytra_shape = Ytra.shape
        Xtra = Xtra.reshape((-1, len(variables)))
        Ytra = Ytra.reshape((-1, 1))
        Xtra = scx.fit_transform(Xtra).reshape(Xtra_shape)
        Ytra = scy.fit_transform(Ytra).reshape(Ytra_shape)

        # For validation
        Xval_shape = Xval.shape
        Yval_shape = Yval.shape
        Xval = Xval.reshape((-1, len(variables)))
        Yval = Yval.reshape((-1, 1))
        Xval = scx.transform(Xval).reshape(Xval_shape)
        Yval = scy.transform(Yval).reshape(Yval_shape)

        # For test
        Xtest_shape = Xtest.shape
        Ytest_shape = Ytest.shape
        Xtest = Xtest.reshape((-1, len(variables)))
        Ytest = Ytest.reshape((-1, 1))
        Xtest = scx.transform(Xtest).reshape(Xtest_shape)
        Ytest = scy.transform(Ytest).reshape(Ytest_shape)
        return Xtra, Ytra, Xval, Yval, Xtest, Ytest, scx, scy

    @staticmethod
    def data_preprocessing(variables: List[str], config: Dict[str, str], lookback: int, type_scaler:str = "MinMax"):
        """Prepare the X,Y datasets for train, test and validation."""

        # Select the variables for the model to be trained on
        train_dict = WDF_Model.read_datasets(variables, config, mode="train")
        test_dict = WDF_Model.read_datasets(variables, config, mode="test")

        X, Y = WDF_Model.build_datasets(variables, train_dict, lookback)
        Xtest, Ytest = WDF_Model.build_datasets(variables, train_dict, lookback)

        # Create train and validation sets
        Xtra, Xval, Ytra, Yval = train_test_split(X, Y, shuffle=True)

        Xtra, Ytra, Xval, Yval, Xtest, Ytest, scx, scy = WDF_Model.scaler(
            Xtra, Ytra, Xval, Yval, Xtest, Ytest, type_scaler,variables
        )
        return Xtra, Ytra, Xval, Yval, Xtest, Ytest, scx, scy
