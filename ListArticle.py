# encoding: utf-8
import re,urllib,sys
import article as art
import xpinyin
from workflow import Workflow
def main(wf):
    site_path = wf.args[0]
    articles = art.Articles(site_path)
    py = xpinyin.Pinyin()
    if len(wf.args) == 2:
        query = wf.args[1]
    else:
        query = ""
    for article in articles.articles:
        if not (query == "" or query in py.get_pinyin(article['title'],'').lower() or query in py.get_pinyin(article['category'],'').lower()):
            continue
        wf.add_item(title = article['title'],
                    subtitle = article['date']+" " + article['category'],
                    arg = '[%s](./%s)' % (article['title'],article['link']),
                    valid=True,
                    icon = "doc.png")

    wf.send_feedback()

if __name__ == "__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
