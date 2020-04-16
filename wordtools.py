from test import test
import string

def test_suite():
    test(cleanword("what?") == "what")
    test(cleanword("’now!’") == "now")
    test(cleanword("?+=’w-o-r-d!,@$()’") == "word")
    test(has_dashdash("distance--but"))
    test(not has_dashdash("several"))
    test(has_dashdash("spoke--"))
    test(has_dashdash("distance--but"))
    test(not has_dashdash("-yo-yo-"))
    test(extract_words("Now is the time! ’Now’, is the time? Yes, now.") == ['now','is','the','time','now','is','the','time','yes','now'])
    test(extract_words("she tried to curtsey as she spoke--fancy") == ['she','tried','to','curtsey','as','she','spoke','fancy'])
    test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
    test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
    test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
    test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)
    test(wordset(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"])
    test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["a", "I", "is", "am"])
    test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) == ["am", "or", "a", "is", "are", "be", "but"])
    test(longestword(["a", "apple", "pear", "grape"]) == 5)
    test(longestword(["a", "am", "I", "be"]) == 2)
    test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
    test(longestword([ ]) == 0)
    
def cleanword(word):
    punctuation = "!\"#$%&’()*+,-./:;<=>?@[\\]^_‘{|}~"
    word_clean = ""
    for letter in word:
        if letter not in punctuation:
            word_clean += letter
    return word_clean


def has_dashdash(word):
    if "".join(word.split("--"))!= word:
        return True
    else:
        return False
        
def extract_words(phrase):
    if has_dashdash(phrase):
        phrase = " ".join(phrase.split("--"))
    clean_phrase = cleanword(phrase)
    lower_clean_phrase = clean_phrase.lower()
    return lower_clean_phrase.split()


def wordcount(word,text_list):
    count = 0
    for i in text_list:
        if i == word:
            count += 1
    return count

def wordset(text_list):
    final_set = []
    for i in range(len(text_list)):
        if final_set == []:
            final_set.append(text_list[i])
        if final_set.count(text_list[i]) == 0:
            final_set.append(text_list[i])
    for k in range(len(final_set)):
        for j in range(len(final_set)-1,0,-1):
            if text_list.count(final_set[j]) > text_list.count(final_set[j-1]):
                prov = final_set[j]
                print(final_set[j])
                final_set.remove(final_set[j])
                final_set.insert(j-1,prov)
    print (final_set)      
    return final_set


def longestword (word_list):
    longest = 0
    for i in word_list:
        if len(i) > longest:
            longest = len(i)
    return longest

    
test_suite()
