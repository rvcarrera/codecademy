# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#learning algorithms - email_one

def censor_one(text, phrase):
    text_split = text.split(' ')
    phrase_split = phrase.split(' ')
    word_index = []
    for i in range(len(phrase_split)):
        for j in range(len(text_split)):
            try:
                if phrase_split[i] == text_split[j] and phrase_split[i+1] == text_split[j+1]:
                    word_index.append(j)
                    word_index.append(j+1)
            except:
                if len(phrase_split) == 1:
                    if phrase_split[i] == text_split[j]:
                        word_index.append(j)
                else:
                    continue
    for index in word_index:
        text_split[index] = '********'
    return ' '.join(text_split)

#print(censor_one(email_one, 'learning algorithms'))

#list of words - email_two

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms", "her", "herself"]

def censor_two(text, words):
    new_text = text
    for word in words:
        new_text = censor_one(new_text, word)
    return new_text

#print(censor_two(email_two, proprietary_terms))

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressing", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_three(text, words):
    text_split = text.split(' ')
    index_list = []
    count = 0
    for text in range(len(text_split)):
        for word in range(len(words)):
            if len(words[word].split(' ')) == 1:
                if text_split[text] == words[word]:
                    count += 1
                    if count > 1:
                        index_list.append(text)
            elif len(words[word].split(' ')) > 1:
                if text_split[text] == words[word].split(' ')[0] and text_split[text + 1] == words[word].split(' ')[1]:
                    count += 1
                    if count > 1:
                        index_list.append(text)
                        index_list.append(text + 1)
    for index in index_list:
        text_split[index] = '*****'
    return ' '.join(text_split)
        
#print(email_three)
#print(censor_three(email_three, negative_words))

def censor_four(text, word_list1, word_list2):
    censor_list = word_list1 + word_list2
    clean_censor_list = [item.split(' ') for item in censor_list]
    splited_text = text.split(' ')
    st_to_censor_index = []
    for st_index in range(len(splited_text)):
        word = splited_text[st_index].lower()
        for ccl_index in range(len(clean_censor_list)):
            word_to_censor = clean_censor_list[ccl_index]
            if len(word_to_censor) == 1:
                if word == word_to_censor[0]:
                    st_to_censor_index.append(st_index - 1)
                    st_to_censor_index.append(st_index)
                    st_to_censor_index.append(st_index + 1)
            else:
                if word == word_to_censor[0] and splited_text[st_index + 1].lower() == word_to_censor[1]:
                    st_to_censor_index.append(st_index - 1)
                    st_to_censor_index.append(st_index)
                    st_to_censor_index.append(st_index + 1)
                    st_to_censor_index.append(st_index + 2)
    for index in st_to_censor_index:
        splited_text[index] = '*****'
    return ' '.join(splited_text)




print(censor_four(email_four, negative_words, proprietary_terms))