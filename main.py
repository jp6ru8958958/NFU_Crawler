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
        self.Verify_Header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_ga=GA1.3.940435730.1553797049; ASP.NET_SessionId=eigfhe45ooq2hd45tb4uio45; .ASPXAUTH_EasyE3P_127.0.0.1=3F376B9C3803A52369118FE98CF28B1BECC0BCD56C0C583409CD5C8539D2833D11B619AF9CF4C792B29D6A9B5B41CBD9C1145540DC7291EA6F950CBCDA4C70A15D4585A64386465B17CAFE27E107A5C1B9AD7C630E3FBBF382AEB7F692901804E22C63F34E01D9F0B11D931FF5796F7D06E20A251AC0E48887D3489821205F23094411B7',
            'Host': 'e3.nfu.edu.tw',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'
        }
        self.Verify_url = 'http://e3.nfu.edu.tw/EasyE3P/LMS2/Public/ValidateCode.aspx'
        self.Verify_png = self.rs.get(self.Verify_url, stream=True, verify=False, headers=self.Verify_Header)
        self.Png_file = open('verify.png', 'wb')
        shutil.copyfileobj(self.Verify_png.raw, self.Png_file)
        self.Png_file.close()
        self.image = Image.open('verify.png')
        self.image.show()
        code_input = input("輸入驗證碼")
        return str(code_input)

    def Get_Account_Info(self):
        with open('../../Account.json', 'r') as json_data:
            data = json.loads(json_data.read())
#            print(data['NFU']['Account_name'])
#            print(data['NFU']['Password'])
            self.Account_Name = data['NFU']['Account_name']
            self.Account_Password = data['NFU']['Password']

    def crawler(self):
        self.Web_html = self.rs.post(url=self.url, headers=self.Headers, data=self.Post_data, verify=False)
        print(self.Web_html.text)

    def Header_data(self):
        self.Headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '1000',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '_ga=GA1.3.940435730.1553797049; ASP.NET_SessionId=eigfhe45ooq2hd45tb4uio45; .ASPXAUTH_EasyE3P_127.0.0.1=3F376B9C3803A52369118FE98CF28B1BECC0BCD56C0C583409CD5C8539D2833D11B619AF9CF4C792B29D6A9B5B41CBD9C1145540DC7291EA6F950CBCDA4C70A15D4585A64386465B17CAFE27E107A5C1B9AD7C630E3FBBF382AEB7F692901804E22C63F34E01D9F0B11D931FF5796F7D06E20A251AC0E48887D3489821205F23094411B7',
            'Host': 'e3.nfu.edu.tw',
            'Origin': 'https://e3.nfu.edu.tw',
            'Referer': 'https://e3.nfu.edu.tw/EasyE3P/LMS2/login.aspx',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

    def Post_data(self, code):
        self.Post_data = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': '/wEPDwUKLTQ1NDgzNDU1Ng9kFgICAw9kFgQCEw8PZBYCHglvbmtleWRvd24FWGlmICggZXZlbnQua2V5Q29kZT09MTMgKSB7IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdidG5Mb2dpbicpLmNsaWNrKCk7IHJldHVybiBmYWxzZTsgfSBkAhUPD2QWAh8ABVhpZiAoIGV2ZW50LmtleUNvZGU9PTEzICkgeyBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnYnRuTG9naW4nKS5jbGljaygpOyByZXR1cm4gZmFsc2U7IH0gZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBwUMYnRuTG9naW5OZXdzBRBidG5Mb2dpbkNhbGVuZGFyBQxidG5Mb2dpbkxpbmsFDWJ0bkxvZ2luSW50cm8FD2J0bkxvZ2luU2VydmljZQUPYnRuTG9naW5Db250YWN0BQhidG5Mb2dpbozEcGbl1zipEJsZcMwd/feNxaY+',
            '__VIEWSTATEGENERATOR': '45F5C14E',
            'txtLoginId': '',
            'txtLoginPwd': '',
            'txtCheck': '',
            'btnLogin.x': '1',
            'btnLogin.y': '1'
        }
        self.Post_data['txtLoginId'] = str(self.Account_Name)
        self.Post_data['txtLoginPwd'] = str(self.Account_Password)
        self.Post_data['txtCheck'] = code


if __name__ == "__main__":
    main = Crawler()
    main.Get_Account_Info()
    main.Header_data()
    code = main.Get_Verify_Code()
    main.Post_data(code)
    main.crawler()

