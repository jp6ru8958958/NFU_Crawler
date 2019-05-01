import requests
url = "https://e3.nfu.edu.tw/EasyE3P/LMS2/login.aspx"
Account = ""
Password = ""
Checkcode = ""
post_data = {
    '__EVENTTARGET': ' ',
    '__EVENTARGUMENT': ' ',
    '__VIEWSTATE': '/wEPDwUKLTQ1NDgzNDU1Ng9kFgICAw9kFgoCEw8PZBYCHglvbmtleWRvd24FWGlmICggZXZlbnQua2V5Q29kZT09MTMgKSB7IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdidG5Mb2dpbicpLmNsaWNrKCk7IHJldHVybiBmYWxzZTsgfSBkAhUPD2QWAh8ABVhpZiAoIGV2ZW50LmtleUNvZGU9PTEzICkgeyBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnYnRuTG9naW4nKS5jbGljaygpOyByZXR1cm4gZmFsc2U7IH0gZAIpDxYCHgZoZWlnaHQFBTcwMHB4ZAIrDw8WAh4HVmlzaWJsZWhkZAIvDxYEHgNzcmMFHmxvZ2luX25ld3MuYXNweD9MYW5ndWFnZT16aC1UVx8CaGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgcFDGJ0bkxvZ2luTmV3cwUQYnRuTG9naW5DYWxlbmRhcgUMYnRuTG9naW5MaW5rBQ1idG5Mb2dpbkludHJvBQ9idG5Mb2dpblNlcnZpY2UFD2J0bkxvZ2luQ29udGFjdAUIYnRuTG9naW4rMLarmvOmgDW5L399V4ifSdd2UQ==',
    '__VIEWSTATEGENERATOR': '45F5C14E',
    'txtLoginId': Account,
    'txtLoginPwd': Password,
    'txtCheck': Checkcode,
    'btnLogin.x': '0',
    'btnLogin.y': '0'
}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Content-Length': '692',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '_ga=GA1.3.940435730.1553797049; hibext_instdsigdipv2=1; ASP.NET_SessionId=qpkfwh45j1jibt453bhkmjj4',
    'Host': 'e3.nfu.edu.tw',
    'Referer': 'https://e3.nfu.edu.tw/EasyE3P/LMS2/login.aspx',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'
}

rs = requests.post(url, data=post_data,headers=headers)
print(rs.text)