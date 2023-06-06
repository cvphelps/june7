import wandb
import random

for n in range(100):

    run = wandb.init(entity="wandb-smle",
                    project="soccer_players")

    run.log({
        "acc": random.random(),
        "loss": random.random(),
        "val_acc": random.random(),
        "val_loss": random.random(),
    })