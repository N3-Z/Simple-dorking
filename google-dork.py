from googlesearch import search
import getopt
import sys

req = 0
search_ = ""
max_ = 10 
interval_ = 2

def help():
    print("Google-dorking")
    print("Example:")
    print("python [file.py] -s [search]")
    print("python [file.py] -s [search] -m [max]")
    print("\t-s\t\tSearch")
    print("\t-m\t\tMaximum result")
    print("\t-t\t\tInterval")


def run():
    global search_, max_, req
    for url in search(search_, tld="com", lang="en", num=max_, start=0, stop=None, pause=interval_):
        print(url)
        req += 1
        if req >= max_:
            break;

def main():
    global search_, page_, engine_
    args,_ = getopt.getopt(sys.argv[1:], "s:m:t:h")
    for key,value in args:
        if key == "-s":
            search_ = value
        elif key == "-m":
            max_ = value
        elif key == "-t":
            interval_ = value
        elif key == "-h":
            help()
            return
    run()
        

if __name__ == "__main__":
    main()