import streamlit as st
import base64
from streamlit_option_menu import option_menu

def home():
    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="Coline Ritz's Portfolio",
        page_icon="🍕",
    )

    page = st.sidebar.selectbox("Select a Page", ["About me", "My projects"])

    # First Page
    if page == "About me":
        homepage()

    # Second Page
    elif page == "My projects":
        analyseddata()


def homepage():

    # CSS styles file (if any)
    with open("styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image file
    with open("assets/IMG_0644.JPG", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

    # PDF CV file
    with open("assets/CV (1).pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Top title
    st.write(f"""<div class="title"><strong>Hi! My name is</strong> Coline Ritz👋</div>""", unsafe_allow_html=True)

    # Profile image
    st.write(f"""
    <div class="container">
        <div class="box">
            <div class="spin-container">
                <div class="shape">
                    <div class="bd">
                        <img src="{img}" alt="Coline Ritz">
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Subtitle
    st.write(f"""<div class="subtitle" style="text-align: center;">Design Engineer</div>""", unsafe_allow_html=True)

    # Social Icons
    social_icons_data = {
        "LinkedIn": ["https://www.linkedin.com/in/e-domingo", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/enricd", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"]
    }

    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", unsafe_allow_html=True)

    st.write("##")

    # About me section
    st.subheader("About Me")
    st.write("""
    - 🧑‍💻 I am a **Senior ML and Software Engineer** @ [ERNI](https://www.betterask.erni/) working on a [Boehringer Ingelheim](https://www.boehringer-ingelheim.com)'s pharma project 

    - 🛩️ prev: Co-founder, Flight Ops Manager and UAS Developer Pilot @ [Venturi Unmanned Technologies](https://www.youtube.com/@venturiunmannedtechnologie2518/featured)

    - ❤️ I am passionate about **Machine Learning/Deep Learning, MLOps, Data, Software Engineering, Computer Vision, Bioinformatics, UAVs, Optimization, Automation**, and more!
    
    - 🤖 I enjoy developing projects such as [SpeedClimbing.AI](https://www.instagram.com/speedclimbing.ai) (🏗️under construction) and participating at platforms like [Kaggle](https://www.kaggle.com/edomingo) 📈
    
    - 🏂 Also practicing sports such as snowboard, wakeboard and climbing 🧗
    
    - 📫 How to reach me: ritzcoline@gmail.com
    
    - 🏠 Europe
    """)

    st.write("##")

    # Download CV button
    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="Colie_Ritz_CV.pdf",
        mime="application/pdf",
    )


def analyseddata():

    # CSS styles file (if any)
    with open("styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
    projects = {
        "Project 1: ML-based SpeedClimbing": "Description of the project...",
        "Project 2: UAS Development": "Another description here...",
        "Project 3: Kaggle Data Science Challenge": "Details of this Kaggle competition...",
        "Project 4: MLOps Pharma Project": "Info about a pharma project...",
    }

    # Create the dropdown menu for project selection
    selected_project = st.selectbox("Select a Project", list(projects.keys()))

    # Display selected project details
    st.subheader(f"Details about {selected_project}")
    st.write(projects[selected_project])


if __name__ == "__main__":
    home()