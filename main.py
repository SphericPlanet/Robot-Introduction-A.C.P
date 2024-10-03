class Alexa:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce(self):
        print("Hello, I am " + self.name + ".")
        print("I am a " + self.model + " model.")
        print("My purpose is to " + self.purpose + ".")

alexa1 = Alexa("Alexa", "Echo Dot 4th Gen", "assist with smart home tasks and answer questions")

alexa1.introduce()
