# coding=utf-8
# 根据班级json文件进行随机摇号

import random
import json

# SETTINGS
numberLimit = 57
reset = True
is_print = True
data_json_fp = "./json/class_9_id_list.json"
arrangement_event_list_fp = "./json/arrangement_event_list.json"
pass_json_fp = "./json/ramdom_pass_index_list.json"
ask_for_leave_list_fp = "./json/ask_for_leave.json"

# INIT
data = json.load(open(data_json_fp, "r", encoding="utf-8"))
arrangement_list = json.load(open(arrangement_event_list_fp, "r", encoding="utf-8"))
ask_for_leave_list = json.load(open(ask_for_leave_list_fp, "r", encoding="utf-8"))
data_keys = data.keys()
if reset:
    pass_data = []
else:
    pass_data = json.load(open(pass_json_fp, "r", encoding="utf-8"))
output = {}


def random_pick(numberLimit_2):
    return_list = []
    for i in range(0, numberLimit_2):
        random_index = random.randint(1, len(data_keys))
        if random_index in pass_data:
            return_list.append(random_pick(1)[0])
            continue
        else:
            pass_data.append(random_index)
            return_list.append(random_index)
    return return_list


def fill_in_list(start, end):
    in_list = []
    for i in range(start, end):
        name = data[str(random_list[i])]["name"]
        if i in ask_for_leave_list:
            name = "AFL: " + str(i)
        in_list.append(name)
    return in_list


random_list = random_pick(numberLimit)
start_point = 0
end_point = 0
for event_a in arrangement_list:
    if event_a["childEvents"] is not None:
        output[event_a["name"]] = {}
        for event_b in event_a["childEvents"]:
            end_point += event_b["numberLimit"]
            output[event_a["name"]][event_b["name"]] = fill_in_list(start_point, end_point)
            start_point += event_b["numberLimit"]
    else:
        end_point += event_a["numberLimit"]
        output[event_a["name"]] = fill_in_list(start_point, end_point)
        start_point += event_a["numberLimit"]

json.dump(output, open("./json/arrangement.json", "w", encoding="utf-8"))
json.dump(pass_data, open(pass_json_fp, "w", encoding="utf-8"))

if is_print:
    output_keys = output.keys()
    for key in output_keys:
        print(key)
        try:
            a = output[key]["xxxx"]
        except KeyError:
            for child_key in output[key].keys():
                print("  " + child_key)
                for name in output[key][child_key]:
                    print("    " + name)
        except TypeError:
            for name in output[key]:
                print("    " + name)
