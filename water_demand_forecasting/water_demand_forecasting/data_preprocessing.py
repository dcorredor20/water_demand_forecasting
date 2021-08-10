import numpy as np

def data_processing(variables, config, mode):
    X_all = list()
    for v in variables:
        assert v in config.keys(), "Variable not in config"
        # Read data
        df = pd.read_csv(config[v][mode], header=None, sep=r"\s+")
        # Reshape data
        if v == "case_study":
            X = df.values.reshape(-1)
        else: 
            X = np.array(df)

        # Create timestemps
        X, Y = utils.dataset(X, T=T)

        if v != "case_study":
            X = np.expand_dims(Xm, axis=2)

        X_all.append(X)
        X_all= np.concatenate(X_all, axis = -1)

        return X_all, Y
