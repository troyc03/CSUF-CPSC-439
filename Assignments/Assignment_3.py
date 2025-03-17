# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:38:05 2025

@author: WINDOWS
"""

class FiniteAutomation:
    def __init__(self, states, alphabet, transitions, start_state, final_state):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_state = final_state