import streamlit as st
import time
import random

st.title("Typing Test 💡")

# ---------------- EASY ---------------- #

easy_paragraphs = [
    "Python is a simple and powerful programming language.",
    "Practice typing every day to improve your speed.",
    "Streamlit helps create web apps using only Python."
]

# ---------------- MEDIUM ---------------- #

medium_paragraphs = [
    """Python is one of the most popular programming languages in the world because it is simple to learn and extremely versatile."""
]

# ---------------- HARD ---------------- #

hard_paragraphs = [
    """Artificial intelligence has rapidly evolved over the past decade, transforming industries and redefining the relationship between humans and technology."""
]

# session state
if "paragraph" not in st.session_state:
    st.session_state.paragraph = ""

if "start_time" not in st.session_state:
    st.session_state.start_time = 0

if "mode" not in st.session_state:
    st.session_state.mode = ""

# ---------------- EASY BUTTON ---------------- #

if st.button("Easy Paragraph", key="easy_button"):

    st.session_state.mode = "easy"

    st.session_state.paragraph = random.choice(easy_paragraphs)

    st.session_state.start_time = time.time()

# ---------------- MEDIUM BUTTON ---------------- #

if st.button("Medium Paragraph", key="medium_button"):

    st.session_state.mode = "medium"

    st.session_state.paragraph = random.choice(medium_paragraphs)

    st.session_state.start_time = time.time()

# ---------------- HARD BUTTON ---------------- #

if st.button("Hard Paragraph", key="hard_button"):

    st.session_state.mode = "hard"

    st.session_state.paragraph = random.choice(hard_paragraphs)

    st.session_state.start_time = time.time()

# ---------------- SHOW PARAGRAPH ---------------- #

if st.session_state.paragraph != "":

    st.write("Type the following paragraph as fast as you can:")

    st.info(st.session_state.paragraph)

    typed_text = st.text_area(
        "Start typing here...",
        key=st.session_state.mode
    )

    if st.button("Submit"):

        end_time = time.time()

        time_taken = end_time - st.session_state.start_time

        word_count_original = len(
            st.session_state.paragraph.split()
        )

        word_count_typed = len(
            typed_text.split()
        )

        diff_words = abs(
            word_count_original - word_count_typed
        )

        wpm = (word_count_typed / time_taken) * 60

        correct_chars = 0

        paragraph = st.session_state.paragraph

        for i in range(min(len(paragraph), len(typed_text))):

            if paragraph[i] == typed_text[i]:

                correct_chars += 1

        accuracy = (
            correct_chars / len(paragraph)
        ) * 100

        st.success(f"Time Taken: {time_taken:.2f} seconds")

        st.success(f"Word Count: {word_count_typed}")

        st.success(f"Difference in Word Count: {diff_words}")

        st.success(f"WPM: {wpm:.2f}")

        st.success(f"Accuracy: {accuracy:.2f}%")