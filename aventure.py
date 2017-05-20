#!/usr/bin/python

class Node(object):
    """
        Concrete class for elements of the storyline.

        This class implemtents all the data strutures and the
        methods useful to implement a tree of narrative elements
        such as the ones that can be found in gamebooks.

        :param description: Describe the situation.
        :param question: How to resolve the situation.
        :param answer: The various resolutions to the question.
        :type description: str
        :type question: str
        :type alternatives: list
        :type answer: list
    """
    
    def __init__(self, description, question, alternatives, answer):
        self.description = description
        self.question = question
        self.alternatives = alternatives
        self.answer = answer
        self.choice = None
        self.children = []
    def __call__(self):
        print(self.description)
        input_line = self.question
        i = 0
        for alternative in self.alternatives:
            i += 1
            input_line = input_line+'\n'+str(i)+") "+alternative
        self.choice = int(input(input_line))
        self.choice -= 1
        print(self.answer[self.choice])
        self.children[self.choice]()
        
enter = Node("Yodlalala young adventurer",
             "Is it an african or a european swallow?",
             ["African","European"],
             ["OMG A NIGGER.","Hmmmkay"])
african_story = Node("Yo mon, so you have an African swallow.",
                     "Do you like coconuts?",
                     ["Yes","No"],

                     ["COCONUT","PACOCONUT"])
european_story = Node("Europe",
                      "Yup!",
                      ["Euro1","Euro2"],
                      ["greuh","HAGREUH"]
)

enter.children = [african_story, european_story]

enter()
