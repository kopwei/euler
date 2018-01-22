import os
def get_word_number(word):
    if not word:
        return 0
    val = 0
    for i in word:
        val += ord(i) - 64
    return val

if __name__ == "__main__":
    t_numbers = []
    for i in range(1, 40):
        t_numbers.append(i * (i + 1) / 2)
    with open(os.path.dirname(__file__) + "/word.txt", 'r') as f:
        line = f.readline()
        quoted_words = line.split(',')
        words = [w.replace("\"", '') for w in quoted_words]
        num_of_twords = 0
        for word in words:
            word_number = get_word_number(word)
            if word_number in t_numbers:
                num_of_twords+=1
                print(word)
        print(num_of_twords)
