# Project name - URL Shortner ( Converts long urls into short )


import random
import string


DB={} #Database

# Version 1
def getshortURL(LongURL):
    """ This function returns a short URL of  given long URL as required rgument"""
    l=random.randint(5,8) # here we'll get the length each time randomly
    char=string.ascii_uppercase
    random.choice(char)
    shortUrl="".join([random.choice(char) for i in range(l)])

    if shortUrl in DB:
        return getshortURL()
    else:
        DB[shortUrl]=LongURL

    final_url="rt.ind/"+ shortUrl # Suppose rt.ind/ is the company name
    print(final_url)
url="https://twitter.com/account/access"
url2="https://www.youtube.com/"
getshortURL(url)
getshortURL(url2)
# print(DB)

def get_longURL(shortURL):
    """ Given a short url and it will return a long url"""
    key=shortURL.split("/")[-1]
    if key in DB:
        print(DB[key])
    else:
        print("Url is not available , you need to purchase subscription")
get_longURL("EVMOOQKM")


# version 2

def getShortURL(longURL,myShortURL=None):
    """Given a long url  returns short url"""
    if myShortURL:
        if myShortURL in DB:
            return "ShortURL already exists"
        else:
            DB[myShortURL]=longURL
            res="rt.ind/"+myShortURL
            print(res)

        l = random.randint(5, 8)  # here we'll get the length each time randomly
        char = string.ascii_uppercase
        random.choice(char)
        shortUrl = "".join([random.choice(char) for i in range(l)])
        shortURL=string.ascii_lowercase+string.digits

        if shortURL in DB:
            print(getshortURL(longURL))
        else:
            DB[shortUrl]=longURL

        result = "rt.ind/" + myShortURL
        print(result)


print(DB)

















