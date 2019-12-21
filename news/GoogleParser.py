from xml.dom import minidom
from news.AbstractNewsParser import AbstractNewsParser
"""
<entry>
    <id>
    https://news.google.com/stories/CAAqOQgKIjNDQklTSURvSmMzUnZjbmt0TXpZd1NoTUtFUWpjbEpuRWxJQU1FY1otVlNZX3RhRmhLQUFQAQ?oc=5
    </id>
    <title type="html">유성엽 석패율 대상서 중진 제외… 청년·여성·정치신인 한정 - 매일경제 - 매일경제</title>
    <updated>2019-12-20T01:55:10.000000000Z</updated>
    <link href="https://news.google.com/__i/rss/rd/articles/CBMiOGh0dHBzOi8vd3d3Lm1rLmNvLmtyL25ld3MvcG9saXRpY3Mvdmlldy8yMDE5LzEyLzEwNjg1Mjcv0gE6aHR0cHM6Ly9tLm1rLmNvLmtyL25ld3MvcG9saXRpY3Mvdmlldy1hbXAvMjAxOS8xMi8xMDY4NTI3Lw?oc=5" type="text/html"/>
    <content type="html">
    <ol><li><a href="https://news.google.com/__i/rss/rd/articles/CBMiOGh0dHBzOi8vd3d3Lm1rLmNvLmtyL25ld3MvcG9saXRpY3Mvdmlldy8yMDE5LzEyLzEwNjg1Mjcv0gE6aHR0cHM6Ly9tLm1rLmNvLmtyL25ld3MvcG9saXRpY3Mvdmlldy1hbXAvMjAxOS8xMi8xMDY4NTI3Lw?oc=5" target="_blank">유성엽 석패율 대상서 중진 제외… 청년·여성·정치신인 한정 - 매일경제</a>&nbsp;&nbsp;<font color="#6f6f6f">매일경제</font></li><li><a href="https://news.google.com/__i/rss/rd/articles/CBMiK2h0dHBzOi8vd3d3LnlvdXR1YmUuY29tL3dhdGNoP3Y9aTJwYkM2R1FiOVnSAQA?oc=5" target="_blank">협상도 멈춰선 '4+1 선거법'…'석패율제' 장기 대치</a>&nbsp;&nbsp;<font color="#6f6f6f">JTBC News</font></li><li><strong><a href="https://news.google.com/stories/CAAqOQgKIjNDQklTSURvSmMzUnZjbmt0TXpZd1NoTUtFUWpjbEpuRWxJQU1FY1otVlNZX3RhRmhLQUFQAQ?oc=5" target="_blank">Google 뉴스에서 전체 콘텐츠 보기</a></strong></li></ol>
    </content>
</entry>
"""
class GoogleParser(AbstractNewsParser):
    """
        atom 피 받는 구상 클래스
    """

    def get_url(self):
        return "https://news.google.com/atom?hl=ko&gl=KR&ceid=KR:ko"

    def parse_content(self, raw_content):
        parsed_content = []

        dom = minidom.parseString(raw_content)

        for node in dom.getElementsByTagName("entry"):
            parsed_item = {}
            try:
                parsed_item['title'] = node.getElementsByTagName('title')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['title'] = None

            try:
                parsed_item['content'] = node.getElementsByTagName('content')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['content'] = None

            try:
                parsed_item['link'] = node.getElementsByTagName('link')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['link'] = None

            try:
                parsed_item['id'] = node.getElementsByTagName('guid')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['id'] = None

            try:
                parsed_item['published'] = node.getElementsByTagName('updated')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['published'] = None
            parsed_content.append(parsed_item)
        return parsed_content
