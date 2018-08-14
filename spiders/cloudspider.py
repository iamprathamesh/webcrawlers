# -*- coding: utf-8 -*-
import scrapy


class CloudspiderSpider(scrapy.Spider):
    name = 'cloudspider'
#    allowed_domains = ['http://www.copssolutions.atwebpages.com/spider.html','http://flipkart.com']
    start_urls = ['http://copssolutions.atwebpages.com/spider.html']

    def parse(self, response):
        user_query = response.css('div.search1::attr(name)').extract_first()
        search_url = 'https://www.flipkart.com/search?q=' + user_query
        search_url = response.urljoin(search_url)
        yield scrapy.Request(url=search_url, callback=self.parseflipkart)





    def parseflipkart(self, response):
        value = response.css('div._1vC4OE::text').extract()
        name_value = response.css('div._3wU53n::text').extract()
        link_value = response.css('a._1UoZlX::attr(href)').extract()
        image_value = response.css('div._3BTv9X').xpath('//img/@src').extract()
        rating_list = response.css('div.hGSR34::text').extract()

        if not link_value:
            value = response.css('div._1vC4OE::text').extract()
            name_value = response.css('a._2cLu-l::text').extract()
            link_value = response.css('a._2cLu-l::attr(href)').extract()
            image_value = response.css('div._3BTv9X').xpath('//img/@src').extract()
            rating_list = response.css('div.hGSR34::text').extract()

            one = int(float(value[1].replace(",", "")))
            two = int(float(value[3].replace(",", "")))
            three = int(float(value[5].replace(",", "")))
            four = int(float(value[7].replace(",", "")))
            five = int(float(value[9].replace(",", "")))

            rating_one = float(rating_list[0].replace(",", ""))
            rating_two = float(rating_list[2].replace(",", ""))
            rating_three = float(rating_list[4].replace(",", ""))
            rating_four = float(rating_list[6].replace(",", ""))
            rating_five = float(rating_list[8].replace(",", ""))
        else:
            one = int(float(value[1].replace(",", "")))
            two = int(float(value[3].replace(",", "")))
            three = int(float(value[5].replace(",", "")))
            four = int(float(value[7].replace(",", "")))
            five = int(float(value[9].replace(",", "")))

            rating_one = float(rating_list[0].replace(",", ""))
            rating_two = float(rating_list[2].replace(",", ""))
            rating_three = float(rating_list[4].replace(",", ""))
            rating_four = float(rating_list[6].replace(",", ""))
            rating_five = float(rating_list[8].replace(",", ""))

        maxi = max(one, two, three, four, five)

        if one is 0:
            one = maxi
        if two is 0:
            two = maxi
        if three is 0:
            three = maxi
        if four is 0:
            four = maxi
        if five is 0:
            five = maxi

        total = one + two + three + four + five
        avg = int(total / 5)
        diff = maxi - avg
        percent = int(diff * 100 / maxi)
        if percent < 10:
            diff = diff * 2
        if percent > 30:
            div = int(percent / 20)
            diff = int(diff / div)
        mini = avg - diff

        list_price = [one, two, three, four, five]
        list_price.sort()

        if one not in range(mini, maxi + 1):
            list_price.remove(one)
            list_price.append(one)
        if two not in range(mini, maxi + 1):
            list_price.remove(two)
            list_price.append(two)
        if three not in range(mini, maxi + 1):
            list_price.remove(three)
            list_price.append(three)
        if four not in range(mini, maxi + 1):
            list_price.remove(four)
            list_price.append(four)
        if five not in range(mini, maxi + 1):
            list_price.remove(five)
            list_price.append(five)

        for identifier in range(0, 5):
            if list_price[identifier] is one:
                price = list_price[identifier]
                name = name_value[0]
                link = link_value[0]
                image = image_value[0]
                rating = rating_one
                one = 0

            elif list_price[identifier] is two:
                price = list_price[identifier]
                name = name_value[1]
                link = link_value[1]
                image = image_value[1]
                rating = rating_two
                two = 0

            elif list_price[identifier] is three:
                price = list_price[identifier]
                name = name_value[2]
                link = link_value[2]
                image = image_value[2]
                rating = rating_three
                three = 0

            elif list_price[identifier] is four:
                price = list_price[identifier]
                name = name_value[3]
                link = link_value[3]
                image = image_value[3]
                rating = rating_four
                four = 0

            elif list_price[identifier] is five:
                price = list_price[identifier]
                name = name_value[4]
                link = link_value[4]
                image = image_value[4]
                rating = rating_five
                five = 0

            items = {
                'price': price,
                'name': name,
                'link': link,
                'image': image,
                'rating': rating
            }
            yield items
