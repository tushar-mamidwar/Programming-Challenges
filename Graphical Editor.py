def take_input_command():
    print("Enter Commands and their options:")
    command_list = []
    command = []
    while True:
        command = input().split()
        command_list.append(command)
        if command[0] == 'X':
            break
    execute_commands(command_list)


def execute_commands(command_list):
    for command in command_list:
        if command[0] == "I":
            picture = []
            for i in range(int(command[2])):
                picture.append([0] * int(command[1]))
        elif command[0] == "C":
            for i in range(len(picture)):
                for j in range(len(i)):
                    picture[i][j] = 0
        elif command[0] == "L":
            picture[int(command[2]) - 1][int(command[1]) - 1] = command[3]
        elif command[0] == "V":
            for i in range(int(command[2]) - 1, int(command[3])):
                picture[i][int(command[1]) - 1] = command[-1]
        elif command[0] == "H":
            for i in range(int(command[1]) - 1, int(command[2])):
                picture[int(command[3]) - 1][i] = command[-1]
        elif command[0] == "K":
            for i in range(int(command[2]) - 1, int(command[4])):
                for j in range(int(command[1]) - 1, int(command[3])):
                    picture[i][j] = command[-1]
        elif command[0] == "F":
            for i in range(len(picture)):
                for j in range(len(picture[i])):
                    if picture[int(command[1]) - 1][int(command[2]) - 1] == picture[i][j] and (i != int(
                            command[2]) - 1 or j != int(command[1]) - 1):
                        picture[i][j] = command[-1]
            picture[int(command[1]) - 1][int(command[2]) - 1] = command[-1]

        elif command[0] == "S":
            filename = command[1].split(".")
            if len(filename[0]) > 8:
                filename[0] = filename[0][:8]
            if len(filename[1]) > 3:
                raise Exception("Extension should have less than or equal to 3 characters")
            print(".".join(filename))
            for i in picture:
                for j in i:
                    print(j, end="")
                print()


take_input_command()
