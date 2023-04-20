class Text:

    def __init__(self, vector, language):
        self.vector = vector
        self.language = language

    def __str__(self):
        return f"vector: {self.vector}, language: {self.language}"