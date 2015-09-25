from string import Template

def main():
    print("First pick a story!")
    print("You need to type story1 or story2, like that.")
    choice = input("> ")
    if choice == "story1":
        print("In order, type an adjective, a noun, a pronoun, an adverb, and a verb.")
        words = input("> ")
        vocab = words.split()
        create_story(choice, vocab)
    elif choice == "story2":
        print("In order, type a noun an adjective another noun a verb an adjective and a noun.")
        words = input("> ")
        vocab = words.split()
        create_story(choice, vocab)
    else:
        main()

def create_story(choice, words):
    story_temps = ["""\tSo this will be a ${adj} story about ${noun}!
                  \r\tWhy is ${pronoun} ${adverb} ${verb}ing? \n\tIsn't this absolutely amazing!""",
                 """\tMost ${noun1} will be doing ${adj1} things. The ${noun2} ${verb} is ${adj2} for ${noun3}."""]
    if choice == "story1":
        # The code '\033[31m' is the start sequence
        # and color code for the text.
        # '\033[0m' is the end sequence.
        adj = '\033[31m' + words[0] + '\033[0m'
        noun = '\033[31m' + words[1] + '\033[0m'
        pronoun = '\033[31m' + words[2] + '\033[0m'
        adverb = '\033[31m' + words[3] + '\033[0m'
        verb = '\033[31m' + words[4] + '\033[0m'
        templ = Template(story_temps[0])
        print(templ.safe_substitute(adj=adj, noun=noun, pronoun=pronoun, adverb=adverb, verb=verb))
    elif choice == "story2":
        n = '\033[31m' + words[0] + '\033[0m'
        a = '\033[31m' + words[1] + '\033[0m'
        n2 = '\033[31m' + words[2] + '\033[0m'
        v = '\033[31m' + words[3] + '\033[0m'
        a2 = '\033[31m' + words[4] + '\033[0m'
        n3 = '\033[31m' + words[5] + '\033[0m'
        templ = Template(story_temps[1])
        print(templ.safe_substitute(noun1=n, adj1=a, noun2=n2, verb=v, adj2=a2, noun3=n3))


if __name__ == '__main__':
    main()
