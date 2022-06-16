import json
import os


def get_battery_properties() -> None:
    os.system('upower -i /org/freedesktop/UPower/devices/battery_BAT0 > battery.txt')


def read_file() -> dict:
    clean_lines: list = []
    result: list = []
    battery_dict: dict = {}
    with open('battery.txt') as f:
        lines: list[str] = f.readlines()
        for line in lines:
            clear_string = line.lstrip().strip('\n').strip(' ').split(',')
            clean_lines.append(clear_string)
        f.close()
        for i in range(len(clean_lines) - 2):
            result.append(' '.join(clean_lines[i][0].split()).split(':', 1))
        for element in result:
            if len(element) < 2:
                element.append('')
        new_dictionary = False
        for key, value in result:
            if new_dictionary:
                if len(value) != 0:
                    battery_dict[current_key][key] = value
            if len(value) == 0:
                battery_dict[key] = {}
                current_key = key
                new_dictionary = True
            if not new_dictionary:
                battery_dict[key] = value
        return battery_dict


def export_to_json_file(file: dict) -> None:
    with open("battery.json", "w") as f:
        json.dump(file, f, indent=4, sort_keys=False)
        f.close()


get_battery_properties()
export_to_json_file(read_file())
# read_file()
# export_to_json_file(read_file())
