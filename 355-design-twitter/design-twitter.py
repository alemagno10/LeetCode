from collections import defaultdict, deque

class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.counter))
        self.counter += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for followee in [*self.follows[userId], userId]:
            feed.extend(self.tweets[followee])
        feed.sort(key=lambda x: x[1], reverse=True)
        return [k[0] for k in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].remove(followeeId)
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)