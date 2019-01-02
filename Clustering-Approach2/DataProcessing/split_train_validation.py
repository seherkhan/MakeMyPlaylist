import csv
users = []
def split_train_test(dataset_csv, user_data_csv, dest_train, dest_test):
   #read the dataset_csv and store it in a list
    with open(dataset_csv) as f:
        content = f.readlines()
   
    content = [x.strip() for x in content]
    #print("len of playlist detaset: ", len(content))
    #print(content[1])
    # track_ids = []
    dataset_list = []
    for i in content:
        dataset_list.append(i.split("|"))
    print("len of dataset_list: ", len(dataset_list))
    print(dataset_list[1])
    #read the user_data_csv and store it in a list
    user_data_list = []
    with open(user_data_csv) as csvfile:
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
    test_users_len = int(len(users) * 0.15)
    test_users = users[:test_users_len]
    train_users = users[test_users_len: ]
    print("Len of train users: ", len(train_users))
    print("Len of test users: ", len(test_users))
    training_list = []
    testing_list = []
    for i in user_data_list:
        if i[0] in test_users:
            testing_list.append(i)
        else:
            training_list.append(i)
    print(training_list[0])
    print("len of traing list: ", len(training_list))
    print("len of testing list: ", len(testing_list))
    with open(dest_train, 'w') as csv_file:
		csv_reader = csv.writer(csv_file, delimiter=',')
        #count = 0
		for row in training_list:
			csv_reader.writerow(row)
    print("Completed writing training csv")
    with open(dest_test, 'w') as csv_file:
		csv_reader = csv.writer(csv_file, delimiter=',')
        #count = 0
		for row in testing_list:
			csv_reader.writerow(row)
    print("Completed writing test csv")
split_train_test('dataset_cleaned.csv', 'training_triplets_final_sep.csv', 'training_triplets_FINAL.csv', 'validation_triplets_FINAL.csv')