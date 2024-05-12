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
        probabilities = []  
        st.subheader(f"Transition probabilities from state {state}: ")
        for target_state_index, target_state in enumerate(states):
            key = f"{state_index}-{target_state_index}" 
            prob = st.number_input(f"Probability of transitioning to state {target_state}", key=key, min_value=0.0, max_value=1.0, step=0.01)
            probabilities.append(prob)
        transition_probabilities.append(probabilities)  

    return states, transition_probabilities

def main():
    st.title("Markov Chain")
    st.write("Enter the details for your Markov chain.")

    states, transition_probabilities = get_input()

    st.write("States:", states)
    st.write("Transition Probabilities:", transition_probabilities)

    transition_matrix = np.array(transition_probabilities) 


    transition_df = pd.DataFrame(transition_matrix, index=states, columns=states)

    st.write("Transition Matrix:")
    st.table(transition_df)

  
if __name__ == "__main__":
    main()
