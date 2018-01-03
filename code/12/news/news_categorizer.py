import os

def get_file_list(dir_name):
    return os.listdir(dir_name)

def get_conetents(file_list):
    y_class = []
    X_text = []
    class_dict ={1:"0", 2:"0", 3:"0", 4:"0", 5:"1", 6:"1", 7:"1", 8:"1"}

    for file_name in file_list:
        f = open(file_name, "r")
        category = int(file_name.split("\\")[1].split("_")[0])

        y_class.append(class_dict[category])
        X_text.append(f.read())
    return X_text, y_class


def get_cleaned_text(text):
    import string
    text = "".join([i for i in text if i is not string.punctuation])
    return text


def get_corpus_dict(text):

    all_text = [get_cleaned_text(contents.lower()) for contents in text]
    all_words = [text.split() for text in all_text]
    all_words =[word for text in all_words for word in text]

    from collections import OrderedDict
    corpus_dict = OrderedDict()
    for i,v in enumerate(set(all_words)):
        corpus_dict[v] = i
    return corpus_dict


if __name__ == "__main__":
    dir_name = "news_data"
    file_list = get_file_list(dir_name)
    file_list = [os.path.join(dir_name, file_name) for file_name in file_list]
    X_text, y_class = get_conetents(file_list)
    corpus = get_corpus_dict(X_text)


    print(corpus)
