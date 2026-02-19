# The Regression Cookbook (in development)
**[View the Book Online](https://alexrod61.github.io/regression-cookbook/)**

## Overview  

**The Regression Cookbook** is an **Open Educational Resource (OER)** that provides a modern, structured approach to regression modelling from a data-science perspective. It integrates statistical modelling, machine learning concepts, and reproducible computation across a broad suite of regression methods—including Ordinary Least-squares (OLS), generalized linear models (GLMs), and survival analysis. Every chapter blends foundational mathematics with real-data examples, enabling readers to interpret models, assess assumptions, and communicate results with clarity. Note each core chapter follows a consistent **eight-stage data science workflow** (Study Design → Data Collection and Wrangling → Exploratory Data Analysis → Data Modelling → Estimation → Goodness of Fit → Results → Storytelling) and presents **parallel `R` and `Python` codes** for reproducible analysis.

##  Learning Goals

After reading this book, readers will be able to:

- Identify the suitable regression model for different types of outcomes and inquiries (either inferential or predictive).
- Implement a variety of regression methods in both `R` and `Python`.
- Diagnose and validate model assumptions in applied settings.
- Interpret coefficients, predictions, and uncertainty with statistical clarity.
- Communicate modelling insights using reproducible data-science workflows.

## Data Science Workflow  

The material follows a unified eight-stage data science workflow used throughout the book:  

1. **Study design:** Define the research question, objectives, and variables of interest to ensure the analysis is purpose-driven and aligned with the problem at hand.
2. **Data collection and wrangling:** Gather and clean data, addressing issues such as missing values, outliers, and inconsistencies to transform it into a usable format.
3. **Exploratory data analysis (EDA):** Explore the data through statistical summaries and visualizations to identify patterns, trends, and potential anomalies.
4. **Data modelling:** Apply statistical or machine learning models to uncover relationships between variables or make predictions based on the data.
5. **Estimation:** Calculate model parameters to quantify relationships between variables and assess the accuracy and reliability of the model.
6. **Goodness of fit:** Evaluate the model’s performance using metrics and model diagnostic checks to determine how well it explains the data.
6. **Results:** Interpret the model's outputs to derive meaningful insights and provide answers to the original research question.
7. **Storytelling** Communicate the findings through a clear, engaging narrative that is accessible to a non-technical audience.

This workflow mirrors the lifecycle of real data-science regression tasks, helping learners move from theory to practice.

## Key Features

- **Dual-language code** (`R` + `Python`) for each model: promoting cross-platform fluency.  
- **Mathematical rigour**: formal equations accompany every model, enabling deeper conceptual understanding.  
- **Practical datasets**: real-world and simulated data with fully reproducible workflows.  
- **Modular cookbook structure**: each chapter stands on its own as a recipe you can apply.  
- **Open educational resource (OER)**: designed for reuse, adaptation and teaching.

## Getting Started 

### Prerequisites

You will need the following tools installed:  
- **`R` (≥ 4.0)** with key packages: `tidyverse`, `glmnet`, `MASS`, `broom`, etc.  
- **`Python` (≥ 3.7)** with key libraries: `pandas`, `numpy`, `scikit-learn`, `statsmodels`, etc.  
- **`Quarto`** (≥ 1.4) for rendering the book locally.

### Clone Locally  

```bash
git clone https://github.com/alexrod61/regression-cookbook.git
```

### Reproducible Environments (`R` + `Python`)

This project uses **two complementary environment managers**—`renv` for `R` and `Conda` for `Python`—to ensure that the Regression Cookbook can be built reproducibly across machines, operating systems, and time.

#### `R` Environment: `renv.lock`

The file `renv.lock` captures the exact versions of all `R` packages used throughout the cookbook (e.g., `tidyverse`, `broom`, etc.). Anyone cloning the repository can restore the full `R` environment by running:

```bash
renv::restore()
```

This recreates the `R `package library precisely as it existed when the book was last built, ensuring that all examples, figures, and modelling results remain fully reproducible.

#### `Python` Environment: `environment.yaml`

For `Python`, the file `environment.yaml` defines a `Conda` environment containing all necessary libraries (e.g., `pandas`, `numpy`, `scikit-learn`, `statsmodels`, `matplotlib`). Users can recreate the environment via:

```bash
conda env create -f environment.yaml
conda activate regression-cookbook-py
```

This ensures that `Python` computations—including regression fits, diagnostics, and visualization pipelines—are executed with the same versions used in the published book.

#### Why Both?

Because the Regression Cookbook is a **bilingual resource**, reproducibility requires maintaining two synchronized computational ecosystems. Using `renv` (`R`) and `Conda` (`Python`):

- Guarantees consistent behaviour across all `R` and `Python` code examples.
- Prevents version drift and dependency conflicts.
- Makes the entire book buildable on any machine with `Quarto` installed.
- Supports long-term stability for teaching, research, and OER use.

### Run Locally

```bash
cd regression-cookbook
quarto preview
```
The book will preview at `http://localhost:54321` (as set in `_quarto.yml`).

To render the full book, use:

```bash
quarto render
```

## Repository Structure

```bash
├── book/                   # Chapter files (.qmd)  
├── data/                   # Datasets (real + simulated)  
├── docs/                   # Rendered HTML site  
├── img/                    # Figures and visual assets  
├── _quarto.yml             # Project configuration  
└── README.md               # This file 
```

## Contributing

Contributions are welcome! 

To propose improvements, fix issues, or add new modelling chapters:

1. Fork the repository.
2. Create a branch for your edits.
3. Modify `.qmd` files under `/book`.
4. Preview your changes with quarto preview.
5. Submit a pull request.

Please ensure contributions maintain bilingual `R` + `Python` parity and reproducibility.

## Authors

[G. Alexi Rodriguez-Arelis](https://alexrod.netlify.app/), [Andy Tai](https://andytai7.github.io/Andy-Tai/), [Ben Chen](https://github.com/phchen5], and [Payman Nickchi](https://pnickchi.github.io/).

For questions or feedback, open an issue on [GitHub](https://github.com/alexrod61/regression-cookbook/issues).

## Collaborators

We extend our warmest thanks to the collaborators whose insight and enthusiasm have strengthened every part of this project. We are especially grateful to **Olivia Liu**, **Michael Sekatchev**, and **Aviv Milner**, whose hard work on chapter drafts, code examples, pedagogical framing, and workflow structure has helped shape the Regression Cookbook into a more rigorous, accessible, and thoughtfully crafted resource.

Your willingness to engage deeply with the material and provide constructive work has made this project richer than it could have been on its own. We are sincerely appreciative of the time, expertise, and encouragement each of you contributed. Thank you for helping build an OER that reflects both technical excellence and the collaborative spirit of the data-science and statistics community.

## OER Fund Acknowledgment

This project is supported by the [**UBC Vancouver (UBCV) OER Fund**](https://oerfund.open.ubc.ca/), through the project:

[**“The Regression Cookbook: A Structured, Data-Science-Based Approach to a Comprehensive Regression Analysis Toolbox.”**](https://oerfund.open.ubc.ca/the-regression-cookbook-a-structured-data-science-based-approach-to-a-comprehensive-regression-analysis-toolbox/) 

We gratefully acknowledge this funding, which enables the creation, maintenance, and free public release of this open-access regression resource for learners and instructors.

## Citation

If you use this material in teaching or research, please cite it as:

> Rodríguez-Arelis, G. A., Tai, A., Chen, B., & Nickchi, P. (2026). *The Regression Cookbook*. University of British Columbia / OER Fund. https://alexrod61.github.io/regression-cookbook/

Here is a BibTeX entry you can use:

```bash
@book{regressioncookbook,
  title     = {The Regression Cookbook},
  author    = {Rodríguez-Arelis, G. Alexi and Tai, Andy and Chen, Ben and Nickchi, Payman},
  year      = {2025},
  url       = {https://alexrod61.github.io/regression-cookbook/},
  note      = {Open-access bilingual (R and Python) textbook},
  publisher = {University of British Columbia / OER Fund}
}
```

## Privacy Policy

For details on data usage, cookies, and user tracking on the website, please refer to the [Privacy Policy](https://alexrod61.github.io/regression-cookbook/book/privacy-policy.html).

## License

This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0"  width="150"  src="img/by-nc-sa.png" /></a>
