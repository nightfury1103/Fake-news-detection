from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe
import pickle


st.set_page_config(layout="centered", page_icon="🎓", page_title="NLP Predict")
st.title("🎓 Fake news prediction")

st.write(
    "This app shows you how you can use the machine learning to predict fake news!"
)

left, right = st.columns(2)

# right.write("Here's the template we'll be using:")

right.image("template.png", width=500)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")


left.write("Fill in the data:")
form = left.form("template_form")
student = form.text_input("Type a news")
course = form.selectbox(
    "Choose model",
    ["Multi-layer Perceptron", "Logistic classifier", "K-neighbour", "Naivebayes"],
    index=0,
)
# grade = form.slider("Grade", 1, 100, 60)
submit = form.form_submit_button("Check")

file = open("MLP.pkl",'rb')
if str(course) == 'Multi-layer Perceptron':
    file = open("MLP.pkl",'rb')
if str(course) == 'Logistic classifier':
    file = open("log_classifier.pkl",'rb')
if str(course) == 'K-neighbour':
    file = open("Kneighbor_classifier.pkl",'rb')
if str(course) == 'Naivebayes':
    file = open("naivebayes_classifier.pkl",'rb')

model = pickle.load(file)

if submit:
    with st.spinner("Predicting..."):
        left.markdown(course)
        if not len(student):
            left.warning('You must type a news!')
        else:
            # model = model_dict[model_name]

            # cleaned_news = text_preprocessing(news)

            # text_vectorized = tfidf_vectorizer.transform([cleaned_news])
                
            pred = model.predict([student])[0]

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
                data='abc',
                file_name="diploma.pdf",
                mime="application/octet-stream",
            )
