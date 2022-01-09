from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe
import pickle
from preprocessing import text_preprocessing

st.set_page_config(layout="centered", page_icon="🎓", page_title="NLP Predict")
st.title("🎓 Fake news prediction")

st.write(
    "This app shows you how you can use the machine learning to predict fake news!"
)

left, right = st.columns(2)

right.write("Your answer will show below the image!")

right.image("template.png", width=500)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")

left.write("Fill in the data:")
form = left.form("template_form")
student = form.text_input("Type a news")
course = form.selectbox(
    "Choose model",
    ["Multi-layer Perceptron", "Logistic classifier", "K-neighbour", "Naivebayes", "Random Forest"],
    index=0,
)
# grade = form.slider("Grade", 1, 100, 60)
submit = form.form_submit_button("Check")

file_name = "mlp_classifier.pkl"
if str(course) == 'Multi-layer Perceptron':
    file_name = "mlp_classifier.pkl"
if str(course) == 'Logistic classifier':
    file_name = "log_classifier.pkl"
if str(course) == 'K-neighbour':
    file_name = "Kneighbor_classifier.pkl"
if str(course) == 'Naivebayes':
    file_name = "naivebayes_classifier.pkl"
if str(course) == 'Random Forest':
    file_name = "RandomForest_classifier.pkl"

file = open(file_name, 'rb')

model = pickle.load(file)

if submit:
    with st.spinner("Predicting..."):
        left.markdown(f"You choose {course} model!")
        if not len(student):
            left.warning('You must type a news!')
        else:
            # model = model_dict[model_name]

            # cleaned_news = text_preprocessing(news)

            # text_vectorized = tfidf_vectorizer.transform([cleaned_news])

            cleaned_news = text_preprocessing(student)
            left.markdown(cleaned_news)
            pred = model.predict([cleaned_news])[0]

            if pred == 1:
                right.success("🎉 Real news!")
            else:
                right.success("🎉 Fake news!")

            st.balloons()

            # right.success("🎉 Your diploma was generated!")
            # st.write(html, unsafe_allow_html=True)
            # st.write("")
            right.download_button(
                "⬇️ Download models",
                data=file_name,
                file_name=file_name,
                mime="application/octet-stream",
            )
