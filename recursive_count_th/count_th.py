'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if 'th' in word:
        count = 1
        index = word.find('th') + 2
        remaining_word = word[index:]
        return count + count_th(remaining_word)
    else:
        count = 0
    return count


# Or you could just do

# def count_th(word):
#     return word.count('th')