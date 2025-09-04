def count_words(book_text):
    words = book_text.split()
    return len(words)


def char_count(book_text):
    count = {}
    for char in book_text:
        curr = char.lower()
        if curr not in count:
            count[curr] = 0
        count[curr] += 1
    
    return count

def make_list(count):
    char_cnt_list = []
    for key,value in count.items():
        if key.isalpha():
            char_cnt_list.append({"char": key, "count": value})
    return char_cnt_list

def sort_on(items):
    return items["count"]

def sort_list(char_cnt_list):
    char_cnt_list.sort(reverse=True , key=sort_on)
    return char_cnt_list