'''그룹 애너그램'''

def groupAnagrams(words):
    words_dict  = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        words_dict[word] = sorted_word
    
    result = []
    for key, value in words_dict.items():
        isIn = False
        for r in result:
            if key in r:
                isIn = True
        if not isIn:
            result.append([k for k, v in words_dict.items() if v == value])
    print(result)

if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    groupAnagrams(words)