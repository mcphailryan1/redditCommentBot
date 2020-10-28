import praw

#Enter your correct Reddit information below

userAgent = '' #The userAgent can be anything. Usually people us it as a description
cID = '' #This is your personal use script, given to you by reddit
cSC = '' #This is your secret code, given to you by reddit
userN = 'username' #This is your reddit username
userP = 'password' #This is your reddit password

numFound = 0
reddit = praw.Reddit(user_agent=userAgent,
                    client_id=cID,
                    client_secret=cSC,
                    username=userN,
                    password=userP)

subreddit = reddit.subreddit('') #This is the subreddit you want to monitor

bot_phrase = '' #This is the phrase that the bot replies with

keywords = {'this', 'is', 'the', 'format', 'for', 'multiple', 'keywords'} #these are the keywords the bot looks for in subreddits

for submission in subreddit.hot(limit=15):
    n_title = submission.title.lower()
    for i in keywords:
        if i in n_title:
            numFound = numFound +1
            print('Comment bot is replying to: ')
            print("Title: ", submission.title) #This prints the title of the commented on
            print("Text: ", submission.selftext) #This prints the text of the post commented on
            print("Score: ", submission.score) #This prints the score of the post commented on
            print("--------------------------------------")
            print('Comment bot saying: ', bot_phrase) #This prints the comment
            print()
            submission.reply(bot_phrase) #This makes the bot comment

if numFound == 0:
    print()
    print("Sorry, didn't find any posts that contained those keywords under that subreddit.")