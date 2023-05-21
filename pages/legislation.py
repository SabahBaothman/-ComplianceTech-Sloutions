
import streamlit as st
import streamlit.components.v1 as components

st.write("")
st.write("")
st.title(" Organizations related to your company ")  
st.write("")
st.write("- General Commission for Audiovisual")
st.write("- Saudi Broadcasting Authority")

st.title("Your company's regulations")  
# Define checkboxes 
check1 = st.checkbox("Policy")  
page1_button = '<button onclick="window.open(\'/Policy\', \'_blank\');">Read More</button>' 
components.html(page1_button, height=50)
check2 = st.checkbox("Standards") 
page2_button = '<button onclick="window.open(\'/main\', \'_blank\');">Read More</button>' 
components.html(page2_button, height=50)
check3 = st.checkbox("regulations form") 
page3_button = '<button onclick="window.open(\'/main\', \'_blank\');">Read More</button>' 
components.html(page3_button, height=50)

# Define function to check if all checkboxes are selected 
def all_checks_selected():     
 return check1 and check2 and check3  
# Add button to check if all checkboxes are selected 
if st.button("Check All"):     
   if all_checks_selected() :         
    st.success("All three checkboxes are selected!")

else:         
  st.warning("Please select all three checkboxes to continue.") 
  # Add recommendations for the user         
  if not check1:             
    st.write("- Check 1 is not selected. Do you want some recommndation about it?.") 
            
  if not check2:             
    st.write("- Check 2 is not selected. Do you want some recommndation about it?.")         
  if not check3:             
      st.write("- Check 3 is not selected. Do you want some recommndation about it?.")
