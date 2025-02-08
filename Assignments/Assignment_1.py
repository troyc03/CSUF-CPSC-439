class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state  # Store the start state
        self.accept_states = accept_states

    def process_string(self, input_string):
        current_state = self.start_state  # Ensure we start fresh
        for symbol in input_string:
            if symbol in self.alphabet:
                current_state = self.transitions.get((current_state, symbol), None)
                if current_state is None:
                    return False  # Reached an invalid transition
            else:
                return False  # Invalid input symbol
        return current_state in self.accept_states

# Defining M4
states = {'s', 'q1', 'q2', 'r1', 'r2'}
alphabet = {'a', 'b'}
transitions = {
    ('s', 'a'): 'q1',
    ('s', 'b'): 'r1',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q2',
    ('q2', 'b'): 'q1',
    ('r1', 'a'): 'r2',
    ('r1', 'b'): 'r1',
    ('r2', 'a'): 'r1',
    ('r2', 'b'): 'r2'
}
start_state = 's'
accept_states = {'q2', 'r2'}

# Create DFA instance
dfa = DFA(states, alphabet, transitions, start_state, accept_states)

# Test strings
test_strings = ["abba", "baab", "bab", "bb", "aaa", "aabb"]
for string in test_strings:
    result = dfa.process_string(string)
    print(f"String '{string}' is {'ACCEPTED' if result else 'REJECTED'}")

print('============================================')

# Question 2

def is_accepted(string, start_state, transition_function, accepting_states):
    current_state = start_state
    
    for symbol in string:
        if symbol not in transition_function[current_state]:
            return False
        current_state = transition_function[current_state][symbol]
        
    return current_state in accepting_states

start_state = 'q1'
accepting_state = {'q4'}

transition_function = {
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q3', 'b': 'q2'},
    'q3': {'a': 'q1', 'b': 'q4'},
    'q4': {'a': 'q4', 'b': 'q4'}
    }

strings = ['abab', 'abaab', 'bbabb']
for s in strings:
    result = is_accepted(s, start_state, transition_function, accepting_state)
    print(f"String '{s}' accepted: '{result}'")
    
print('============================================')

# Question 3

class DFA:
    
    def __init__(self, states, alphabet, transition, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition = transition
        self.start_state = start_state
        self.accept_states = accept_states
        
    def accepts(self, string):
        state = self.start_state
        for char in string:
            state = self.transition.get((state, char), None)
            if state is None:
                return False
            return state in self.accept_states

states = {'q0', 'q1', 'q2'}
alphabet = {'a', 'b'}
transition = {
    ('q0', 'a'): 'q1', ('q0', 'b'): 'q0',
    ('q1', 'a'): 'q2', ('q1', 'b'): 'q1',
    ('q2', 'a'): 'q2', ('q2', 'b'): 'q2'
}
start_state = 'q0'
accept_states = {'q2'}

dfa_at_least_two_as = DFA(states, alphabet, transition, start_state, accept_states)
    
complement_states = {'p0', 'p1', 'p2', 'p3'}
complement_transition = {  # Example transitions, should match complement of M
    ('p0', 'a'): 'p1', ('p0', 'b'): 'p0',
    ('p1', 'a'): 'p2', ('p1', 'b'): 'p1',
    ('p2', 'a'): 'p2', ('p2', 'b'): 'p2'
}
complement_start = 'p0'
complement_accept = {'p0', 'p1', 'p2'}
dfa_complement = DFA(complement_states, alphabet, complement_transition, complement_start, complement_accept)

def union_dfa(dfa1, dfa2):
    new_states = {(s1, s2) for s1 in dfa1.states for s2 in dfa2.states}
    new_start = (dfa1.start_state, dfa2.start_state)
    new_accept = {(s1, s2) for s1 in dfa1.accept_states for s2 in dfa2.states} | {(s1, s2) for s1 in dfa1.states for s2 in dfa2.accept_states}
    new_transition = {}
    
    for (s1, s2) in new_states:
        for char in alphabet:
            next_s1 = dfa1.transition.get((s1, char), s1)
            next_s2 = dfa2.transition.get((s2, char), s2)
            new_transition[((s1, s2), char)] = (next_s1, next_s2)
    
    return DFA(new_states, alphabet, new_transition, new_start, new_accept)

dfa_union = union_dfa(dfa_at_least_two_as, dfa_complement)
print("States:", dfa_union.states)
print("Alphabet:", dfa_union.alphabet)
print("Start State:", dfa_union.start_state)
print("Accept States:", dfa_union.accept_states)
print("Transitions:")

for key, value in dfa_union.transition.items():
    print(f"  δ{key} -> {value}")
test_strings = ["aa", "ab", "bba", "bbb", "aab", "aba"]
for string in test_strings:
    print(f"String '{string}' accepted?", dfa_union.accepts(string))
    

