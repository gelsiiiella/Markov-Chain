import streamlit as st

def get_input():
    num_states = st.number_input("Enter the number of states",min_value=1, step=1)
    states=[]

    for i in range(num_states):
        state = st.text_input(f"Enter the name of state {i+1}")
        states.append(state)

    transition_probabilities = {}


    for state in states:
        transition_probabilities[state] = {}
        st.subheader(f"Transition probabilities from state {state}: ")
        for target_state in states:
            prob = st.number_input(f"Probability of transitioning to state {target_state}",min_value=0.0,max_value=1.0,step=0.01)
            transition_probabilities[state][target_state] = prob

        return states, transition_probabilities
    
def main():
    st.title("Markov Chain")
    st.write("Enter the details for your Markov chain.")

    states, transition_probabilities = get_input()

    st.write("States:",states)
    st.write("Transition Probabilities:",transition_probabilities)

if __name__=="__main__":
    main()


