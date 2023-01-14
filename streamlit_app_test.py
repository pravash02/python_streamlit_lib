# streamlit run streamlit_app.py

import streamlit as st
import pandas as pd
from datetime import datetime

print(eval('(datetime(2022, 10, 12))'))

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

js = st.json({

    'fruit':'apple',

    'book': 'maths',

    'game' : 'football'

})
json_obj = {

    'fruit':'apple',

    'book': 'maths',

    'game' : 'football'

}

df = pd.read_json(js)
