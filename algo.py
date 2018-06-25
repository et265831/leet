class ReverseInteger:
    def run(self, x):
        #O(n), n = length of x
        low = -1 * pow(2, 31)
        high = pow(2, 31) - 1
        neg = x<0
        if neg:
            x*=-1
        results = 0

        while x != 0:
            last = x%10
            x = x//10
            results = results*10 + last
        results = results if not neg else -1 * results
        if results < high and results > low:
            return results
        else:
            return 0
class Palindrome:
    #Condition: solve without string conversion
    def isPalindrome(self, x):
        original = x
        if x<0:
            return False
        else:
            rev = 0
            while x != 0:
                tail = x%10
                x = x//10
                rev= rev*10 + tail
            return rev == original
class RomanConvert:
    def run(self, inp):
        # example XIV:
        # X = 10, pred = 9999, pred > suc => res + 10 = 10
        # I = 1, pred = 10 pred > suc => res + 1 = 11
        # V = 5, pred = 1 pred < suc => res -= pred*2 = 9; res += suc = 9+5 = 14
        # return 14
        # this example only searched for dict once in each loop

        rom_dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        res = 0
        pred = 9999
        for i, roman in enumerate(inp):
            suc = rom_dict[roman]
            if pred < suc:
                res -= pred*2
            res += suc
            pred = suc
        return res
    def run_two_dict_search(self, s):
        # intuitive solution, but check dict twice in each loop
        rom_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        for i, roman in enumerate(s):
            roman = rom_dict[roman]
            if i < len(s) - 1:
                next_roman = rom_dict[s[i + 1]]
                if roman >= next_roman:
                    res += roman
                else:
                    res -= roman
            else:
                res += roman
        return res
class LongestCommonPrefix:
    def longestCommonPrefix(self, strs):

        prefix = ""
        # if strs is empty, return ""
        if len(strs)==0:
            return prefix
        # for each n-th charactor in first word, check the n-th character in second-to-last words
        # if n is out of bound, or n-th character in second-to-last words is not the same as n-th character in first word, break for
        # if char_match_all, add prefix, if not char_match_all, terminate and return prefix
        for i, char in enumerate(strs[0]):
            char_match_all = True
            for sen in strs[1:]:
                if i>=len(sen) or sen[i] != char:
                    char_match_all = False
                    break
            if char_match_all:
                prefix += char
            else:
                break
        return prefix














