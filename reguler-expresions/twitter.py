import re


def main():
    url = input("URL: ").strip()
    print(get_twitter_username(url))


def get_twitter_username(url):
    # Add validation to user name the username should be "a-zA-Z0-9_"
    if matches := re.search(
        r"^(?:https?://)?(?:www\.)?(?:twitter|x)\.com/([a-z0-9_]+)$",
        url,
        re.IGNORECASE,
    ):
        return matches.group(1)
    # 7 non capturing group on REGEX with (?:...) and use wolverus operator on conditionals
    # if matches := re.search(
    #     r"^(?:https?://)?(?:www\.)?(?:twitter|x)\.com/(.+)$", url, re.IGNORECASE
    # ):
    #     return matches.group(1)

    # 6 instead of removing url get the user name only
    # and handle if user just type url withput thier username
    # matches = re.search(
    #     r"(https?://)?(www\.)?(twitter|x)\.com/(.+)", url, re.IGNORECASE
    # )
    # if matches:
    #     return matches.group(4)

    # 5 handle if user type any other symbol befor "com" domain like ?com
    # username = re.sub(r"(https?://)?(www\.)?(twitter|x)\.com/", "", url)

    # 4,adding support for urls without protocols like x.com/ehtisham_dev
    # username = re.sub(r"(https?://)?(www\.)?(twitter|x).com/","",url)

    # 3 adding support for twitter new domain "x.com"
    # username = re.sub(r"https?://(www\.)?(twitter|x).com/","",url)

    # 2 handlig the optional "www." in domain
    # username = re.sub(r"https?://(www\.)?twitter.com/","",url)

    # 1 handling http and https
    # username = re.sub("https?://twitter.com/","",url)

    # return username


""" _other-methods_
This methods is just removing the twitter url and not handling all problems user might face 
like using http instead of https and url without domain protocol etc

username = re.sub("https://twitter.com/","",url)
username  = url.removeprefix("https://twitter.com/")
username  = url.replace("https://twitter.com/","")
print(username)
"""

if __name__ == "__main__":
    main()
