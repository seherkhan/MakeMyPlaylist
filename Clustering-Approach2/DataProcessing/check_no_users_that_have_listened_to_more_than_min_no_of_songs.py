import csv
from random import shuffle

#considers only those users that have listened to more than 5 different songs
users = []
def split_train_test(triplet_csv, min_songs):
    user_data_list = []
    with open(triplet_csv) as csvfile:
        rows = csv.reader(csvfile)
        user_data_list = list(rows)
    print("converted the user data csv file")
    print("len of user_data_list: ", len(user_data_list))
    # print(user_data_list[1])
    # get all unique users
    users = []
    for i in user_data_list:
            users.append(i[0])
    users = list(set(users))
    print("Completed finding out number of users: ")
    print("Total number of unique users: ", len(users))
    c = 0
    for i in users:
        songs = []
        for j in user_data_list:
            if j[0] == i:
                songs.append(j)
        #print("No of songs in total for this user: ", len(songs))
        if(len(songs) > min_songs):
            print(c)
            c += 1
        
    print("No of users with more songs than min_songs: ", c)
   

split_train_test('test_triplets_FINAL.csv', 5)