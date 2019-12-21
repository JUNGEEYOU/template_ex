from urllib.request import urlopen


class AbstractNewsParser(object):
    def __init__(self):
        # 클래스 인스턴스 생성 방지
        if self.__class__ is AbstractNewsParser:
            raise TypeError("abstract class cannot be instatiated")

    def print_top_news(self):
        """
         템플릿 메소드. 모든 웹사이트에서 3개의 최신 뉴스를 반환한다.
        :return:
        """
        # 1. url 얻고 피드 서버에 요청 보낸다
        url = self.get_url()
        # 2. 가공되지 않은 콘텐츠 얻는다
        raw_content = self.get_raw_content(url)
        # 3. 파싱한다.
        content = self.parse_content(raw_content)
        # 4. 탑 3만 크롭
        cropped = self.crop(content)
        # 5. 사용자에게 출력해서 보내준다.
        for item in cropped:
            print("Title: ", item['title'])

    def get_url(self):
        """
        url 얻고 피드 서버에 요청 보낸다 - 추상 메소드
        :return:
        """
        raise NotImplementedError()

    def get_raw_content(self, url):
        """
        가공되지 않은 콘텐츠 얻는다
        :param url:
        :return:
        """
        return urlopen(url).read()

    def parse_content(self, content):
        """
        파싱한다 - 추상 메소드
        :param content:
        :return:
        """
        raise NotImplementedError()

    def crop(self, parsed_content, max_items=3):
        return parsed_content[:max_items]



