import time

import requests
from lxml import etree
import json

if __name__ == '__main__':
    start_time=time.time()
    pages = list(range(1, 205))
    str_list = []
    comments_result=[]
    for page in pages:
        url = 'https://mobile.ximalaya.com/album-comment-mobile/web/album/comment/list/query/1715270351851?albumId=11549955&order=content-score-desc&pageId=' + str(
            page) + '&pageSize=10'
        head = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        }
        # url = url + '&page=' + str(page)
        json_body = requests.get(url=url, headers=head).text
        str_body = json.loads(json_body)
        comments = str_body['data']['comments']['list'][0]['content']
        comments_result.append(comments)
    print(f'共{len(comments_result)}个评论:\n')
    with open('ximalaya.txt', 'w', encoding='utf') as stream:
        for comment in comments_result:
            stream.write('{}\n'.format(comment))
    end_time = time.time()
    cost = end_time - start_time
    print(f'!done{cost}秒')