Sys.setenv(RENV_CONFIG_SANDBOX_ENABLED = "false")
source("renv/activate.R")

# Register Python dependencies before Python is initialized.
reticulate::py_require(c(
  "pandas",
  "numpy",
  "scipy",
  "matplotlib",
  "seaborn",
  "statsmodels",
  "scikit-learn",
  "pyreadr",
  "plotnine"
))
