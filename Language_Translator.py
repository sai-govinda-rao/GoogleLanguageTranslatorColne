import streamlit as sl
sl.set_page_config(
    page_title="language Translator",
    page_icon="img_1.png"
)
language_dict = \
        {
        "Telugu": "te",
        "English": "en",
        "Hindi": "hi",
        "Sanskrit": "sa",
        "Tamil": "ta",
        "Kannada": "kn",
        "Malayalam": "ml",
        "Oriya": "or",
        "Punjabi": "pa",
        "Urdu": "ur",
        "Arabic": "ar",
        "Japanese": "ja",
        "Russian": "ru",
        "Nepali": "ne",
        "Marathi": "mr",
        "Dutch": "nl",
        "German": "de",
        "Norwegian": "no",
        "French": "fr",
        "Latin": "la",
        "Italian": "it",
        "Spanish": "es",
        "Romanian": "ro",
        "Mizo": "lus",
        "Zulu": "zu",
        "Esperanto(UK)": "eo"
        }
l1 = ["None"]
for i in language_dict:
    l1.append(i)
lang_list = tuple(l1)
sl.markdown("<center><h1><b>Language Translator</b></h1></center>", unsafe_allow_html=True)
col1, col2 = sl.columns(2)
col1.markdown("<h3>From Language</h3>", unsafe_allow_html=True)
col2.markdown("<h3>To Language</h3>", unsafe_allow_html=True)
from_lang = col1.selectbox("label1", l1, label_visibility="collapsed")
to_lang = col2.selectbox("label2", l1, label_visibility="collapsed")
sl.session_state.box1 = ""
sl.session_state.box2 = ""
sl.session_state.box1 = col1.text_area("Text1", placeholder="Enter Text", label_visibility="collapsed", height=150)
if sl.session_state.box1 and from_lang != "None" and to_lang != "None":
    from deep_translator import GoogleTranslator
    translator_obj = GoogleTranslator(source=language_dict[from_lang], target=language_dict[to_lang])
    translation_text = translator_obj.translate(sl.session_state.box1)
    sl.session_state.box2 = translation_text
col2.text_area("Text2", sl.session_state.box2, key="box2", placeholder="Translation", label_visibility="collapsed", height=150)
