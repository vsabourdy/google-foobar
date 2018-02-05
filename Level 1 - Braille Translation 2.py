# Braille translation 2
# ===================
# 
# Because Commander Lambda is an equal-opportunity despot, she has several visually-impaired minions. But she never bothered to follow intergalactic standards for workplace accommodations, so those minions have a hard time navigating her space station. You figure printing out Braille signs will help them, and - since you'll be promoting efficiency at the same time - increase your chances of a promotion.
# 
# Braille is a writing system used to read by touch instead of by sight. Each character is composed of 6 dots in a 2x3 grid, where each dot can either be a bump or be flat (no bump). You plan to translate the signs around the space station to Braille so that the minions under Commander Lambda's command can feel the bumps on the signs and "read" the text with their touch. The special printer which can print the bumps onto the signs expects the dots in the following order:
# 1 4
# 2 5
# 3 6
# 
# So given the plain text word "code", you get the Braille dots:
# 
# 11 10 11 10
# 00 01 01 01
# 00 10 00 00
# 
# where 1 represents a bump and 0 represents no bump.  Put together, "code" becomes the output string "100100101010100110100010".
# 
# Write a function answer(plaintext) that takes a string parameter and returns a string of 1's and 0's representing the bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters, handle capital letters by adding a Braille capitalization mark before that character, and use a blank character (000000) for spaces. All signs on the space station are less than fifty characters long and use only letters and spaces.
#
# ===================
# Due to some dark bug, my time to send the solution was expired even if I had plenty of hours left.
#
# The direct translation of the alphabet into Braille using an array was for me the simpliest and most effective way.
# There is some kind of patterns to calculate Braille letters (http://www.brl.org/intro/session02/abcs.html)
# But it would just add unwanted complexity.
# With this solution, you can easily maintain the code. Numbers translation can be effortlessly implemented.
# ===================


def answer( plaintext ):
    brailleText = ""
    
    for ch in list ( plaintext ):
        brailleText += returnCharAsBrailleCode( ch )
        
    return brailleText

def returnCharAsBrailleCode( letter ):
    brailleCode = ""
    
    if letter.isupper():
        brailleCode += "000001"
        
    brailleCode += brailleAlphabet[ ord( letter.lower() ) ]
    
    return brailleCode

def generateBrailleAlphabet():
    brailleAlphabet = [None]*123
    
    brailleAlphabet[32] = "000000"
    brailleAlphabet[97] = "100000"
    brailleAlphabet[98] = "110000"
    brailleAlphabet[99] = "100100"
    brailleAlphabet[100] = "100110"
    brailleAlphabet[101] = "100010"
    brailleAlphabet[102] = "110100"
    brailleAlphabet[103] = "110110"
    brailleAlphabet[104] = "110010"
    brailleAlphabet[105] = "010100"
    brailleAlphabet[106] = "010110"
    brailleAlphabet[107] = "101000"
    brailleAlphabet[108] = "111000"
    brailleAlphabet[109] = "101100"
    brailleAlphabet[110] = "101110"
    brailleAlphabet[111] = "101010"
    brailleAlphabet[112] = "111100"
    brailleAlphabet[113] = "111110"
    brailleAlphabet[114] = "111010"
    brailleAlphabet[115] = "011100"
    brailleAlphabet[116] = "011110"
    brailleAlphabet[117] = "101001"
    brailleAlphabet[118] = "111001"
    brailleAlphabet[119] = "010111"
    brailleAlphabet[120] = "101101"
    brailleAlphabet[121] = "101111"
    brailleAlphabet[122] = "101011"
    
    return brailleAlphabet
    
brailleAlphabet = generateBrailleAlphabet()


print answer("The quick brown fox jumps over the lazy dog")
# 000001101010000001101100000001110110000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110

