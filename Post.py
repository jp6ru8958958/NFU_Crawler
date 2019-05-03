import requests
url = "https://e3.nfu.edu.tw/EasyE3P/LMS2/login.aspx"
Account = ''
Password = ''
Checkcode = ''
post_data = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': '/wEPDwUKLTQ1NDgzNDU1Ng9kFgICAw9kFgQCEw8PZBYCHglvbmtleWRvd24FWGlmICggZXZlbnQua2V5Q29kZT09MTMgKSB7IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdidG5Mb2dpbicpLmNsaWNrKCk7IHJldHVybiBmYWxzZTsgfSBkAhUPD2QWAh8ABVhpZiAoIGV2ZW50LmtleUNvZGU9PTEzICkgeyBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnYnRuTG9naW4nKS5jbGljaygpOyByZXR1cm4gZmFsc2U7IH0gZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBwUMYnRuTG9naW5OZXdzBRBidG5Mb2dpbkNhbGVuZGFyBQxidG5Mb2dpbkxpbmsFDWJ0bkxvZ2luSW50cm8FD2J0bkxvZ2luU2VydmljZQUPYnRuTG9naW5Db250YWN0BQhidG5Mb2dpbozEcGbl1zipEJsZcMwd/feNxaY+',
    '__VIEWSTATEGENERATOR': '45F5C14E',
    'txtLoginId': Account,
    'txtLoginPwd': Password,
    'txtCheck': Checkcode,
    'btnLogin.x': '0',
    'btnLogin.y': '0'
}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '1000',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '_ga=GA1.3.1290244348.1551788372; ASP.NET_SessionId=dcevlc55xczm4a453b0iln45',
    'Host': 'e3.nfu.edu.tw',
    'Origin': 'https://e3.nfu.edu.tw',
    'Referer': 'https://e3.nfu.edu.tw/EasyE3P/LMS2/login.aspx',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

rs = requests.post(url, data = post_data, headers = headers)
print(rs.text)
