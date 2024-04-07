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
  array[N] real heights; // Height of the ball after each bounce
  heights[1] = initial_h; // Initial drop height
  
  for (i in 2:N) {
    heights[i] = heights[i-1] * r; // Calculate height after each bounce
  }
}
