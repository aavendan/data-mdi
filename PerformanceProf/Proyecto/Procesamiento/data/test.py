from nltk.corpus import wordnet

def get_word_synonyms_from_sent(word, sent):

    word_synonyms = []
    print("1 " + str(wordnet.synsets(word, lang='spa')))
    for synset in wordnet.synsets(word, lang='spa'):
        print("2 " + str(synset.lemma_names(lang='spa')))
        for lemma in synset.lemma_names(lang='spa'):
            if lemma in sent:
                word_synonyms.append(lemma)
    return word_synonyms

word = "comer"
sent = ['yo', 'quiero', 'almorzar', 'un', 'carne', 'ahora', '.']
word_synonyms = get_word_synonyms_from_sent(word, sent)
print ("WORD:", word)
print ("SENTENCE:", sent)
print ("SYNONYMS FOR '" + word.upper() + "' FOUND IN THE SENTENCE: " + ", ".join(word_synonyms))