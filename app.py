import streamlit as st
from agent import generate_content


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Social Media Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# HEADER
# ============================================================

st.title("🤖 AI Social Media Assistant")

st.caption("✦ AI Powered Marketing Copilot")

st.divider()


# ============================================================
# MAIN LAYOUT
# ============================================================

left_column, right_column = st.columns(
    [1, 1],
    gap="large"
)


# ============================================================
# LEFT SIDE
# ============================================================

with left_column:

    st.subheader("✨ Smart. Simple. Powerful.")

    st.title(
        "Engaging Content Idea\n"
        "Marketing Content\n"
        "with AI"
    )

    st.write(
        "Your AI marketing copilot for creating "
        "engaging, platform-optimized content in seconds."
    )

    st.info(
        "💡 Give your business, platform, topic and audience. "
        "Your AI assistant will create the content for you."
    )


# ============================================================
# RIGHT SIDE
# ============================================================

with right_column:

    st.subheader("Let's Create Amazing Content")

    st.caption(
        "Tell us about your content and let AI do the work."
    )

    # --------------------------------------------------------
    # BUSINESS / NICHE
    # --------------------------------------------------------

    business = st.text_input(
        "🏢 Business / Niche",
        placeholder="e.g. Digital Marketing Agency"
    )


    # --------------------------------------------------------
    # PLATFORM
    # --------------------------------------------------------

    platform = st.selectbox(
        "📱 Platform",
        [
            "Instagram",
            "LinkedIn",
            "Facebook",
            "X",
            "YouTube"
        ]
    )


    # --------------------------------------------------------
    # TOPIC
    # --------------------------------------------------------

    topic = st.text_input(
        "✏️ Topic",
        placeholder="e.g. AI in Marketing"
    )


    # --------------------------------------------------------
    # TARGET AUDIENCE
    # --------------------------------------------------------

    audience = st.text_input(
        "👥 Target Audience",
        placeholder="e.g. Small business owners"
    )


    # --------------------------------------------------------
    # TONE
    # --------------------------------------------------------

    tone = st.selectbox(
        "😊 Tone",
        [
            "Professional",
            "Casual",
            "Educational",
            "Friendly",
            "Persuasive"
        ]
    )


    st.write("")


    # --------------------------------------------------------
    # GENERATE BUTTON
    # --------------------------------------------------------

    generate = st.button(
        "✨ Generate Content →",
        type="primary",
        use_container_width=True
    )


# ============================================================
# GENERATE CONTENT
# ============================================================

if generate:

    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    if not business.strip():

        st.warning(
            "Please enter your Business / Niche."
        )

    elif not topic.strip():

        st.warning(
            "Please enter a Topic."
        )

    elif not audience.strip():

        st.warning(
            "Please enter your Target Audience."
        )

    else:

        # ----------------------------------------------------
        # CALL YOUR EXISTING LANGCHAIN + GROQ AGENT
        # ----------------------------------------------------

        with st.spinner(
            "✨ Creating your marketing content..."
        ):

            try:

                result = generate_content(
                    business,
                    platform,
                    topic,
                    audience,
                    tone
                )


                # ------------------------------------------------
                # SHOW RESULT
                # ------------------------------------------------

                st.divider()

                st.subheader(
                    "✨ Your Generated Content"
                )

                st.write(result)


            except Exception as e:

                st.error(
                    "Something went wrong while generating content."
                )

                st.caption(
                    str(e)
                )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AI Social Media Assistant"
)