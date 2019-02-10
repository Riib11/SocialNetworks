def extract_id(link):
    for i in range( len(link)-1 , -1 , -1 ):
        c = link[i]
        if c == "/": return link[i+1:]

with open("missing_links_gA.txt", "r+") as links:
    with open("missing_ids_gA.txt", "w+") as ids:
        for link in links:
            link = link.replace("\n","")
            id = extract_id(link)
            print(id)
            ids.write(id+"\n")