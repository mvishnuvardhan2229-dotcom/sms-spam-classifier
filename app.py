from pathlib import Path
import joblib
import streamlit as st

APP_DIR = Path(__file__).resolve().parent
MODEL_PATH = APP_DIR / "spam_classifier.joblib"

st.set_page_config(page_title="SMS Spam Classifier", page_icon="🛡️", layout="centered")

@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        return None
    return joblib.load(MODEL_PATH)

st.title("🛡️ SMS Spam Classifier")
st.write(
    "A small machine-learning demo trained on the UCI SMS Spam Collection. "
    "Enter a message to see the model's prediction."
)
st.warning(
    "Educational demo only. It detects patterns similar to this historical SMS dataset; "
    "it does not prove a message is safe, and it is not a financial-fraud detector."
)

model = load_model()
if model is None:
    st.error("Model file not found. Run the Colab notebook, download artifacts/spam_classifier.joblib, and place it beside app.py.")
    st.stop()

message = st.text_area("Message text", height=140, placeholder="Paste a suspicious or normal SMS here...")
if st.button("Classify message", type="primary", disabled=not message.strip()):
    prediction = model.predict([message.strip()])[0]
    st.subheader("Prediction")
    if prediction == "spam":
        st.error("Likely SPAM based on the model")
    else:
        st.success("Likely HAM (normal message) based on the model")

    if hasattr(model, "predict_proba"):
        classes = list(model.classes_)
        probabilities = model.predict_proba([message.strip()])[0]
        scores = {str(label): float(score) for label, score in zip(classes, probabilities)}
        st.write("Model scores (not a guarantee of safety)")
        st.bar_chart(scores)
        st.caption("These scores are model outputs and may not be calibrated probabilities.")

with st.expander("How it works"):
    st.markdown(
        """
        1. TF-IDF converts the message into numeric word/phrase features.
        2. A classifier predicts `spam` or `ham`.
        3. The complete fitted pipeline is loaded from `spam_classifier.joblib`.

        Dataset: [UCI SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)  
        Citation: Almeida & Hidalgo (2011), DOI: [10.24432/C5CC84](https://doi.org/10.24432/C5CC84). Licensed CC BY 4.0.
        """
    )

st.caption("Do not paste private, financial, medical, or otherwise sensitive messages into a public demo.")
