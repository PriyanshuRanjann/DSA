"""
Find Frequency of Characters in Python
"""

freq= {}
def get_char_freq(s: str):
    try:
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        return freq
    except Exception as e :
        raise e

if __name__=="__main__":
    s = input('Enter String:')
    result = get_char_freq(s)
    print(s)
    print(result)
