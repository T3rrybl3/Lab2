def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)
    print(f"BMI = {bmi:.2f}")
    if bmi < 18.5:
        print("Under Weight")
        return -1
    elif bmi > 25:
        print("Over Weight")
        return 1
    else:
        print("Normal Weight")
        return 0


calculate_bmi(weight=57, height=1.73)


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    user_input = get_user_input()
    print(f"You Type: {user_input}")
    print(f"Average = {calc_average(user_input)}")
    print(f"Min and Max = {find_min_max(user_input)}")
    sort_input = sort_temperature(user_input)
    print(f"Temp in ascending order = {sort_input}")
    print(f"Median temp = {calc_median_temperature(sort_input)}")


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    temp = input()
    user_input = temp.split(",")
    float_list = [float(item) for item in user_input]
    return float_list


def calc_average(user_input):
    number = len(user_input)
    total = 0
    for value in user_input:
        total += value
    avg = total/number
    return avg


def find_min_max(user_input):
    max = user_input[0]
    min = user_input[0]
    for number in user_input:
        if number > max:
            max = number
        if number < min:
            min = number
    return [min, max]


def sort_temperature(user_input):
    for value in user_input:
        for number in range(len(user_input)-1):
            if user_input[number] > user_input[number+1]:
                temp = user_input[number]
                user_input[number] = user_input[number+1]
                user_input[number+1] = temp
    return user_input


def calc_median_temperature(sort_input):
    if len(sort_input) % 2:
        middle = len(sort_input)//2
        median = sort_input[middle]
    else:
        middle = len(sort_input)//12
        median = (sort_input[middle]+sort_input[middle-1])/2
    return median


if __name__ == "__main__":
    main()
