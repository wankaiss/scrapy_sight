from pyArango.connection import *
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def make_data_to_arango():
    conn = Connection(arangoURL="http://127.0.0.1:8529", username="username",
                      password="password")
    db = conn["ybbapp"]
    col = db.collections['geo_mapping']
    with open('added0823.txt', 'r') as f:
        for line in f.readlines():
            try:
                doc = col.createDocument()
                split = line.split(':')
                doc['key'] = split[0]
                doc['value'] = split[1].replace('\n', '')
                doc.save()
            except IndexError as e:
                print e
                continue
        f.close


def find_attract():
    conn = Connection(arangoURL="http://127.0.0.1:8529", username="username",
                      password="password")
    db = conn["ybbapp"]
    col = db.collections['scrapy_data']
    for result in col.fetchAll():
        if result['result']['type'] == 'attraction':
            print result['result']['city']

if __name__ == '__main__':
    make_data_to_arango()
