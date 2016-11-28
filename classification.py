import sys

sentimentData = 'Dictionary1.txt'
twitterData = 'Dataset3.txt'


def tweet_dict(twitterData):
    ''' (file) -> list of dictionaries
This method should take your output.txt
file and create a list of dictionaries.
'''
    twitter_list_dict = []
    # storing the user given sentance to the dictionary for the classification
    Data=open(twitterData)
    for line in Data:
        line_1=line.lstrip(' ')
        twitter_list_dict.extend([line_1])
    # twitter_list_dict = ["it is good not bad","good movie i love it", "hate this, really hate this movie"] you can use this if you want to work with direct list with data
    #print twitter_list_dict
    return twitter_list_dict



def sentiment_dict(sentimentData):
    ''' (file) -> dictionary
This method should take your sentiment file
and create a dictionary in the form {word: value}
'''
    afinnfile = open(sentimentData)
    scores = {}  # initialize an empty dictionary
    for line in afinnfile:
        score, term = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        term,junck=term.split('\n')
        scores[term] = float(score)  # Convert the score to an integer.
    print scores
    return scores  # Print every (term, score) pair in the dictionary


def main():
    tweets = tweet_dict(twitterData)
    sentiment = sentiment_dict(sentimentData)

    '''Create a method below that loops through each tweet in your
twees_list. For each individual tweet it should add up you sentiment
score, based on the sent_dict.
'''
    result = []
    for index in range(len(tweets)):

        tweet_word = tweets[index].split()
        # sent_score is a variable which will take care of word strength / word weightage
        sent_score = 0
        for word in tweet_word:
            word = word.rstrip('?:!.,;"!@')  # delete the char in the end of the String
            word = word.replace("\n", "")

            if word in sentiment.keys():
                sent_score = sent_score + float(sentiment[word])
                #print word, sentiment[word]

            else:
                sent_score = sent_score

        if float(sent_score) > 0.7:
            sent_score = 1
        elif float(sent_score) < -0.7:
            sent_score = -1
        else:
            sent_score = 0
        result.extend([sent_score])

        #print sent_score
        '''
        if float(sent_score) > 0:
            print tweets[index]
            if float(sent_score) > 0.7:
                print sent_score
                print 'Highly Positive Sentiment'
            else:
                print sent_score
                print 'Positive Sentiment'

        if float(sent_score) < 0:
            print tweets[index]
            if float(sent_score) < -0.7:
                print sent_score
                print 'Highly Negative Sentiment'
            else:
                print sent_score
                print 'Negative Sentiment'

        if float(sent_score) == 0:
            print tweets[index]
            print 'Neutral Sentiment'
        '''
    label = open('labels3.txt')
    count = 0
    num = 0
    for line in label:
        line2 = line.strip('\xef,\xbb,\xbf,\n')
        if result[count] == int(line2):
            num = num+1
        count = count + 1
    print "accuracy: ",float(num)/(len(tweets))
    #print result

if __name__ == '__main__':
    main()

