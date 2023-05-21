import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
from PIL import Image
#from multiapp import MultiApp
#from pages import main 
import streamlit.components.v1 as components


#Title
PAGE_TITLE = "ComplianceTech Sloutions"
st.set_page_config(page_title=PAGE_TITLE)

    # --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "m.css"
pic = current_dir / "assets" / "pic.png"

# navbar 
selected = option_menu(
            menu_title=None,  # required
            options=["Home", "About us", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#46AFCC"},
                "icon": {"color": "white", "font-size": "15px"},
                "nav-link": {
                    "font-size": "15px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "black"},
            },
        )
#End of navbar 

if selected == "Home":
 # Set page title and subtitle 
 st.title("") 
 st.write("") 
 st.title("ComplianceTech Sloutions") 
 #st.subheader("This is our web")  
 # Add content to the page 
 st.write("Analyze and interpret regulatory documents and policies. To startup!")
 st.title("") 
 st.write("") 
 st.markdown("----")


 #info
 NAME = "Ready to get started?"
 DESCRIPTION = """
 Click the 'Try it' button under to see how ComplianceTech Sloutions can help you Analyze and interpret organizational documents and policies based on the sector you choose!.
 """

 # --- LOAD CSS, PDF & PROFIL PIC ---
 with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

 pic = Image.open(pic)

 # --- HERO SECTION ---
 col1, col2 = st.columns(2, gap="small")
 with col1:
    st.image(pic, width=230)

 with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    
    # Add a button to try the platform 
  #  if st.button("Try it"):     
        # Redirect to another page  
        #st.title(f"You have selected {selected}")   
          # Set the current page to the selected option 
      #  session_state.current_page = selected

       #Add a button to try the platform     
    if st.button("Try it"):         
       # Redirect to another page         
      components.html(f"""<a href="/Info" target="_blank">Click here</a>""")

if selected == "About us":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")