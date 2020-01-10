# building a translator

# Giraffe language: Vowels ==> g
# ex. god = dgg

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "A E I O U a e i o u":
            translation = translation + 'g'
        else:
            translation = translation + letter
    return translation
print(translate(input("enter a phrase"))) 
