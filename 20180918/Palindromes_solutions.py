import re # regular expression

def clean_string(string):
    num_letter = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    output_string = ""
    for character in string:
        if character in num_letter:
            output_string = output_string + character.lower()
    return output_string

def clean_string_RegualarExpression(string):
    return re.sub(r'\W+', '', string).lower()


def isPalindrome_stringParse(string):
    string_len = len(string)
    result = True
    for index, ch in enumerate(string):
        ch_other=string[string_len-index-1]
        if ch <> ch_other:
            result=False
            break
    return result


def isPalindrome_stringParseEfficent(string):
    string_len = len(string)
    result = True
    for x in range(string_len//2):
        ch=string[x]
        ch_other=string[string_len-x-1]
        if ch <> ch_other:
            result=False
            break
    return result


def isPalindrome_reverse1(string1):
    string2 = string1[::-1]
    if string1 == string2:
        return True
    else:
        return False


def isPalindrome_reverse2(string):
    return string == string[::-1]


def isPalindrome_recursive(string):
    if (len(string) <= 2): # base (terminating) case
        return (string[0] == string[-1])
    else:  # recursive case
        print string, string[0], string[-1], string[1:-1]
        return (string[0] == string[-1]) and isPalindrome_recursive(string[1:-1])



# main part of program
palindromes = [ 'this is not a palindrome',
                '7.10.17',
                'A man, a plan, a canal: Panama.',
                'Borrow or rob?',
                "Dammit, I'm mad.", # notice I had to use double quotes to perserve the contained single quote
                'Do geese see God?',
                'Lisa Bonet ate no basil.',
                'Never odd or even',
                'Was it a car or a cat I saw?',
                'Yo, banana boy!',
                '1',
                '11',
                '12']

palindromes = [ 'Yo, bananax boy!']

for string in palindromes:
    string_cleaned = clean_string(string)
    print "original String: "+string
    print " cleaned String: "+string_cleaned

##    result = isPalindrome_stringParse(string_cleaned)
##    print "        isPalindrome_stringParse: "+str(result)
##    result = isPalindrome_stringParseEfficent(string_cleaned)
##    print "isPalindrome_stringParseEfficent: "+str(result)
##    result = isPalindrome_reverse1(string_cleaned)
##    print "           isPalindrome_reverse1: "+str(result)
##    result = isPalindrome_reverse2(string_cleaned)
##    print "           isPalindrome_reverse2: "+str(result)
    result = isPalindrome_recursive(string_cleaned)
    print "          isPalindrome_recursive: "+str(result)
    print
