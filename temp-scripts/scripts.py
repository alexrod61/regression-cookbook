### Scatterplot

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create made-up data showing a positive relationship between square footage and sale price
np.random.seed(42)
square_footage = np.random.uniform(800, 4000, 100)  # Square footage between 800 and 4000
sale_price = square_footage * 200 + np.random.normal(0, 50000, 100)  # Positive linear relationship

# Create a DataFrame
data = pd.DataFrame({
    'Square Footage': square_footage,
    'Sale Price': sale_price
})

# Create scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Square Footage', y='Sale Price', data=data)

# Add title and labels
plt.title('Scatterplot of Square Footage vs Sale Price')
plt.xlabel('Square Footage')
plt.ylabel('Sale Price')

# Show plot
plt.show()



### QQ plot

import statsmodels.api as sm

# Generate made-up data for linear regression
np.random.seed(42)
X = np.random.uniform(800, 4000, 100)  # Independent variable: square footage
y = X * 200 + np.random.normal(0, 50000, 100)  # Dependent variable: sale price with noise

# Fit a simple linear regression model
X_with_const = sm.add_constant(X)  # Add constant term for intercept
model = sm.OLS(y, X_with_const).fit()

# Get residuals
residuals = model.resid

# Create QQ plot of residuals
sm.qqplot(residuals, line='s')
plt.title('QQ Plot of Residuals')
plt.show()


# Residual Plot

# Create residual plot to check for outliers
plt.figure(figsize=(8, 6))
sns.scatterplot(x=model.fittedvalues, y=residuals)

# Add a horizontal line at y=0 for reference
plt.axhline(0, color='red', linestyle='--')

# Add labels and title
plt.title('Residual Plot to Check for Outliers')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')

# Show plot
plt.show()


### Heatmap

import matplotlib.pyplot as plt
import seaborn as sns

# Creating a heatmap for the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.2f')

# Adding title
plt.title('Correlation Matrix Heatmap', fontsize=16)
plt.show()
