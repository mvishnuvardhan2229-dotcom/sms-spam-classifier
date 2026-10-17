# SMS Spam Classifier — Learning by Building

A deployable machine-learning demo that classifies SMS text as `spam` or `ham` using a fitted TF-IDF + scikit-learn pipeline.

## Dataset and attribution

- Dataset: [UCI SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)
- Citation: Almeida, T. & Hidalgo, J. (2011). *SMS Spam Collection*. UCI Machine Learning Repository. https://doi.org/10.24432/C5CC84
- License: CC BY 4.0. Please retain attribution when redistributing dataset-derived work.

## Important limitation

This model learns patterns from a historical SMS spam dataset. It is not a financial fraud detector, does not validate links or accounts, and cannot guarantee a message is safe. It may perform poorly on new scams, regional languages, code-mixed messages, or other domains.

## Files

- `notebooks/SMS_Spam_Classifier_Learning_by_Building.ipynb` — guided, reproducible training notebook
- `app.py` — Streamlit demo
- `requirements.txt` — Python dependencies
- `spam_classifier.joblib` — **add this after training in Colab**
- `metrics.json` — optional measured metrics exported by the notebook

## Run locally

1. Open and run the notebook in Google Colab.
2. Download `artifacts/spam_classifier.joblib` from Colab.
3. Put `spam_classifier.joblib` beside `app.py` in this repository root.
4. Install dependencies and launch:

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows:
# .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Community Cloud

1. Push this repository to your GitHub account, including `app.py`, `requirements.txt`, and the trained `spam_classifier.joblib`.
2. Visit https://share.streamlit.io/
3. Create an app and select your repository, branch, and `app.py`.
4. Deploy. See the [official deployment guide](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy).

## Deploy to Hugging Face Spaces

Hugging Face's built-in Streamlit SDK is deprecated for new Spaces; use a **Docker Space** for Streamlit.

1. Create a new Space at https://huggingface.co/new-space and choose **Docker**.
2. Add `app.py`, `requirements.txt`, `Dockerfile`, `README.md`, and `spam_classifier.joblib`.
3. Commit/push the files. Spaces builds and restarts the app.
4. See [Docker Spaces documentation](https://huggingface.co/docs/hub/spaces-sdks-docker).

## Evaluation checklist

Run the notebook and record actual:
- Accuracy
- Spam precision
- Spam recall
- Spam F1-score
- Confusion matrix
- A few false positives and false negatives

Do not add unmeasured performance claims to your portfolio post.
