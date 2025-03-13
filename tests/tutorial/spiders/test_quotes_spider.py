from scrapy.http import Request


def test_start_requests(spider):
    """
    Test that Spider stars correctly and generates the defined requests.

    :param spider: instance of spider;
    """
    requests = list(spider.start_requests())
    assert len(requests) == 2
    assert requests[0].url == "https://quotes.toscrape.com/page/1/"
    assert requests[1].url == "https://quotes.toscrape.com/page/2/"


def test_parse_quote(spider, mock_html_page):
    """
    Test that Spider is returned correctly the information from site.

    :param spider: instance of spider;
    :param mock_html_page: mock of HTML page;
    """
    results = list(spider.parse(mock_html_page))

    items = [item for item in results if isinstance(item, dict)]

    # pylint: disable=line-too-long
    expected_item = {
        "text": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”",
        "author": "Albert Einstein",
        "tags": ["change", "deep-thoughts", "thinking", "world"],
    }  # pylint: enable=line-too-long

    assert len(items) == 1
    assert items[0] == expected_item


def test_parse_quotes_next_page(spider, mock_html_page):
    """
    Test if exists next page.

    :param spider: instance of spicer;
    :param mock_html_page: mock of HTML page;
    """
    results = list(spider.parse(mock_html_page))
    next_page_requests = [r for r in results if isinstance(r, Request)]
    assert len(next_page_requests) == 1
    assert next_page_requests[0].url == "https://quotes.toscrape.com/page/2/"
