from pathlib import Path

import scrapy
import re


class ShareSansarSpider(scrapy.Spider):
    name = "govsite"
    start_urls = [
        "https://sidingbamun.gov.np/staff",
        "https://mikwakholamun.gov.np/staff",
        "https://meringdenmun.gov.np/staff"
    ]

    def parse(self, response):
        emails = []
        for row in response.xpath("//table//tr//td/text()").getall():
            email_match = re.search(r'[\w.-]+@[\w.-]+', row)
            if email_match:
                emails.append(email_match.group(0))
        
        file_path = Path(__file__).parent / "emails.txt"
        file_path.write_text("\n".join(emails))
            