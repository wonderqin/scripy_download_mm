import urllib.request
import os


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    return html

def get_page(url):
    html = url_open(url).decode('gbk')

    a = html.find('thisclass')+11
    b = html.find('<',a)
    img_page = int(html[a:b])
    return img_page


def find_imgs(url):
    html = url_open(url).decode('gbk')
    img_addrs = []

    a = html.find('img src="')

    while a != -1:
        b = html.find('.jpg', a,a+255)
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a +9

        a = html.find('img src="',b)
    print(img_addrs)
    return img_addrs


def save_imgs(img_addrs):

    for each in img_addrs:
        name = each.split('/')
        filename = str(name[-3]+name[-2]+name[-1])
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)

def download_mm(folder = 'OOXX',pages = 5):

    os.mkdir(folder)
    os.chdir(folder)

    url = "http://www.meizitu.com/"
    page_num = get_page(url)

    while page_num <= page_num+pages:
        page_num+=1
        print(page_num)
        # jandan.net / ooxx / page - 48  # comments
        # http: // www.meizitu.com / a / more_2.html
        page_url = url + "a/" + "more_" + str(page_num) + ".html"
        img_addrs = find_imgs(page_url)
        save_imgs(img_addrs)

if __name__ == '__main__':
    download_mm()