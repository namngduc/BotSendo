from rasa_core_sdk import Action
from bs4 import BeautifulSoup
import requests
import json
import time
import re

class ActionGetNewst(Action):

    def name(self):
        return 'action_get_news'

    def run(self, dispatcher, tracker, domain):
        category = tracker.get_slot('category')
        print(category)
        if category == None:
            dispatcher.utter_message('Giá trị None chứng tỏ sản phẩm bạn đang tìm kiếm không có trong danh mục của chúng tôi 😢❗ Xin vui lòng điền lại!!!')
        else:
            url = 'https://mapi.sendo.vn/mob/product/search?p=1&q={category}.json'.format(category=category.split())
            response = requests.get(url).text
            data = []
            n = 0
            while n < 3:
                n += 1
                json_data = json.loads(response)['data'][n]
                data.append(json_data)
            for results in range(len(data)):
                message = f'''
{str(results + 1)}.ID của sản phẩm: {data[results]['product_id']}
Tên sản phẩm: {data[results]['name']}
Url sản phẩm: sendo.vn/{data[results]['cat_path']}
Giá bán sản phẩm: {data[results]['price']}đ
Giá bán sau khuyến mãi: {data[results]['final_price']}đ
                            '''
                dispatcher.utter_message(message)
        return[]
class ActionGetNum(Action):

    def name(self):
        return 'action_get_num'

    def run(self, dispatcher, tracker, domain):
        number = tracker.get_slot('number')
        print(number)
        category = tracker.get_slot('category')
        print(category)
        if category == None and number == None:
            dispatcher.utter_message('Giá trị None chứng tỏ sản phẩm bạn đang tìm kiếm không có trong danh mục của chúng tôi 😢❗ Xin vui lòng điền lại!!!')
        elif number == None:
            dispatcher.utter_message('Vui lòng điền số lượng sản phẩm bạn muốn tìm ❗')
        else:
            url = 'https://mapi.sendo.vn/mob/product/search?p=1&q={category}.json'.format(category=category.split())
            response = requests.get(url).text
            data = []
            n = 0
            if int(number) > len(json.loads(response)['data']):
                dispatcher.utter_message('Xin lỗi số lượng sản phẩm quá lớn, số lượng tối đa có thể tìm kiếm là 34. Xin vui lòng điền lại!!!')
            else:
                while n < int(number):
                    n += 1
                    json_data = json.loads(response)['data'][n]
                    data.append(json_data)
                for results in range(len(data)):
                    message = f'''
{str(results + 1)}.ID của sản phẩm: {data[results]['product_id']}
Tên sản phẩm: {data[results]['name']}
Url sản phẩm: sendo.vn/{data[results]['cat_path']}
Giá bán sản phẩm: {data[results]['price']}đ
Giá bán sau khuyến mãi: {data[results]['final_price']}đ
                            '''
                    dispatcher.utter_message(message)
        return[]

class ActionGetid(Action):
    def name(self):
        return 'action_get_id'

    def run(self, dispatcher, tracker, domain):
        productid = tracker.get_slot('productid')
        print(productid )
        url = 'https://mapi.sendo.vn/mob/product/{productid}/detail/'.format(productid=productid)
        response = requests.get(url).text
        json_data = json.loads(response)
        if json_data == [] or productid == None:
            dispatcher.utter_message('Xin lỗi Id của bạn không hợp lệ hoặc sản phẩm không tồn tại. Id sản phẩm là một chuỗi bao gồm 8 chữ số ')
        else:
            if json_data['stock_status'] == 1:
                sale = 'Còn hàng'
            else:
                sale = 'Hết hàng'
            soup = BeautifulSoup(json_data['description'], 'html.parser')
            des = []
            for x in soup.find_all('p'): des.append(x.string)
            res = []
            for val in des:
                if val != None:
                    res.append(val)
            if soup.find('a') != None:
                try:
                    string_length = len(soup.find('a')['href']) + 2
                    string_revised = soup.find('a')['href'].center(string_length)
                    res.insert(1, string_revised)
                except KeyError:
                    pass
            else:
                pass
            review = ''.join(map(str, res))
            review = re.sub('[\xa0]', ' ', review)
            message = f'''
Tên sản phẩm: {json_data['name']}
Giá bán sản phẩm: {json_data['price']}đ
ID của shop: {json_data['admin_id']}
Giá khuyến mãi: {json_data['special_price']}
Url của sản phẩm: sendo.vn/{json_data['cat_path']}
Mô tả chi tiết sản phẩm: {review}
Tổng số lượt yêu thích sản phẩm: {json_data['counter_like']}
Trạng thái còn hàng: {sale}
Thông tin chủ shop: Tên Shop- {json_data['shop_info']['shop_name']}, Số điện thoại- {json_data['shop_info']['phone_number']}
                    '''
            dispatcher.utter_message(message)
        return[]


time.sleep(1)