# Simulating housing data with n = 2000
set.seed(123)

n <- 2000

# Simulating covariates
bedrooms <- rpois(n, lambda = 3) + 1  # Number of bedrooms: 1 to ~7 bedrooms
sqft <- round(rnorm(n, mean = 1800, sd = 400), 2) # Square footage: continuous and positively unbounded
neighbourhood <- factor(sample(c("Urban", "Suburban", "Rural"),
  n,
  replace = TRUE,
  prob = c(0.4, 0.4, 0.2)
)) # Neighbourhood type: discrete and categorical
school_distance <- round(runif(n, min = 0.1, max = 5), 2) # Distance in km

# Create sale price with a linear model + noise
sale_price <- round(50000 + 15000 * bedrooms + 100 * sqft +
  ifelse(neighbourhood == "Urban", 60000,
    ifelse(neighbourhood == "Suburban", 30000, 0)
  ) -
  8000 * school_distance + rnorm(n, mean = 0, sd = 30000), 2)

# Bundle into a data frame
housing_data <- data.frame(
  sale_price,
  bedrooms,
  sqft,
  neighbourhood,
  school_distance
)
