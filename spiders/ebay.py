# -*- coding: utf-8 -*-
import scrapy
import re


class EbaySpider(scrapy.Spider):
    name = 'ebay'
    allowed_domains = ['https://ebay.in']
    url = 'https://www.ebay.in/sch/i.html?_from=R40&_nkw={}'
    start_urls = [url.format('case')]

    def parse(self, response):
        '''value = response.css('div._1vC4OE::text').extract()
        name_value = response.css('div._3wU53n::text').extract()
        link_value = response.css('a._1UoZlX::attr(href)').extract()
        image_value = response.css('div._3BTv9X').xpath('//img/@src').extract()
        rating_list = response.css('div.hGSR34::text').extract()

        if not link_value:
            value = response.css('div._1vC4OE::text').extract()
            name_value = response.css('a._2cLu-l::text').extract()
            link_value = response.css('a._2cLu-l::attr(href)').extract()
            image_value = response.css('div._3BTv9X').xpath('//img/@src').extract()
            rating_value = 'N/A'

            one = int(float(value[1].replace(",", "")))
            two = int(float(value[3].replace(",", "")))
            three = int(float(value[5].replace(",", "")))
            four = int(float(value[7].replace(",", "")))
            five = int(float(value[9].replace(",", "")))


        else:
            one = int(float(value[1].replace(",", "")))
            two = int(float(value[3].replace(",", "")))
            three = int(float(value[5].replace(",", "")))
            four = int(float(value[7].replace(",", "")))
            five = int(float(value[9].replace(",", "")))'''

        value = response.css('li.lvprice > span.bold::text').extract()
        length = len(value)
        for x in range(0, length):
            reaesc = re.compile(r'\n\t\t\t\t\t')
            value[x] = reaesc.sub('', value[x])
        for x in range(0, length):
            reaesc = re.compile(r'\t')
            value[x] = reaesc.sub('', value[x])
        for x in value:
            if x is "":
                value.remove(x)
        link_value = response.css('h3.lvtitle > a::attr(href)').extract()
        name_value = response.css('h3.lvtitle > a::text').extract()
        image_value = response.css('div.lvpicinner > a > img::attr(src)').extract()
        rating_value = 'N/A'

        if not link_value:
            value = response.css('span.bold::text').extract()
            length = len(value)
            for x in range(0, length):
                reaesc = re.compile(r'\n\t\t\t\t\t')
                value[x] = reaesc.sub('', value[x])
            for x in range(0, length):
                reaesc = re.compile(r'\t')
                value[x] = reaesc.sub('', value[x])
            for x in value:
                if x is "":
                    value.remove(x)
            link_value = response.css('div.gvtitle > h3 > a::attr(href)').extract()
            name_value = response.css('div.gvtitle > h3 > a::text').extract()
            image_value = response.css('div.imgWr > a > img::attr(src)').extract()

            one = int(float(value[0].replace(",", "")))
            two = int(float(value[1].replace(",", "")))
            three = int(float(value[2].replace(",", "")))
            four = int(float(value[3].replace(",", "")))
            five = int(float(value[4].replace(",", "")))

        else:

            one = int(float(value[0].replace(",", "")))
            two = int(float(value[1].replace(",", "")))
            three = int(float(value[2].replace(",", "")))
            four = int(float(value[3].replace(",", "")))
            five = int(float(value[4].replace(",", "")))

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




