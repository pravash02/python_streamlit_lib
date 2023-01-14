## prerequisites ##
# pip install googletrans==4.0.0rc1
# pip install itranslate


import google_trans_new as gtn
import streamlit as st

translator = gtn.google_translator()
st.title('Google translator using streamlit')

src_text = st.text_input('please enter your text')
print(src_text)
translated_text = translator.translate(src_text, lang_tgt='fr')

st.write(translated_text)
