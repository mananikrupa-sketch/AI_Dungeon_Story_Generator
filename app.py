import streamlit as st
from story_generator import StoryGenerator
from utils import save_story


# ----------------------------------
# Custom CSS
# ----------------------------------
st.markdown("""
<style>

/* Main page */
.main {
    padding-top: 0.5rem;
}

/* Title */
.main-title{
    text-align:center;
    color:#2563EB;
    font-size:42px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:#64748B;
    font-size:18px;
    margin-bottom:25px;
}

/* Buttons */
.stButton > button{

    width:100%;

    background: linear-gradient(135deg,#8B5CF6,#A855F7);

    color:white;

    border:none;

    border-radius:12px;

    height:52px;

    font-size:17px;

    font-weight:600;

    transition:0.3s;

    box-shadow:0px 6px 18px rgba(139,92,246,0.35);

}

.stButton > button:hover{

    background:linear-gradient(135deg,#7C3AED,#9333EA);

    color:white;

    transform:translateY(-2px);

    box-shadow:0px 8px 22px rgba(124,58,237,0.45);

}

/* Text Area */
textarea{
    border-radius:12px !important;
}

/* Footer */
.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)


# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="AI Dungeon Story Generator",
    page_icon="📖",
    layout="centered"
)


# ----------------------------------
# Load GPT-2 Model Only Once
# ----------------------------------
@st.cache_resource
def load_model():
    return StoryGenerator()


generator = load_model()

# ----------------------------------
# Sidebar
# ----------------------------------

with st.sidebar:

    st.title("📚 AI Dungeon")

    st.markdown("---")

    st.subheader("About")

    st.write(
        """
Generate creative AI-powered stories using GPT-Neo.

✔ Multiple Story Continuations

✔ Story Saving

✔ Genre Selection

✔ Interactive Web Application
"""
    )

    st.markdown("---")

    st.subheader("Supported Genres")

    st.markdown("""
🏰 Fantasy

⚔ Adventure

🕵 Mystery

👻 Horror

🚀 Sci-Fi

❤️ Romance
""")

    st.markdown("---")

    st.subheader("Technology")

    st.markdown("""
🐍 Python

🎈 Streamlit

🤗 Hugging Face

🧠 GPT-Neo
""")

    st.markdown("---")

    st.success("✅ GPT-Neo Model Loaded")


# ----------------------------------
# Session State
# ----------------------------------
if "stories" not in st.session_state:
    st.session_state.stories = []

if "prompt" not in st.session_state:
    st.session_state.prompt = ""

if "genre" not in st.session_state:
    st.session_state.genre = ""


# ----------------------------------
# Professional Header
# ----------------------------------

# ----------------------------------
# Hero Banner
# ----------------------------------

st.markdown("""
<div style="
background: linear-gradient(135deg,#6D28D9,#9333EA,#C084FC);
padding:35px;
border-radius:18px;
text-align:center;
color:white;
margin-bottom:25px;
box-shadow:0px 8px 25px rgba(0,0,0,0.18);
">

<h1 style="margin-bottom:5px;">
📖 AI Dungeon Story Generator
</h1>

<p style="font-size:18px;">
Create magical AI-powered stories using GPT-Neo
</p>

<p>
🏰 Fantasy &nbsp;&nbsp;
❤️ Romance &nbsp;&nbsp;
🚀 Sci-Fi &nbsp;&nbsp;
👻 Horror &nbsp;&nbsp;
🕵 Mystery
</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------
# Dashboard Cards
# ----------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="
        background:white;
        padding:20px;
        border-radius:15px;
        text-align:center;
        box-shadow:0px 4px 12px rgba(0,0,0,0.12);
        border:1px solid #E5E7EB;
    ">
        <h2>🤖</h2>
        <h4>Model</h4>
        <p style="font-size:18px;font-weight:bold;color:#7C3AED;">
            GPT-Neo
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background:white;
        padding:20px;
        border-radius:15px;
        text-align:center;
        box-shadow:0px 4px 12px rgba(0,0,0,0.12);
        border:1px solid #E5E7EB;
    ">
        <h2>📚</h2>
        <h4>Genres</h4>
        <p style="font-size:18px;font-weight:bold;color:#7C3AED;">
            6
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        background:white;
        padding:20px;
        border-radius:15px;
        text-align:center;
        box-shadow:0px 4px 12px rgba(0,0,0,0.12);
        border:1px solid #E5E7EB;
    ">
        <h2>📖</h2>
        <h4>Stories</h4>
        <p style="font-size:18px;font-weight:bold;color:#7C3AED;">
            1 - 3
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ----------------------------------
# Story Settings
# ----------------------------------

st.subheader("⚙ Story Settings")

col1, col2, col3 = st.columns(3)

with col1:

    genre = st.selectbox(
        "📚 Genre",
        (
            "Fantasy",
            "Adventure",
            "Mystery",
            "Horror",
            "Sci-Fi",
            "Romance"
        )
    )

with col2:

    num_stories = st.selectbox(
        "📖 Stories",
        (1, 2, 3)
    )

with col3:

    story_length = st.selectbox(
        "📏 Length",
        (
            "Short",
            "Medium",
            "Long"
        )
    )

temperature = st.slider(
    "🎨 Creativity Level",
    min_value=0.5,
    max_value=1.5,
    value=0.8,
    step=0.1,
    help="Higher values generate more creative stories."
)


# ----------------------------------
# Prompt Input
# ----------------------------------
prompt = st.text_area(
    "✍️ Enter your story prompt",
    height=180,
    placeholder="Example: A young prince entered a magical forest..."
)


# ----------------------------------
# Generate Story
# ----------------------------------
if st.button("✨ Generate AI Story", use_container_width=True):

    if prompt.strip() == "":
        st.warning("Please enter a story prompt.")

    else:

        with st.spinner("Generating story... Please wait..."):

            stories = generator.generate_story(
                prompt=prompt,
                genre=genre,
                story_length=story_length,
                temperature=temperature,
                num_stories=num_stories
            )

        st.session_state.stories = stories
        st.session_state.prompt = prompt
        st.session_state.genre = genre

        st.success(f"Successfully generated {len(stories)} story(s)!")


# ----------------------------------
# Display Stories
# ----------------------------------

if st.session_state.stories:

    st.markdown("## 📚 Generated Stories")

    for index, story in enumerate(st.session_state.stories, start=1):

        st.markdown(f"""
        <div style="
            background:#FFFFFF;
            padding:20px;
            border-radius:15px;
            border-left:6px solid #A855F7;
            box-shadow:0px 10px 25px rgba(124,58,237,0.18);
            margin-bottom:20px;
        ">
            <h3 style="color:#7C3AED;">
                📖 Story {index}
            </h3>
        </div>
        """, unsafe_allow_html=True)

        st.text_area(
            "",
            value=story,
            height=300,
            key=f"story_{index}"
        )

        st.markdown("<br>", unsafe_allow_html=True)

    # ----------------------------------
    # Save Button
    # ----------------------------------
    if st.button("💾 Save to Stories Folder", use_container_width=True):

        filepath = save_story(
            prompt=st.session_state.prompt,
            genre=st.session_state.genre,
            stories=st.session_state.stories
        )

        st.success("Stories saved successfully!")

        st.info(f"Saved to: {filepath}")
    
    # ----------------------------------
    # Download Stories
    # ----------------------------------

    download_text = f"Genre: {st.session_state.genre}\n\n"
    download_text += f"Prompt: {st.session_state.prompt}\n\n"

    for index, story in enumerate(st.session_state.stories, start=1):
        download_text += "=" * 60 + "\n"
        download_text += f"Story {index}\n"
        download_text += "=" * 60 + "\n\n"
        download_text += story + "\n\n"

    st.download_button(
        label="⬇ Download Story (.txt)",
        data=download_text,
        file_name="AI_Dungeon_Stories.txt",
        mime="text/plain",
        use_container_width=True
)

st.markdown("---")

st.markdown("""
<div style="
text-align:center;
padding:15px;
color:#6B7280;
font-size:15px;
">

Made with ❤️ using
<b>Python</b> •
<b>Streamlit</b> •
<b>Hugging Face</b> •
<b>GPT-Neo</b>

<br><br>

© 2026 AI Dungeon Story Generator

</div>
""", unsafe_allow_html=True)