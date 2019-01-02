import csv
from random import shuffle

#considers only those users that have listened to more than 5 different songs
users = []
def split_train_test(validation_csv, dest_seed, dest_checking, ratio, min_songs):
    user_data_list = []
    with open(validation_csv) as csvfile:
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
    seed_songs = []
    checking_songs = []
    #users = users[:100]
    c = 0
    for i in users:
        songs = []
        for j in user_data_list:
            if j[0] == i:
                songs.append(j)
        print("No of songs in total for this user: ", len(songs))
        if(len(songs) > min_songs):
            c += 1
        if(len(songs) > min_songs):
            len_removed = int(len(songs) * ratio)
            print("No of songs to be removed: ", len_removed)
            shuffle(songs)
            checking_songs.extend(songs[:len_removed])
            seed_songs.extend(songs[len_removed:])
    print(seed_songs[0])
    print(checking_songs[0])
    print("No of seed songs: ", len(seed_songs))
    print("No of checking songs: ", len(checking_songs))
    print("No of users with more songs than min_songs: ", c)
    with open(dest_seed, 'w') as csv_file:
		csv_reader = csv.writer(csv_file, delimiter=',')
        #count = 0
		for row in seed_songs:
			csv_reader.writerow(row)
    print("Completed writing seed csv")
    with open(dest_checking, 'w') as csv_file:
		csv_reader = csv.writer(csv_file, delimiter=',')
        #count = 0
		for row in checking_songs:
			csv_reader.writerow(row)
    print("Completed writing checking csv")

#split_train_test('validation_triplets_FINAL.csv', 'validation_triplets_seed.csv', 'validation_triplets_checking.csv', 0.40, 5)
split_train_test('validation_triplets_FINAL_min_5.csv', 'validation_triplets_seed_min_5.csv', 'validation_triplets_checking_min_5.csv', 0.40, 5)