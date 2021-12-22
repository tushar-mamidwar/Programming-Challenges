def initialize_lcd_digit():
    global lcd_digit
    lcd_digit = []
    for i in range(size * 2 + 3):
        lcd_digit.append([" "] * (size + 2))


def convert_to_lcd_style():
    input_string = input("Enter input as no. of digits and number separated by space:\n")
    list_of_input = []
    while input_string != "0 0":
        list_of_input.append(input_string.split())
        input_string = input()
    convert_and_add_to_lcd_number_list(list_of_input)


def convert_and_add_to_lcd_number_list(list_of_input):
    for input_command in list_of_input:
        global size
        global lcd_number_list
        lcd_number_list = []
        size = int(input_command[0])
        initialize_lcd_digit()
        for digit in input_command[1]:
            initialize_lcd_digit()
            digit = int(digit)
            function_list[digit]()
            lcd_number_list.append(lcd_digit)
        output_list.append(lcd_number_list)


def draw_horizontal_segment(line_number):  # line_number is defined as below:
                                            # 0 = top-line
                                            # 1 = middle-line
                                            # 2 = bottom-line
    index_number = line_number * size + line_number
    for i in range(1, size + 1):
        lcd_digit[index_number][i] = "-"


def draw_vertical_segment(vertical_segment_code):  # Vertical_segment_code is defined as below:
                                                    # 0 = top-left
                                                    # 1 = bottom-left
                                                    # 2 = top-right
                                                    # 3 = bottom-left
    row_index = vertical_segment_code % 2 * size + 1 + vertical_segment_code % 2
    if vertical_segment_code > 1:
        column_index = size + 1
    else:
        column_index = 0
    for i in range(size):
        lcd_digit[row_index + i][column_index] = "|"


def zero():
    draw_horizontal_segment(0)
    draw_vertical_segment(0)
    draw_vertical_segment(1)
    draw_vertical_segment(2)
    draw_vertical_segment(3)
    draw_horizontal_segment(2)


def one():
    draw_vertical_segment(2)
    draw_vertical_segment(3)


def two():
    draw_horizontal_segment(0)
    draw_vertical_segment(2)
    draw_horizontal_segment(1)
    draw_vertical_segment(1)
    draw_horizontal_segment(2)


def three():
    draw_vertical_segment(2)
    draw_vertical_segment(3)
    draw_horizontal_segment(0)
    draw_horizontal_segment(1)
    draw_horizontal_segment(2)


def four():
    draw_vertical_segment(0)
    draw_vertical_segment(2)
    draw_vertical_segment(3)
    draw_horizontal_segment(1)


def five():
    draw_vertical_segment(0)
    draw_vertical_segment(3)
    draw_horizontal_segment(0)
    draw_horizontal_segment(1)
    draw_horizontal_segment(2)


def six():
    draw_vertical_segment(0)
    draw_vertical_segment(1)
    draw_vertical_segment(3)
    draw_horizontal_segment(0)
    draw_horizontal_segment(1)
    draw_horizontal_segment(2)


def seven():
    draw_vertical_segment(2)
    draw_vertical_segment(3)
    draw_horizontal_segment(0)


def eight():
    draw_vertical_segment(0)
    draw_vertical_segment(1)
    draw_vertical_segment(2)
    draw_vertical_segment(3)
    draw_horizontal_segment(0)
    draw_horizontal_segment(1)
    draw_horizontal_segment(2)


def nine():
    draw_vertical_segment(0)
    draw_vertical_segment(2)
    draw_vertical_segment(3)
    draw_horizontal_segment(0)
    draw_horizontal_segment(1)
    draw_horizontal_segment(2)


def print_lcd_style():
    for lcd_number_list in output_list:
        i = 0
        j = 0
        k = 0
        for i in range(len(lcd_number_list[0])):
            for j in range(len(lcd_number_list)):
                for k in range(len(lcd_number_list[0][0])):
                    print(lcd_number_list[j][i][k], end="")
                print(end=" ")
            print()
        print("\n")


output_list = []  # this will be four dimensional list containing the whole input in LCD style
lcd_number_list = []  # this will be three dimensional list containing one line of input in LCD style
lcd_digit = []  # This will be two dimensional list conaining a single digit in LCD style
function_list = (zero, one, two, three, four, five, six, seven, eight, nine) #tuple of functions
convert_to_lcd_style()
print_lcd_style()
