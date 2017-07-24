# -*- coding: utf-8 -*-
import inspect
import os
import urllib
import uuid
import re
import linecache
import platform

from PIL import Image


def random_string(n):
    return (''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(n))))[0:16]


def jpg_test(img_url=None):
    try:
        if img_url is None:
            script_dir = inspect.getfile(inspect.currentframe())
            print 'img_url is None at line 21 ' + 'in ' + script_dir
            return None
            # img_url = 'http://img10.cn.gcimg.net/gcproduct/day_20141101/6af7012efba587f84c8cbda1f63b3e41.jpg'
        result = img_url.split(r'.')
        result = result[len(result) - 1]
        # print 'result: %s, type: %s, jpg type: %s' % (result, type(result), type('jpg'))
        if result == 'jpg':
            print 'in picture_utils at line 28 in if condition'
            return img_url
        else:
            print 'in picture_utils at line 30 in else condition'
            return None
    except Exception as e:
        print 'img_url is None: ' + str(e) + 'at line 31 in ' + script_dir


def save_img(img_url=None, file_path=None, id_num=9000000001L):
    """
    :param id_num: 
    :description 
            根据url将图片保存到本地
    :param img_url: 图片url
    :param file_name: 文件名
    :param file_path: 文件保存本地路径
    :return: 
    """
    # img_url = 'http://s14.sinaimg.cn/mw690/003v9wUkgy6T2CmMOoBdd.jpg'
    if file_path is None:
        system = platform.system()
        if system == "Windows":
            file_path = 'D:\\landmark\\' + str(id_num) + '\\'
            print ("windows path")
        elif system == "Linux":
            file_path = '/opt/download/landmark/' + id_num + '/'
            print ("linux path")
        else:
            file_path = '/opt/download/landmark/' + id_num + '/'
    file_path = file_path.decode('utf-8')
    file_name = uuid.uuid1()
    # 保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 book\img文件夹
    try:
        if not os.path.exists(file_path):
            print 'file', file_path, ' not exist, creating'
            # os.mkdir(file_path)
            os.makedirs(file_path)
        # 获得图片后缀
        file_suffix = os.path.splitext(img_url)[1]
        # 拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
        # 下载图片，并保存到文件夹中
        urllib.urlretrieve(img_url, filename=filename)
        saved_img = file_path + str(file_name) + file_suffix
        script_dir = inspect.getfile(inspect.currentframe())
        print 'start resize picture from save_img at line 69' + ' in ' + script_dir
        img_resize(img_url=saved_img)
    except IOError as e:
        print 'file operated failed', e
    except Exception as e:
        print 'Exception：', e


def img_resize(img_url=None):
    """
    :description: 对图片进行比例缩放
    :param img_url: 
    :return: 
    """
    try:
        if img_url is None:
            script_dir = inspect.getfile(inspect.currentframe())
        original_image = Image.open(img_url)
        original_size = original_image.size
        print original_size
        new_width = 299
        new_height = new_width * (int(original_size[1]) / int(original_size[0]))
        new_image = original_image.resize((new_width, new_height), Image.ANTIALIAS)
        print new_image
        new_image.save(img_url)
    except Exception as e:
        print 'img_resize exception: ' + str(e) + 'at ' + script_dir


if __name__ == '__main__':
    jpg_test(img_url='http://image.tupian114.com/20140430/15025135.jpg')
