from xml.dom import minidom
from news.AbstractNewsParser import AbstractNewsParser

"""
    <item>
        <title>
        In new Yahoo News/YouGov poll, most voters agree with Trump&#39;s impeachment — but support for his removal falls just short of 50%
        </title>
        <description>
        <p><a href="https://news.yahoo.com/in-new-yahoo-news-you-gov-poll-most-voters-agree-with-trumps-impeachment-but-support-for-his-removal-falls-just-short-of-50-002004515.html"><img src="http://l1.yimg.com/uu/api/res/1.2/yKUmQ6vZHHop1XVcNgIDIQ--/YXBwaWQ9eXRhY2h5b247aD04Njt3PTEzMDs-/https://media-mbst-pub-ue1.s3.amazonaws.com/creatr-uploaded-images/2019-12/63ec1200-22b2-11ea-86ff-1be5902577dc" width="130" height="86" alt="In new Yahoo News/YouGov poll, most voters agree with Trump&#39;s impeachment — but support for his removal falls just short of 50%" align="left" title="In new Yahoo News/YouGov poll, most voters agree with Trump&#39;s impeachment — but support for his removal falls just short of 50%" border="0" ></a>The bottom line is that registered voters favor the House’s decision to impeach the president by a 50 percent to 45 percent margin.<p><br clear="all">
        </description>
        <link>
        https://news.yahoo.com/in-new-yahoo-news-you-gov-poll-most-voters-agree-with-trumps-impeachment-but-support-for-his-removal-falls-just-short-of-50-002004515.html
        </link>
        <pubDate>Thu, 19 Dec 2019 19:20:04 -0500</pubDate>
        <source url="https://news.yahoo.com/">Yahoo News</source>
        <guid isPermaLink="false">
        in-new-yahoo-news-you-gov-poll-most-voters-agree-with-trumps-impeachment-but-support-for-his-removal-falls-just-short-of-50-002004515.html
        </guid>
        <media:content height="86" url="http://l1.yimg.com/uu/api/res/1.2/yKUmQ6vZHHop1XVcNgIDIQ--/YXBwaWQ9eXRhY2h5b247aD04Njt3PTEzMDs-/https://media-mbst-pub-ue1.s3.amazonaws.com/creatr-uploaded-images/2019-12/63ec1200-22b2-11ea-86ff-1be5902577dc" width="130"/>
        <media:text type="html">
        <p><a href="https://news.yahoo.com/in-new-yahoo-news-you-gov-poll-most-voters-agree-with-trumps-impeachment-but-support-for-his-removal-falls-just-short-of-50-002004515.html"><img src="http://l1.yimg.com/uu/api/res/1.2/yKUmQ6vZHHop1XVcNgIDIQ--/YXBwaWQ9eXRhY2h5b247aD04Njt3PTEzMDs-/https://media-mbst-pub-ue1.s3.amazonaws.com/creatr-uploaded-images/2019-12/63ec1200-22b2-11ea-86ff-1be5902577dc" width="130" height="86" alt="In new Yahoo News/YouGov poll, most voters agree with Trump&#39;s impeachment — but support for his removal falls just short of 50%" align="left" title="In new Yahoo News/YouGov poll, most voters agree with Trump&#39;s impeachment — but support for his removal falls just short of 50%" border="0" ></a>The bottom line is that registered voters favor the House’s decision to impeach the president by a 50 percent to 45 percent margin.<p><br clear="all">
        </media:text>
        <media:credit role="publishing company"/>
    </item>
"""

class YahooParser(AbstractNewsParser):
    """
    야후 뉴스 받는 구상 클래스
    """
    def get_url(self):
        return "https://news.yahoo.com/rss"

    def parse_content(self, raw_content):
        parsed_content = []

        dom = minidom.parseString(raw_content)

        for node in dom.getElementsByTagName("item"):
            parsed_item ={}
            try:
                parsed_item['title'] = node.getElementsByTagName('title')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['title'] = None

            try:
                parsed_item['content'] = node.getElementsByTagName('description')[0].childNodes[0].nodeValue
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
                parsed_item['published'] = node.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['published'] = None
            parsed_content.append(parsed_item)
        return parsed_content
