from test import test
import string

def test_suite():
    test(cleanword("what?") == "what")
    test(cleanword("’now!’") == "now")
    test(cleanword("?+=’w-o-r-d!,@$()’") == "word")

def remove_punctuation(word):
    punctuation = "!\"#$%&’()*+,-./:;<=>?@[\\]^_‘{|}~"
    word_no_punct = ""
    for letter in word:
        if letter not in punctuation:
            word_no_punct += letter
    return word_no_punct


def cleanword(word):
    print(remove_punctuation(word))
    return remove_punctuation(word)


test_suite()
