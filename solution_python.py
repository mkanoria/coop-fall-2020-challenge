class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self._undo_actions = []
        self._redo_actions = []

    def add(self, num: int):
        self.value += num 
        self._undo_actions.append(num)

    def subtract(self, num: int):
        self.value -= num
        self._undo_actions.append(-num)

    def undo(self):
        if not self._undo_actions:
            return
        action = self._undo_actions.pop()
        self._redo_actions.append(action)
        self.value -= action

    def redo(self):
        if not self._redo_actions:
            return
        action = self._redo_actions.pop()
        self._undo_actions.append(action)
        self.value += action

    def bulk_undo(self, steps: int):
        while steps > 0:
            if not self._undo_actions:
                return
            self.undo()
            steps -= 1

    def bulk_redo(self, steps: int):
        while steps > 0:
            if not self._redo_actions:
                return
            self.redo()
            steps -= 1
