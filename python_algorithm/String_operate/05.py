'''그룹 애너그램'''
import collections

# 내 풀이
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
    return result


# 정렬하여 딕셔너리에 추가
def groupAnagrams(strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values)


if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(words))

