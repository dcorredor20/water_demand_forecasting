from tensorflow.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint,
    ReduceLROnPlateau,
    LearningRateScheduler,
)
from tensorflow.keras.callbacks import *


CALLBACKS = [
    EarlyStopping(
        monitor="val_loss", patience=6, verbose=1, min_delta=1e-4, mode="min"
    ),
    ModelCheckpoint(
        "mdl_wts.hdf5",
        save_best_only=True,
        monitor="val_loss",
        mode="min",
        save_weights_only=True,
    ),
    ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.5,
        patience=5,
        verbose=1,
        min_delta=1e-3,
        mode="min",
    ),
]
