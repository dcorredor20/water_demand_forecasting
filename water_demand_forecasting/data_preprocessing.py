import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from typing import Dict, List, Tuple


def data_preprocessing(variables: List[str], config: Dict[str, str], lookback: int):
    """Prepare the X,Y datasets for train, test and validation."""

    # Select the variables for the model to be trained on
    X, Y = build_datasets(variables, config, mode="train", lookback=lookback)
    Xtest, Ytest = build_datasets(variables, config, mode="test", lookback=lookback)

    # Create train and validation sets
    Xtra, Xval, Ytra, Yval = train_test_split(X, Y, shuffle=True)

    # Scalers
    scx = MinMaxScaler([0, 1])
    scy = MinMaxScaler([0, 1])

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


def build_datasets(
    variables: List[str], config: Dict[str, str], mode: str, lookback: int
) -> Tuple[np.array, np.array]:
    """Load data and return X and Y."""

    assert mode in ["train", "test"], "Mode not in train, test"
    assert "case_study" in variables, "case_study must be in variables"

    X_all = list()

    for v in variables:
        assert v in config.keys(), "Variable not in config"
        import pdb; pdb.set_trace()
        # Read data
        df = pd.read_csv(config[v][mode], header=None, sep=r"\s+")
        # Reshape data
        if v == "case_study":
            X = df.values.reshape(-1)
            X, Y = create_sequences(X, lookback)
        else:
            X = np.array(df)
            X, _ = create_sequences(X, lookback)        

        # If more than one variable reshape
        if len(variables) > 1 and v == "case_study":
            X = np.expand_dims(X, axis=2)

        X_all.append(X)

    X_all = np.concatenate(X_all, axis=-1)

    return X_all, Y


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
