# coding: utf-8

import re

text = '菌香饭                                ,' + \
       '石斑鱼汤锅                                ,'

# result = re.sub(r'<[^>]+>', '', text).strip()

print re.sub(r'[\s]+', '', text)
