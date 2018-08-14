# -*- coding: utf-8 -*-
import scrapy
import re


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.py']
    url = 'https://www.amazon.in/s/field-keywords={}'
    start_urls = [url.format('Nike Mens Zoom Winflo Grey;Red Running Shoes')]

    def parse(self, response):
        value = response.css('span.s-price::text').extract()
        name_value = response.css('h2.s-access-title::text').extract()
        link_value = response.css('a.s-access-detail-page::attr(href)').extract()
        image_value = response.css('img.s-access-image.cfMarker::attr(src)').extract()
        rating_value = response.css('i.a-icon-star > span.a-icon-alt::text').extract()

        count = 0
        if "-" not in value[count]:
            one = int(float(value[count].replace(",", "").replace(" ", "").replace("-", "")))
            count += 1
        else:
            one = int(float(value[count].replace(",", "").replace(" ", "").replace("-", "")))
            count += 2
        if "-" not in value[count]:
            two = int(float(value[count].replace(",", "").replace(" ", "").replace("-", "")))
            count += 1
        else:
            two = int(float(value[count].replace(",", "").replace(" ", "").replace("-", "")))
            count += 2
        if "-" not in value[count]:
            three = int(float(value[count].replace(",", "").replace(" ", "").replace("-", "")))
            count += 1
        else:
            three = int(float(value[count].replace(",", "").replace(" ", "").replace("-", "")))
            count += 2
        if "-" not in value[count]:
            four = int(float(value[count].replace(",", "").replace(" ", "").replace("-", "")))
            count += 1
        else:
            four = int(float(value[count].replace(",", "").replace(" ", "").replace("-", "")))
            count += 2

        five = int(float(value[count].replace(",", "").replace(" ", "").replace("-", "")))

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

        '''list_price = [one,two,three,four,five]
        list_price.sort()'''

        '''accurate_value = response.css('span.s-price::text').extract()
        newone = accurate_value[0].replace(" ","").replace("-","")
        newtwo = accurate_value[1].replace(" ", "").replace("-", "")
        newthree = accurate_value[2].replace(" ", "").replace("-", "")
        newfour = accurate_value[3].replace(" ", "").replace("-", "")
        newfive = accurate_value[4].replace(" ", "").replace("-", "")'''


        for identifier in range(0, 5):
            if list_price[identifier] is one:
                price = list_price[identifier]
                name = name_value[0]
                link = link_value[0]
                image = image_value[0]
                rating = rating_value[0]
                one = 0

            elif list_price[identifier] is two:
                price = list_price[identifier]
                name = name_value[1]
                link = link_value[1]
                image = image_value[1]
                rating = rating_value[1]
                two = 0

            elif list_price[identifier] is three:
                price = list_price[identifier]
                name = name_value[2]
                link = link_value[2]
                image = image_value[2]
                rating = rating_value[2]
                three = 0

            elif list_price[identifier] is four:
                price = list_price[identifier]
                name = name_value[3]
                link = link_value[3]
                image = image_value[3]
                rating = rating_value[3]
                four = 0

            elif list_price[identifier] is five:
                price = list_price[identifier]
                name = name_value[4]
                link = link_value[4]
                image = image_value[4]
                rating = rating_value[4]
                five = 0



                #        best_price = min(one,two,three,four,five)

            items = {
                'price': price,
                'name': name,
                'link': link,
                'image': image,
                'rating': rating
            }

            yield items

        item = 'Nike Mens Zoom Winflo Grey;Red Running Shoes'
        new_url = 'https://www.flipkart.com/search?q='+ item
        yield scrapy.Request(url=new_url,callback=self.parseflipkart,dont_filter=True)

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