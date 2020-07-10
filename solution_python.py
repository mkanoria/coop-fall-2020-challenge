class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self._undo_history = []
        self._redo_history = []

    def add(self, num: int):
        self.value += num 
        self._undo_history.append(num)

    def subtract(self, num: int):
        self.value -= num
        self._undo_history.append(-num)

    def undo(self):
        # Return if nothing to undo
        if not self._undo_history:
            return
        action = self._undo_history.pop()
        self._redo_history.append(action)
        self.value -= action

    def redo(self):
        # Return if nothing to redo
        if not self._redo_history:
            return
        action = self._redo_history.pop()
        self._undo_history.append(action)
        self.value += action

    def bulk_undo(self, steps: int):
        while steps > 0:
            self.undo()
            steps -= 1

    def bulk_redo(self, steps: int):
        while steps > 0:
            self.redo()
            steps -= 1
