class Chord(object):
    # TODO: doctring
    def __init__(self, root_note):
        # TODO: doctring
        # TODO: validation
        self.notes = [root_note]
    
    def root(self):
        # TODO: doctring
        # TODO: tests
        return self.notes[0]

    def add_note(self, new_note):
        # TODO: docstring
        # TODO: tests
        if new_note < self.root():
            self.notes.insert(0, new_note)
            return

        for i in range(len(self.notes) - 1):
            if (new_note >= self.notes[i]) and (new_note < self.notes[i + 1]):
                self.notes.insert(i + 1, new_note)
                return

        self.notes.append(new_note)
    
    def __str__(self):
        # TODO: docstring
        out = ''
        for n in self.notes:
            out += n.__str__() + '+'
        out = out [:-1]
        
        return out