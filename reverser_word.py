# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"


def reverse_words(text):
    
    splitted_text = text.split(' ')
    sentence = []
    
    for word in splitted_text:
        reversed_word = word[::-1]
#         print(reversed_word)
        sentence.append(reversed_word)
    return ' '.join(sentence)
  #go for it
