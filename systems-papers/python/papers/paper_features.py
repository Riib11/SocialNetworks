import utils.data as u_data

def getBibtex(paper_id):
    with open(u_data.papers_directory + paper_id + ".bibtex", 'r') as file:
        lines = []
        start = True
        for line in file:
            line = line.strip()
            if start:
                if line.startswith("@article"):
                    start = False
                else:
                    lines.append(line)
            else:
                if line.startswith("}"):
                    start = True
        return lines


def getBibtexValue(line):
    i = line.index("{")
    line = line[i+1:]
    i = line.index("}")
    line = line[:i]
    return line

def getCitationsTitles(paper_key):
    bibtex = getBibtex(paper_key)
    titles = []
    
    inside = False
    for line in bibtex:
        if not inside:
            if line.startswith("@proceedings"):
                inside = True
        else:
            if line.startswith("title"):
                titles.append(getBibtexValue(line))
            elif line.startswith("}"):
                inside = False
    
    return titles

def toDataAuthorName(name):
    name = name.split(",")
    for i in range(len(name)):
        name[i] = name[i].replace(" ","").replace(".","")
    if len(name) == 2:
        return name[1]+" "+name[0]
    return name[0]

def getCitationsData(paper_key):
    bibtex = getBibtex(paper_key)
    data = {"size":0,"author":[],"journal":[],"title":[],"year":[]}
    keys = data.keys()
    inside = False
    for line in bibtex:
        if not inside:
            inside = line.startswith("@proceedings")
        else:
            if line.startswith("}"):
                inside = False
                data["size"] += 1
            else:
                value = getBibtexValue(line)
                for key in keys:
                    if line.startswith(key):
                        if key == "author":
                            value = [ toDataAuthorName(n) for n in value.split(".,")]
                        data[key].append(str(value))
    return data