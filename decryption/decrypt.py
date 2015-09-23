import sys, weakref
two_d_f = open("2letterwords.txt","r")
three_d_f = open("3letterwords.txt","r")
four_d_f = open("4letterwords.txt","r")
five_d_f = open("5letterwords.txt","r")
six_d_f = open("6letterwords.txt","r")
seven_d_f = open("7letterwords.txt","r")
eight_d_f = open("8letterwords.txt","r")
nine_d_f = open("9letterwords.txt","r")
ten_d_f = open("10letterwords.txt","r")
eleven_d_f = open("11letterwords.txt","r")
twelve_d_f = open("12letterwords.txt","r")
thirteen_d_f = open("13letterwords.txt","r")
fourteen_d_f = open("14letterwords.txt","r")
fifteen_d_f = open("15letterwords.txt","r")


two_d = two_d_f.read().lower().split()
three_d = three_d_f.read().lower().split()
four_d = four_d_f.read().lower().split()
five_d = five_d_f.read().lower().split()
six_d = six_d_f.read().lower().split()
seven_d = seven_d_f.read().lower().split()
eight_d = eight_d_f.read().lower().split()
nine_d = nine_d_f.read().lower().split()
ten_d = ten_d_f.read().lower().split()
eleven_d = eleven_d_f.read().lower().split()
twelve_d = twelve_d_f.read().lower().split()
thirteen_d = thirteen_d_f.read().lower().split()
fourteen_d = fourteen_d_f.read().lower().split()
fifteen_d = fifteen_d_f.read().lower().split()

dictionary_letters_rev = {"a": 1, "b": 2, "c":3, "d": 4, "e": 5, "f":6, "g": 7,
"h": 8, "i":9, "j": 10, "k": 11, "l":12, "m": 13, "n": 14, "o":15,
"p": 16, "q":17, "r": 18, "s": 19, "t":20, "u": 21, "v": 22, "w":23,
"x": 24, "y":25, "z": 26}

dictionary_dictionaries = {102:two_d, 103:three_d, 104:four_d, 105:five_d,
106:six_d, 107:seven_d, 108:eight_d, 109:nine_d, 110:ten_d, 111:eleven_d,
112:twelve_d, 113:thirteen_d, 114:fourteen_d, 115:fifteen_d}

matches = open("matches.txt", "w")

#enter_encrypted = raw_input("Enter encrypted message: ")
code = "pjq kefp yklexpsvp lxelqxpb em s lxerxsk yf gjqpjqx yp szzekliyfjqf pjq yvpqvpyev em ypf cfqx. - z.s.x. jesxq"
encrypted = "szzekliyfjqf"
encrypted_list = encrypted.split()


def reverse_dictionary(dictionary):
    inv_dictionary = {v: k for k, v in dictionary.items()};
    print inv_dictionary;
    return inv_dictionary;
def search_two ():
    word = ""

    for wordsize in range(0,len(encrypted_list)):
        if len(encrypted_list[wordsize]) >= len(word):
            word = encrypted_list[wordsize]
        #WORD = SZZEKLIYFJQF

    for dictionarysize in range(0,len(dictionary_dictionaries[len(word)+100])):
        dictionary_letters_word_temp = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g",
        8:"h", 9:"i", 10:"j", 11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q",
        18:"r", 19:"s", 20:"t", 21:"u", 22:"v",23:"w", 24:"x", 25:"y", 26:"z"};
        for letter in range(0,len(word)):

            dictionary_letters_word_temp2 = dictionary_letters_word_temp;
            rev_dict = reverse_dictionary(dictionary_letters_word_temp);
            letter_of_dictionary = dictionary_dictionaries[len(word)+100][dictionarysize][letter]
            index_dic_rev = rev_dict[letter_of_dictionary];
            index_word_letter = rev_dict[word[letter]];

            dictionary_letters_word_temp[index_word_letter] = dictionary_letters_word_temp2[index_dic_rev];
            dictionary_letters_word_temp[index_dic_rev] = dictionary_letters_word_temp2[index_word_letter];

        doofus = encrypted;
        for letter in range (0, len(encrypted)):
            if doofus[letter].islower():
                index_dic_rev = dictionary_letters_rev[encrypted[letter]];
                doofus = doofus.replace(encrypted[letter], dictionary_letters_word_temp[index_dic_rev].upper());
        print doofus;
            #else:
                #print doofus[letter];
        if doofus.lower() in dictionary_dictionaries[len(word)+100]:
            matches.write(doofus + "\n");

        dictionary_letters_word_temp = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g",
        8:"h", 9:"i", 10:"j", 11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q",
        18:"r", 19:"s", 20:"t", 21:"u", 22:"v",23:"w", 24:"x", 25:"y", 26:"z"};

search_two();
