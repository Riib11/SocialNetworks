import urllib.parse

application = "Safari"

def format_title(title):
    return urllib.parse.quote(title.encode("utf-8"))

def make_query_url(title):
    title = format_title(title)
    return "https://www.semanticscholar.org/search?q="+title+"&sort=relevance"

def make_query(title):
    return "open -a "+application+" "+make_query_url(title)+"\n"

titles = [ title.replace("\n","") for title in open("../notes/missing_titles_gA.txt") ]

titlesecs_count = 15
titlesecs = []
for i in range(len(titles)):
    if i%titlesecs_count == 0: titlesecs.append([])
    titlesecs[-1].append(titles[i])

for i in range(len(titlesecs)):
    with open("../script/open_missingtitlequeries_gA_sec"+str(i), "w+") as file:
        for t in titlesecs[i]: file.write(make_query(t))