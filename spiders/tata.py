# -*- coding: utf-8 -*-
import scrapy
import re

class TataSpider(scrapy.Spider):
    name = 'tata'
    allowed_domains = ['https://www.tatacliq.com']
    url = 'https://www.tatacliq.com/search/?searchCategory=all&text={}'
    start_urls = [url.format('nike')]

    def parse(self, response):
        value = response.css('span.priceFormat > span::text').extract()
        length = len(value)
        for x in range(0,length):
            reaesc = re.compile(r'₹')
            value[x] = int(float(reaesc.sub('', value[x])))
        name_value = response.css('h2.product-name > a::text').extract()
        link_value = response.css('h2.product-name > a::attr(href)').extract()
        image_value = response.css('div.image > a > img::attr(data-original)').extract()
        rating_value = 'N/A'

        one = value[1]
        two = value[3]
        three = value[5]
        four = value[7]
        five = value[9]

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
                rating = rating_value
                one = 0

            elif list_price[identifier] is two:
                price = list_price[identifier]
                name = name_value[1]
                link = link_value[1]
                image = image_value[1]
                rating = rating_value
                two = 0

            elif list_price[identifier] is three:
                price = list_price[identifier]
                name = name_value[2]
                link = link_value[2]
                image = image_value[2]
                rating = rating_value
                three = 0

            elif list_price[identifier] is four:
                price = list_price[identifier]
                name = name_value[3]
                link = link_value[3]
                image = image_value[3]
                rating = rating_value
                four = 0

            elif list_price[identifier] is five:
                price = list_price[identifier]
                name = name_value[4]
                link = link_value[4]
                image = image_value[4]
                rating = rating_value

            items = {
                'price': price,
                'name': name,
                'link': link,
                'image': image,
                'rating': rating
            }
            yield items