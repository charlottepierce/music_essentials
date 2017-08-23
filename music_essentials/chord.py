class Chord(object):
    # TODO: doctring
    def __init__(self, root_note):
        # TODO: doctring
        # TODO: validation
        self.notes = [root_note]
    
    def root(self):
        # TODO: doctring
        return self.notes[0]