import streamlit as st

st.set_page_config(
    page_title="Zeng Zhang - Engineer, Educator, Entrepreneur",
    page_icon="👨🏻‍💻",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([0.3, 0.7])
with col1:
    st.markdown(
        """
        <style>
        .profile-img img {
            width: 100%;
            border-radius: 50%;
        }
        </style>

        <div class="profile-img">
            <img src="https://images.unsplash.com/photo-1519256155806-cd510524ed97?q=80&w=3174&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Profile Image">
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        """
        # Zeng Zhang

        - Education:
            - Beijing Forestry University
            - University of Washington
        - Work/Project Experience:
            - INFINITY Rescuer Jul. 2019 - Sep. 2019
                - Group Project; UX Design Lead
                - Led the design of an emergency aid application to facilitate interactions among individuals and medical staff, completing two rounds of testing and product deployment within a month.
                - Conducted six rounds of interviews throughout the design process, resulting in an 85% positive feedback rate on the final usability testing. Enhanced the existing physical prototype model iteratively by leveraging data collected from IMU sensors.
            - FUN Kit Smart Pillbox Aug. 2019 - Nov. 2019
                - Product Designer & Partner
                - Addressed the issue of memory decline and medication aversion in elderly depression patients by providing a more immersive and engaging medication experience.
                - Collaborated with cross-functional teams, such as Prototypers and Engineers, to ensure the user-friendliness and ease of use for applications and product hardware.
                - Facilitated users in tracking their medication intake with the help of rotary bearings and PCB boards, resulting in a 30% reduction in the average instances of target users either repeating or forgetting to take their medication.
        - Hobbies and Interests:
            - City walk
            - Gym
        - Interesting Projects:
            - Tele-Health Related
            - Vulnerable Population Related
        - Contact:
            - Seattle, WA 
            - +1 425 5316 702 
            - zhangzeng1999@gmail.com
        """
    )

footer_template = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: absolute;
left: 0;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/sape94" target="_blank"> by sape94</a></p>
</div>

</div>
"""
st.markdown(footer_template, unsafe_allow_html=True)
