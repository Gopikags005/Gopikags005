from machine import Pin
import ili9341
from xglcd_font import XglcdFont
import mySetup
import utime


# Initialize display
display = mySetup.createMyDisplay()
unispace = XglcdFont('Unispace12x24.c', 12, 24)

# Define menu items for UP and DOWN directions
up_menu_items = [
    "CAPE - NCJ",
    "TEN - NCJ",
    "NCJ - TVC",
    "TVC - QLN",
    "QLN - KYJ",
    "KYJ - KTYM - ERS (ERS 'D' - ERN )",
    "ERN - SRR",
    "KYJ - ALLP - ERS",
    "ERS - ERN",
    "PNQ - GUV",
    "QLN - SCT"
]

down_menu_items = [
    "QLN - TEN (NCJ - TEN)",
    "NCJ - CAPE",
    "SRR - ERS (ERN - ERS)",
    "ERN - 'D' - CAB",
    "ERS - 'D' - CAB",
    "ERN/ERS - KTYM - KYJ",
    "ERS - ALLP - KYJ",
    "GUV - PNQ",
    "SCT - QLN"
]

up_menu_dict = {
    "CAPE - NCJ": {"key1": "value1", "key2": "value2"},
    "TEN - NCJ": {"key3": "value3", "key4": "value4"},
    # Add more items as needed
}

down_menu_dict = {
    "QLN - TEN (NCJ - TEN)": {
        "KOLLAM": {
            "Place": "KOLLAM",
            "Des": "S",
            "Signalno": "4A",
            "Loc": "155/21-23",
            "Lcno": "540"
        },
        "KOLLAM-1": {
            "Place": "KOLLAM",
            "Des": "LSS RT",
            "Signalno": "13/G31D",
            "Loc": "156/36-38",
            "Lcno": "543,544"
        },
        "KOLLAM-2": {
            "Place": "KOLLAM",
            "Des": "G1",
            "Signalno": "G31/G41D",
            "Loc": "157/28-30",
            "Lcno": "545"
        },
        "KOLLAM-3": {
            "Place": "KOLLAM",
            "Des": "G2",
            "Signalno": "G41/G51D/12D",
            "Loc": "158/18-20",
            "Lcno": "545"
        },
        "KOLLAM-4": {
            "Place": "KOLLAM",
            "Des": "G3",
            "Signalno": "G51",
            "Loc": "159/18-20",
            "Lcno": "545"
        },
    },
    "NCJ - CAPE": {"key7": "value7", "key8": "value8"},
    "SRR - ERS (ERN - ERS)": {"key9": "value9"},
    "ERN - 'D' - CAB": {"key10": "value10"},
    "ERS - 'D' - CAB": {"key11": "value11"},
    "ERN/ERS - KTYM - KYJ": {"key12": "value12"},
    "ERS - ALLP - KYJ": {"key13": "value13"},
    "GUV - PNQ": {"key14": "value14"},
    "SCT - QLN": {"key15": "value15"}
}

# Define button pins
button_up_pin = Pin(2, Pin.IN, Pin.PULL_UP)
button_down_pin = Pin(3, Pin.IN, Pin.PULL_UP)
button_ok_pin = Pin(22, Pin.IN, Pin.PULL_UP)
button_right_pin = Pin(27, Pin.IN, Pin.PULL_UP)
button_left_pin = Pin(26, Pin.IN, Pin.PULL_UP)
start_stop_button_pin = Pin(4, Pin.IN, Pin.PULL_UP)  # Assuming pin 4 for the start/stop button

# Define initial color values
color_white = ili9341.color565(200, 200, 200)
color_blue = ili9341.color565(0, 0, 255)  # Blue color

# Define constants for layers
LAYER_HOME = 0
LAYER_MENU_UP = 1
LAYER_MENU_DOWN = 2

# Initialize variables
current_layer = LAYER_HOME
selected_option = None
selected_index_up = 0
selected_index_down = 0
start_index_up = 0
start_index_down = 0
current_page_index = 0
# Define initial station index
current_station_index = 0
current_index = 0

# Function to display station information
def display_station_info(station_info):
    display.clear()
    display.draw_text(0, 0, station_info["station"], unispace, color_white)
    y_offset = 30
    for key, value in station_info.items():
        if key != "station":
            display.draw_text(0, y_offset, f"{key}: {value}", unispace, color_white)
            y_offset += 30

# Function to draw the home screen
def draw_home_screen():
    display.clear()
    display.draw_text(0, 0, "SELECT THE DIRECTION:", unispace, color_white)
    if selected_option == "UP":
        display.draw_text(0, 40, "UP", unispace, color_blue)
        display.draw_text(0, 80, "DOWN", unispace, color_white)
    elif selected_option == "DOWN":
        display.draw_text(0, 40, "UP", unispace, color_white)
        display.draw_text(0, 80, "DOWN", unispace, color_blue)
    else:
        display.draw_text(0, 40, "UP", unispace, color_white)
        display.draw_text(0, 80, "DOWN", unispace, color_white)

# Function to draw the UP menu
def draw_up_menu():
    display.clear()
    display.draw_text(0, 0, "UP MENU:", unispace, color_white)
    for i in range(5):
        index = start_index_up + i
        color = color_blue if index == selected_index_up else color_white
        if index < len(up_menu_items):
            display.draw_text(0, 40 + i * 30, up_menu_items[index], unispace, color)

# Function to draw the DOWN menu
def draw_down_menu():
    display.clear()
    display.draw_text(0, 0, "DOWN MENU:", unispace, color_white)
    for i in range(5):
        index = start_index_down + i
        color = color_blue if index == selected_index_down else color_white
        if index < len(down_menu_items):
            display.draw_text(0, 40 + i * 30, down_menu_items[index], unispace, color)


def display_selected_dictionary(menu_item):
    display.clear()

    max_y = display.height - 30  # Adjusted to leave some space at the bottom
    y_offset = 30

    # Sort the keys of the menu item
    keys = sorted(menu_item.keys())

    # Iterate over the sorted keys
    for key in keys:
        if key in menu_item:
            specific_info = menu_item[key]
            display.draw_text(0, y_offset, key, unispace, color_white)
            y_offset += 30
            for sub_key, value in specific_info.items():
                if y_offset < max_y:
                    display.draw_text(0, y_offset, f"{sub_key}: {value}", unispace, color_white)
                    y_offset += 30
                else:
                    break
            y_offset += 10

    # Reset the current index if it exceeds the length of keys
    current_index = (current_index + 1) % len(keys)


    # Reset the current index if it exceeds the length of keys
    current_index = (current_index + 1) % len(keys)

    




# Main loop
draw_home_screen()

# Variable to track the current page of the displayed information
current_page = 0
max_pages = 0  # Variable to store the maximum number of pages


while True:
    if current_layer == LAYER_HOME:
        if not button_up_pin.value():
            selected_option = "UP"
            draw_home_screen()
            utime.sleep_ms(200)
        elif not button_down_pin.value():
            selected_option = "DOWN"
            draw_home_screen()
            utime.sleep_ms(200)
        elif not button_ok_pin.value() and selected_option:
            if selected_option == "UP":
                current_layer = LAYER_MENU_UP
                draw_up_menu()
            elif selected_option == "DOWN":
                current_layer = LAYER_MENU_DOWN
                draw_down_menu()
            utime.sleep_ms(200)
    elif current_layer == LAYER_MENU_UP:
        if not button_up_pin.value():
            if selected_index_up > 0:
                selected_index_up -= 1
                if start_index_up > 0:
                    start_index_up -= 1
                draw_up_menu()
        elif not button_down_pin.value():
            if selected_index_up < len(up_menu_items) - 1:
                selected_index_up += 1
                if selected_index_up >= 5:
                    start_index_up += 1
                draw_up_menu()
        elif not button_ok_pin.value():
            selected_item = up_menu_items[selected_index_up]
            selected_dict = up_menu_dict.get(selected_item, {})
            display_selected_dictionary(selected_dict)
    elif current_layer == LAYER_MENU_DOWN:
        if not button_up_pin.value():
            if selected_index_down > 0:
                selected_index_down -= 1
                if start_index_down > 0:
                    start_index_down -= 1
                draw_down_menu()
        elif not button_down_pin.value():
            if selected_index_down < len(down_menu_items) - 1:
                selected_index_down += 1
                if selected_index_down >= 5:
                    start_index_down += 1
                draw_down_menu()
        elif not button_ok_pin.value():
            selected_item = down_menu_items[selected_index_down]
            selected_dict = down_menu_dict.get(selected_item, {})
            display_selected_dictionary(selected_dict)
        elif not button_right_pin.value():
            # Handle right button press to display next dictionary
            selected_item = down_menu_items[selected_index_down]
            print("selectedIndex")
            print(selected_index_down)
            print("selectedItem")
            print(selected_item)

            selected_dict = down_menu_dict[selected_item]

            # Create a list of key-value tuples
            dict_items = list(selected_dict.items())

            if len(dict_items) > 0:
                # Find the index of the current page
                current_page_index = 0
                for idx, (key, _) in enumerate(dict_items):
                    if key == "KOLLAM":
                        current_page_index = idx
                        break

                # Get the next dictionary starting from the current page index
                num_dicts = len(dict_items)
                current_page_index = (current_page_index + 1) % num_dicts
                selected_key, selected_info = dict_items[current_page_index]
                display.clear()
                display.draw_text(0, 0, selected_key, unispace, color_white)
                y_offset = 30
                for key, value in selected_info.items():
                    if y_offset < display.height:  # Ensure we don't exceed display height
                        display.draw_text(0, y_offset, f"{key}: {value}", unispace, color_white)
                        y_offset += 30
                    else:
                        break
                utime.sleep_ms(200)  # Delay to prevent multiple selections
