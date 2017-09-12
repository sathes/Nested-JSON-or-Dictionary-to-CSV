import json
import csv

def is_dict(item, ans=[]):
    tree = []
    for k,v in item.items():
        if isinstance(v,dict):
            ans.append(str(k))
            tree.extend(is_dict(v, ans))
            ans=[]
        else:
            if ans:
                ans.append(str(k))
                key = ','.join(ans).replace(',','.')
                tree.extend([(key, str(v))])
                ans.remove(str(k))
            else:
                tree.extend([(str(k),str(v))])
    return tree

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except (ValueError,TypeError) as e:
        return False
    return True

def get_tree(item):
    tree = []
    if isinstance(item, dict):
        tree.extend(is_dict(item, ans=[]))
        return tree
    elif isinstance(item, list):
        tree = []
        for i in item:
            if is_json(i) == True:
                i = json.loads(i)
            tree.append(get_tree(i))
        return tree
    elif isinstance(item, str):
        if is_json(item) == True:
            item = json.loads(item)
            tree.extend(is_dict(item, ans=[]))
            return tree
    else:
        tree.extend([(key, item)])
    return tree

def render_csv(header, data, out_path='out3.csv'):
    input = []
    with open(out_path, 'w') as f:
        dict_writer = csv.DictWriter(f, fieldnames=header)
        dict_writer.writeheader()
        if not isinstance(data[0],list):
            input.append(dict(data))
        else:
            for i in data:
                input.append(dict(i))
        dict_writer.writerows(input)
    return

def main(obj):
    tree = get_tree(obj)
    if isinstance(obj, list):
        header = [i[0] for i in tree[0]]
    else:
        header =[i[0] for i in tree]
    return render_csv(header, tree)

if __name__ == '__main__':
    #a = {'_index': 'test_demo', '_type': 'test', '_id': 'AV3BhIYlQv4ihfkxpDQ1', '_score': 1.0,'dummy': {'date': '1-08-2013', 'cost': '300', 'custid': 'c1', 'busno': '1234', 'source': 'Chennai', 'bid': '1', 'dest': 'Coimbatore'}, '_source': {'date': '1-08-2013', 'cost': '300', 'custid': 'c1', 'busno': '1234', 'source': 'Chennai', 'bid': '1', 'dest': 'Coimbatore','next':{'date': '1-08-2013', 'cost': '300', 'custid': 'c1'}},'new':2}
    #a = '{"_index": "test_demo", "_type": "test", "_id": "AV3BhIYlQv4ihfkxpDQ1", "_score": 1.0, "dummy": {"date": "1-08-2013", "cost": "300", "custid": "c1", "busno": "1234", "source": "Chennai", "bid": "1", "dest": "Coimbatore"}, "_source": {"date": "1-08-2013", "cost": "300", "custid": "c1", "busno": "1234", "source": "Chennai", "bid": "1", "dest": "Coimbatore", "next": {"date": "1-08-2013", "cost": "300", "custid": "c1"}}, "new": 2}'
    a = [{'_index': 'test_demo', '_type': 'test', '_id': 'AV3BhIYlQv4ihfkxpDQ1', '_score': 1.0, '_source': {'date': '1-08-2013', 'cost': '300', 'custid': 'c1', 'busno': '1234', 'source': 'Chennai', 'bid': '1', 'dest': 'Coimbatore'}}, {'_index': 'test_demo', '_type': 'test', '_id': 'AV3BhI0Y9ttR5YXxNp8D', '_score': 1.0, '_source': {'date': '1-08-2013', 'cost': '300', 'custid': 'c3', 'busno': '1234', 'source': 'Chennai', 'bid': '3', 'dest': 'Coimbatore'}}, {'_index': 'test_demo', '_type': 'test', '_id': 'AV3BhH0tmWD1jFsCgtYU', '_score': 1.0, '_source': {'date': '1-08-2013', 'cost': '300', 'custid': 'c11', 'busno': '1234', 'source': 'Chennai', 'bid': '11', 'dest': 'Coimbatore'}}, {'_index': 'test_demo', '_type': 'test', '_id': 'AV3BhI0-9ttR5YXxNp8H', '_score': 1.0, '_source': {'date': '1-08-2013', 'cost': '300', 'custid': 'c15', 'busno': '1234', 'source': 'Chennai', 'bid': '15', 'dest': 'Coimbatore'}}, {'_index': 'test_demo', '_type': 'test', '_id': 'AV3BhH1DmWD1jFsCgtYX', '_score': 1.0, '_source': {'date': '1-08-2013', 'cost': '300', 'custid': 'c20', 'busno': '1234', 'source': 'Chennai', 'bid': '20', 'dest': 'Coimbatore'}}, {'_index': 'test_demo', '_type': 'test', '_id': 'AV3BhI1L9ttR5YXxNp8J', '_score': 1.0, '_source': {'date': '1-08-2013', 'cost': '300', 'custid': 'c21', 'busno': '1234', 'source': 'Chennai', 'bid': '21', 'dest': 'Coimbatore'}}, {'_index': 'test_demo', '_type': 'test', '_id': 'AV3BhIZyQv4ihfkxpDQ9', '_score': 1.0, '_source': {'date': '1-08-2013', 'cost': '200', 'custid': 'c25', 'busno': '2345', 'source': 'Chennai', 'bid': '25', 'dest': 'Coimbatore'}}, {'_index': 'test_demo', '_type': 'test', '_id': 'AV3BhH1XmWD1jFsCgtYa', '_score': 1.0, '_source': {'date': '1-08-2013', 'cost': '200', 'custid': 'c29', 'busno': '2345', 'source': 'Chennai', 'bid': '29', 'dest': 'Coimbatore'}}, {'_index': 'test_demo', '_type': 'test', '_id': 'AV3BhIZ_Qv4ihfkxpDQ_', '_score': 1.0, '_source': {'date': '1-08-2013', 'cost': '200', 'custid': 'c31', 'busno': '2345', 'source': 'Chennai', 'bid': '31', 'dest': 'Coimbatore'}}, {'_index': 'test_demo', '_type': 'test', '_id': 'AV3BhH1tmWD1jFsCgtYd', '_score': 1.0, '_source': {'date': '1-08-2013', 'cost': '200', 'custid': 'c38', 'busno': '2345', 'source': 'Chennai', 'bid': '38', 'dest': 'Coimbatore'}}]

    main(a)    