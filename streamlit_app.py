import streamlit as st

st.set_page_config(
    page_title="Zeng Zhang - Designer, Landscape Architect",
    page_icon="👾",
    layout="centered",
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
        <h1 style='font-size: 36px;'>Zeng Zhang</h1>

        <h2 style='font-size: 24px;'>Education:</h2>
        <ul>
            <li>Beijing Forestry University</li>
            <li>University of Washington</li>
        </ul>

        <h2 style='font-size: 24px;'>Work/Project Experience:</h2>
        <ul>
            <li><strong>INFINITY Rescuer Jul. 2019 - Sep. 2019</strong>
                <ul>
                    <li>Group Project; UX Design Lead</li>
                    <li>Led the design of an emergency aid application to facilitate interactions among individuals and medical staff, completing two rounds of testing and product deployment within a month.</li>
                    <li>Conducted six rounds of interviews throughout the design process, resulting in an 85% positive feedback rate on the final usability testing. Enhanced the existing physical prototype model iteratively by leveraging data collected from IMU sensors.</li>
                </ul>
            </li>
            <li><strong> FUN Kit Smart Pillbox Aug. 2019 - Nov. 2019</strong>
                <ul>
                    <li>Product Designer & Partner</li>
                    <li>Addressed the issue of memory decline and medication aversion in elderly depression patients by providing a more immersive and engaging medication experience.</li>
                    <li>Collaborated with cross-functional teams, such as Prototypers and Engineers, to ensure the user-friendliness and ease of use for applications and product hardware.</li>
                    <li>Facilitated users in tracking their medication intake with the help of rotary bearings and PCB boards, resulting in a 30% reduction in the average instances of target users either repeating or forgetting to take their medication.</li>
                </ul>
            </li>
        </ul>

        <h2 style='font-size: 24px;'>Hobbies and Interests:</h2>
        <ul>
            <li>City walk, Hiking</li>
            <li>Fitness, Tennis</li>
            <li>Scuba diving</li>
        </ul>

        <h2 style='font-size: 24px;'>Interesting Projects:</h2>
        <ul>
            <li>Tele-Health Related</li>
            <li>Vulnerable Population Related</li>
        </ul>

        <h2 style='font-size: 24px;'>Contact:</h2>
        <ul>
            <li>Seattle, WA</li>
            <li>+1 425 5316 702</li>
            <li>zhangzeng1999@gmail.com</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

footer_template = """
<style>
a:link, a:visited {
    color: #BFBFBF; /* theme's text color hex code at 75 percent brightness */
    background-color: transparent;
    text-decoration: none;
}

a:hover, a:active {
    color: #0283C3; /* theme's primary color */
    background-color: transparent;
    text-decoration: underline;
}

#page-container {
    position: relative;
    min-height: 10vh;
}

.footer {
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: transparent;
    color: #808080; /* theme's text color hex code at 50 percent brightness */
    text-align: left; /* you can replace 'left' with 'center' or 'right' if you want */
}

footer {
    visibility: hidden;
}
</style>

<div id="page-container">
    <div class="footer">
        <p style='font-size: 14px;'>Made with <a href="https://streamlit.io/" target="_blank">Streamlit</a><br>
        with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height="10"/><a href="https://github.com/sape94" target="_blank"> by sape94</a></p>
    </div>
</div>
"""
st.markdown(footer_template, unsafe_allow_html=True)
