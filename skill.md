MASTER EDITING PROMPT FOR REGRESSION COOKBOOK CO-AUTHORS
Regression Cookbook chapter revision, completion, audit, and quality-control protocol based on the completed Chapters 1, 2, 8, and 10

PURPOSE OF THIS PROMPT

Use this prompt whenever you are asked to revise, complete, audit, or quality-check a chapter of the Regression Cookbook. It is written for any co-author, collaborator, textbook assistant, or other contributor working on the book.

The completed Chapters 1, 2, 8, and 10 jointly define the current standard. Use them for different reasons rather than treating any one chapter as a universal template:

- Chapter 1 establishes the book-wide data science workflow, terminology bridge, split-sample logic, and the distinction among validation, diagnostics, testing, inference, and prediction.
- Chapter 2 establishes probability notation, random-variable language, likelihood/MLE foundations, goodness-of-fit framing, hypothesis-testing conventions, and the distinction among parameters, estimators, estimates, model checking, and prediction.
- Chapter 8 shows how the workflow adapts to a probability model with a binary response, including separation/convergence checks, functional-form refinement, calibration, discrimination, threshold-based classification, model freezing, and a full second coding case.
- Chapter 10 remains the main completed count-regression exemplar for GLM derivations, model-based uncertainty, Poisson-specific adequacy checks, model extension, and the connection between variance assumptions and standard errors.

These chapters are pedagogical and production standards, not text to be copied mechanically. Adapt every requirement to the target method, response type, assumptions, inferential target, predictive target, diagnostics, neighbouring chapters, and approved scope.

The objective is not merely to improve grammar or add code. Your job is to turn the target chapter into a coherent, mathematically sound, computationally reproducible, visually consistent, workflow-based teaching chapter that:

1. fits the identity of the Regression Cookbook established in Chapters 1 and 2;
2. preserves and improves valid work already present in the chapter;
3. develops one running case study through the complete data science workflow;
4. supports both inference and prediction whenever both are part of the chapter brief;
5. explains the mathematics behind estimation, uncertainty, interpretation, diagnostics, and prediction;
6. provides parallel, genuinely equivalent implementations in R and Python;
7. distinguishes model fitting from model checking, inference, prediction, and communication;
8. uses responsible language about association, uncertainty, model adequacy, and limitations;
9. ends with a balanced conceptual exercise bank and a second full applied coding case; and
10. renders successfully as part of the Quarto book.

Do not treat any completed chapter as a template into which model names are replaced. Reconstruct the same depth and logic for the target method while transferring only the conventions that genuinely apply.

======================================================================
1. MATERIALS YOU MUST REVIEW BEFORE EDITING
======================================================================

Before drafting any replacement text, read the following materials in full whenever they are available:

A. The latest target chapter source file, not an older duplicate or an early exported copy.
B. The finished Chapter 1, especially its data science workflow, study-design framing, training/testing logic, results organization, storytelling section, code/output conventions, and practice exercises.
C. The finished Chapter 2, especially its probability notation, random-variable language, likelihood and MLE foundations, goodness-of-fit framing, definitions, question-and-answer boxes, and distinction between estimation, inference, model checking, and prediction.
D. The completed Chapters 8 and 10, using each for what it does best. Chapter 8 is the main completed exemplar for binary/probability modelling, calibration/discrimination, thresholding, separation, model freezing, and a full coding case. Chapter 10 is the main completed exemplar for count-model GLM derivations, variance-linked uncertainty, model-specific diagnostics, model extension, interpretation, prediction, and exercises.
E. The chapters immediately before and after the target chapter, so the new chapter neither repeats material unnecessarily nor assumes material that has not yet been introduced.
F. The relevant distribution appendix and the distributional mind map.
G. The book bibliography, Quarto project configuration, custom CSS, reusable images, and existing cross-reference conventions.
H. The actual dataset files and data-source documentation.
I. Any existing co-author drafts, rationale files, lead-author comments, or previously approved revisions for the target chapter.

Use this source hierarchy when materials disagree:

1. The lead author's or current task owner's newest explicit instruction.
2. The latest approved/integrated version of the target chapter.
3. The finished conventions in completed reference chapters, currently Chapters 1, 2, 8, and 10, with model-specific conventions taken from the most relevant completed chapter rather than copied indiscriminately.
4. The most recent approved section-level revision, rationale, audit decision, or explicitly accepted local correction.
5. Older drafts, screening calculations, raw originals, and superseded exports.

When an actually executed current result conflicts with an older screening result for the same analysis, the current executed result governs. Do not preserve stale numerical conclusions merely because they appeared in an earlier draft.

Never assume that a file with the simplest name is the newest version. Confirm the latest source before editing.

======================================================================
2. REQUIRED WORKING METHOD: SECTION BY SECTION, WITH AN AUDIT TRAIL
======================================================================

Work one requested section or tightly connected group of sections at a time. Do not rewrite an entire chapter in one uncontrolled pass unless explicitly asked. Preserve approved prose, equations, code, figures, and pedagogical decisions unless there is a concrete statistical, pedagogical, reproducibility, notation, or rendering reason to change them.

For a SUBSTANTIAL section-level revision, the default deliverables are two separate plain-text files:

1. `[chapter]-[section]-proposed.txt`
   - Contains the exact Quarto-ready replacement text.
   - Includes headings, IDs, equations, code chunks, captions, callouts, tables, cross-references, and citations needed for insertion.
   - Does not contain commentary about the editing process.

2. `[chapter]-[section]-rationale.txt`
   - Explains what was reviewed.
   - Identifies what was preserved from the existing chapter.
   - Identifies what was revised, expanded, relocated, or removed.
   - Explains why every substantive change improves mathematical correctness, pedagogy, workflow consistency, accessibility, or reproducibility.
   - Notes unresolved choices, implementation risks, references to add, and dependencies on later sections.
   - Includes exact placement instructions.

For a LOCAL correction, late-stage audit, typo/notation fix, or narrowly scoped QC pass, do not manufacture two large files unnecessarily. Use the requested format, and when proposing corrections provide exact `BEFORE` and `AFTER` text/code so the change can be applied without guesswork.

Every item in an existing section must be accounted for. Preserve it, revise it, relocate it, or explain why it should be removed. Do not silently delete valid material merely because a different organization is stylistically preferable.

After the main chapter body is complete, use a staged audit process:

A. Audit the chapter body before the Chapter Summary for statistical, mathematical, workflow, notation, cross-reference, code, and prose coherence.
B. Audit the Chapter Summary separately to ensure it synthesizes rather than introduces.
C. Audit the Practice Exercises and second coding case separately, including notation, coverage, answer correctness, and consistency with the final chapter.
D. Produce an exact before/after correction list for local changes identified by the audit.
E. Perform a final static and render-based QC pass after the corrections are integrated.

After all sections are approved, produce as requested:

A. One merged, integrated `.qmd` chapter.
B. A comprehensive change report organized by section.
C. A pre-render quality-control report.
D. A bibliography-additions file containing complete BibTeX entries that are not already present.
E. A code/data validation log stating what was executed, with which data, and whether R/Python results agree.

Distinguish static checking from execution. Syntax checks, label audits, or text searches are not equivalent to executing R/Python code or rendering Quarto. Do not claim that code was executed, a reference was verified, or a file rendered unless it was actually checked.

======================================================================
3. EDITORIAL PHILOSOPHY
======================================================================

The chapter must read as an applied statistical story, not as disconnected definitions, equations, software commands, and output tables.

Use this progression throughout:

1. Why the method is needed.
2. What kind of response and scientific/data-science question it addresses.
3. What the data represent.
4. What the model assumes.
5. How the model is estimated.
6. How adequacy is checked.
7. How coefficients or other parameters are interpreted.
8. How held-out prediction is evaluated, when prediction is in scope.
9. What the results mean for the original inquiry.
10. What the model cannot establish or do reliably.
11. How the findings should be communicated to an applied audience.

The main explanatory prose must carry the chapter. Callout boxes should reinforce, warn, define, or enrich the exposition; they must not contain all the important teaching while the main body remains thin.

Do not rewrite approved prose merely to make it sound different. At late stages, prefer the smallest change that fixes the identified issue. Preserve the statistical story and approved wording unless there is a concrete reason to change them.

Prefer clear connective prose between definitions, equations, code, output, and interpretation. A table, figure, equation, or diagnostic output must never appear without prose explaining why the reader is seeing it, what to inspect, and what it contributes to the workflow.

Preserve a warm, engaging, precise tone suitable for data science students who have some statistical background but may not yet be comfortable with the target method. Do not oversimplify the mathematics, but introduce it incrementally and interpret every important object in words.

Use Canadian/British spelling consistently where the book already does so: for example, “modelling,” “colour,” “centre,” and “behaviour.”

======================================================================
4. NON-NEGOTIABLE CHAPTER-LEVEL ARCHITECTURE
======================================================================

Adapt the following architecture to the target chapter. Not every model needs identical subsection names, but every stage must be represented explicitly or its omission justified.

1. Chapter title and stable section ID.
2. A conceptual “When to Use and Not Use” warning.
3. Learning objectives.
4. Technical setup and package requirements.
5. Introduction and roadmap.
6. Documented real-world use cases.
7. Running case study.
8. Study design.
   a. Observational unit.
   b. Response variable.
   c. Regressors or explanatory variables.
   d. Inferential inquiry.
   e. Predictive inquiry, when in scope.
9. Data collection, provenance, and wrangling.
10. Exploratory data analysis.
11. Formal statistical/model formulation.
12. Simple or baseline model specification.
13. Estimation and software fitting.
14. Goodness-of-fit/model-adequacy checks.
15. Model extension or refinement, when justified.
16. Repeated diagnostics for the extended model.
17. Parameter/coefficient interpretation.
18. Prediction for new or held-out observations.
19. Results and statistical interpretation.
   a. Final inferential analysis.
   b. Formal tests and intervals.
   c. Held-out predictive performance.
20. Storytelling for an applied audience.
21. Chapter summary.
22. Practice exercises.
   a. Conceptual questions.
   b. A second full coding case study.

This is a workflow architecture, not a rigid table of contents. Do not force identical subsection names, a model extension, a predictive component, or a second coding case when the approved chapter scope genuinely does not require them. Conversely, do not omit a necessary stage merely to make the chapter shorter.

The chapter should continually remind the reader where they are in the workflow and why the current step must occur before the next one.

======================================================================
5. TOP-OF-CHAPTER ELEMENTS
======================================================================

5.1 “When to Use and Not Use” warning

Place a concise warning box near the beginning. It must be conceptual and should not contain equations. It should state:

- the required support/type of the response;
- the observational independence or dependence conditions relevant to the method;
- the model's main distributional and structural assumptions;
- when the link function or transformation is appropriate;
- important warning signs that suggest another model;
- which alternative cookbook chapters should be consulted for different response types or assumption failures.

For Chapter 10, this meant non-negative integer counts, conditional independence, positive expected counts through a log link, and the adequacy of the Poisson mean-variance structure. It also redirected readers to binary logistic, OLS/Gamma, Negative Binomial, Generalized Poisson, Zero-Inflated Poisson, and mixed-effects models as appropriate. For another chapter, create the corresponding model-specific decision guide.

Do not introduce offsets, exposure terms, interactions, penalization, random effects, ordinal-polynomial contrasts, recalibration procedures, or other optional advanced topics simply because they are common in the literature. Include an advanced topic only when it is part of the approved scope of the target chapter or explicitly requested. Model refinement must respond to a concrete modelling need rather than to a desire for complexity.

5.2 Learning objectives

Use the existing Learning Objectives callout style. Objectives should use observable verbs and cover the entire chapter, including:

- recognizing when the model is appropriate;
- identifying its random and systematic components;
- understanding the link or transformation;
- writing the model mathematically;
- fitting it in R and Python;
- explaining the estimation method;
- diagnosing assumption violations or lack of fit;
- interpreting parameters on both native and transformed scales;
- conducting relevant inference;
- making and evaluating predictions;
- communicating limitations and results.

Do not write objectives that promise content the chapter does not actually deliver.

5.3 Setup

Audit all packages before adding them. Every loaded package must be used. Every used package must be loaded or otherwise available. Remove stale comments and unused dependencies.

Examples of Chapter 10 QC issues that must not recur:

- Spell `scipy` correctly; never list a nonexistent package such as `spicy`.
- Do not load a package claiming it supplies a dataset when the chapter actually imports that dataset from a repository.
- Keep the setup aligned with the code used later.

Use reproducible package requirements for Python and a consistent R setup. Suppress routine package messages and harmless warnings where appropriate, but never hide a warning that signals a genuine statistical or data problem.

5.4 Distributional/model mind map

When relevant, update or include the regression/distributional mind map to show where the chapter's model sits according to response support and modelling assumptions. Ensure labels and chapter numbers are current.

If a Mermaid diagram is used, ensure it renders in HTML and supports the book's click-to-enlarge convention. Do not leave raw Mermaid code that fails in the book build.

5.5 Documented use cases

Add a short, well-supported table of real applications. Use scholarly or authoritative sources and include columns such as:

- paper/title;
- authors;
- application area;
- outcome variable;
- substantive question;
- general method;
- main modelling lesson.

The purpose is not to create a literature review. The table should show that the method is used beyond the teaching example and should illuminate when the model is useful or when a more flexible alternative was needed.

Verify every citation and BibTeX key. Do not cite a source merely because its title seems relevant.

======================================================================
6. RUNNING CASE STUDY
======================================================================

Choose or retain one case study that can support the full chapter. The case must have enough substance for EDA, modelling, checking, interpretation, prediction if applicable, and storytelling.

The case-study introduction must explain:

- the practical/scientific setting in plain language;
- why the setting matters;
- why the dataset may be familiar or unfamiliar to data science students;
- why it is nevertheless pedagogically useful;
- the observational unit;
- the response variable and its support;
- the available regressors and their roles;
- whether the data are observational, experimental, secondary, simulated, or otherwise collected;
- the inferential and predictive opportunities the data provide;
- important ethical, scientific, or operational context.

Do not begin with a function call or a coefficient. Establish the real-world question first.

For an observational dataset, do not imply causal identification. Use language such as “associated with,” “related to,” or “helps predict,” unless the design actually supports a causal claim.

Cite the original study and the source from which the usable data file was obtained. Distinguish the original scientific source from a textbook or repository copy. When an approved local copy of the dataset is stored in the cookbook repository, prefer that local file for runtime reproducibility while retaining the original source/DOI/license citation in the prose.

When using an unfamiliar biological, medical, industrial, or social-science dataset, explain the domain terms needed to understand the response. Do not assume readers know what the observational units or events are.

======================================================================
7. STUDY DESIGN: DEFINE THE TWO INQUIRIES BEFORE MODELLING
======================================================================

Before EDA or model fitting, explicitly state what the analysis is intended to learn.

Define:

- the target population or system;
- the observational unit;
- the response random variable;
- the observed response;
- the candidate regressors;
- the parameter or estimand of interest;
- the prediction target, if applicable;
- the limits created by the study design;
- the timing and availability of candidate regressors at the intended prediction time, when prediction is in scope;
- any deliberate exclusions made for scientific, pedagogical, operational, or usefulness reasons.

Do not label every deliberately excluded strong regressor as “data leakage.” A variable is leakage only when it improperly uses information unavailable at the intended prediction time or otherwise violates the intended prediction setup. A variable may instead be excluded because it would dominate the problem, change the scientific question, reduce usefulness, or move the prediction time later. State the actual reason.

When both inference and prediction are in scope, create separate subsections and state separate questions.

Inferential inquiry:
- asks how an expected response, probability, rate, quantile, hazard, or other model quantity is associated with regressors;
- requires coefficient/parameter estimates, uncertainty, tests or intervals, and cautious interpretation.

Predictive inquiry:
- asks how well the fitted model predicts a held-out response or distributional quantity;
- requires out-of-sample predictions, appropriate metrics, and a meaningful baseline.

Include a table that maps each inquiry to what the Results section must ultimately deliver.

Explain that the two inquiries can use the same model but require different workflow decisions. Do not collapse inference and prediction into one vague goal.

======================================================================
8. DATA COLLECTION, PROVENANCE, AND WRANGLING
======================================================================

Document the data source precisely:

- original investigator/source;
- repository or package;
- raw-file URL versus browser-view URL when applicable;
- license or access information if relevant;
- sampling/collection design;
- units of measurement;
- meaning of category codes;
- missing-value codes;
- transformations or recoding.

Explain every wrangling decision in prose before or after code. Do not let recoding happen silently.

Create a conceptual variable table in native Markdown, not with R or Python, containing:

- variable name in code;
- role (response, regressor, identifier, grouping variable, etc.);
- data type;
- statistical notation;
- units;
- description;
- category/reference coding where applicable.

Conceptual tables belong in Markdown. Computed summaries belong in code-generated tables.

Check and report:

- number of rows and columns;
- variable storage types;
- response support and integer/continuity conditions;
- missing values;
- duplicated observations where relevant;
- impossible values;
- unusual but potentially valid values;
- category counts and empty levels;
- factor/reference ordering.

Distinguish an unusual value from a data error. Do not delete or change an observation merely because it is surprising.

Use descriptive object names. Keep R and Python names aligned wherever possible.

Special handling for `.rda`/`.RData` files:

- In R, load the file using the appropriate local or downloaded file workflow.
- In Python, download the remote `.rda` file to a local path first, then use `pyreadr.read_r()` on that local file. Do not assume `pyreadr.read_r()` can read a web URL directly.
- Verify the object names inside the file.
- Reconstruct factor/category labels and reference ordering explicitly after conversion.

======================================================================
9. TRAINING/TESTING LOGIC AND PROTECTION AGAINST DOUBLE DIPPING
======================================================================

Follow the book's split-sample workflow whenever the chapter has both model-development and final-assessment stages.

The training set is used for:

- EDA;
- candidate model specification;
- model fitting during development;
- goodness-of-fit and diagnostic checks;
- decisions about a pre-specified model extension;
- calculation of any baseline that must be learned from training data.

The testing set remains untouched until the Results stage.

Before the testing outcomes are examined, freeze the selected specification. “Frozen” means that the substantive model structure is fixed: response definition, regressors, transformations, polynomial terms, interactions if any, category/reference contrasts, link/family, and the diagnostic/refinement decisions that determined the final form.

For the inferential inquiry:

- after the model form has been selected and checked using the training data, refit that fixed model specification on the testing data;
- use the testing-set refit for the final coefficient-level inferential summary;
- do not use the testing data to change regressors, transformations, reference categories, interactions, polynomial terms, or diagnostic choices;
- do not remove a term merely because its testing-set Wald p-value is large if the term was legitimately retained during training-stage model development.

For the predictive inquiry:

- do not refit using testing responses;
- use the model fitted on the training data to generate predictions for testing observations;
- compare those predictions with observed testing outcomes only at final evaluation;
- do not recalibrate, retune a classification threshold, or otherwise alter the model using the testing outcomes and then report performance on those same observations.

Explain the distinction explicitly. The same testing set has two different roles in the two workflow flavours, and the roles must not be mixed.

The purpose of the inferential refit is to avoid using the same observations for exploration, model development, diagnostics, and final coefficient-level claims. State this as protection against double dipping. The purpose of the predictive holdout is different: it assesses the already training-fitted model without giving the testing outcomes back to model development.

Do not copy Chapter 10's 50/50 split automatically. Chapter 10 used a comparatively balanced split because the dataset was small and the chapter needed meaningful samples for both the inferential refit and predictive evaluation. For another dataset, justify the allocation based on sample size, model complexity, inquiry, and stability. A Tip box may discuss alternatives such as 80/20 splits, repeated sample splitting, cross-validation for prediction, or resampling-based methods.

R/Python split alignment:

1. Create the canonical split in R with a stated seed.
2. Show the conceptually equivalent independent Python split if it is pedagogically useful.
3. Explain that the same seed in different languages does not guarantee the same observations.
4. Import the R-generated training and testing sets into Python through `reticulate` for all downstream side-by-side analyses.
5. Restore categorical data types and baseline ordering in Python after transfer.
6. Include sanity checks for total, training, and testing sample sizes and disjointness.

This approach preserves genuine R/Python parity rather than merely producing similar-looking analyses on different observations.

======================================================================
10. EXPLORATORY DATA ANALYSIS
======================================================================

EDA must occur after wrangling and after the split. Use only the training data.

Organize EDA in a purposeful sequence:

1. Overall data and variable summaries.
2. Distribution of the response.
3. Response versus continuous regressors.
4. Response versus categorical regressors.
5. A concise EDA summary that links findings to later modelling decisions.

For the response, examine model-relevant features. Depending on the chapter, these may include:

- support and range;
- centre and spread;
- skewness;
- zero, boundary, or censored values;
- sample mean and variance;
- class balance;
- proportions near 0 or 1;
- repeated measurements or cluster sizes;
- event/censoring patterns;
- potential outliers.

For Chapter 10, the raw mean, variance, variance-to-mean ratio, zero proportion, and count distribution were useful early warnings. Make clear that raw marginal summaries do not by themselves test a conditional model assumption. For example, raw mean-versus-variance comparisons are descriptive; equidispersion is conditional on included regressors.

For continuous regressors:

- report ranges and useful grouped summaries such as quartiles or bins;
- plot the response against each regressor;
- use a model-appropriate exploratory smoother only when it helps reveal a descriptive pattern;
- match smoothing parameters between R and Python;
- explain that a smoother is an exploratory visual guide, not the fitted regression model.

For categorical regressors:

- report category sizes and imbalance;
- summarize response distributions by category;
- use plots that reveal individual observations and distributional overlap;
- if jitter is needed, jitter only in the categorical/horizontal direction so the response value is not falsified;
- explain the jitter in a Heads-up box.

Never fit the target regression model in the EDA section. Never inspect the testing responses. Never interpret an EDA pattern as an adjusted coefficient, a formal inferential finding, or a causal effect. Exploratory bins, grouped summaries, or smoothers are descriptive devices; they do not automatically become the transformations or functional forms used in the final regression model.

End EDA with a Markdown summary table such as:

- feature investigated;
- descriptive evidence;
- implication for model specification or checking;
- caution.

Then write a transition explaining why the formal model is the next step.

======================================================================
11. FORMAL MODEL PRESENTATION
======================================================================

Introduce the statistical model before fitting it. Define the model in words first, then equations.

For a generalized linear model, explicitly separate:

1. Random component.
2. Systematic component.
3. Link function.

For other model classes, identify the equivalent structural pieces.

Contrast the new model with a familiar earlier model when this prevents a common misconception. In Chapter 10, the OLS additive-error form was contrasted with direct modelling of the conditional Poisson distribution. The comparison clarified that the GLM systematic component is the linear predictor, not necessarily the conditional mean on the original response scale.

Do not represent a GLM as “OLS with a different outcome.” Explain how the conditional distribution and link change the model.

11.1 Random component

Define:

- the response random variable;
- the conditioning regressors;
- the support;
- the distribution and its parameterization;
- the conditional PMF/PDF;
- the conditional mean;
- the conditional variance;
- any dependence assumptions;
- whether the response is represented at the individual-observation level or as grouped/aggregated observations.

Do not treat mathematically related response representations as automatically interchangeable. For example, individual Bernoulli rows and grouped Binomial successes/trials can contain equivalent coefficient information only when the grouping preserves the relevant regressor pattern and common conditional success probability. Grouping does not solve dependence or clustering.

Use conditional notation. For a discrete response, use a PMF; for a continuous response, use a PDF. Do not use “density” for a discrete probability mass.

11.2 Systematic component

Write the general model with $k$ regressors before specializing to the case study. Define every symbol. Explain that linearity refers to linearity in the coefficients, not necessarily a straight-line mean on the response scale.

11.3 Link/transformation

Define the link and inverse link. Explain:

- why it is used;
- how it respects the support of the model quantity;
- what scale the coefficients inhabit;
- how the original response-scale quantity is recovered;
- how this affects interpretation.

11.4 Self-contained definitions

Every Definition box containing mathematics must define every symbol used inside the box, even when those symbols appeared earlier in the surrounding text. A reader should be able to understand the definition without searching backwards.

11.5 Historical context

Historical Tip boxes may be used when they enrich understanding. Chapter 10 separated the history of the Poisson distribution from the history of Poisson regression/GLMs so the boxes were not adjacent and each appeared where conceptually relevant. Follow the same restraint:

- verify historical claims;
- cite a reputable source;
- credit portraits or other images fully;
- do not crowd the chapter with trivia;
- do not place multiple history boxes back to back.

======================================================================
12. MATHEMATICAL NOTATION STANDARDS
======================================================================

Use the book's notation consistently.

Probability and distributions:

- Use $\Pr(\cdot)$ for probabilities, not $P(\cdot)$.
- Use $p_Y(y;\theta)$ for a PMF and $f_Y(y;\theta)$ for a PDF, with a semicolon separating the observation from the parameter.
- Use $F_Y(y;\theta)$ for a CDF when parameters are displayed.
- Reserve vertical bars for conditional probability or conditional distributions.
- Use $\mathbb{E}(Y)$ and $\operatorname{Var}(Y)$.
- Use `\operatorname{Normal}`, `\operatorname{Poisson}`, and similarly explicit distribution names.

Random variables and observations:

- Uppercase letters for random variables: $Y_i$.
- Lowercase letters for realizations: $y_i$.
- State index ranges, such as $i=1,\ldots,n$.
- State support explicitly.

Regressors and parameters:

- Use regressors, not predictors, unless “predictor” is required in a distinctly predictive context.
- Use numeric subscripts consistently: $x_{i,1},x_{i,2},\ldots,x_{i,k}$.
- Do not put literal code-variable names inside mathematical notation. Avoid coefficient symbols such as $\beta_{\texttt{income}}$ or indicator definitions involving $\texttt{study\_time}_i$. Define the working variable in prose or a notation table, assign it a mathematical symbol, and use that symbol consistently thereafter.
- Once a notation table or model definition establishes that a working variable corresponds to $x_{i,j}$, do not later repurpose $x_{i,j}$ for a different quantity.
- Use $\boldsymbol{\beta}$ for a coefficient vector and $\beta_j$ for a scalar coefficient.
- Use a consistent bold vector notation for $\mathbf{x}_i$, $\mathbf{y}$, and the design matrix $\mathbf{X}$.
- Define whether $\mathbf{x}_i$ includes the intercept.
- Keep vector orientation explicit when needed.

Estimation:

- Distinguish a parameter, estimator, and realized estimate.
- Use notation such as $\widehat{\boldsymbol{\beta}}_{\operatorname{MLE,obs}}$ when the distinction is pedagogically useful.
- Define fitted model quantities such as $\widehat{\mu}_i$ or $\widehat{\pi}_i$ before using them.
- When one substantive regressor enters through multiple terms, such as $x_{i,j}$ and $x_{i,j}^2$, do not describe the separate coefficients as independent constant effects. The terms act jointly when the regressor changes.

Cross-references:

- Label important equations using stable `#eq-...` identifiers.
- Label sections `#sec-...`, tables `#tbl-...`, figures `#fig-...`, and listings `#lst-...` or Quarto's `lst-label` option.
- Refer to objects by cross-reference, not by brittle prose such as “the equation above.”

Audit the entire chapter after editing for collisions, broken labels, mixed notation, and undefined symbols.

======================================================================
13. MODEL SPECIFICATION AND ESTIMATION
======================================================================

Begin with a simple, interpretable model that supports the teaching progression. Explain why the first regressor or reduced specification was chosen. Do not let the simple model look like arbitrary automated selection.

State the random component, linear/systematic component, link, and expected response-scale form for the specific case.

Defer substantive coefficient interpretation until the model has undergone goodness-of-fit checking. It is acceptable to explain the algebraic meaning of a coefficient before diagnostics, but avoid presenting it as a trustworthy empirical conclusion prematurely.

13.1 Likelihood and log-likelihood

Develop the estimation machinery rather than jumping directly to software. Include, as appropriate:

- the independent-observation likelihood;
- the log-likelihood;
- the coefficient-vector MLE;
- the scalar score equation for a representative coefficient;
- the vector score;
- the Hessian or second derivatives;
- observed or expected Fisher information;
- the model-based covariance matrix;
- standard errors.

Use both matrix notation and a scalar derivation when each serves a different teaching purpose. Matrix notation shows the general computational structure; scalar calculus shows how an individual coefficient enters the likelihood.

Do not invent an OLS-style closed-form solution when none exists.

13.2 Iterative estimation

Explain the numerical algorithm used by software. For GLMs, discuss Fisher scoring and/or Iteratively Reweighted Least Squares (IRLS) at an appropriate level.

Use correct terminology:

- $\boldsymbol{\beta}$ is the coefficient vector, not a “regression term vector.”
- Capitalize the formal name “Iteratively Reweighted Least Squares (IRLS).”
- Use lowercase “weighted least-squares” when describing the temporary subproblem outside the formal algorithm name.

Explain the iterative cycle conceptually:

1. start from coefficient values;
2. compute fitted means/model quantities;
3. construct working responses and weights or an equivalent local approximation;
4. solve the temporary weighted least-squares/Newton step;
5. update coefficients;
6. continue until convergence.

Connect the algorithm back to the score equations and likelihood.

13.3 Variance assumptions and standard errors

Make the connection between the model's conditional variance assumption and model-based uncertainty explicit.

In Chapter 10, the same Poisson mean parameter determines both the conditional mean and variance. The Fisher information, covariance matrix, standard errors, Wald tests, and confidence intervals therefore rely on equidispersion. With overdispersion, model-based standard errors can be underestimated, leading to overly optimistic tests and confidence intervals.

For another model, identify the corresponding dependency. Explain which variance, dispersion, independence, likelihood, or censoring assumptions underpin standard errors. This connection is essential and must not be left implicit.

13.4 Conceptual estimation table

A small Markdown table may summarize:

- likelihood;
- score;
- information/Hessian;
- coefficient estimate;
- fitted model quantity;
- covariance matrix;
- standard error;
- software object.

Use conceptual tables to connect mathematics to software, not to duplicate prose.

======================================================================
14. MODEL-FITTING CODE AND FUNCTION EXPLANATIONS
======================================================================

Explain the syntax and role of every central fitting function before or immediately after the code.

For R `glm()`, explain:

- `formula = response ~ regressors` specifies the systematic component;
- `family = ...` specifies the random component and link;
- `data = training_data` identifies the fitting sample.

For Python `statsmodels.formula.api.glm()`, explain:

- `formula` specifies the response and regressors;
- `data` identifies the fitting data frame;
- `family=...` specifies the distribution/link;
- `.fit()` carries out estimation.

For other chapters, provide the analogous explanation for the relevant R and Python functions. Do not assume that a student understands what each argument represents statistically.

Use clear comments, but do not comment every punctuation mark. Comments should explain statistical intent, data handling, and non-obvious implementation choices.

Keep code readable and executable with minimal hidden state. Avoid unexplained helper objects created many pages earlier.

======================================================================
15. R/PYTHON PARITY
======================================================================

Every substantive computational task must have an R and Python implementation unless the chapter explicitly states otherwise.

Parity means:

- the same dataset observations;
- the same response and regressors;
- the same transformations and units;
- the same reference categories;
- the same model family/link/parameterization;
- the same diagnostic definitions;
- the same prediction target;
- the same rounding policy;
- numerically equivalent results within expected software tolerance;
- visually comparable plots.

Do not settle for two superficially similar analyses that use different samples or category baselines.

Use a `.panel-tabset` for paired languages.

When code is meant to be visibly presented as a listing, use `lst-label` and `lst-cap`. When code produces a table or figure, use the appropriate table or figure label/caption.

If R and Python use different default parameterizations, make one explicit so the results agree. If exact agreement is impossible because of a documented algorithmic difference, explain the difference rather than concealing it.

If direct Python stdout/`print()` output is unreliable in the Quarto execution environment, build the desired reader-facing text as a Python string and render it through a small hidden R chunk using `reticulate::py$...`. Use this only for presentation; do not obscure the underlying Python computation.

======================================================================
16. TABLE AND OUTPUT CONVENTIONS
======================================================================

16.1 Conceptual tables

Write conceptual tables directly in Markdown. Examples include:

- variable definitions;
- inquiry mapping;
- diagnostic interpretation guides;
- model-component summaries;
- dummy-variable arrangements;
- chapter roadmaps;
- final EDA or GOF synthesis.

Do not generate conceptual tables with R merely to display fixed text.

16.2 Computed R tables

For compact computed outputs, prefer `knitr::kable()` with deliberate column names, alignment, and rounding. Do not print raw tibbles, model summaries, or unwieldy console output when a compact teaching table is clearer.

Use interactive `DT` tables only for full datasets or genuinely exploratory large outputs. Do not use an interactive widget for a five-row coefficient table.

16.3 Computed Python tables

Do not rely on plain pandas/DataFrame notebook representation because it may render inconsistently in Quarto and may not match the R display.

The current book-wide standard is the reusable responsive helper used in the completed Chapters 1, 2, 8, and 10:

```python
def scrollable_table_html(data, **kwargs):
    kwargs.setdefault("index", False)
    kwargs.setdefault("border", 0)

    return (
        '<div class="table-responsive">'
        + data.to_html(
            **kwargs
        )
        + '</div>'
    )
```

Use the project’s approved responsive-table CSS so narrow tables display normally and genuinely wide tables can scroll horizontally.

Preferred pattern:

1. Create a concise display DataFrame in Python.
2. Round only the display copy, not the values used in calculations.
3. Convert it with `scrollable_table_html(...)`, not a direct `.to_html(...)` call scattered throughout the chapter.
4. Pass special display arguments through `**kwargs` only when needed, for example `index=True` for a meaningful row index or `na_rep="—"` for display-only missing values.
5. Store the resulting HTML string in a descriptive Python object.
6. Render it in a following hidden R chunk using `results: asis` and `cat()` through `reticulate::py$...`.
7. Give the rendered table its own `tbl-...-py` label and caption.

Canonical rendering pattern:

```r
#| echo: false
#| label: tbl-...
#| tbl-cap: "..."
#| message: false
#| warning: false
#| results: asis
cat(
  "
",
  reticulate::py$some_table_py_html,
  "
",
  sep = ""
)
```

This helper-based arrangement is now the standard for future chapters. Do not return to dozens of direct `.to_html()` calls.

16.4 General table rules

- Give R and Python outputs parallel captions.
- Use language suffixes in labels where both versions exist: `-r` and `-py`.
- Use meaningful column names rather than raw software names.
- Keep p-value and interval precision consistent across languages.
- Preserve very small p-values rather than rounding all of them to `0.00`; use scientific notation or threshold notation where appropriate.
- Do not mix incompatible numbers of decimal places without a reason.
- Use a `.table-scroll` wrapper and suitable minimum width for genuinely wide tables.
- Avoid making every table wide. Select only pedagogically useful columns.
- Refer to the correct R or Python table in surrounding prose.

======================================================================
17. FIGURE AND VISUALIZATION CONVENTIONS
======================================================================

R and Python figures must be designed as matched pairs.

Match:

- data observations;
- axes and limits;
- units;
- category ordering;
- point transparency and size;
- smoothing method and tuning parameters;
- reference lines;
- annotations;
- legend meaning and placement;
- captions;
- figure dimensions.

Do not rely on language defaults when they create visibly different graphics.

Assign plots to descriptive objects before displaying them whenever practical. In R, prefer `plot_object <- ggplot(...) + ...` followed by `plot_object` rather than constructing a long anonymous plot as the final expression. In Python, keep the figure/axis object explicit when it helps later formatting and end visible Matplotlib chunks with `plt.show()` so rendering is reliable.

Every figure needs:

- a unique `fig-...` label;
- a clear caption stating what is plotted and which data split/model is used;
- surrounding prose explaining what the reader should inspect;
- cautious interpretation.

If a line is added to a histogram, scatterplot, calibration plot, or diagnostic plot, explain exactly how it was obtained. A curve must not appear as if by magic. State whether it is a fitted model curve, a nonparametric smoother, a theoretical density, a reference line, or a grouped average.

For exploratory smoothers, emphasize visual inspection and sampling variability. For diagnostic reference bands such as Pearson residual lines at -2 and 2, state that they are informal guides rather than hard decision boundaries.

All decorative or historical images must have complete, accurate credits and working source links/citations. Audit author names and capitalization; Chapter 10 required corrections to inconsistent or misspelled image credits.

======================================================================
18. GOODNESS OF FIT AND PRACTICAL MODEL ADEQUACY
======================================================================

Model fitting is not model validation. Build a distinct goodness-of-fit section before final interpretation.

Use multiple complementary layers:

1. Graphical checks.
2. Numerical descriptive checks.
3. Formal or approximately formal diagnostics.
4. A practical adequacy synthesis.

Do not reduce model adequacy to one p-value. Do not say a large p-value proves the model is true or “a good fit.” Phrase conclusions as evidence for or against particular aspects of adequacy.

For every diagnostic:

- define what it checks;
- provide the relevant formula or computation;
- explain the reference distribution/benchmark if one is used;
- state assumptions or regularity conditions;
- show R and Python implementations;
- interpret the actual output;
- explain how the result affects the next workflow decision.

Chapter 10's diagnostic sequence is an exemplar:

A. Observed versus fitted expected counts.
   - Define fitted expected counts.
   - Compare grouped observed and fitted means, such as across fitted-value quartiles.
   - Plot observed counts against fitted expected counts.
   - Distinguish in-sample fit from held-out prediction.

B. Mean-variance structure and overdispersion.
   - Define Pearson residuals.
   - Define the Pearson Chi-squared statistic.
   - Define the dispersion estimate, typically statistic divided by residual degrees of freedom.
   - State a one-sided overdispersion test when used.
   - Connect overdispersion to standard-error reliability.

C. Boundary or excess-zero check.
   - For a Poisson model, compare observed zero counts with the fitted expected number of zeros, $\sum_i \exp(-\widehat{\mu}_i)$.
   - If using an approximate z statistic, derive the Bernoulli-indicator variance and state the approximation's limitations.
   - Define survival-function calculations when they appear in p-value code.
   - Explain that a zero-count diagnostic is not identical to proving a zero-inflated data-generating process.

D. Residual deviance/global likelihood check.
   - Explain the saturated model.
   - give the model-specific deviance formula;
   - define residual degrees of freedom;
   - explain the approximate Chi-squared reference;
   - state the hypotheses and limitations.

E. Residual plot.
   - Plot appropriate residuals against fitted values or another relevant axis.
   - Explain patterns, heteroskedasticity, clusters, curvature, or extreme residuals.

F. Practical adequacy summary.
   - Combine the evidence in a Markdown table.
   - State whether the model is adequate for the intended inferential and predictive purposes.
   - Avoid declaring the model wholly useful or useless from one statistic.

For another model, design the corresponding model-specific diagnostic set. Examples may involve calibration, discrimination, proportional-odds checks, residual patterns, censoring assumptions, dispersion, boundary inflation, random-effects adequacy, or distributional shape.

======================================================================
19. MODEL EXTENSION AND REPEATED DIAGNOSTICS
======================================================================

If the simple model is inadequate or intentionally incomplete, return to the modelling stage and extend it using scientifically plausible regressors or structures already motivated in the study design and EDA.

Do not use unrestricted data dredging. Explain why each added regressor belongs in the model. Do not add polynomial terms, interactions, or other flexibility automatically; connect the refinement to a prespecified comparison, a concrete training-stage diagnostic, or a substantive modelling need.

When a likelihood-ratio test or another nested-model comparison is used to decide a training-stage refinement, always include:

1. the reduced and full models, written mathematically and described in plain language;
2. why the models are nested;
3. $H_0$ and $H_1$;
4. the test statistic;
5. the null reference distribution and degrees of freedom;
6. the actual rendered result;
7. the training-stage modelling decision that follows.

Do not report only a p-value. If the refinement is retained, update the named candidate model and all downstream mathematics/code to that specification.

For categorical regressors:

- define the reference category;
- show the dummy/indicator arrangement in a Markdown table;
- align R factor levels and Python treatment coding;
- define each dummy variable mathematically;
- explain what the intercept represents.

For ordinal categorical regressors, ordering alone does not imply equal spacing. Do not automatically enter raw codes such as `1,2,3,4` as one numerical regressor, and do not automatically introduce polynomial contrasts. Use treatment coding when separate category-versus-reference comparisons are the clearest approved representation, unless a scientifically justified ordinal structure is explicitly part of the chapter.

After fitting the extended or refined model on training data, repeat the same core diagnostics used for the earlier model. A diagnostic conclusion for an old specification does not automatically carry over after the model changes. This direct repetition allows the reader to see what improved and what did not.

Residual, leverage, influence, or related thresholds should be presented as screening heuristics unless the underlying method supplies a genuine decision rule. Crossing a heuristic threshold is not, by itself, a reason to delete an observation. Removal requires a substantive data-quality or study-population justification.

Do not merely say “the fit improved.” Compare evidence:

- observed-versus-fitted alignment;
- dispersion;
- boundary/zero behavior;
- deviance;
- residual patterns;
- practical adequacy.

Create an extended-model GOF summary table and, where useful, a comparison with the simple model.

If the extended model still fails important checks, say so clearly. It may remain a useful pedagogical baseline or mean-structure summary, but final standard errors, tests, intervals, and probabilistic predictions must carry visible caveats. Link the failure to the appropriate subsequent model chapter.

======================================================================
20. PARAMETER AND COEFFICIENT INTERPRETATION
======================================================================

Interpret parameters only after the relevant adequacy discussion.

Always distinguish:

- the model's native scale;
- the transformed or response scale;
- a one-unit change versus a substantively meaningful multi-unit change;
- continuous-regressor interpretations;
- categorical-regressor comparisons;
- intercept interpretation;
- fitted values versus held-out predictions.

For log-link count models, prefer “expected-count ratio” or “multiplicative change in the expected count.” The term “incidence-rate ratio” may be mentioned only when a genuine rate/exposure interpretation exists. Do not call every exponentiated Poisson coefficient an IRR by default.

Use “holding other regressors fixed,” not “holding all other variables constant.” The former correctly describes a conditional model comparison without implying an intervention.

For a coefficient $\beta_j$, show the algebra that produces the transformed-scale comparison. For example, take the ratio of expected responses after increasing a continuous regressor by one unit. For a $c$-unit change, use the corresponding exponentiated quantity. Define percent change carefully and note the direction.

For categorical regressors, compare each non-reference level with the reference category while holding other regressors fixed. Do not compare two non-reference categories by subtracting labels informally; derive the correct contrast if needed.

When a substantive regressor enters through multiple terms, such as a linear and quadratic contribution, interpret the terms jointly. Do not describe $\exp(\widehat{\beta}_1)$ and $\exp(\widehat{\beta}_2)$ as two independent constant effects if changing the regressor changes both terms. Use meaningful contrasts, fitted probabilities/means, derivatives, or another model-appropriate summary when that relationship is a substantive inferential target. If it is only an adjustment term and no such analysis was carried out, communicate only that the more flexible specification was retained; do not invent a detailed substantive shape.

When a table exponentiates every coefficient mechanically, label those columns carefully. “Exponentiated coefficient” is safer than a universal “odds ratio” or “rate ratio” label when some terms do not admit a standalone transformed-effect interpretation.

Use separate tables when necessary:

1. Native-scale estimates, SEs, test statistics, and p-values.
2. Transformed-scale estimates, confidence intervals, ratios, and percent changes.

Do not overload one table with so many columns that the statistical story becomes unreadable.

======================================================================
21. PREDICTION
======================================================================

Define precisely what the model predicts.

For Chapter 10, the fitted model predicts an expected count, not the exact realized count. Decimal expected counts are valid even though observed counts are integers. Include the analogous distinction for the target model:

- probability versus class;
- conditional mean versus realized outcome;
- median/quantile versus exact response;
- hazard/survival probability versus event time;
- latent score versus observed category.

Write the prediction equation for a new regressor vector. Define every element and show at least one manual or semi-manual calculation before relying entirely on software.

Generate test-set predictions from the training-fitted model only. Display a small first-rows table containing the observed outcome and the relevant predicted quantity.

Do not use the testing set to tune the model, choose variables, decide transformations, recalibrate probabilities, or change the threshold before final evaluation.

21.1 Additional rules for probability models and classifiers

When the model predicts event probabilities:

- keep the predicted probability distinct from the class assigned after thresholding;
- treat the classification threshold as a downstream decision rule, not as part of the fitted Logistic regression model itself;
- if $\tau=0.50$ is used only for illustration, say so explicitly;
- do not select a threshold because it optimizes testing accuracy, F1 score, sensitivity, specificity, or another testing metric;
- explain that an operational threshold should depend on the consequences of false positives/false negatives, intervention purpose, resources, fairness, and the intended use, and should be chosen independently of the final test evaluation or assessed on new data.

Evaluate multiple predictive properties rather than collapsing performance into one number:

- probability accuracy/proper scoring, such as log loss and Brier score when appropriate;
- ranking/discrimination, such as ROC AUC and average precision when appropriate;
- calibration, using grouped calibration and/or a calibration model when appropriate;
- threshold-dependent classification summaries only after the threshold is stated.

Do not infer improved calibration merely from a lower log loss or Brier score. Those metrics assess probability prediction quality but calibration must be examined separately.

When a held-out calibration regression is used, define the model mathematically and explain why ideal calibration corresponds to the relevant reference values. For the common Logistic calibration model,

$$
\operatorname{logit}\left[
\Pr\left(Y_i=1\mid\widehat{\pi}_i^{\,\text{train}}\right)
\right]
=
\alpha_{\text{cal}}
+
\gamma_{\text{cal}}
\operatorname{logit}\left(\widehat{\pi}_i^{\,\text{train}}\right),
$$

ideal calibration corresponds to $\alpha_{\text{cal}}=0$ and $\gamma_{\text{cal}}=1$. Interpret the intercept jointly with the slope. A slope below $1$ is consistent with predictions that are too extreme on the held-out sample; a slope above $1$ is consistent with predictions that are not dispersed enough.

Grouped calibration points are finite-sample summaries, not exact population identities. Explain the direction and size of important discrepancies without demanding that every group lie exactly on the diagonal.

Do not use a held-out calibration intercept/slope to recalibrate the model and then report the recalibrated performance on those same testing observations.

For ROC AUC, explain the pairwise ranking interpretation when pedagogically useful: the AUC is the probability that a randomly chosen positive observation receives a higher score than a randomly chosen negative observation, subject to the usual tie convention. Avoid calling a modest AUC “good” merely because it exceeds $0.50$.

======================================================================
22. RESULTS: KEEP INFERENCE AND PREDICTION SEPARATE
======================================================================

Open the Results section by revisiting the two guiding inquiries in a table. Then explain the two distinct final analyses.

22.1 Final inferential results

Refit the fixed, selected model specification on the testing data, following the book's sample-splitting workflow. Report:

- coefficient/parameter estimate;
- model-based standard error;
- test statistic;
- p-value, where relevant;
- confidence interval on the native scale;
- transformed estimate and transformed interval;
- substantive magnitude and direction.

State that this refit is for final inference, not additional model development.

22.2 Wald or model-specific tests

For every formal test, include:

1. Parameter being tested.
2. Null hypothesis.
3. Alternative hypothesis.
4. Test statistic.
5. Null reference distribution and regularity conditions.
6. Two-sided or one-sided p-value formula.
7. Decision rule or interpretation at the chosen level.
8. Equivalent null on a transformed scale, when applicable.
9. Applied interpretation.
10. Caution created by any failed model assumptions.

For a Wald test, explain that the statistic is the estimate divided by its model-based standard error. Be precise: a large absolute statistic means the estimate is far from the null relative to its model-based uncertainty; it does not establish causation or practical importance.

On an exponentiated scale, explain the equivalence between $H_0:\beta_j=0$ and $H_0:\exp(\beta_j)=1$.

Keep the warning visible when diagnostics call model-based standard errors into question. Do not present small p-values as definitive if the variance/distribution assumptions are strained.

22.3 Held-out predictive results

Evaluate the training-fitted model on testing observations. Include a simple baseline learned only from training data. In Chapter 10, the baseline predicted the training mean count for every testing observation.

Choose metrics appropriate to the model and inquiry. Explain what each metric emphasizes, its scale, and whether lower or higher is better.

Chapter 10 used:

- mean error, to assess average signed bias;
- MAE, for typical absolute error;
- RMSE, to penalize large errors more strongly;
- mean Poisson deviance, a likelihood-tailored discrepancy;
- average Kullback-Leibler discrepancy;
- mean negative log predictive probability.

It also explained that mean Poisson deviance is twice the average KL discrepancy, so those two metrics contain the same information on different scales.

For another chapter, adapt the metrics rather than copying these blindly. Use proper scoring rules or likelihood-based measures when the model supplies a full predictive distribution. Use “negative log predictive probability” or “mass” for discrete outcomes and “negative log predictive density” for continuous outcomes. Define the PMF/PDF notation before using it in a metric table.

Compare the model and baseline directly. State whether evidence is consistently better, consistently worse, or mixed across metrics. Do not declare predictive success from one favourable number. A training-stage likelihood improvement or significant model-comparison result does not, by itself, guarantee held-out predictive improvement.

For probability models, keep probability scores, discrimination, calibration, and threshold-dependent classification metrics conceptually separate in the prose. If a constant training-derived baseline predicts the majority class at a chosen threshold, explain why ordinary accuracy can be high even when specificity or balanced accuracy is poor.

22.4 Predictive results summary

Create a compact final table and prose that answer the predictive inquiry in practical units. For example, translate MAE/RMSE into the response's units and explain the operational consequence.

Where the chapter has both inference and prediction, include a final synthesis that explains why the two conclusions are not redundant. A statistically precise association for one regressor does not guarantee strong individual-level prediction, and a useful predictive model can derive performance from several terms jointly even when some individual coefficients are imprecise. Statistical significance, probability accuracy, discrimination, calibration, and threshold-based classification describe different properties and should not be substituted for one another.

======================================================================
23. STORYTELLING
======================================================================

The storytelling section is not a repetition of the Results tables. It translates the analysis for an applied audience while preserving statistical honesty.

Use a structure such as:

1. Main message.
2. What the association/inferential analysis suggests.
3. What the model can predict.
4. How the stakeholder should use the findings.
5. Key limitations and next steps.

The narrative must:

- answer the original inquiries directly;
- prioritize magnitude and uncertainty, not only p-values;
- use transformed-scale effects in accessible language;
- distinguish adjusted association from causation;
- distinguish expected/predicted quantities from exact outcomes;
- compare predictive performance with the baseline;
- explain practical prediction error;
- state the consequences of failed diagnostics;
- avoid labelling an outcome as inherently “good” or “bad” without domain justification;
- propose a responsible use of the model;
- identify the next model or data improvement when needed;
- avoid giving a detailed substantive interpretation to a secondary nonlinear/multi-term adjustment relationship unless the chapter actually computed the contrasts, fitted probabilities, derivatives, or other summaries needed to support that interpretation;
- distinguish “the training-stage evidence supported retaining a more flexible specification” from “the data establish a particular substantive shape.”

Where the prose depends on computed outputs, use carefully controlled inline values or verify every hard-coded number against the final executed results. The narrative must not become stale after code changes.

Do not hide an inconvenient result. If the baseline predicts better, say so and explain that the model may still have descriptive or inferential value, subject to assumptions.

======================================================================
24. CHAPTER SUMMARY
======================================================================

The summary should:

- revisit the type of response and problem the model addresses;
- recap the model's structural components;
- summarize estimation and interpretation;
- recap the main diagnostics;
- distinguish inferential and predictive uses;
- mention the role of the training/testing workflow;
- emphasize limitations.

Do not introduce new methods, notation, analyses, or results in the summary. Do not force a “Looking Ahead” subsection or forward-looking bridge merely because another chapter follows. Add a brief connection to another chapter only when it is pedagogically useful, already motivated by the current chapter, and consistent with the approved scope.

======================================================================
25. PRACTICE EXERCISES: CONCEPTUAL BANK
======================================================================

Use the finalized Question/Answer box structure established in the completed Chapters 2, 8, and 10.

Question template:

::: {.Question}
:::: {.Question-header}
Question X.Y
::::
:::: {.Question-container}
**Question type**

Question text.
::::
:::

Answer template:

::: {.Answer}
:::: {.Answer-header}
Answer X.Y
::::
:::: {.Answer-container}
<details>
<summary><strong>Click here to reveal the answer!</strong></summary>

Complete answer.

</details>
::::
:::

Use a mixed order of question types rather than separate blocks.

Do not use a fixed question count merely because another completed chapter used one. The number of conceptual questions should be large enough to cover the full chapter without becoming repetitive. Use a deliberate mixture of open-ended, multiple-choice, and true/false questions, with the balance adapted to the target chapter's scope. Chapter 8, for example, required a broader bank than Chapter 10 because it covered binary-response suitability, odds/log-odds, separation, calibration, discrimination, thresholding, inference/prediction distinctions, nonlinear terms, and predictive scoring.

The questions must cover the full chapter, including:

- when the model should and should not be used;
- response support and random component;
- systematic component and link/transformation;
- core assumptions;
- estimation and likelihood;
- coefficient/parameter interpretation;
- continuous and categorical regressors;
- reference categories and dummy variables;
- goodness-of-fit and diagnostics;
- assumption violations;
- uncertainty and formal tests;
- fitted versus predicted quantities;
- test-set prediction and baselines;
- metric interpretation;
- connections to alternative models.

Use fresh applied contexts rather than recycling the running case study. Chapter 10 used contexts such as libraries, hospitals, transit, call centres, city maintenance, websites, university help desks, restaurants, bike share, wildlife, retail, delivery, apps, and manufacturing. Choose similarly varied contexts appropriate to the target model.

Answers should be sufficiently detailed to teach, not one-word keys. However, they should remain focused and should not become new mini-chapters.

Terminology and notation in the exercises must match the final chapter. Do not revert to old terms such as “predictors,” “IRR” without context, “predicted count” for a fitted expected count, or a one-number definition of goodness of fit. Do not introduce code-variable names as mathematical coefficient subscripts or mathematical regressors merely because the applied context uses convenient software names. Define a mathematical symbol and use it consistently.

======================================================================
26. PRACTICE EXERCISES: SECOND FULL CODING CASE
======================================================================

After the conceptual bank, include a second applied dataset that does not reuse the running case. It should allow students to transfer the full workflow to a new context.

Wrap the scenario in the existing `.CodingCase`, `.CodingCase-header`, and `.CodingCase-container` structure.

The coding case should reproduce the chapter's statistical logic closely enough that students transfer the complete workflow to a new context, but it does not need a mechanically identical number of questions or subsection names. Include the stages that are actually relevant to the target model. A typical full case includes:

1. Practical scenario and stakeholder context.
2. Inferential inquiry.
3. Predictive inquiry.
4. Statistical model and notation.
5. Data understanding/variable table.
6. Data import and wrangling.
7. Response validity and missingness checks.
8. Inspection of ranges and unusual values.
9. Categorical coding and baseline choices.
10. Canonical training/testing split and cross-language alignment.
11. EDA of the response.
12. EDA with continuous regressors.
13. EDA with categorical regressors.
14. Simple/baseline model.
15. Mathematical model setup.
16. Likelihood/score or other model-specific mathematical work.
17. Simple-model diagnostics.
18. Extended model.
19. Dummy-variable mathematics and coefficient algebra.
20. Extended/refined-model diagnostics.
21. Manual prediction.
22. Freezing the final specification before examining testing outcomes, when the chapter uses training-stage refinement.
23. Final testing-set fixed-specification inferential refit.
24. Held-out predictions from the training-fitted model and baseline comparison.
25. Model-specific predictive checks such as calibration/discrimination/threshold summaries when relevant.
26. Final inferential and predictive synthesis.
27. Stakeholder-facing storytelling.

Include both conceptual and mathematical tasks. Chapter 10's enhanced doctor-visits case asked students to work with:

- random, systematic, and link components;
- response mean/variance calculations;
- coefficient-ratio algebra;
- the log-likelihood;
- score equations;
- dummy-variable model equations;
- manual expected-count prediction;
- KL discrepancy/proper predictive scoring.

Create corresponding tasks for the target model.

Do not include a method, such as an interaction, that the chapter has not taught unless it is clearly labelled as optional extension work.

Execute the entire exercise solution using the actual dataset. Prefer an approved local repository copy of the data for runtime reproducibility when one exists, while still citing the original source and documentation. The written interpretation must refer to the real outputs, not generic placeholders. R and Python solutions must use the same observations and produce equivalent results.

If a training-stage diagnostic or prespecified comparison changes the candidate specification, every downstream question, equation, code chunk, diagnostic, final inferential refit, prediction, calibration/discrimination analysis, and stakeholder summary must use the refined specification. Do not leave stale text from the pre-refinement model.

Use dynamic inline values for result-dependent prose when practical, or verify every hard-coded number against the final executed output. If the current executed result differs from an older screening calculation, update the exercise narrative to the current result rather than forcing the old story.

A useful pedagogical choice is to select an exercise dataset that contrasts with the running case. Chapter 10's running crab model remained diagnostically problematic, whereas the extended doctor-visits model showed much more acceptable dispersion/deviance behavior and outperformed its baseline. This demonstrated both how the model can fail and how it can work. Seek a similarly instructive contrast when feasible.

======================================================================
27. QUARTO CALLOUT AND FORMATTING CONVENTIONS
======================================================================

Use the book's existing classes consistently:

- `.Warning` for important use/not-use or validity warnings;
- `.Heads-up` for common misunderstandings and workflow distinctions;
- `.Tip` for optional context, historical notes, or practical alternatives;
- `.definition` with the established definition header/container structure;
- `.Question` and `.Answer` for conceptual exercises;
- `.CodingCase` for the applied exercise scenario.

Callouts must be purposeful. Avoid:

- repeating the immediately preceding paragraph;
- placing several callouts back to back;
- putting indispensable core explanation only in a callout;
- using a Warning for ordinary information;
- using a Tip to introduce a required assumption.

Use native Markdown tables with the established `.striped .hover` classes where appropriate.

Use `<br>` only when the book's rendering genuinely requires spacing; do not use repeated manual breaks as a substitute for sound structure.

======================================================================
28. REFERENCES, LINKS, AND ATTRIBUTION
======================================================================

Use reputable references:

- original methodological papers;
- major textbooks;
- official software documentation;
- original data sources;
- authoritative domain sources;
- primary historical sources where possible.

For technical claims, prefer primary or standard references. Verify that each source actually supports the claim.

For every new reference:

- check whether the BibTeX key already exists;
- add a complete, valid BibTeX entry if needed;
- use a stable DOI or publisher information where available;
- avoid duplicate keys or duplicate entries with slightly different metadata.

Link software functions to official documentation when the link helps students learn the syntax, but do not clutter every sentence with links.

Credit all images accurately. Check creator spelling, capitalization, source page, license expectations, and file path. Never distribute font files or unlicensed image assets.

======================================================================
29. SCOPE CONTROL AND CONNECTIONS TO OTHER CHAPTERS
======================================================================

The target chapter should be complete within its stated scope but should not absorb the contents of later chapters.

Use short forward references when diagnostics motivate a more flexible model. For a count chapter, these might include Negative Binomial, Generalized Poisson, Zero-Inflated Poisson, or mixed-effects count models. For another response type, link to the appropriate alternatives.

Do not solve every violation inside the current chapter. Explain the limitation, show why it matters, and point to the chapter designed to address it.

Preserve the chapter's role in the book sequence. Avoid re-teaching all of probability, all of OLS, or all of the GLM framework when a concise cross-reference is enough.

======================================================================
30. LANGUAGE AND TERMINOLOGY AUDIT
======================================================================

Before finalizing, audit the chapter for consistent terminology.

Use:

- “regressor” for a variable on the right-hand side of a regression model;
- “response variable” rather than switching among outcome/target without reason;
- “fitted expected count/mean/probability” for an in-sample fitted conditional quantity;
- “predicted expected count/mean/probability” for a new or held-out observation;
- “holding other regressors fixed” for adjusted comparisons;
- “expected-count ratio,” “odds ratio,” “hazard ratio,” or another model-specific transformed quantity only when mathematically appropriate;
- “model adequacy” rather than “model truth”;
- “evidence of lack of fit” rather than categorical declarations based solely on a p-value;
- “model-based standard error” when uncertainty depends on the assumed likelihood/variance.

Avoid:

- causal verbs for observational associations;
- “significant” without statistical and substantive context;
- “all other variables constant”;
- “good fit” based only on failure to reject;
- calling decimal expected values impossible because observed responses are discrete;
- calling a PMF a density;
- treating a fitted value as a realized prediction;
- implying that a baseline-free metric proves useful prediction;
- unexplained acronyms.

Smooth transitions. Avoid repetitive openings such as “Now,” “Then,” or “Hence” in consecutive paragraphs. Chapter 10 required a late-stage edit to replace an awkward “Hence” in its storytelling prose; make this a general language check.

======================================================================
31. FINAL TECHNICAL AND STATISTICAL QUALITY-CONTROL CHECKLIST
======================================================================

Perform a line-by-line QC pass before calling the chapter complete.

31.1 Structure

[ ] All required workflow stages are present.
[ ] Section order is logical.
[ ] Each section has a unique stable ID.
[ ] Transitions explain why the next stage follows.
[ ] Inferential and predictive inquiries remain visible throughout.
[ ] No chapter section is duplicated or stranded.

31.2 Mathematical notation

[ ] $\Pr(\cdot)$ is used consistently.
[ ] PMF/PDF notation uses the correct symbol and semicolon parameter convention.
[ ] Random variables and observations use uppercase/lowercase consistently.
[ ] Every symbol is defined before use.
[ ] Definition boxes are self-contained.
[ ] Numeric regressor subscripts are consistent.
[ ] Literal code-variable names do not appear as mathematical regressors or coefficient subscripts.
[ ] A mathematical symbol is not repurposed after its meaning has been fixed.
[ ] Multi-term representations of one substantive regressor are interpreted jointly.
[ ] Vector and matrix notation is bold and dimensionally coherent.
[ ] Distribution notation matches Chapter 2.
[ ] Equations are correctly labelled and referenced.
[ ] Hypotheses, statistics, and reference distributions are correct.

31.3 Statistical logic

[ ] The response support matches the model.
[ ] The study design supports the language used.
[ ] Training data are used for EDA/model development/diagnostics only.
[ ] Testing data are not used for model selection.
[ ] The final specification is explicitly frozen before testing outcomes are examined.
[ ] The final inferential refit uses the frozen specification.
[ ] Testing-set p-values do not reopen model selection.
[ ] Held-out predictions come from the training-fitted frozen model.
[ ] Held-out calibration or thresholds are not used to modify the model and then re-evaluate it on the same testing outcomes.
[ ] Variance/likelihood assumptions are explicitly connected to SEs and tests.
[ ] Diagnostics are model-specific and multi-layered.
[ ] Failed diagnostics remain visible in final inference and storytelling.
[ ] Prediction is compared with a training-derived baseline.
[ ] Metric definitions and directions are correct.
[ ] For probability models, probability accuracy, discrimination, calibration, and threshold-based classification are kept distinct.
[ ] Calibration is not inferred from log loss/Brier score alone.
[ ] Any classification threshold is justified as illustrative, prespecified, or operationally motivated rather than optimized on the final test set.
[ ] Screening heuristics are not treated as automatic deletion rules.
[ ] Any model change is followed by the relevant diagnostic rechecks.
[ ] No causal claim exceeds the design.

31.4 R/Python code

[ ] All code has been executed on the actual data.
[ ] R and Python use the same observations.
[ ] Reference categories match.
[ ] Transformations and units match.
[ ] Results agree within numerical tolerance.
[ ] Seeds and split logic are explained.
[ ] Python category types are restored after `reticulate` transfer.
[ ] Remote `.rda` files are downloaded locally before `pyreadr.read_r()`.
[ ] Every package is correctly spelled, installed/required, and used.
[ ] No unused dependency or misleading package comment remains.
[ ] Object names remain consistent across sections.
[ ] No hidden reliance on an object that is never created.
[ ] Warnings/messages are controlled without concealing real problems.

31.5 Tables and figures

[ ] Conceptual tables are native Markdown.
[ ] Computed R tables use compact, intentional displays.
[ ] Python tables use the shared `scrollable_table_html()` helper rather than scattered direct `.to_html()` calls.
[ ] Python tables render through hidden R/reticulate chunks with `results: asis`.
[ ] R/Python captions and columns correspond.
[ ] Labels are unique and include language suffixes where needed.
[ ] P-values use sensible precision.
[ ] Wide tables scroll rather than breaking layout.
[ ] Figures use the same samples, scales, ordering, smoothers, and reference lines.
[ ] Every added curve/reference line is explained.
[ ] Image credits and creator names are correct.
[ ] Plots and tables are referenced in the correct prose.

31.6 Quarto/rendering

[ ] The target chapter renders independently.
[ ] The full book renders in the intended formats.
[ ] Cross-references resolve.
[ ] Citations resolve.
[ ] Links work.
[ ] Images exist at the stated paths.
[ ] Panel tabsets open correctly.
[ ] HTML tables appear inside the intended tabs.
[ ] No raw code, HTML, warning, or error leaks into the published output.
[ ] Table and figure widths work on ordinary screens.
[ ] Mermaid content renders and enlarges correctly if used.

31.7 Cross-chapter copyediting details learned from Chapters 1, 2, 8, and 10

[ ] Use “coefficient vector,” not “regression term vector.”
[ ] Use lowercase “weighted least-squares” except in the formal IRLS name.
[ ] Use Chapter 2's distribution notation and capitalization.
[ ] Define PMF/PDF notation before using it in a predictive metric formula.
[ ] Explain a Wald statistic as estimate relative to model-based SE.
[ ] For every LRT/model-comparison decision, show competing models, nesting, hypotheses, statistic, reference distribution/df, actual result, and modelling consequence.
[ ] Keep p-value precision consistent in R and Python.
[ ] Check table headers for cramped mathematical notation and add sensible spacing.
[ ] Use “exponentiated coefficient” rather than a universal effect label when a multi-term coefficient lacks a standalone transformed interpretation.
[ ] Distinguish predictive probability from class assignment and from predictive density.
[ ] Do not call a deliberate feature exclusion “leakage” unless the timing/information structure actually makes it leakage.
[ ] Check every image-credit spelling and capitalization.
[ ] Remove stale package comments and unused imports.
[ ] Assign complex plots to descriptive objects before displaying them where practical.
[ ] Avoid awkward repetitive transitions.
[ ] Do not force a “Looking Ahead” section or add new material in the Chapter Summary.

======================================================================
32. REQUIRED RATIONALE-FILE FORMAT
======================================================================

For every proposed section, write the rationale file using this structure:

# Revision rationale for [section name]

## Scope
- Target chapter/file.
- Exact section ID(s).
- Reference chapters/files reviewed.

## What was preserved
- Valid concepts, examples, equations, code, references, or instructional choices retained from the original or earlier assistant draft.

## What changed
- Structural changes.
- Mathematical changes.
- Terminology changes.
- Code/output changes.
- Plot/table changes.
- New callouts or cross-references.
- Removed or relocated material.

## Why the changes help
- Statistical correctness.
- Pedagogical sequence.
- Alignment with the completed reference chapters, currently Chapters 1, 2, 8, and 10.
- Reproducibility.
- R/Python parity.
- Accessibility and storytelling.

## Execution and validation
- Data file used.
- Code executed.
- R/Python comparison.
- Render status.
- Any unresolved warnings.

## What should be avoided
- Specific old wording, outdated notation, inappropriate methods, unsupported claims, or code patterns that should not return.

## References to add or verify
- Citation keys.
- Complete BibTeX entries when needed.

## Placement and dependencies
- Exact replacement location.
- Cross-references needed.
- Later sections that must use the objects or notation introduced here.

For a final QC report, use exact `BEFORE / AFTER / RATIONALE` entries when reporting local corrections. Quote enough surrounding text or code that the replacement location is unambiguous; do not summarize a change when the contributor needs literal replacement text.

======================================================================
33. FINAL DELIVERY STANDARD
======================================================================

A chapter is not finished merely because it is long, contains equations, or runs a model. It is finished only when:

- the scientific/data-science inquiry is clear;
- the response and model are compatible;
- the mathematics and software agree;
- estimation is explained rather than hidden;
- assumptions are connected to uncertainty;
- diagnostics genuinely influence the workflow;
- inference and prediction are kept distinct;
- R and Python use the same data and tell the same statistical story;
- tables and figures are publication-ready;
- limitations remain visible in the final conclusions;
- the storytelling answers the stakeholder's question responsibly;
- the exercises reinforce the whole chapter rather than only software syntax;
- every source, cross-reference, and output has been verified; and
- the Quarto chapter and full book render successfully.

When adapting this protocol to a new chapter, state explicitly which conventions from the completed reference chapters are directly transferable, which require model-specific counterparts, and which are outside the approved scope. Use Chapter 1 for workflow, Chapter 2 for probability/inference notation, Chapter 8 for binary-probability/calibration/classification logic when relevant, and Chapter 10 for count-GLM/variance/diagnostic logic when relevant. The goal is consistency of reasoning and delivery across the cookbook, not superficial uniformity.

END OF MASTER PROMPT
