import streamlit as st
import numpy as np
import pandas as pd

def get_input():
    num_states = st.number_input("Enter the number of states", min_value=1, step=1)
    states = []

    for i in range(num_states):
        state = st.text_input(f"Enter the name of state {i+1}")
        states.append(state)

    transition_probabilities = []

    for state_index, state in enumerate(states):
        probabilities = {}
        st.subheader(f"Transition probabilities from state {state}: ")
        for target_state_index, target_state in enumerate(states):
            key = f"{state_index}-{target_state_index}"
            prob = st.number_input(f"Probability of transitioning to state {target_state}", key=key, min_value=0.0, max_value=1.0, step=0.01)
            probabilities[target_state] = prob  
        transition_probabilities.append(probabilities)

    return states, transition_probabilities

def create_transition_matrix(states, transition_probabilities):
    num_states = len(states)
    transition_matrix = np.zeros((num_states, num_states))

    for i, probs in enumerate(transition_probabilities):
        for j, target_state in enumerate(states):
            transition_matrix[i][j] = probs.get(target_state, 0)  

    return transition_matrix

def main():
    st.title("Markov Chain")
    st.write("Enter the details for your Markov chain.")

    states, transition_probabilities = get_input()

    st.write("States:", states)
    st.write("Transition Probabilities:", transition_probabilities)

    transition_matrix = create_transition_matrix(states, transition_probabilities)


    transition_df = pd.DataFrame(transition_matrix, index=states, columns=states)

    st.write("Transition Matrix:")
    st.table(transition_df)



if __name__ == "__main__":
    main()
