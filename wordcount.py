## GOOD WORDS ##

# Open txt file of all lyrics.
goodRaw = open("goodLyrics.txt")

# Read contents of txt file and load it into a string
goodString = goodRaw.read()

# Close the file
goodRaw.close()

# Split the string via whitespace into an list
goodArray = goodString.split()

# Remove all special characters
goodWords = [''.join(e for e in string if e.isalnum()) for string in goodArray]

# Make everything lower case
goodWords = [each_string.lower() for each_string in goodWords]

# Remove all duplicates by converting into a dictionary, then back into an list.
goodWords = list(dict.fromkeys(goodWords))


## BAD WORDS ##

# Same steps as GOOD WORDS, just with the badLyrics txt file.

badRaw = open("badLyrics.txt")
badString = badRaw.read()
badRaw.close()
badArray = badString.split()
badWords = [''.join(e for e in string if e.isalnum()) for string in badArray]
badWords = [each_string.lower() for each_string in badWords]
badWords = list(dict.fromkeys(badWords))

## COMPARE LISTS ##

# Create an empty list to store the final bad words.
finalBadWords = []

# Loop through the badWords list, and check if the word exists in the good list
# and add it to the final list if it isn't.
for x in badWords:
    if x not in goodWords:
        #used for debug
        #print(x + " is NOT in Good Words.")
        finalBadWords.append(x)


## CLEAN UP AND OUTPUT ##

finalBadWords.sort()

badWordsLen = str(len(finalBadWords))


output = open("finalBadWords.txt", "w")
output.write("There are " + badWordsLen + " possible bad words:\n")
for n in finalBadWords:
    output.write(n + "\n")

output.close()
