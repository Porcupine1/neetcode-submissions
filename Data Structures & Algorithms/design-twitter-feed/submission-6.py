from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.net = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        hp = []
        def push_trim(items):
            for t, tid in items:
                heapq.heappush(hp, (t, tid))
                if len(hp) > 10:
                    heapq.heappop(hp)

        push_trim(self.posts[userId][-10:])

        for f in self.net[userId]:
            push_trim(self.posts[f][-10:])

        hp.sort(reverse=True)
        return [tid for _, tid in hp]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.net[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.net[followerId]:
            self.net[followerId].remove(followeeId)

