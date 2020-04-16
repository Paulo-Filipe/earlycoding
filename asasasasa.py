import sys

this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print ("teste 1: {0}".format (this is that))
that = this
print("teste 2: {0}".format(this is that))
