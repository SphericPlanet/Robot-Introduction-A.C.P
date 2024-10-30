class Robot:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce(self):
        print("Hello, I am " + self.name + ".")
        print("I am a " + self.model + " model.")
        print("My purpose is to " + self.purpose + ".")


robot1 = Robot("Alexa", "Echo Dot 4th Gen", "assist with smart home tasks and answer questions")
robot2 = Robot("Jarvis", "AI Assistant", "assist with daily tasks and provide information")


robot1.introduce()
robot2.introduce()
