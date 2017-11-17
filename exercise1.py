communism = {"spanish": "communismo", "french": "communisme", "german": "kommunismus", "russian": "коммунизм", "hebrew": "קוֹמוּנִיזם"}
def cross_of_gold():
    for x, y in communism.items():
        print(f"Communism in {x} is {y}! Viva la revolucion!")
def guevara():
    speech = input("Have some communism, pick a language: \nSpanish, German, French, Russian, or Hebrew\n").lower()
    print(communism[speech])
    return speech
