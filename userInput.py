import questionary

debug = 0


def prompt(fallback='input.txt'):
    if debug:
        return fallback

    try:
        file = questionary.select(
            "Which file should be used?",
            choices=[
                'input.txt',
                'test.txt',
                'test2.txt',
            ]).ask()  # returns value of selection
    except:
        file = input("Which file should be used? >") or fallback
        print(file)
    return file
