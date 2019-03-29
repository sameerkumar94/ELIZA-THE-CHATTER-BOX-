# Parastou Yaghmai, Sameer Kumar, Ekagaar Singh Hara
# We are designing a program called Eliza which reponse to user in Natural Language
# First step this program ask for user name, if the user enter empty space it will ask again
# After entering the name, the user start interacting with Eliza by answering question or asking question
# This program will answers users questions or interacts with the user based on the pre-defined set of instructions
# Steps of Eliza
# 1: accepting the first input as String
# 2: Analyze the string for a pattern
# 3: Then return a corresponding response
# 4: Respond in the form of string
# 5: Loops until the accepting string is "quit"

# importing packages Re for reading regular expression and random is for getting a random response
import re
import random

# Defining the regular expressions
expression = [
    [r'[I|i] need (.*)',
     ["Why do you think you need {0}?",
      "Is it important to get {0}?",
      "You sound certain that you need {0}"]],

    [r'[W|w]hy don\'?t you ([^\?]*)\??',
     ["Why do you care if I don't {0}?",
      "I like it and will do {0}.",
      "Are you forcing me to {0}?",
      "Do you suggest I should {0}?"]],

    [r'[W|w]hy can\'?t [I|i] ([^\?]*)\??',
     ["Are you sure {0} will benefit you?",
      "After doing {0}, what do you think would happen?",
      "I have NO idea why you can't {0}!",
      "Is it worth it?"]],

    [r'[I|i] can\'?t (.*)',
     ["Are you sure you can't {0}?",
      "Who knows you can't {0} unless you go for it..",
      "To what extent you think you can't {0}?"]],

    [r'[A|a]re you ([^\?]*)\??',
     ["How does it affect you me being {0}?",
      "Are you implying me to modify myself3??",
      "Yes! Who knows Right?.",
      "What happens if I am {0}? Would you still be the same with me?"]],

    [r'[W|w]hat (.*)',
     ["Any reason to ask this question?",
      "Will it help you if I tell you what {0}?",
      "I need time to think about it. Can we talk about something else?",
      "What do you think about it? Did you ask yourself this question?"]],

    [r'[H|h]ow (.*)',
     ["What do you think?",
      "It can be answered on its own. Think about it.",
      "You need to be more specific about what you are asking."]],

    [r'[B|b]ecause (.*)',
     ["I doubt that!",
      "There can be some more justification on this.",
      "Is this a generalized reason?",
      "Keeping {0} in mind, What else can you say about it?"]],

    [r'[H|h]ello(.*)',
     ["Hey there!",
      "Oh Hi! What an amazing day it is right?",
      "Greetings Sir. How can I help you today?"
      "Hello! How are you feeling on this beautiful day?"]],

    [r'[I|i] think (.*)',
     ["Why do you think {0}?",
      "Maybe you are correct. It is your own perspective.",
      "Are you 100% sure about?"]],

    [r'[Y|y]es',
     ["You sound confident. ",
      "Good! Could you Explain why you agree to this?"]],

    [r'(.*) computer(.*)',
     ["Are you directing this towards me?",
      "Do you like communicating with a Computer?",
      "Are you comfortable sharing with me?",
      "Computers are the greatest invention by humanity."]],

    [r'[C|c]an you ([^\?]*)\??',
     ["Why do you think I can {0}?",
      "Even if I {0}, What happens next?",
      "Is it a favour you want?"]],

    [r'[Y|y]ou are (.*)',
     ["Why do you feel that about me??",
      "Do you feel happy thinking I am {0}?",
      "Are you suggesting I should be {0}?",
      "Are you implying that I can be {0} too?"]],

    [r'[I|i] don\'?t (.*)',
     ["Its good to {0} sometimes.",
      "Have you tried it once?",
      "You should give {0} a chance"]],

    [r'[I|i] feel (.*)',
     ["I need more information on it.",
      "Did you share it with someone?",
      "Have you thought about it thoroughly?",
      ]],

    [r'[I|i] have (.*)',
     ["Are you proud of having {0}?",
      "I know others with {0} and No attitude about it."
      ]],

    [r'[I|i] would (.*)',
     ["Do you really want to {0}?",
      "If you {0}, What would happen after that?"
      ]],

    [r'[W|w]hy (.*)',
     ["You need ask that to your self.",
      "Okay! Think about why you {0}?"
      ]],

    [r'[A|a]mazing(.*)',
     ["Wow! Perfect. So what you want to talk today?",
      "Good to hear.",
      "You look over excited! What is the matter?"]],

    [r'(.*)',
     ["Could you elaborate it.",
      "Pardon? Could you repeat it again?",
      "Nevermind. Let us share something about you",
      ]],

    [r'[M|m]y name is (.*)',
     ["Ah..{0}!, Wonderful name Buddy!"
      ]]
]

# Defining a Dictionary
transform = {
    "i": "you",
    "you": "me",
    "me": "you",
    "am": "are",
    "my": "your",
    "your": "my",
    "yours": "mine",
    "are": "am",
    "was": "were",
    "i would": "you would",
    "i have": "you have",
    "you have": "I have",
    "i will": "you will",
    "you will": "I will"
}


# function process()v matched response from check() and transforms

def process(data):
    tokens = data.lower().split()
    for i, token in enumerate(tokens):
        if token in transform:
            tokens[i] = transform[token]
    return ' '.join(tokens)


# This function matches the input string with a pattern/regular expression from the list-expression
def check(string):
    for pattern, responses in expression:
        match = re.match(pattern, string)
        if match:
            response = random.choice(responses)
            return response.format(*[process(g) for g in
                                     match.groups()])  # this statement passes the string as well as the index of the characters.


# Main Funtion
def main():
    print('Welcome, Could you please tell me your name?')
    name = input()  # put the name as input in form of string

    while (name == ''):
        print ( 'Do not be Shy, tell me, what is your name?')
        name = input()
        while (name ==''):
            print ( 'I could not hear, lets start again....what is your name?')
            name=input()
            while ((name == '') or (name == ' ')): # this loop is for, when a user inputs space again after typing enter
                print ( 'Silence wont help, lets start again....what is your name?')
                name = input()
                break


    print('Hello ' + name.rstrip("!@#$%^&*()?") + ', how is your day so far?')
    statement = input()
    while ((statement != '') or (statement != ' ')):
        print(check(statement))  # calling function check
        statement = input()
        if ((statement == "quit") or (statement == "Quit") or (statement == "QUIT")):
            break
    print('It was such a wonderful talk. Hope to see you again.')

if __name__ == "__main__":
    main()

#END