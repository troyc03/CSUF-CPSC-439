# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 12:08:45 2025

@author: WINDOWS
"""

from collections import deque

class NFA:
   
        def __init__(self, states, alphabet, transitions, start_state, accept_states):
            """
            Initialize class attributes.
            """
            self.states = states # All states of the NFA
            self.alphabet = alphabet # All elements of the alphabet 
            self.transitions = transitions # Transition function
            self.start_state = start_state # Start state of NFA
            self.accept_states = accept_states #Accepting states of NFA
        
        def epsilon_closure(self, states):
            """
            Compute the epsilon closure.
            """
            
            closure = set(states)
            stack = list(states)
            
            while stack:
                state = stack.pop()
                if (state, '') in self.transitions: #Epsilon-transitions
                    for next_state in transitions[(state, '')]:
                        if next_state not in closure:
                            closure.add(next_state)
                            stack.append(next_state)
            return closure
        
        def accepts(self, input_string):
            """ 
            Simulate the NFA to check if it accepts the input string.
            """
            current_states = self.epsilon_closure({self.start_state})
            
            for symbol in input_string:
                next_states = set()
                for state in current_states:
                    if (state, symbol) in self.transitions:
                        next_states.update(self.transitions[(state, symbol)])
                    current_states = self.epsilon_closure(next_states) # Apply epsilon-closure
            return any(state in self.accept_states for state in current_states)
        
# Define the NFA from Exercise 1.16(a)

states = {'q0', 'q1', 'q2'}
alphabet = {'a', 'b'}
transitions = {
    ('q0', 'a'): {'q0', 'q1'},
    ('q1', 'b'): {'q2'},
    ('q2', 'b'): {'q2'},
    }
start_state = 'q0'
accept_states = {'q2'}

nfa = NFA(states, alphabet, transitions, start_state, accept_states)

# Test strings
test_strings = ['abb', 'aaa', 'aab']

# Run NFA simulation
for s in test_strings:
    print(f"String '{s}' is accepted? {nfa.accepts(s)}")
                    
            