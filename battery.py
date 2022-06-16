import json


def read_file() -> dict:
    clean_lines = []
    result = []
    battery_dict = {}
    with open('battery.txt') as f:
        lines = f.readlines()
        for line in lines:
            clear_string = line.strip('').strip(' ').strip('\n').strip('').split(',')
            clean_lines.append(clear_string)
        f.close()
        for i in range(len(clean_lines) - 2):
            result.append(' '.join(clean_lines[i][0].split()).split(':', 1))
        for j in result:
            if len(j) < 2:
                j.append('')
        new_dictionary = False
        for k, v in result:
            if new_dictionary:
                if len(v) != 0:
                    battery_dict[current_key][k] = v
            if len(v) == 0:
                battery_dict[k] = {}
                current_key = k
                new_dictionary = True
            if not new_dictionary:
                battery_dict[k] = v
        return battery_dict


def export_to_json_file(file: dict) -> None:
    with open("test1.json", "w") as f:
        json.dump(file, f, indent=4, sort_keys=False)
        f.close()


print(read_file())
# export_to_json_file(read_file())
