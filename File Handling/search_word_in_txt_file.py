
fp1 = open('cat.txt','r')
fp2 = open('catModified2.txt','w+')

List_of_lines = fp1.readlines()


for list_of_words in List_of_lines:
    count = 0
    FinalLinesList = []
    # print(list_of_words,end=(''))
    if 'CAT_' in list_of_words:
        split_list=list_of_words.split()
        # print(split_list)

        for word in split_list:
            if "CAT_" in word:
                modified_word = word.rstrip('.')
                print(modified_word)

                if modified_word in FinalLinesList:
                    print(modified_word)

                else:
                    fp2.write(modified_word)
                    FinalLinesList.append(modified_word)
                    fp2.write('\n')

fp1.close()


















#
# fp = open('cat.txt','r')
# fp2 = open('catModified2.txt','w+')
#
# LinesList = fp.readlines()
# count=0
# FinalLinesList = []
# for line in LinesList:
#     if 'CAT_' in line:
#         wordsList = line.split()
#
#         for word in wordsList:
#             if 'CAT_' in word:
#                 modified_word = word.rstrip('.')
#
#                 print(modified_word)
#                 if modified_word in FinalLinesList:
#                     print(modified_word)
#                 else:
#                     fp2.write(modified_word)
#                     FinalLinesList.append(modified_word)
#                     fp2.write('\n')
# fp.close()