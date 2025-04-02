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
        "LinkedIn": ["https://www.linkedin.com/in/coline-ritz-958870182/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/cocoritzy", "https://cdn-icons-png.flaticon.com/512/25/25231.png"]
    }

    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", unsafe_allow_html=True)

    # About me section
    st.subheader("About Me")
    st.write("""
    🧑‍💻 I am a **Design Engineer** teaching Data scicence @ [Data bird](https://www.data-bird.co/)
    
    ✨ I design, build, and innovate — turning ideas into sustainable solutions
    
    🌱 I have experiences in Sustainable IT and AI @[IJO](https://ijo.tech/index.html) and in carbon removal technologies @[DSS+](https://www.consultdss.com/) and @[BlackBull Biocahr](https://www.blackbullbiochar.com/)
             
    ❤️ I hold a Master Degree from @ [Imperial College](https://www.imperial.ac.uk/)
  
    🤖 I created a climate collective [Ecocircular](https://www.instagram.com/ecocircular_/?hl=fr)
             
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

    st.title("🌍 Internet carbon footrpint ")
    st.markdown(
    """
    <div style="border: 1px solid gray; padding: 10px; border-radius: 5px; background-color: #f9f9f9;">
        <em>The I.C.E tool is a real-time Internet carbon footprint analyser to 
        encourage behaviour change through increasing user awareness</em>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown("""
    ### 🔍 The Problem
    Streaming videos, sending emails, and editing documents are all examples of activities that are responsible for an individual’s ever-increasing data consumption. Several solutions focusing on the IT hardware have been developed in recent years, but the increase of the Internet users’ data consumption lacks attention, becoming a threat to a viable digital future. 
    Internet traffic is predicted to grow at a compound annual growth rate (CAGR) of 26 % in the coming years . Due to this dramatic growth, Internet data traffic represents already 7% of the global electricity consumption, producing 3.5%, of global greenhouse gas (GHG) emissions. In this context, if nothing is done, the carbon footprint of total internet traffic could reach 14% of GHG by 2040.
    Two major problems persist:

    - **Lack of awareness:** The carbon footprint of the internet is invisible, making users unaware of its environmental impact.
    - **Inaccurate measurement:** Current tools for measuring internet carbon footprints are often unreliable, with estimates varying by up to five orders of magnitude.
    """)

    ("""
    ### The Internet Carbon Emission Tool (I.C.E)
    For this project I design end-to-end, test, and implement the Internet Carbon Emission (I.C.E) tool. 
    The I.C.E tool is a real-time Internet carbon footprint analyser to encourage behaviour change through increasing user awareness. 
    Built on a network traffic analyser and a machine learning (ML) classifier, the tool can classify up to 35 network applications to display a detailed breakdown of user consumption via a web interface app. 
    The aim of the tool is to promote sustainable behavior and to provide personalized feedback on emissions.
    """)
    # Load your images (replace with your image paths)
    image1 = "assets/firstpage.png"
    image2 = "assets/secondpage.png"

    # Create two columns
    col1, col2 = st.columns(2)

    # Display the first image in the first column
    with col1:
        st.image(image1, caption="Tool Onboarding", use_container_width=True)

    # Display the second image in the second column
    with col2:
        st.image(image2, caption="User Internet Emission Dashboard", use_container_width=True)
    ("""
    ### How did i built it?
    1. Defining system boundaries : 
    This model adopts the widest possible system boundaries to capture the total GHG footprint. The results of this model can be segmented into sub-systems to provide greater insight. These subsystems are:

        - Data centers: The energy consumed for data storage and processing.

        - Networks: The energy allocated to data transmission across networks.

        - User devices: The energy used by end users when interacting with a product or service.

        *The data for these subsystems is sourced from the International Energy Agency (IEA, 2022), as well as studies by Anders Andrae (Andrae, 2020)* .""")

    st.image("assets/internet.jpg", caption="The system boundaries", use_container_width=True)

    ("""
    2. Collecting the data: The tool uses Wireshark (Network Traffic Analyzer) to capture Internet network traffic of users.

    3. Analysing and Transforming the Data: A Random Forest ML model classifies 35 common applications and their data usage (GB) are converted into carbon emissions equivalent (CO₂e) based on location-specific energy grids.""")

# Display the equation in a readable format
# Display the equation and explanation in a single cell
    st.write("""
    ### Carbon Footprint Equation

    ```

    Total Carbon Footprint (gCO2) = 
        (W_Data_Centers × C_i_ip + W_End_users × C_i_uk) 
        + (W_Transmission_equipment + W_Manufacturing_and_production) 
        × C_i_world × E_internet

    Where:

    - W represents the weight per segment:
        - W_Data Centers = 0.15
        - W_End users = 0.52
        - W_Transmission_equipment = 0.14
        - W_Manufacturing_and_production = 0.15
    - C_i_world = World carbon intensity (gCO₂/kWh)
    - C_i_ip = Data Centers carbon intensity (gCO₂/kWh) 
    - C_i_uk = UK grid carbon intensity (gCO₂/kWh)
    - E_internet = Internet energy consumption (kWh)
             
    """)

    st.write(""" 4. Visualization: A web interface displays real-time carbon footprints, personalized tips, and comparisons with peers.

     """)
    
    # Embed the YouTube video using iframe
    st.components.v1.iframe(
    "https://www.youtube.com/embed/EwC8Pk5zgQM?si=pVmxQSAYZpLl-lkI",
    width=560,
    height=315
    )
    
    st.subheader(" The final architecture")

    # Display image (Replace with actual project image)
    st.image("assets/system.JPG", caption="The architecture", use_container_width=True)

    st.markdown("""
    ### References
    - Aslan et al. (2018) - Electricity intensity of Internet data transmission.
    - Andrae & Edler (2015) - Global electricity usage of communication technology.
    - Greenpeace’s Click Clean Report (2016) - Breakdown of data traffic per application.         
    """)

def ernegy_consumption():

    st.title("🌍 Can social media influence energy consumption?")

    st.markdown(""" 

    The average UK household uses 6 to 8 kWh of electricity daily[1]. With electricity generation being a major source of greenhouse gas emissions, reducing consumption is vital for addressing climate change. All this climate discussions during COP26 on social media made me reflect on this further and ask myself : **Does alarming ‘energy and climate change’ news impact my household energy consumption behaviour?** 

    ## So what did i do ?
    
    I explored the correlation between my household energy consumption and shared information about climate change shared on Twitter.
                 """)


    # Create a container for the images and points
    with st.container():
    # First row with two images
        col1, col2 = st.columns(2)

    # Image 1 in the first column
    with col1:
        st.image("assets/flash.png", caption="**Collect**: Track household electricity with the red meter flashes, a light sensor and ESP32.", use_container_width=True)

    # Image 2 in the second column
    with col2:
        st.image("assets/corr.png", caption="**Analyze**: Use machine learning to predict electricity usage and identify correlations.", use_container_width=True)

    # Second row with two images
    col3, col4 = st.columns(2)

    # Image 3 in the first column
    with col3:
        st.image("assets/tweets.png", caption="**Actuate**: Send SMS alerts to housemates when electricity use exceeds predictions.", use_container_width=True)

    # Image 4 in the second column
    with col4:
        st.image("assets/analyse.png", caption="**Visualize**: Provide real-time electricity and tweet data via a web app.", use_container_width=True)


    st.markdown(""" 
   ## The Architecture
                 """)
    col1, col2 = st.columns(2)

    # In the first column, place the image

    # Create two columns with specific width ratios
    col1, col2 = st.columns([1, 3])  # More space for the text column

    # In the first column, place the image with a smaller width
    with col1:
        st.image("assets/system_final.png", caption="System Architecture")  # Remove width to preserve quality

    # In the second column, place the text
    with col2:
        st.markdown(""" 
        1. **Electricity data collection**: ESP32 with a light sensor to track electricity meter flashes.  
        2. **Twitter Data**: Twitter API to collect tweets about "climate change" and "energy" and Twilio API to send SMS alerts.  
        3. **Cloud**: MongoDB for data storage and AWS EC2 for hosting scripts.  
        4. **Data Analysis**: Python (Pandas, ARIMA, SARIMA) for energy predictions.  
        5. **Web App**: Streamlit for real-time data visualization.  
        """)

    st.markdown( """           
    ## The results

    - Unfortunatly, there was no correlation between energy use and tweets. But hopefully SMS alerts could influence energy-saving behavior over time !  
             
    """)
    # Add the text
    st.markdown("## Want to see the full project?")

    # Embed the YouTube video
    video_url = "https://www.youtube.com/embed/xOVhrPEBo9Y?start=40"
    st.markdown(f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

def ecocircular():

    st.title("🌍 Ecorcicular : climate collective")
    
    st.text(""" Ecocircular is a collective fueled by hope and the belief in collective action to inspire meaningful change in the fight against climate change. I co-led an activism project that spanned from Canada to Peru, connecting climate and environmental activists while organizing workshops on climate science and solutions. During this journey, we:

            - Connected with 45 climate and environmental activists
            - Organized over 30 workshops
            - Hosted conferences to exchange ideas (Academy of Climate, Maison Citoyenne) """)
    st.subheader(""" Who did we meet ?
                 """)
        # Load your images (replace with your image paths)
    image1 = "assets/Name.gif"
    image2 = "assets/eddie.gif"
    image3 = "assets/fernando.gif"
    image4 = "assets/eliane.gif"
    image5 = "assets/ruth.gif"
    image6 = "assets/jim.gif"
    image7 = "assets/soa.gif"
    image8 = "assets/luiz.gif"

    # Create the first row with four columns
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image(image1, caption="Name from Mexico", use_container_width=True, width=100)
    with col2:
        st.image(image2, caption="Eddie from Costa Rica", use_container_width=True, width=100)
    with col3:
        st.image(image3, caption="Fernando from Ecuador", use_container_width=True, width=100)
    with col4:
        st.image(image4, caption="Eliane from Perù", use_container_width=True, width=100)

    # Create the second row with four columns
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        st.image(image5, caption="Ruth from Mexico", use_container_width=True, width=100)
    with col6:
        st.image(image6, caption="Jim from Costa Rica", use_container_width=True, width=100)
    with col7:
        st.image(image7, caption="Jabel from Guatemala", use_container_width=True, width=100)
    with col8:
        st.image(image8, caption="Luiz from Guatemala", use_container_width=True, width=100)
    
    st.subheader(""" Our itinerary
                 """)
    st.markdown(
    """
    <iframe src="https://coline-ritz.travelmap.net" 
        width="100%" 
        height="600" 
        frameborder="0" 
        allowfullscreen>
    </iframe>
    """,
    unsafe_allow_html=True
)


    st.subheader("🌍 Want to learn more ? @[ecocircular](https://www.instagram.com/ecocircular_/)")

def analyseddata():
    """Handles the projects section"""
    
    projects = {
        "Internet Carbon Footprint": internet_carbon_footprint,
        "Energy Prediction Algorithm": ernegy_consumption,
        "Ecocircular": ecocircular
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
