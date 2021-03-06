import json

# 크롤링
from ruri_crawler import WebCrawler


# 크롤링
class Crawling:
    def setcsstags(self):
        ## 크롤링에 쓸 css태크 호출
        with open('C:/Java/data/hr/hr/mycrawling.json') as f:
            print('css tag가 설정된 %s파일을 호출합니다 : ' % f.name)
            cdata = json.load(f)
            return cdata

    def crawling(self, lastpage):
        cdata = self.setcsstags()
        ## 순서대로 번호, 게시글 링크, 제목, 추천, 게시글 내 링크, 댓글
        wc = WebCrawler()
        result = wc.crawlingposts(
            lastpage,
            cdata['cno'],
            cdata['clink'],
            cdata['ctitle'],
            cdata['cthumb'],
            cdata['ccontent'],
            cdata['clinks'],
            cdata['creplies']
        )
        return result

