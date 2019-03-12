import util.data as data
import semantic_scholar.s2data as s2data


def get_each_conference_papers():
  for conf_name, conf_dict in data.getAllConferences():
    yield conf_name, conf_dict["papers"]

# matches semantic scholar papers to their appropriate conference,
# as organized in /authors/data/conf/
def get_conferences_for_s2():
  conf_papers = list(get_each_conference_papers())
  papers = s2data.get_dict_gA()
  for paper_id, paper in papers.items():
