from googletrans import Translator #import the package
trans = Translator() #initialize the object
phrase = str(input("Input your text>>"))
translated_phrase = trans.translate(phrase)
print(translated_phrase.text)
