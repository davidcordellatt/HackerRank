from html.parser import HTMLParser

L=int(input())

class Res_html(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :",tag)
        if attrs:
            for item in attrs:
                print("->",item[0],">",item[1])
    def handle_endtag(self, tag):
        print("End   :",tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :",tag)
        if attrs:
            for item in attrs:
                print("->",item[0],">",item[1])
new_html = Res_html()
for _ in range(L):
    new_html.feed(input())