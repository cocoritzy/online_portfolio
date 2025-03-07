import streamlit as st
import base64
import streamlit.components.v1 as components

def home():
    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="Coline Ritz's Portfolio",
        page_icon="💡",  # Changed pizza to a tech-related lightbulb icon
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
    st.write(f"""<div class="title"><strong>Hi! I am </strong> Coline, a Design Engineer 👋</div>""", unsafe_allow_html=True)

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

    # Social Icons
    social_icons_data = {
        "LinkedIn": ["https://www.linkedin.com/in/e-domingo", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/enricd", "https://cdn-icons-png.flaticon.com/512/25/25231.png"]
    }

    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", unsafe_allow_html=True)

    # About me section
    st.subheader("About Me")
    st.write("""
    🧑‍💻 I am a **Design Engineer** teaching @ [Data bird](https://www.data-bird.co/)
    
    ✨ I design, build, and innovate — turning ideas into sustainable solutions
    
    🌱 I have experiences in Sustainable IT and AI @[IJO](https://ijo.tech/index.html) and in carbon removal technologies @[DSS+](https://www.consultdss.com/)
             
    ❤️ I hold a Master Degree from @ [Imperial College](https://www.imperial.ac.uk/)
  
    🤖 I created of a climate collective [Ecocircular](https://www.instagram.com/ecocircular_/?hl=fr)
             
    """)

    # Download CV button
    st.download_button(
        label="Download my resume",
        data=pdf_bytes,
        file_name="Coline_Ritz_CV.pdf",
        mime="application/pdf",
    )

        # Embed the carbon badge
    carbon_badge = """
    <div id="wcb" class="carbonbadge"></div>
    <script src="https://unpkg.com/website-carbon-badges@1.1.3/b.min.js" defer></script>
    """

    # Use components.html to render the badge
    components.html(carbon_badge, height=100)

def internet_carbon_footprint():
    """Detailed project page for Internet Carbon Footprint"""

    st.title("🌍 The Internet's Carbon Footprint")

    st.markdown("""
    The internet is an invisible but significant contributor to **global carbon emissions**.  
    Data centers, networks, and devices consume vast amounts of electricity, with estimates suggesting that **the internet is responsible for 2-4% of global CO₂ emissions**—comparable to the aviation industry! ✈️🌍  

    ### 🔍 The Problem
    Internet usage is growing at a 26% compound annual growth rate (CAGR), contributing 7% of global electricity consumption and 3.5% of global greenhouse gas (GHG) emissions. If unchecked, Internet-related emissions could reach 14% of global GHG emissions by 2040. Current tools for measuring Internet carbon footprints are often inaccurate, with estimates varying by 5 orders of magnitude. 
    """)

    # Display image (Replace with actual project image)
    st.image("assets/internet.JPG", caption="Internet carbon footprint", use_container_width=True)

    ("""
    ### So... here is what is created
    The Internet Carbon Emission (I.C.E) tool is a real-time Internet carbon footprint analyzer designed to increase user awareness and encourage sustainable behavior. It combines a network traffic analyzer with a machine learning (ML) classifier to track and classify Internet usage, providing personalized feedback on carbon emissions.
    import streamlit as st
  """)
    # Load your images (replace with your image paths)
    image1 = "assets/firstpage.png"
    image2 = "assets/secondpage.png"

    # Create two columns
    col1, col2 = st.columns(2)

    # Display the first image in the first column
    with col1:
        st.image(image1, caption="Image 1", use_container_width=True)

    # Display the second image in the second column
    with col2:
        st.image(image2, caption="Image 2", use_container_width=True)
    ("""
    ### How does it work?
    1. Data Collection: The tool uses Wireshark to capture network traffic and nDPI to classify data flows.

    2. Data Transformation: A Random Forest ML model classifies 35 common applications, converting data usage (GB) into carbon emissions (CO₂e) based on location-specific energy grids.

    3. Visualization: A web interface displays real-time carbon footprints, personalized tips, and comparisons with peers.

     """)
    # Display image (Replace with actual project image)
    st.image("assets/system.JPG", caption="The architecture", use_container_width=True)

    st.markdown("""
    ### The results
    Video streaming (e.g., YouTube, Netflix) and cloud storage were major contributors to emissions. Personalized feedback and notifications effectively reduced energy consumption.

    ### References
    - Aslan et al. (2018) - Electricity intensity of Internet data transmission.
    - Andrae & Edler (2015) - Global electricity usage of communication technology.
    - Greenpeace’s Click Clean Report (2016) - Breakdown of data traffic per application.         
    """)

def ernegy_consumption():

    st.title("🌍 Energy consumption")

    st.markdown(""" Can social media influence energy consumption?

    As electricity production generates an important amount of greenhouse gas emissions, rethinking and reducing our electricity consumption is crucial to address climate change issues. 

    This project explored the correlation between my household energy consumption and shared information about climate change shared on Twitter.
    In other words: **Does alarming ‘energy and climate change’ news impact my household energy consumption behaviour?** 

    ## MY CONCEPT

    **A data-driven approach to energy awareness**:  
    1. **Collect**: Track household energy consumption and climate change-related tweets.  
    2. **Analyze**: Use machine learning to predict energy usage and identify correlations.  
    3. **Actuate**: Send SMS alerts to housemates when energy use exceeds predictions.  
    4. **Visualize**: Provide real-time energy and tweet data via a web app.  

    ## ARCHITECTURE

    1. **Hardware**:ESP32 with a light sensor to track electricity meter flashes.  

    2. **APIs**: Twitter API to collect tweets about "climate change" and "energy" and Twilio API to send SMS alerts.  

    3. **Cloud**: MongoDB for data storage and AWS EC2 for hosting scripts.  

    4. **Data Analysis**: Python (Pandas, ARIMA, SARIMA) for energy predictions.  

    5. **Web App**: Streamlit for real-time data visualization.  
                
    ## DATA COLLECTION & ANALYSIS

    1. **Energy Data**: Collected via ESP32 and light sensor, stored in MongoDB.  

    2. **Twitter Data**: Tweets collected daily via Twitter API, stored in MongoDB.  

    3. **Analysis**:  
       - SARIMA models predict next day’s energy consumption.  
       - Pearson correlation used to analyze the relationship between energy use and tweets.  

    ## THE RESULTS (SO FAR!)

    - **Correlation**: A slight correlation (Pearson r = 0.37) between energy use and tweets.  
    - **Behavioral Impact**: SMS alerts could influence energy-saving behavior over time.  
    - **Web App**: Real-time energy and tweet data visualized via Streamlit.  
    """)

def analyseddata():
    """Handles the projects section"""
    
    projects = {
        "Internet Carbon Footprint": internet_carbon_footprint,
        "Energy Prediction Algorithm": ernegy_consumption,
        "RAG for Climate Change": lambda: st.write("🔬 Researching AI solutions for environmental monitoring..."),
        "Ecocircular": lambda: st.write("🎨 Exploring creative design solutions...")
    }

    selected_project = st.selectbox("Select a Project", list(projects.keys()))

    # Call the function corresponding to the selected project
    projects[selected_project]()

    # Embed the carbon badge
    carbon_badge = """
    <div id="wcb" class="carbonbadge"></div>
    <script src="https://unpkg.com/website-carbon-badges@1.1.3/b.min.js" defer></script>
    """

    # Use components.html to render the badge
    components.html(carbon_badge, height=100)

    


if __name__ == "__main__":
    home()
