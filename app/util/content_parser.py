import requests
import os
import uuid

from bs4 import BeautifulSoup

img_src = ['src', 'data-src', '_src', 'data-original-src']
not_new_line = ['a', 'span', 'strong', 'b']

# server_path = 'http://10.0.3.96/'
server_path = 'http://127.0.0.1/'
local_path = 'E:/images/'


def parser(content_html, headers):
    content_soup = BeautifulSoup(content_html, 'html.parser')
    content = ''

    for node in content_soup.descendants:
        if node.name is None:
            if str(node).strip() == '':
                continue
            else:
                # 去除 不换行标签前后的换行
                if node.parent.name in not_new_line and not(node.parent.previous_sibling is None):
                    content = content[:-1]
                    content += node
                else:
                    content += node
                    content += '\n'

        elif node.name == 'img':
            src = list(set(img_src) & set(node.attrs))[0]
            img_url = node[src]
            if 'http' not in img_url:
                img_url = 'http:' + img_url

            r = requests.get(img_url, headers=headers)
            img_name = str(uuid.uuid4()) + '.jpg'
            try:
                if not os.path.exists(local_path):
                    os.mkdir(local_path)
                with open(local_path + img_name, 'wb') as f:
                    f.write(r.content)
                    f.flush()
                    f.close()
                content += server_path + img_name
                content += '\n'
            except:
                content += '>>>图片下载失败'
                content += '\n'

    return content[:-1]
