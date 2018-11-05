#akshya srinivasa raghavan
#1001547268
import os
import math
print("Training.................................................")
'''the data set contains 1000 documents from each of the 20 newsgroups'''
no_of_train_data = 500
no_of_test_data = 500
data_folder = "20_newsgroups/"
'''dirs contains all the folders within 20_newsgroups'''
dir = os.listdir(data_folder)
final_dict={}
files_read = 0
total_word_freq={}
folders_processed={}
sum_p=0
for folders in dir:
    temp_word_freq={}
    # print(folder)
    #eg:20_newsgroups/alt.atheisn
    curr_path=data_folder+folders
    curr_file_counter=0
    folder=os.listdir(curr_path)
    for files in folder:
        curr_file_counter=curr_file_counter+1
        if curr_file_counter>no_of_train_data:
            break
        #go to each file within this folder
        temp_path=curr_path+'/'+files
        '''reading each file and converting all the data to lower case and replacing all these symbols with space '''
        curr_file=open(temp_path,'r')
        file_data=curr_file.read()
        file_data=file_data.lower()
        symbols=['\n','+','-','+','_','{','}','[',']','|','\\','\,','"',':',';','<','>',',','.','/','?','!','@','#','$','%','^','&','*','(',')','~','`']
        for i in symbols:
            file_data=file_data.replace(i,' ')
        #print(file_data)
        word_list=file_data.split(' ')
        count=0
        space=[' ']
        count=0
        for word in word_list:
            word.strip()
            if word!=' ':
             freq=temp_word_freq.get(word,0)
             if freq==0:
                temp_word_freq[word]=1
             else:
                new_freq=freq+1
                temp_word_freq[word]=new_freq
             total_freq=total_word_freq.get(word,0)
             if total_freq==0:
                 total_word_freq[word]=1
             else:
                 new_total_freq=total_freq+1
                 total_word_freq[word]=total_freq
        folder.remove(files)
    folders_processed[folders]=folder
    final_dict[folders]=temp_word_freq
print("Testing.................................................")
test_dir=os.listdir(data_folder)
test_total_dic={}
sorted(test_dir, reverse=True)
probability = []
test_final_list={}
hits=0
counter=0
for test_fol in test_dir:
    dic = {}
    testfolder = data_folder + test_fol
    files = os.listdir(testfolder)
    it = 0
    for fi in files:
        it = it + 1
        if it > no_of_test_data:
            break
        add = testfolder + '/'+fi
        testfile = open(add,'r')
        test_file_data = testfile.read()
        test_file_data = test_file_data.lower().strip()
        symbols = ['\n', '+', '-', '+', '_', '{', '}', '[', ']', '|', '\\', '\,', '"', ':', ';', '<', '>', ',', '.','/', '?', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '~', '`']
        for i in symbols:
            test_file_data = test_file_data.replace(i, ' ')
        # print(file_data)
        testfields = test_file_data.split(' ')
        if ' ' in testfields: testfields.remove(' ')
    sump = sum(final_dict[test_fol].values())
    p = 0.0
    for f in testfields:
        value = final_dict[test_fol].get(f, 0.0) + 0.0001
        p = p + math.log(float(value)/float(sump))
    probability.append(p)
    #probability=list(set(probability))
    maximum=max(probability)
    # print(probability.index(maximum))
    # print(test_dir[int(probability.index(maximum))])
    counter=counter+1
    if(test_fol==test_dir[int(probability.index(maximum))]):
        hits=hits+1

# print(success)
# print(counter)
print("Accuracy: "+str(hits/counter*100) + "%")
