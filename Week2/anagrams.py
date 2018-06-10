def anagrams(word1, word2):
    word1_list = list(word1.lower())
    word2_list = list(word2.lower())

    word1_list.sort()
    word2_list.sort()

    if ''.join(word1_list) == ''.join(word2_list):
        return "ANAGRAMS"
    else:
        return "NOT ANAGRAMS"
