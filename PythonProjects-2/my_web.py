from instapy import InstaPy

session = InstaPy(username="__jptattoo", password="rvvjayprakash!?!?")
session.login()
session.like_by_tags(["bmw", "mercedes"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "so hard man!", "Beautiful"])
session.end()