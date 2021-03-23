from flask import Flask, request
from collections import defaultdict
from functools import reduce
from collections import OrderedDict
from datetime import datetime, timedelta

app = Flask(__name__)


def convert_time(time_value) -> str:
    """
    Converting second time stamp to 12 hr format with AM and PM value
    :param time_value:
    :return:
    """
    return datetime.strptime(str(timedelta(seconds=time_value)), "%H:%M:%S").strftime("%I:%M:%S %p")


def list_to_dict_presentation(r, d) -> None:
    """
    Convert list of dictionaries to ordered dictionary to match key value pair
    :param r:
    :param d:
    :return:
    """
    for k in d:
        r[k].append(d[k])


def display_formatting(display_json) -> dict:
    """
    Resultant display dict to the payload dict
    :param display_json:
    :return:
    """
    return reduce(lambda r, d: list_to_dict_presentation(r, d) or r, display_json, defaultdict(list))


def restaurant_timing_update(i, key, value, result_list) -> None:
    """
    This function updates the opening and closing time of the restaurant in 12-hr time format.
    :param i:index
    :param key:days
    :param value:opening and closing time list
    :param result_list:result list
    :return:
    """
    restaurant_timing_dict = {}
    dict_data = value[i]
    if dict_data['type'] == 'open':
        time_open_12hr = convert_time(dict_data['value'])
        restaurant_timing_dict[key] = 'Open' + ' ' + str(time_open_12hr)
        result_list.append(restaurant_timing_dict)

    elif dict_data['type'] == 'close':
        time_open_12hr = convert_time(dict_data['value'])
        restaurant_timing_dict[key] = 'Closed' + ' ' + str(time_open_12hr)
        result_list.append(restaurant_timing_dict)


@app.route('/open-time-stamp-conversion/', methods=['POST'])
def routing_function():
    """
    Routing function taking the payload dict and returning the human readable time formatting response
    Only allowed methods are POST with the payload JSON or DICT
    Other service such as GET, PATCH, PUT and DELETE are not allowed method and hence will return 405 response
    method not allowed for the service.
    :return: Readable time formatting on daily basis for the restaurant (dict as datatype)
    """
    jsonFile = request.json
    result_list = []
    for key, value in OrderedDict(jsonFile).items():
        result_dictionary = {}
        if not len(value):
            result_dictionary[key] = 'Closed'
            result_list.append(result_dictionary)
        else:
            for i in range(len(value)):
                restaurant_timing_update(i, key, value, result_list)
    return display_formatting(result_list)


if __name__ == '__main__':
    """
    Running flask application route
    """
    app.run()
