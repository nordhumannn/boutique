def renumber_todo_list(input_file):
    with open(input_file, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        current_number = 1

        for line in lines:
            index = line.find('.')
            if index != -1:
                number = line[:index]
                if number.isdigit():
                    new_line = str(current_number) + line[index:]
                    current_number += 1
                    file.write(new_line)
                else:
                    file.write(line)
            else:
                file.write(line)
        file.truncate()

renumber_todo_list(input('FILE PATH: '))