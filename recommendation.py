header = ["Name", "Gender", "Age", "Interest"]
users = [
    ["UserA", "Female", 25, "Cricket"],
    ["UserB", "Male", 27, "Cricket, Football, Movies"],
    ["UserC", "Male", 26, "Movies, Tennis, Football, Cricket"],
    ["UserD", "Female", 24, "Tennis, Football, Badminton"],
    ["UserE", "Female", 32, "Cricket, Football, Movies, Badminton"],
]

if __name__ == '__main__':
    input_user = "UserB"
    input_count=2

    gender = ""
    age = 0
    interest = ""
    for user in users:
        if user[0] == input_user:
            gender = user[1]
            age = int(user[2])
            interest = user[3]
            break

    input_interests = interest.split(", ")
    matched = []

    for user in users:
        if user[0] == input_user:
            user.append(0)
        else:
            user_integests = user[3].split(", ")
            matched_count = 0
            for ii in input_interests:
                for ui in user_integests:
                    if ii == ui:
                        matched_count += 1
            user.append(matched_count)
        matched.append(user)

    matched.sort(key=lambda x: (x[4],x[1]!=gender,x[2]-age),reverse=True)
    print(matched[0:input_count])
