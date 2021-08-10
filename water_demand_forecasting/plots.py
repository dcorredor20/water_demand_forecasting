"""Plots."""
import matplotlib.pyplot as plt


def loss_plot(model, model_str: str, color: str):
    """Plot the loss plots."""
    f, ax = plt.subplots(1, 2, figsize=(18, 6))
    ax[0].plot(model_def2.history["loss"], label=f"{model_str} loss", color=color)
    ax[0].plot(
        model.history["val_loss"],
        label=f"{model_str} val loss",
        color=color,
        ls="--",
    )
    ax[0].legend()
    ax[1].plot(model_def2.history["mse"], label=f"{model_str} MSE", color=color)
    ax[1].plot(
        model_def2.history["val_mse"],
        label=f"{model_str} val MSE",
        color=color,
        ls="--",
    )
    ax[1].legend()
    return
