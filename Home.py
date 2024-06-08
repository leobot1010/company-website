import streamlit as st
import pandas

st.set_page_config(layout="wide")
df = pandas.read_csv('data.csv')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     HEADING     <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

st.title('The Best Company')

content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua. Lacus sed viverra tellus in hac. Dictum non consectetur a erat nam at lectus. 
Adipiscing elit pellentesque habitant morbi. Tristique risus nec feugiat in fermentum posuere urna nec. 
Venenatis tellus in metus vulputate. Pretium aenean pharetra magna ac placerat vestibulum. Sed risus ultricies 
tristique nulla aliquet. Cursus risus at ultrices mi. Sollicitudin tempor id eu nisl nunc mi ipsum faucibus. 
"""

st.write(content)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    OUR TEAM     <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

st.subheader('Our Team')

col1, space_col1, col2, space_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

with col1:
    for index, row in df[:4].iterrows():
        fullname = (row['first name'].strip() + ' ' + row['last name'].strip()).title()
        st.subheader(fullname)
        st.write(row['role'])
        st.image("images/" + row["image"])
        st.write('')
        st.write('')
        st.write('')

with col2:
    for index, row in df[4:8].iterrows():
        fullname = (row['first name'].strip() + ' ' + row['last name'].strip()).title()
        st.subheader(fullname)
        st.write(row['role'])
        st.image("images/" + row["image"])
        st.write('')
        st.write('')
        st.write('')

with col3:
    for index, row in df[8:12].iterrows():
        fullname = (row['first name'].strip() + ' ' + row['last name'].strip()).title()
        st.subheader(fullname)
        st.write(row['role'])
        st.image("images/" + row["image"])
        st.write('')
        st.write('')
        st.write('')


