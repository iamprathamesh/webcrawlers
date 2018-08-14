# -*- coding: utf-8 -*-
import scrapy


class PaytmmallSpider(scrapy.Spider):
    name = 'paytmmall'
    allowed_domains = ['https://paytmmall.com']
    url = 'https://paytmmall.com/shop/search?q={}'
    start_urls = [url.format('reebok')]

    def parse(self, response):
        value = response.css('span._1kMS > span::text').extract()
        name_value = response.css('div._2apC::text').extract()
        link_value = response.css('div._2i1r > a::attr(href)').extract()
        image_value = response.css('div._3nWP > img::attr(src)').extract()
#        rating_list = response.css('span.c-ax::text').extract()

        one = int(float(value[0]))
        two = int(float(value[1]))
        three = int(float(value[2]))
        four = int(float(value[3]))
        five = int(float(value[4]))

        rating_one = 'N/A'
        rating_two = 'N/A'
        rating_three  = 'N/A'
        rating_four = 'N/A'
        rating_five = 'N/A'

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