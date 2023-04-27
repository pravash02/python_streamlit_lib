import streamlit as st
import random
import time
from datetime import datetime


# Function to generate a random word
def generate_word():
    return random.choice(word_list)


# Function to calculate typing speed
def calculate_typing_speed(start_time, end_time, word):
    elapsed_time = end_time - start_time
    elapsed_time_in_seconds = elapsed_time.total_seconds()
    words_per_minute = (len(word.split()) / elapsed_time_in_seconds) * 60
    return words_per_minute


# Initialize game variables
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "kiwi", "lemon", "mango", "orange",
             "pear", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]
game_over = False
word = ""
start_time = None
end_time = None
user_input = None

# Set Streamlit app title and layout
st.title("Typing Game")
st.sidebar.title("Game Options")
st.sidebar.write("Select the options below to start the game.")

# Set game difficulty level
difficulty = st.sidebar.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])

# Set game duration based on difficulty level
if difficulty == "Easy":
    duration = 60
elif difficulty == "Medium":
    duration = 45
else:
    duration = 30

# Display game instructions
st.write("Type the words that appear on the screen as fast as you can. Press 'Enter' after typing each word. "
         "Your typing speed will be calculated at the end of the game.")
st.write(f"Game duration: {duration} seconds")

# Game loop
cnt = 0
while not game_over:
    cnt += 1
    if not word:
        word = generate_word()
        start_time = datetime.now()

        # Display current word and user input
        st.write("Word: ", word)
        user_input = st.text_input(label="Type the word here:", key=f"{word}_{cnt}")

    # Check if user input matches the word
    st.write(user_input)
    if user_input is not None:
        # st.write("inside user_input")
        if word == user_input:
            end_time = datetime.now()
            typing_speed = calculate_typing_speed(start_time, end_time, word)
            st.success(f"Great! You typed '{word}' correctly in {round(typing_speed, 2)} words per minute.")
            st.write("Press the button below to play again.")
            st.session_state[word] = {}  # Remove word from session state
            game_over = True
            # user_input = None

        # Check if user input exceeds word length
        elif len(user_input) >= len(word):
            st.warning("Oops! Your input is longer than the word. Try again!")

    # Check if game duration has exceeded
    if (datetime.now() - start_time).seconds >= duration:
        st.warning("Game Over! Press the button below to play again.")
        game_over = True

    # Update user input in session state
    # st.session_state[word]["user_input"] = user_input
    # time.sleep(duration)

# Play again button
if st.button("Play Again"):
    game_over = False
    st.session_start_time = datetime.now()
