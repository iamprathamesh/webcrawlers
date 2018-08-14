# -*- coding: utf-8 -*-
import scrapy


class ShpocluesSpider(scrapy.Spider):
    name = 'shpoclues'
    allowed_domains = ['https://www.shopclues.com']
    url = 'http://www.shopclues.com/search?q={}'
    start_urls = [url.format('nike')]

    def parse(self, response):
        value = response.css('div.ori_price > span.p_price::text').extract()
        name_value = response.css('div.column > a > h2::text').extract()
        link_value = response.css('div.column > a::attr(href)').extract()
        image_value = response.css('div.img_section > img::attr(src)').extract()
        rating_value = 'N/A'

        one = int(float(value[0].replace("Rs.", "")))
        two = int(float(value[1].replace("Rs.", "")))
        three = int(float(value[2].replace("Rs.", "")))
        four = int(float(value[3].replace("Rs.", "")))
        five = int(float(value[4].replace("Rs.", "")))

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
                five = 0

            items = {
                'price': price,
                'name': name,
                'link': link,
                'image': image,
                'rating': rating
            }
            yield items
