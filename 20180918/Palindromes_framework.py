palindromes = [ 'this is not a palindrome (test case)',
                '7.10.17',
                'A man, a plan, a canal: Panama.',
                'Borrow or rob?',
                "Dammit, I'm mad.", # notice I had to use double quotes to perserve the contained single quote
                'Do geese see God?',
                'Lisa Bonet ate no basil.',
                'Never odd or even',
                'Was it a car or a cat I saw?',
                'Yo, banana boy!' ]

def isPalindrome(string):
    # write the code to determin if the contents of 'string' is a palindrome
    # and return True/False accordingly

for string in palindromes:
    print "original String: "+string
    results = isPalindrome(string)
    print "is it a palindrone?", results
    print
