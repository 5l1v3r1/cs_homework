import tweepy #Import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.home_timeline()

#Input Twitter usernames
user1 = raw_input("User 2: ")
user2 = raw_input("User 1: ")

#Define function
def get_last_tweets(self, i):
    tweet = self.client.user_timeline(id = self.client_id, count = 10)[i]
    print(tweet.text)

#Get last 10 tweets for user1
for i in range(10):
    get_last_tweets(user1, i)

#Get last 10 tweets for user2
for i in range(10):
    get_last_tweets(user1, i)


#Define follower count
follower_count1 = api.get_user(user1).followers_count
follower_count2 = api.get_user(user2).followers_count

#Print amount of followers per user
print "User1 has " + str(follower_count1) + " followers."
print "User2 has " + str(follower_count2) + " followers."


#Define word count
words_user1 = api.get_user(user1).tweets_word_count
words_user2 = api.get_user(user2).tweets_word_count

#Print amount of words for each user
print "User1 has " +str(words_user1)+ " words in his tweets."
print "User2 has " +str(words_user2)+ " words in his tweets."

#Check which user has a higher Followers x Words product
if follower_count1*words_user1 > follower_count2*words_user2:
    print(str(user1)+" has a higher Followers x Words product than "+str(user2))
elif follower_count2*words_user2 > follower_count1*words_user1:
    print(str(user2)+" has a higher Followers x Words product than "+str(user1))
else:
    print("Users' products are equal.")