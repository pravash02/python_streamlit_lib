import streamlit as st
import time
import random
import pyautogui

restart_game = False


def generate_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "A stitch in time saves nine.",
        "Actions speak louder than words.",
        "Beauty is in the eye of the beholder.",
        "Cleanliness is next to godliness.",
        "Don't count your chickens before they hatch.",
        "Every cloud has a silver lining.",
        "Fortune favors the bold.",
        "You can't have your cake and eat it too.",
        "Where there's smoke, there's fire."
    ]
    return random.choice(sentences)


def typing_game():
    st.write("# Typing Game")
    st.write("Test your typing speed!")
    st.write("Type the given text as fast as you can within the time limit.")

    # text = "Fortune favors the bold"
    # if "text" not in st.session_state or st.session_state.get("restart"):  # Check if "text" is not in session state or restart flag is set
    #     text = generate_random_sentence()  # Generate new random sentence
    #     st.session_state["text"] = text  # Store new text in session state

    text = st.session_state.get("text")  # Get stored text from session state
    if "text" not in st.session_state or text is None or st.session_state.get("restart"):  # If text is None or restart flag is set
        text = generate_random_sentence()  # Generate new random sentence
        st.session_state["text"] = text  # Store new text in session state

    st.write("## Text to type:")
    st.write(text)

    user_input = st.text_input("Type the text here:", key="user_input", value="", placeholder="Type here...")
    start_time = st.session_state.get("start_time")
    restart = st.session_state.get("restart")

    if start_time is None or restart:
        start_time = time.time()
        st.session_state["start_time"] = start_time

    elapsed_time = time.time() - start_time
    words_typed = user_input.split()
    correct_words = [word for word in words_typed if word in text.split()]
    incorrect_words = [word for word in words_typed if word not in correct_words]

    if elapsed_time < 10.0:
        st.write("## Time remaining: {:.2f} seconds".format(10.0 - elapsed_time))
    else:
        st.write("## Time's up!")
        st.write("Your typing speed is: {:.2f} words per minute".format(len(user_input.split()) / (elapsed_time / 60)))

        if incorrect_words:
            st.write("Incorrect words: {}".format(", ".join(incorrect_words)))

        # restart = st.button("Restart", key="restart")
        # if restart:
        if st.button("Restart", key="restart"):
            pyautogui.hotkey("ctrl", "F5")
            # st.session_state["restart"] = True
            # st.session_state.clear()

        # if st.button("Restart", key="restart"):
        #     st.session_state["start_time"] = None
        #     st.session_state["restart"] = True

    # if st.session_state.get("restart"):
    #     st.session_state.clear()


if __name__ == "__main__":
    typing_game()
