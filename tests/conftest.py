import pytest
from scrapy.http import HtmlResponse

from tutorial.spiders.quotes_spider import QuotesSpider


@pytest.fixture
def spider():
    """
    Spider instance to be used in testing.

    :return: Spider instance;
    """
    return QuotesSpider()


@pytest.fixture
def mock_html_page():
    html_content = """
    <html>
        <body>
            <div class="row">
                <div class="col-md-8">
                    <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
                        <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
                        <span>by <small class="author" itemprop="author">Albert Einstein</small>
                        <a href="/author/Albert-Einstein">(about)</a>
                        </span>
                        <div class="tags">
                            Tags:
                            <meta class="keywords" itemprop="keywords" content="change,deep-thoughts,thinking,world" /    >
                            <a class="tag" href="/tag/change/page/1/">change</a>
                            <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
                            <a class="tag" href="/tag/thinking/page/1/">thinking</a>
                            <a class="tag" href="/tag/world/page/1/">world</a>
                        </div>
                    </div>
                    <nav>
                        <ul class="pager">
                            <li class="next">
                                <a href="/page/2/">Next <span aria-hidden="true">&rarr;</span></a>
                            </li>
                        </ul>
                    </nav>
                </div>
            </div>
        </body>
    </html>    
    """
    return HtmlResponse(
        url="https://quotes.toscrape.com/page/1/", body=html_content, encoding="utf-8"
    )
