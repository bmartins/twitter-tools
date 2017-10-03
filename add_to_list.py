import twitter
import local_settings as settings
import sys
import time

api = twitter.Api(consumer_key=settings.consumer_key, consumer_secret=settings.consumer_secret, access_token_key=settings.access_token, access_token_secret=settings.access_token_secret)

#print(api.VerifyCredentials())

list_id = None

for l in api.GetLists():
    print l
    if l.name == settings.list_name:
        list_id = l.id


print list_id
if list_id is not None:
    user = sys.stdin.readline()
    while user != '':
        user = user.rstrip()
        print user
        try:
            api.CreateListsMember(list_id=list_id, screen_name=user)
        except Exception:
            print "failed to add this member"
        else:
            print "added..."
        time.sleep(2)
        user = sys.stdin.readline()




