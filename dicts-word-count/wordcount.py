import sys

def word_count():

    word_dict = {}

    for line in open(sys.argv[1]):
        
        line = line.split()

        for word in line:
            
            word_dict[word] = word_dict.get(word, 0) + 1
    
    for word, count in word_dict.items():
        print(f'{word} {count}')

word_count()
