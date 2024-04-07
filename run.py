# h/t: https://cmdstanpy.readthedocs.io/en/stable-0.9.65/generate_quantities.html#example-add-posterior-predictive-checks-to-bernoulli-stan
import os
from cmdstanpy import CmdStanModel, cmdstan_path

# bernoulli_dir = os.path.join(cmdstan_path(), "examples", "bernoulli")
ball_path = "ball.stan"  # os.path.join(bernoulli_dir, "ball.stan")
ball_data = "ball.data.json"  # os.path.join(bernoulli_dir, "bernoulli.data.json")

# instantiate, compile model
ball_model = CmdStanModel(stan_file=ball_path)

# fit the model to the data
bern_fit = ball_model.sample(data=ball_data)
