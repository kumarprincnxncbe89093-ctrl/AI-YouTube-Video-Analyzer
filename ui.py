import streamlit as st
import time
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="AI YouTube Video Analyzer",
    page_icon="🎥",
    layout="centered",
    initial_sidebar_state="collapsed"
)

if "report" not in st.session_state:
    st.session_state.report = ""


st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Inter',sans-serif;
}

/* Background */

.stApp{
    background:#1f1f1f;
    color:white;
}

/* Hide Streamlit */

#MainMenu{
visibility:hidden;
}

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

/* Width */

.block-container{
    max-width:900px;
    padding-top:40px;
}

/* Title */

.title{
    text-align:center;
    font-size:48px;
    font-weight:700;
    color:white;
}

.subtitle{
    text-align:center;
    color:#9ca3af;
    margin-bottom:35px;
}

/* Card */



/* Labels */

label{
    color:white !important;
    font-weight:600;
}

/* Input */

.stTextInput input{

    background:#343541 !important;

    color:white !important;

    border:1px solid #444 !important;

    border-radius:14px !important;

    padding:15px !important;

}

/* Placeholder */

.stTextInput input::placeholder{

    color:#9ca3af !important;

}

/* Selectbox */

.stSelectbox div[data-baseweb="select"]{

    background:#343541;

    border-radius:14px;

}

/* Button */

.stButton button{

    width:100%;

    background:#10A37F;

    color:white;

    border:none;

    border-radius:14px;

    height:52px;

    font-size:18px;

    font-weight:600;

}

.stButton button:hover{

    background:#0f8f70;

}

/* Progress */

.stProgress > div > div > div > div{

    background:#10A37F;

}

/* Report */

.report{

    background:#2b2b2b;

    border-radius:18px;

    border:1px solid #3d3d3d;

    padding:25px;

    font-size:17px;

    line-height:1.8;

    color:#ECECEC;

}

/* Success */

.success{

    background:#0e3b30;

    border-left:5px solid #10A37F;

    padding:15px;

    border-radius:10px;

    margin-top:15px;

}

</style>
""", unsafe_allow_html=True)

st.markdown(
"""
<div class='title'>
🎥 AI YouTube Video Analyzer
</div>

<div class='subtitle'>
Analyze any YouTube video using AI in seconds.
</div>
""",
unsafe_allow_html=True
)

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()


video_url = st.text_input(
    "",
    placeholder="🔗 Paste YouTube URL...",
    label_visibility="collapsed"
)

language = st.selectbox(
    "🌐 Output Language",
    [
        "English",
        "Hindi (हिन्दी)",
        "Sanskrit (संस्कृत)",
        "Assamese	(অসমীয়া)",
        "Bengali	(বাংলা)",
        "Bodo	(बड़ो)",
        "Dogri	(डोगरी)",
        "Gujarati	(ગુજરાતી)",
        "Kannada	(ಕನ್ನಡ)",
        "Kashmiri	(کٲشُر / कॉशुर)",
        "Konkani	(कोंकणी)",
        "Maithili	(मैथिली)",
        "Malayalam	(മലയാളം)",
        "Manipuri (Meitei)	ꯃꯤꯇꯩꯂꯣꯟ (Meitei Mayek) / মৈতৈলোন (Bengali script)",
        "Marathi	(मराठी)",
        "Nepali	(नेपाली)",
        "Odia	(ଓଡ଼ିଆ)",
        "Punjabi	(ਪੰਜਾਬੀ)",
        "Santali	(ᱥᱟᱱᱛᱟᱲᱤ) (Ol Chiki)",
        "Sindhi	(سنڌي / सिन्धी)",
        "Tamil	(தமிழ்)",
        "Telugu	(తెలుగు)",
        "Urdu	(اردو)",
        "Bhili	(भीली)",
        "Bhojpuri	(भोजपुरी)",
        "Chhattisgarhi	(छत्तीसगढ़ी)",
        "Garhwali	(गढ़वाली)",
        "Gondi	(गोंडी)",
        "Haryanvi	(हरियाणवी)",
        "Ho	𑢷𑣉 (Warang Citi) / हो",
        "Kumaoni	(कुमाऊँनी)",
        "Kurukh	(कुड़ुख) / 𑻠𑻱𑻢𑻟𑻤 (Tolong Siki)",
        "Magahi	(मगही)",
        "Mizo (Lushai)	(Mizo)",
        "Nagamese	(Nagamese)",
        "Rajasthani	(राजस्थानी)",
        "Tulu	(ತುಳು)",
        "Kokborok	(Kokborok)",
        "Khasi	(Khasi)",
        "Mishing	(Mising)",
        "Lepcha	ᰛᰧᰵᰚᰩᰵ (Róng script)",
        "Nicobarese	(Nicobarese)"
    ]
)

analyze = st.button(
    "🚀 Analyze Video",
    use_container_width=True
)

if analyze:

    if video_url == "":

        st.warning("Please enter a YouTube URL.")

    else:

        progress = st.progress(0)

        status = st.empty()

        status.info("🔗 Validating URL...")
        progress.progress(10)
        time.sleep(0.4)

        status.info("📥 Fetching Video...")
        progress.progress(30)
        time.sleep(0.5)

        status.info("📝 Extracting Transcript...")
        progress.progress(55)
        time.sleep(0.6)

        status.info("🤖 AI is Thinking...")
        progress.progress(75)

        time.sleep(0.5)

        status.info("📊 Generating Analysis...")
        progress.progress(90)

        time.sleep(0.5)

        status.info("✨ Finalizing Report...")
        progress.progress(98)

        try:

 
            prompt = f"""
            Analyze this YouTube video.

            URL:
            {video_url}

            Return the report in {language}.

            Include the following sections:

            # Executive Summary

            # Key Points

            # Important Insights

            # Sentiment Analysis

            # Actionable Takeaways

            Use bullet points where appropriate.

            Format the report using Markdown headings and lists.

            If the selected language is English, write the entire report in English only.

            If the selected language is Hindi (हिन्दी), write the entire report in Hindi only.

            If the selected language is Sanskrit (संस्कृत), write the entire report in Sanskrit only."""

            # If the selected language is Assamese (অসমীয়া), write the entire report in Assamese only.

            # If the selected language is Bengali (বাংলা), write the entire report in Bengali only.

            # If the selected language is Bodo (बड़ो), write the entire report in Bodo only.

            # If the selected language is Dogri (डोगरी), write the entire report in Dogri only.

            # If the selected language is Gujarati (ગુજરાતી), write the entire report in Gujarati only.

            # If the selected language is Kannada (ಕನ್ನಡ), write the entire report in Kannada only.

            # If the selected language is Kashmiri (کٲشُر / कॉशुर), write the entire report in Kashmiri only.

            # If the selected language is Konkani (कोंकणी), write the entire report in Konkani only.

            # If the selected language is Maithili (मैथिली), write the entire report in Maithili only.

            # If the selected language is Malayalam (മലയാളം), write the entire report in Malayalam only.

            # If the selected language is Manipuri (Meitei), write the entire report in Manipuri (Meitei) only.

            # If the selected language is Marathi (मराठी), write the entire report in Marathi only.

            # If the selected language is Nepali (नेपाली), write the entire report in Nepali only.

            # If the selected language is Odia (ଓଡ଼ିଆ), write the entire report in Odia only.

            # If the selected language is Punjabi (ਪੰਜਾਬੀ), write the entire report in Punjabi only.

            # If the selected language is Santali (ᱥᱟᱱᱛᱟᱲᱤ), write the entire report in Santali only.

            # If the selected language is Sindhi (سنڌي / सिन्धी), write the entire report in Sindhi only.

            # If the selected language is Tamil (தமிழ்), write the entire report in Tamil only.

            # If the selected language is Telugu (తెలుగు), write the entire report in Telugu only.

            # If the selected language is Urdu (اردو), write the entire report in Urdu only.

            # If the selected language is Bhili (भीली), write the entire report in Bhili only.

            # If the selected language is Bhojpuri (भोजपुरी), write the entire report in Bhojpuri only.

            # If the selected language is Chhattisgarhi (छत्तीसगढ़ी), write the entire report in Chhattisgarhi only.

            # If the selected language is Garhwali (गढ़वाली), write the entire report in Garhwali only.

            # If the selected language is Gondi (गोंडी), write the entire report in Gondi only.

            # If the selected language is Haryanvi (हरियाणवी), write the entire report in Haryanvi only.

            # If the selected language is Ho (𑢷𑣉 / हो), write the entire report in Ho only.

            # If the selected language is Kumaoni (कुमाऊँनी), write the entire report in Kumaoni only.

            # If the selected language is Kurukh (कुड़ुख / 𑻠𑻱𑻢𑻟𑻤), write the entire report in Kurukh only.

            # If the selected language is Magahi (मगही), write the entire report in Magahi only.

            # If the selected language is Mizo (Lushai), write the entire report in Mizo only.

            # If the selected language is Nagamese, write the entire report in Nagamese only.

            # If the selected language is Rajasthani (राजस्थानी), write the entire report in Rajasthani only.

            # If the selected language is Tulu (ತುಳು), write the entire report in Tulu only.

            # If the selected language is Kokborok, write the entire report in Kokborok only.

            # If the selected language is Khasi, write the entire report in Khasi only.

            # If the selected language is Mishing (Mising), write the entire report in Mishing only.

            # If the selected language is Lepcha (ᰛᰧᰵᰚᰩᰵ), write the entire report in Lepcha only.

            # If the selected language is Nicobarese, write the entire report in Nicobarese only.

            # Do not mix languages. Do not translate technical terms into English unless there is no widely accepted equivalent in the selected language. Keep the entire report, including headings, tables, bullet points, captions, and conclusions, in the selected language.
            

            response = agent.run(prompt)

            progress.progress(100)

            status.success("✅ Analysis Completed Successfully!")

            st.session_state.report = response.content
            # -------------------------------
            # Display Report
            # -------------------------------

            if st.session_state.report:

                st.divider()

                st.subheader("📄 Analysis Report")

                with st.container(border=True):

                    st.markdown(st.session_state.report)

                st.download_button(
                    "📥 Download Report",
                    data=st.session_state.report,
                    file_name="youtube_analysis.txt",
                    mime="text/plain",
                    # use_container_width=True
                )

        except Exception as e:

            st.error(e)