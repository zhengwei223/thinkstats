import json
import os
import re
import time
import requests


class Spider:
    def __init__(self):
        self.session = requests.Session()

    def run(self, start_url):
        img_base_ids = self.get_img_base_ids(start_url)
        # print(img_base_ids)
        for _id in img_base_ids:
            img_info = self.get_img_assembly_info(_id)
            # print(img_info)
            # break
            self.save(img_info)

    # 列表页的集合
    def get_img_base_ids(self, start_url):
        '获得第一级地址列表'
        response = self.download(start_url)
        if response:
            html = response.text
            ids = re.findall(r'http://tu.duowan.com/gallery/(\d+).html', html)
            return set(ids)

    # 获取url对应的response
    def download(self, url):
        response = self.session.get(url)
        # print(response.text)
        try:
            return response
        except Exception as e:
            print(e)

    # 根据套图id获得图片组的信息，一般来自json
    def get_img_assembly_info(self, _id):
        '返回json准换后的字典'
        url = 'http://tu.duowan.com/index.php?r=show/getByGallery/&gid={0}&_={1}'.format(_id, int(time.time() * 1000))
        response = self.download(url)
        if response:
            return json.loads(response.text)

    # 保存图片
    def save(self, img_info):
        title_ = strip_file_path(img_info['gallery_title'].strip())
        # 新建文件夹
        if not os.path.exists(title_):
            os.mkdir(title_)
        # 遍历每张图
        for picInfo in img_info['picInfo']:
            img_name = strip_file_path(picInfo['title'].strip())  # 图片名称
            img_url = picInfo['url']  # 图片地址
            # 后缀
            pix = img_url.split('.')[-1]
            # 拼接路径
            img_path = os.path.join(title_, '%s.%s' % (img_name, pix))
            if not os.path.exists(img_path):
                response = self.download(img_url)
                if response:
                    # 下载图片内容
                    img_data = response.content
                    with open(img_path, 'wb') as file:
                        # 保存至文件
                        file.write(img_data)


def strip_file_path(path):
    path = re.sub(r'[？.\\*|"<>/]', '', str(path))
    return path


if __name__ == '__main__':
    spider = Spider()
    # spider.download('http://tu.duowan.com/m/meinv')
    start_url = 'http://tu.duowan.com/m/meinv'
    spider.run(start_url)
