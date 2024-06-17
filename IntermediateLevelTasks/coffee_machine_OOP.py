class User:

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user1 = User("001", "Martin")
user2 = User("002", "Nigger")

user1.follow(user2)
user2.follow(user1)

print(user1.followers)
print(user1.following)

print(user2.followers)
print(user2.following)