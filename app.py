import random
import streamlit as st

from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    # Number of attempts allowed for each difficulty level
    # FIX: Easy has less attempts than Normal (6 < 8) so it was changed to have 8 and normal has 6
    "Easy": 8,
    "Normal": 6,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

# Initialize session state variables if they don't exist
# FIX: should start at 0 but was set to 1 in the original code
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

st.subheader("Make a guess")

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

show_hint = st.checkbox("Show hint", value=True)

submit = False
raw_guess = None

if st.session_state.status == "playing":
    with st.form(key="guess_form"):
        raw_guess = st.text_input(
            "Enter your guess:",
            key=f"guess_input_{difficulty}"
        )
        submit = st.form_submit_button("Submit Guess 🚀")

just_finished = False

if submit:
    ok, guess_int, err = parse_guess(raw_guess, low, high)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        #FIX: Increment attempts only after a valid guess is parsed
        st.session_state.attempts += 1
        st.session_state.history.append(guess_int)

        # Convert the secret to a string if the attempt number is even
        # FIX: not needed so commented out
        #if st.session_state.attempts % 2 == 0:
        #    secret = str(st.session_state.secret)
        #else:
        #    secret = st.session_state.secret

        outcome, message = check_guess(guess_int, st.session_state.secret)

        if show_hint:
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            just_finished = True
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                just_finished = True
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

if st.session_state.status != "playing" and not just_finished:
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")

new_game = st.button("New Game 🔁")

if new_game:
    st.session_state.attempts = 0
    #FIX: random.randint was hardcoded a range 1:100, so I change it to low,high
    st.session_state.secret = random.randint(low, high)
    st.session_state.status = "playing"
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
