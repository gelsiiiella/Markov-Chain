import streamlit as st
import numpy as np
import pandas as pd

def get_input():
    num_states = st.number_input("Enter the number of states", min_value=1, step=1)
    states = []

    for i in range(num_states):
        state = st.text_input(f"Enter the name of state {i+1}")
        states.append(state)

    transition_periods = ["Next month", "Next week", "Custom"]  
    selected_period = st.selectbox("Select the transition period", transition_periods)

    if selected_period == "Custom":
        custom_period = st.number_input("Enter the custom transition period in days", min_value=1, step=1)
    else:
        custom_period = None

    return states, selected_period, custom_period

def compute_transition_matrix(states, selected_period, custom_period):
    num_states = len(states)
    transition_matrix = np.zeros((num_states, num_states))


    if selected_period == "Next month":
        transition_probability = 1.0 / 30  
    elif selected_period == "Next week":
        transition_probability = 1.0 / 7  
    elif selected_period == "Custom":
        transition_probability = 1.0 / custom_period

  
    for i in range(num_states):
        for j in range(num_states):
            if i == j:
                transition_matrix[i][j] = 1 - transition_probability 
            else:
                transition_matrix[i][j] = transition_probability / (num_states - 1)  

    return transition_matrix

def main():
    st.title("Markov Chain")
    st.write("Enter the details for your Markov chain.")

    states, selected_period, custom_period = get_input()

    st.write("States:", states)
    st.write("Transition Period:", selected_period)
    if selected_period == "Custom":
        st.write("Custom Transition Period (days):", custom_period)

    transition_matrix = compute_transition_matrix(states, selected_period, custom_period)

    transition_df = pd.DataFrame(transition_matrix, index=states, columns=states)

    st.write("Transition Matrix:")
    st.table(transition_df)



if __name__ == "__main__":
    main()
