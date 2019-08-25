from .base import Module


class CourseName(Module):
    DESCRIPTION = "Generate a fake course title"

    def __init__(self):
        super().__init__()
        with open("resources/coursename.txt", "r") as f:
            words = f.read().replace("\"", "").split()
        index = 1
        self.chain = {}
        for word in words[index:]:
            key = words[index - 1]
            if key in self.chain:
                self.chain[key].append(word)
            else:
                self.chain[key] = [word]
            index += 1

    def response(self, query, message):
        word = random.choice(list(self.chain.keys()))
        message = word.capitalize()
        for _ in range(100):
            word = random.choice(self.chain[word])
            message += " " + word

        return message
