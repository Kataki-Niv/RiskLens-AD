# RiskLens-AD

**Interpretable Machine Learning for Alzheimer’s Risk Stratification**

---

## Overview

RiskLens-AD is an interpretable machine learning framework designed to assess Alzheimer's disease risk using structural brain and cognitive features.

Instead of producing a simple binary diagnosis, the system introduces a **risk-stratification approach** that categorizes patients into:

* Low Risk
* Uncertain Risk
* High Risk

This provides more clinically meaningful insights than traditional classification systems.

The project emphasizes **interpretability, transparency, and patient-level reasoning**, making it suitable for healthcare decision support scenarios.

---

## Research Contribution

RiskLens-AD explores an interpretable machine learning approach for early Alzheimer’s risk assessment. The project contributes:

• A risk-stratification framework replacing binary diagnosis
• Explicit uncertainty bands for safer decision support
• Age-adjusted brain atrophy modeling
• Patient-level visualization in cognition–atrophy space
• A reproducible research notebook for transparent experimentation

## Hackathon Recognition

RiskLens-AD was developed during a hackathon focused on innovative applications of AI in healthcare.

The project received an **Honorable Mention** for its emphasis on interpretable medical AI and transparent risk modelling.

Devpost Submission:
https://devpost.com/software/risklens-ad

---

## Problem Motivation

Many machine learning models for Alzheimer's disease prediction rely on **black-box models** and produce binary outputs.

However, clinical decision making rarely operates in a strictly binary way. Physicians must often deal with **uncertainty and varying levels of risk**.

RiskLens-AD addresses this gap by:

* Using **interpretable models instead of opaque architectures**
* Introducing **explicit uncertainty bands**
* Visualizing patient risk in a **cognition–atrophy feature space**
* Safety-First Triage: By intentionally classifying ambiguous cases as "Uncertain", the system avoids overconfident predictions that could delay clinical intervention or cause unnecessary patient anxiety.


This allows the model to support **risk assessment rather than automated diagnosis**.

---

## Methodology

### Dataset

The project uses the **OASIS Longitudinal MRI Dataset**, which contains brain imaging and cognitive assessment information for subjects across multiple timepoints.

Dataset source:
https://www.oasis-brains.org/

---

### Key Steps

1. **Data preprocessing and cleaning**
2. **Modeling expected brain volume as a function of age to isolate abnormal neurodegeneration from normal aging.**
3. **Quantifying the Cognitive-Brain Mismatch—identifying subjects whose cognitive performance is disproportionately low relative to their structural brain health while accounting for educational background.**
4. **Feature scaling**
5. **Logistic Regression modelling enabling direct inspection of feature contributions and transparent clinical reasoning.**
6. **Risk band stratification**
7. **Patient-level interpretability analysis**
8. **Model evaluation using a held-out test set to ensure reproducibility and robustness.**


---

## Features

RiskLens-AD includes several interpretability-focused components:

* Age-adjusted brain atrophy estimation
* Cognitive reserve index
* Logistic Regression based risk prediction
* Explicit **risk-band uncertainty modelling**
* Visualization of **cognition vs atrophy space**
* Patient-level explanation of predictions

---

## Project Structure

```
RiskLens-AD
│
├── notebooks/          # Reproducible ML notebook
├── src/                # Modular Python code (future extensions)
├── results/            # Generated visualizations
├── data/               # Dataset access instructions
├── report/             # Project documentation
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## How to Run

1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/RiskLens-AD.git
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Open the notebook

```
notebooks/risklens_ad_reproducible.ipynb
```

4. Run all cells to reproduce the analysis.

---

## Results

The model produces:

* ROC-AUC evaluation metrics
* Risk band stratification
* Cognition vs Atrophy visualization
* Patient-level explanations

![Cognition vs Atrophy Risk Space](results/cognition_atrophy_space.png)


These outputs demonstrate how interpretable models can support clinical reasoning in neurodegenerative disease risk assessment.

---

## Reproducibility

This repository is structured to support reproducible research:

• The full experimental pipeline is available in the notebook
• Dataset access instructions are provided in the data folder
• All dependencies are listed in requirements.txt
• The methodology is documented in the accompanying report

## Future Improvements

Possible extensions of the project include:

* Integration with neuroimaging pipelines
* Explainable AI techniques such as SHAP or LIME
* External dataset validation
* Interactive clinical decision support interface

---

## Author

Developed by **Nivedana** during a hackathon project focused on interpretable machine learning for medical risk assessment.

Devpost Submission:
https://devpost.com/software/risklens-ad
