def qln_ten():
    # Define station information
    stations = {
        "Kollam": {
            "station": "Kollam",
            "place": "Some place",
            "description": "Some description",
            "signalno": "Some signalno",
            "location": "Some location",
            "lcno": "Some lcno"
        },
        "Paravur": {
            "station": "Paravur",
            "place": "Some place",
            "description": "Some description",
            "signalno": "Some signalno",
            "location": "Some location",
            "lcno": "Some lcno"
        },
        # Add more stations as needed
    }
    
    down_menu_dict = {
        "QLN - TEN (NCJ - TEN)": [
            stations["Kollam"],  # Include station information directly
            stations["Paravur"],  # Include station information directly
            # Add more stations as needed
        ],
        # Add more items as needed
    }

    return stations, down_menu_dict

# Function to display the selected dictionary
def display_selected_dictionary(menu_item):
    display.clear()
    
    y_offset = 30
    for key, value in menu_item.items():
        display.draw_text(0, y_offset, f"{key}: {value}", unispace, color_white)
        y_offset += 30

# Main loop
draw_home_screen()

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
            utime.sleep_ms(200)  # Delay to prevent multiple selections



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
            utime.sleep_ms(200)  # Delay to prevent multiple selections
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
        utime.sleep_ms(200)  # Delay to prevent multiple selections
    elif not button_right_pin.value():
        current_station_index = (current_station_index + 1) % len(down_menu_dict[selected_item])
        display_station_info(down_menu_dict[selected_item][current_station_index])
        utime.sleep_ms(200)  # Delay to prevent multiple selections





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
            utime.sleep_ms(200)  # Delay to prevent multiple selections
                elif not button_right_pin.value():
            selected_item = down_menu_items[selected_index_down]
            selected_dict = down_menu_dict.get(selected_item, {})
            if "Kollam" in selected_dict:
                kollam_info = selected_dict["Kollam"]
                if current_page < len(kollam_info) - 1:
                    current_page += 1  # Increment current_page to display the next page of information
                    display_selected_dictionary(kollam_info[f"Kollam{current_page}"])
                else:
                    current_page = 0  # Reset to the first page if reached the end
                    display_selected_dictionary(kollam_info["Kollam"])  # Display the first page
            else:
                for location, info in selected_dict.items():
                    if isinstance(info, dict):
                        display_selected_dictionary(info)
                        break  # Only display the first dictionary found
            utime.sleep_ms(200)  # Delay to prevent multiple selections



elif not button_right_pin.value():
            selected_item = down_menu_items[selected_index_down]
            selected_dict = down_menu_dict.get(selected_item, {})
            dict_items = list(selected_dict.items())
            if len(dict_items) > 0:
                current_page = (current_page + 1) % len(dict_items)
                selected_key, selected_info = dict_items[current_page]
                display.clear()
                display.draw_text(0, 0, selected_key, unispace, color_white)
                y_offset = 30
                for key, value in selected_info.items():
                    display.draw_text(0, y_offset, f"{key}: {value}", unispace, color_white)
                    y_offset += 30
            utime.sleep_ms(200)  # Delay to prevent multiple selections
