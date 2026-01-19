import streamlit as st
import time
import random
from datetime import datetime
from openai import OpenAI

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Student Wellness AI", layout="wide")
st.markdown("""
<style>
.block-container {
    padding-top: 1.0rem;
}
</style>
""", unsafe_allow_html=True)
# ---------------- PHASE 3: CHAT UI STYLES ----------------
st.markdown("""
<style>
.chat-user {
    background: #4b6cff;
    color: white;
    padding: 10px 14px;
    border-radius: 15px;
    max-width: 70%;
    margin-left: auto;
    margin-bottom: 8px;
}
.chat-ai {
    background: #eef2ff;
    color: black;
    padding: 10px 14px;
    border-radius: 15px;
    max-width: 70%;
    margin-right: auto;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "mood" not in st.session_state:
    st.session_state.mood = "Okay"

if "intensity" not in st.session_state:
    st.session_state.intensity = 5

if "interactions" not in st.session_state:
    st.session_state.interactions = 0

if "mood_history" not in st.session_state:
    st.session_state.mood_history = []

if "last_mood" not in st.session_state:
    st.session_state.last_mood = "Okay"

if "show_animation" not in st.session_state:
    st.session_state.show_animation = False


# ---------------- MOOD LOGIC ----------------
MOOD_KEYWORDS = {
    "Happy": ["happy", "excited", "great", "good", "joy"],
    "Stressed": ["stress", "worried", "exam", "pressure", "tension"],
    "Angry": ["angry", "frustrated", "irritated", "mad"],
    "Sad": ["sad", "low", "down"],
}

MOOD_EMOJI = {
    "Happy": "😄",
    "Stressed": "😟",
    "Angry": "😡",
    "Sad": "😢",
    "Okay": "🙂",
}
INTENSITY_MAP = {
    "Happy": 6,
    "Okay": 5,
    "Sad": 6,
    "Stressed": 8,
    "Angry": 8,
}

def detect_mood(text):
    t = text.lower()
    for mood, keys in MOOD_KEYWORDS.items():
        if any(k in t for k in keys):
            return mood
    return "Okay"

# ---------------- EMOJI SHOWER ----------------
def emoji_shower(emoji):
    st.markdown(
        f"""
        <style>
        .emoji {{
            position: fixed;
            font-size: 48px;
            animation: float 5s linear forwards;
        }}
        @keyframes float {{
            0% {{ top:100%; opacity:1; }}
            100% {{ top:-10%; opacity:0; }}
        }}
        </style>
        """ +
        "".join(
            f"<div class='emoji' style='left:{random.randint(0,100)}%;'>"
            f"{emoji}</div>"
            for _ in range(25)
        ),
        unsafe_allow_html=True
    )


# ---------------- HYBRID AI ----------------
def hybrid_reply(user_text, mood):
    # 1️⃣ ALWAYS give instant response first (NO BLOCK)
    instant_replies = {
        "Happy": "That’s amazing 😄 Tell me more!",
        "Stressed": "I hear you 😟 One step at a time. What’s worrying you most?",
        "Angry": "That sounds frustrating 😡 I’m listening.",
        "Sad": "I’m really glad you shared this 😢 I’m here with you.",
        "Okay": "I’m here. What’s on your mind?"
    }

    base_reply = instant_replies.get(mood, "I’m listening.")

    # 2️⃣ TRY OpenAI (OPTIONAL enhancement)
    try:
        with st.spinner("Thinking…"):
            res = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a calm student wellness assistant."},
                    {"role": "user", "content": user_text},
                ],
                timeout=10  # ⬅️ VERY IMPORTANT
            )
            return res.choices[0].message.content
    except:
        # 3️⃣ Fallback if API slow / fails
        return base_reply


# ---------------- UI HEADER ----------------
st.markdown("""
<style>
.title-container {
    text-align: center;
    margin-top: 10px;
    margin-bottom: 20px;
    animation: fadeIn 1.2s ease-in-out;
}
@keyframes fadeIn {
    0% { opacity: 0; transform: translateY(-10px); }
    100% { opacity: 1; transform: translateY(0); }
}
</style>

<div class="title-container">
    <h1>🌱 Student Wellness AI</h1>
    <p style="color:gray;font-size:16px;">
        Your calm, supportive mental health companion
    </p>
</div>
""", unsafe_allow_html=True)
st.info("This system provides emotional support for educational purposes only.")
# ---------- CARD ANIMATION (Phase 4 - A) ----------
st.markdown("""
<style>
.animate-card {
    animation: floatIn 1.2s ease-in-out;
}
@keyframes floatIn {
    0% {transform: translateY(12px); opacity: 0;}
    100% {transform: translateY(0); opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

# ---------------- INPUT ----------------
# INPUT (replace this section only)

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_area("Share what's on your mind")
    send = st.form_submit_button("Send")

if send and user_input.strip():
    new_mood = detect_mood(user_input)

    # mark animation only if mood changed
    if new_mood != st.session_state.last_mood:
        st.session_state.show_animation = True
        st.session_state.last_mood = new_mood

    st.session_state.mood = new_mood
    st.session_state.intensity = INTENSITY_MAP[new_mood]
    st.session_state.interactions += 1
    st.session_state.mood_history.append(st.session_state.intensity)

    st.session_state.messages.append(("You", user_input))
    reply = hybrid_reply(user_input, new_mood)
    st.session_state.messages.append(("AI", reply))

    

# trigger emoji animation once (outside Send block)
if st.session_state.get("show_animation"):
    emoji_shower(MOOD_EMOJI[st.session_state.mood])
    st.session_state.show_animation = False


# ---------------- MODE BUTTONS ----------------
st.markdown("### 🧠 Modes")
c1, c2, c3 = st.columns(3)
c1.button("📘 Exam Mode")
c2.button("🎯 Focus Mode")
c3.button("💬 Vent Mode")

# ---------- DEMO BUTTON (FOR EVALUATOR / TEACHER) ----------
with st.expander("👩‍🏫 Demo Controls (for evaluation only)"):
    if st.button("🔍 Demo Calm Feature"):
        st.session_state.mood = "Stressed"


# ---------------- STATUS CARDS (FAV UI) ----------------
c1, c2, c3 = st.columns(3)

c1.markdown(
    f"""
    <div style="padding:20px;border-radius:15px;
    background:linear-gradient(135deg,#ff4b4b,#7a0000);color:white">
    <h4>Current Mood</h4>
    <h1>{MOOD_EMOJI[st.session_state.mood]}</h1>
    {st.session_state.mood}
    </div>
    """,
    unsafe_allow_html=True,
)

c2.markdown(
    f"""
    <div style="padding:20px;border-radius:15px;
    background:linear-gradient(135deg,#ffb000,#7a4a00);color:white">
    <h4>Emotion Intensity</h4>
    <h2>{st.session_state.intensity}/10</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

c3.markdown(
    f"""
    <div style="padding:20px;border-radius:15px;
    background:linear-gradient(135deg,#4b6cff,#000c7a);color:white">
    <h4>Interactions</h4>
    <h2>{st.session_state.interactions}</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------- CHAT (Phase 3) ----------------
# ---------------- CHAT (PHASE 3) ----------------
st.markdown("### 💬 Conversation")

for role, msg in st.session_state.messages:
    if role == "You":
        st.markdown(
            f"""
            <div style="
                max-width:65%;
                margin-left:auto;
                margin-bottom:10px;
                padding:12px 16px;
                border-radius:18px;
                background:#4f46e5;
                color:white;
                text-align:right;
                ">
                {msg}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="
                max-width:65%;
                margin-right:auto;
                margin-bottom:10px;
                padding:12px 16px;
                border-radius:18px;
                background:#eef2ff;
                color:#111827;
                text-align:left;
                ">
                {msg}
            </div>
            """,
            unsafe_allow_html=True
        )
# ---------------- PHASE 4: CALM EXERCISE (SIMPLE & SAFE) ----------------
#a ---------------- PHASE 4: CALM EXERCISE (ANIMATED & SAFE) ----------------

if st.session_state.mood in ["Stressed", "Sad", "Angry"]:
    st.markdown("### 🌬️ 1-Minute Calm Exercise")

    st.markdown(
        """
        <style>
        .calm-card {
            animation: fadeFloat 1.2s ease-in-out;
        }

        @keyframes fadeFloat {
            0% {
                opacity: 0;
                transform: translateY(12px);
            }
            100% {
                opacity: 1;
                transform: translateY(0px);
            }
        }
        </style>

        <div class="calm-card" style="
        padding:20px;
        border-radius:15px;
        background:linear-gradient(135deg,#e0f7fa,#e8f5e9);
        color:#333;
        font-size:16px;
        ">
        <b>Let’s pause together 🌱</b><br><br>
        🫁 Breathe in for <b>4 seconds</b><br>
        ⏸️ Hold for <b>4 seconds</b><br>
        🌬️ Breathe out for <b>6 seconds</b><br><br>
        Repeat this 3 times.<br><br>
        <i>You’re doing your best. This feeling will pass.</i>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- QUICK COPING ACTIONS ----------------
if st.session_state.mood in ["Stressed", "Sad", "Angry"]:
    st.markdown("### 🛠 Quick Coping Actions")

    cols = st.columns(3)
    with cols[0]:
        if st.button("🎧 Deep Breathing"):
            st.write("Pause… Inhale 4s, Hold 4s, Exhale 6s… Repeat 🙂")
    with cols[1]:
        if st.button("📚 Study Motivation"):
            st.write("Every small step matters! Break work into tiny pieces.")
    with cols[2]:
        if st.button("🧘 Self-Care Tip"):
            st.write("Take a 5-min walk, hydration break, or stretch 😊")


# ---------------- PHASE 3: REFLECTION JOURNAL ----------------
# ---------------- REFLECTION JOURNAL (PHASE 3) ----------------
st.markdown("### 📝 Reflection Journal")

journal = st.text_area(
    "Write your thoughts, learnings, or feelings from this session:",
    placeholder="What did you learn today? How are you feeling now?",
    height=120
)

if st.button("💾 Save Reflection"):
    st.session_state.journal_entry = journal
    st.success("Reflection saved for this session 🌱")
# ---------------- AFFIRMATION ----------------
if st.session_state.mood in ["Sad", "Stressed", "Angry"]:
    st.info("💙 You’re doing your best. Progress matters more than perfection.")

# ---------------- SESSION SUMMARY (PHASE 3) ----------------
st.markdown("### 📊 Session Summary")

st.markdown(f"""
- **Final Mood:** {st.session_state.mood} {MOOD_EMOJI[st.session_state.mood]}
- **Avg Intensity:** {round(sum(st.session_state.mood_history)/len(st.session_state.mood_history),1) if st.session_state.mood_history else st.session_state.intensity}/10
- **Total Interactions:** {st.session_state.interactions}
- **Active Mode:** Normal
""")

# ---------------- GRAPH ----------------
if st.session_state.mood_history:
    st.markdown("### 📊 Mood Trend (Tracker)")
st.line_chart(
    st.session_state.mood_history,
    height=200
)

# ---------------- ETHICS ----------------
st.markdown("### 🔐 Responsible AI & Ethics")
st.markdown("""
- No personal data stored  
- Secure API usage  
- Educational use only  
- Hybrid rule + AI logic  
""")
