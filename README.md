# SMS Spam Classifier

A small end-to-end machine-learning project that classifies an SMS message as **spam** or **ham**. Built as a learning-by-building project: real dataset → data inspection → text features → model comparison → evaluation → saved model → deployed web app.

**Live demo:** https://sms-spam-classifier-vishnu.streamlit.app/  
**Source code:** https://github.com/mvishnuvardhan2229-dotcom/sms-spam-classifier

> **Scope and safety:** This is an educational SMS spam classifier trained on a historical dataset. It is not a financial-fraud detector, does not inspect links or verify accounts, and cannot prove that a message is safe. Do not paste private or sensitive messages into the public demo.

## What it does

1. Accepts an SMS message in a Streamlit web interface.
2. Loads a saved scikit-learn pipeline.
3. Converts text into numerical features using TF-IDF.
4. Predicts a label: `spam` or `ham`.
5. Displays the prediction and model scores, where available.

The saved pipeline contains both preprocessing and the classifier. Keeping them together ensures new messages receive the same text transformation used during training.

## Machine-learning workflow

```text
UCI SMS Spam Collection
        ↓
Inspect and clean the data
        ↓
Define X (message text) and y (label)
        ↓
Stratified train/test split
        ↓
TF-IDF text representation
        ↓
Compare Multinomial Naive Bayes and Logistic Regression
        ↓
Evaluate accuracy, spam precision, spam recall and spam F1
        ↓
Export fitted pipeline and evaluation metrics
        ↓
Streamlit web app
```

### Techniques used

- **Supervised text classification:** learns from labelled examples.
- **TF-IDF:** represents words and word pairs as numeric features.
- **scikit-learn Pipeline:** keeps text vectorization and classification together.
- **Multinomial Naive Bayes and Logistic Regression:** two candidate classifiers compared in the notebook.
- **Evaluation:** accuracy, spam precision, spam recall, spam F1-score and confusion matrix.
- **Streamlit:** provides the interactive web interface.
- **Joblib:** saves and reloads the fitted pipeline.

## Dataset and attribution

This project uses the **UCI SMS Spam Collection**.

- Dataset page: https://archive.ics.uci.edu/dataset/228/sms+spam+collection
- Citation: Almeida, T. & Hidalgo, J. (2011). *SMS Spam Collection*. UCI Machine Learning Repository.
- DOI: https://doi.org/10.24432/C5CC84
- Dataset licence shown by UCI: **CC BY 4.0**. Retain appropriate attribution and review the dataset page's terms when redistributing dataset-derived material.

The dataset contains SMS messages labelled as `ham` (normal) or `spam`. It is a historical English-language dataset, so results may not transfer to modern scams, Telugu-English code-mixed messages, other languages, or other messaging platforms.

## Repository structure

```text
sms-spam-classifier/
├── app.py
├── spam_classifier.joblib
├── requirements.txt
├── Dockerfile
├── README.md
└── notebooks/
    └── SMS_Spam_Classifier_Learning_by_Building.ipynb
```

Evaluation artifact:
- `metrics.json` — the measured metrics exported by the training notebook.
- `test_predictions.csv` — optional per-example predictions for error analysis; not required by the web app.

## Run locally

Requirements: Python 3 and pip.

### 1. Clone the repository

```bash
git clone git@github.com:mvishnuvardhan2229-dotcom/sms-spam-classifier.git
cd sms-spam-classifier
```

HTTPS clone also works if preferred.

### 2. Create and activate a virtual environment

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\\Scripts\\Activate.ps1
```

### 3. Install dependencies and run

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

Streamlit prints a local URL, usually http://localhost:8501.

The `spam_classifier.joblib` file must be in the same directory as `app.py`. Only load serialized model files from a source you trust. Scikit-learn models may not be compatible across arbitrary library versions; use compatible training and runtime dependencies.

## Deployment

The app is deployed on **Streamlit Community Cloud**:

https://sms-spam-classifier-vishnu.streamlit.app/

The deployment is connected to this GitHub repository. Changes pushed to the configured branch can trigger a redeployment.

## Evaluation and honest reporting

The notebook compares models using the same held-out test split and selects a candidate based on spam-class F1 in this teaching workflow. Review the exported `metrics.json` and confusion matrix before reporting performance.

| Metric | What it tells us |
|---|---|
| Accuracy | Fraction of all test messages classified correctly |
| Spam precision | Of messages predicted as spam, how many were labelled spam |
| Spam recall | Of actual spam messages, how many the model caught |
| Spam F1-score | Balance between spam precision and spam recall |
| Confusion matrix | Counts correct and incorrect predictions by actual and predicted class |

### Measured test-set results

These values are copied from the committed `metrics.json` produced by the notebook run:

| Metric | Measured value | Interpretation |
|---|---:|---|
| Selected model | Logistic Regression | Highest spam-class F1 among the two candidates in this notebook run |
| Test messages | 1,032 | Number of examples in the evaluation split |
| Accuracy | 97.77% | Fraction of all test messages classified correctly |
| Spam precision | 88.32% | Of messages predicted as spam, the fraction labelled spam |
| Spam recall | 94.53% | Of actual spam messages in the test split, the fraction caught |
| Spam F1-score | 91.32% | Harmonic mean of spam precision and spam recall |

Interpretation: the model caught a high proportion of the test-set spam examples, while its lower spam precision means some legitimate messages were also flagged as spam. These are test-set measurements for this dataset and split, not guarantees for future messages.

**Evaluation caveat:** this learning notebook selects the model using spam F1 calculated on the same split used for reporting. That makes the test set part of model selection, so the reported metrics may be somewhat optimistic. For a stronger next iteration, compare models on a validation split or with cross-validation, then evaluate the chosen model once on a separate untouched test set. Manual demo examples are smoke tests, not a substitute for formal evaluation.

## Limitations

- The model learns patterns in the training dataset; it does not understand intent the way a human investigator does.
- Model scores are not necessarily calibrated probabilities.
- A false positive may flag a legitimate message; a false negative may miss spam.
- It does not check URLs, sender identity, bank accounts, or transaction activity.
- It is not validated for financial fraud detection or real-world security decisions.
- Do not enter private, financial, medical, or otherwise sensitive messages in the public demo.

## Learning outcomes

This project demonstrates a complete beginner-friendly ML workflow: acquiring a real dataset, inspecting and cleaning data, avoiding test-set leakage through a pipeline, comparing models, evaluating classification errors, serializing a fitted model, and deploying a small web application.

## Future improvements

- Pin and document exact Python and scikit-learn versions for reproducible deployment.
- Add tests for model loading and prediction behaviour.
- Add a documented evaluation summary and inspect false positives/false negatives.
- Evaluate on a newer, appropriately licensed dataset before claiming support for current scams or other languages.

---
Built as a learning-by-building Data Science Lab project.
