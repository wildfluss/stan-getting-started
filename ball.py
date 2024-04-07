import stan

ball_code = """
data {
  int<lower=1> N;           // Number of bounces to model
  real<lower=0> initial_h;  // Initial height from which the ball is dropped
  real<lower=0, upper=1> r; // Coefficient of restitution (percentage of height retained after each bounce)
}

parameters {
  // No parameters to estimate in this simple model
}

model {
  // The model does not estimate parameters, so this block is empty
}

generated quantities {
  real heights[N]; // Height of the ball after each bounce
  heights[1] = initial_h; // Initial drop height
  
  for (i in 2:N) {
    heights[i] = heights[i-1] * r; // Calculate height after each bounce
  }
}

"""

ball_data = {
    "N": 8,
    # "y": [28, 8, -3, 7, -1, 1, 18, 12],
    # "sigma": [15, 10, 16, 11, 9, 11, 10, 18],
}

posterior = stan.build(
    ball_code,
    data=ball_data,
    random_seed=1,
)

fit = posterior.sample(num_chains=4, num_samples=1000)

# eta = fit["eta"]  # array with shape (8, 4000)

# df = fit.to_frame()

# df.to_csv("draws.csv")
