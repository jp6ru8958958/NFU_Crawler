import requests
import json
import shutil
from PIL import Image
import urllib3


class Crawler():
    def __init__(self):
        urllib3.disable_warnings()
        self.url = 'https://e3.nfu.edu.tw/EasyE3P/LMS2/login.aspx'
        self.rs = requests.Session()

    def Get_Verify_Code(self):
        self.Verify_png = self.rs.get('http://e3.nfu.edu.tw/EasyE3P/LMS2/Public/ValidateCode.aspx', stream=True, verify=False)
        self.Png_file = open('verify.png', 'wb')
        shutil.copyfileobj(self.Verify_png.raw, self.Png_file)
        self.Png_file.close()
        self.image = Image.open('verify.png')
        self.image.show()

    def Get_Account_Info(self):
        with open('../../Account.json', 'r') as json_data:
            data = json.loads(json_data.read())
#            print(data['NFU']['Account_name'])
#            print(data['NFU']['Password'])
            self.Account_Name = data['NFU']['Account_name']
            self.Account_Password = data['NFU']['Password']

    def crawler(self):
        self.Web_html = self.rs.post(self.url, data=self.Post_data, headers=self.Headers, verify=False)
        print(self.Web_html.text)

    def Post_and_Header_data(self):
        self.Checkcode = str(input("輸入驗證碼"))
        self.Post_data = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': '/wEPDwUKLTQ1NDgzNDU1Ng9kFgICAw9kFgQCEw8PZBYCHglvbmtleWRvd24FWGlmICggZXZlbnQua2V5Q29kZT09MTMgKSB7IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdidG5Mb2dpbicpLmNsaWNrKCk7IHJldHVybiBmYWxzZTsgfSBkAhUPD2QWAh8ABVhpZiAoIGV2ZW50LmtleUNvZGU9PTEzICkgeyBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnYnRuTG9naW4nKS5jbGljaygpOyByZXR1cm4gZmFsc2U7IH0gZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBwUMYnRuTG9naW5OZXdzBRBidG5Mb2dpbkNhbGVuZGFyBQxidG5Mb2dpbkxpbmsFDWJ0bkxvZ2luSW50cm8FD2J0bkxvZ2luU2VydmljZQUPYnRuTG9naW5Db250YWN0BQhidG5Mb2dpbozEcGbl1zipEJsZcMwd/feNxaY+',
            '__VIEWSTATEGENERATOR': '45F5C14E',
            'txtLoginId': self.Account_Name,
            'txtLoginPwd': self.Account_Password,
            'txtCheck': self.Checkcode,
            'btnLogin.x': '0',
            'btnLogin.y': '0'
        }
        self.Headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '674',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '_ga=GA1.3.1290244348.1551788372; ASP.NET_SessionId=dcevlc55xczm4a453b0iln45',
            'Host': 'e3.nfu.edu.tw',
            'Origin': 'https://e3.nfu.edu.tw',
            'Referer': 'https://e3.nfu.edu.tw/EasyE3P/LMS2/login.aspx',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }


if __name__ == "__main__":
    main = Crawler()
    main.Get_Account_Info()
    main.Get_Verify_Code()
    main.Post_and_Header_data()
    main.crawler()
