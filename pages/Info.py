import streamlit as st 
import streamlit.components.v1 as components


st.write("")
st.write("")


st.title("Enter your company information")  
company_name = st.text_input("Company Name") 
company_field = st.selectbox("Field of the Company", ["Technology", "Finance", "Healthcare","Media"])
company_name = st.text_input("Describe the company") 
company_size = st.slider("Company Size", 1, 5000, 10) 


st.write("")
st.write("")

# Add a button to try the platform 
if st.button("Send it"):     
        # Redirect to another page 
    components.html(f"""<a href="/legislation" target="_blank">Click here</a>""") 
     

 



