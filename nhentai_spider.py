#coding: utf-8
import urllib.request
import os
import re

def open_url(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    page=urllib.request.urlopen(req)
    html=page.read().decode('utf-8')
    return html

def get_img(url):
    html=open_url(url)
    p=r'<img src="(https://i.nhentai.net/galleries/[^"]+\.jpg)"'
    img=re.findall(p,html)
    for i in img:
        filename=i.split("/")[-1]
        urllib.request.urlretrieve(i,filename,None)

def get_pages(url):
    p=r'<div>(\d+) pages</div>'
    html=open_url(url)
    pages=re.findall(p,html)
    return pages[0]

def get_title(url):
    p=r'<h2>(.+)</h2>'
    html=open_url(url)
    title=re.findall(p,html)
    return title[0]

def download_nhentai():
    book_num=input('请输入本子的数字代码:')
    while not book_num.isdigit():
        book_num=input('请输入正确的本子代码:')
    url='https://nhentai.net/g/'+book_num+'/'
    print('本子的标题是%s吗?',get_title(url))
    t=input('是的话请输入1,不是请输入0')
    while t=='0':
        book_num=input('请输入正确的本子代码:')
        url='https://nhentai.net/g/'+book_num+'/'
        print('本子的标题是%s吗?',get_title(url))
        t=input('是的话请输入1,不是请输入0')
    title=get_title(url).replace('/','').replace('\\','').replace(':','').replace('*','').replace('?','').replace('"','').replace('<','').replace('>','')
    pages=int(get_pages(url))
    print(pages)
    os.mkdir(title)
    os.chdir(title)
    for i in range(1,pages+1):
        print(i)
        page_url=url+str(i)
        print(page_url)
        get_img(page_url)
    

if __name__=='__main__':
    '''
    url='https://nhentai.net/g/209599/'
    get_img(open_url(url))
    get_pages(url)
    get_title(url)
    download_nhentai()
    title='(C92) [Yan-Yam] 堕聖女飼育 (Fate/Grand Order) [中国翻訳]'.encode('GBK')
    os.mkdir(title)
    '''
    download_nhentai()
