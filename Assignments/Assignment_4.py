class TuringMachine:
    def __init__(self, tape, blank='_'):
        self.tape = list(tape) + [blank]  # Tape initialized with input
        self.head = 0  # Head starts at position 0
        self.blank = blank
        self.state = 'q0'  # Initial state
        self.transitions = {
            ('q0', 'a'): ('q1', 'X', 'R'),
            ('q0', 'b'): ('q_reject', 'b', 'R'),
            ('q0', '_'): ('q_accept', '_', 'N'),
            ('q1', 'b'): ('q2', 'Y', 'R'),
            ('q1', 'X'): ('q1', 'X', 'R'),
            ('q1', '_'): ('q_reject', '_', 'N'),
            ('q2', 'b'): ('q3', 'Y', 'L'),
            ('q2', 'Y'): ('q2', 'Y', 'R'),
            ('q2', '_'): ('q_reject', '_', 'N'),
            ('q3', 'Y'): ('q3', 'Y', 'L'),
            ('q3', 'X'): ('q3', 'X', 'L'),
            ('q3', '_'): ('q0', '_', 'R'),
            ('q0', 'X'): ('q0', 'X', 'R'),
            ('q0', 'Y'): ('q0', 'Y', 'R'),
            ('q0', 'b'): ('q_reject', 'b', 'N')
        }
    
    def step(self):
        char = self.tape[self.head] if self.head < len(self.tape) else self.blank
        if (self.state, char) in self.transitions:
            new_state, write_char, move = self.transitions[(self.state, char)]
            if self.head < len(self.tape):
                self.tape[self.head] = write_char
            else:
                self.tape.append(write_char)
            self.state = new_state
            if move == 'R':
                self.head += 1
            elif move == 'L':
                self.head = max(0, self.head - 1)
        else:
            self.state = 'q_reject'
    
    def run(self):
        while self.state not in ['q_accept', 'q_reject']:
            self.step()
        return self.state == 'q_accept'

# Test cases
test_cases = ["aabb", "babbab", "aabbb", "aabbabb", "ababab"]

for case in test_cases:
    tm = TuringMachine(case)
    result = "Accepted" if tm.run() else "Rejected"
    print(f"Input: {case} -> {result}")

