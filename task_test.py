import os
import csv
import timeit

# Бібліотека timeit -> https://docs.python.org/uk/3/library/timeit.html

# Визначаємо поточну директорію
dir = os.path.dirname(__file__)

# Вказуємо ім'я файлу
file_path = os.path.join(dir, '10m.txt')


def main():
    # Читаємо числа з файлу
    def read_numbers_from_file(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            numbers = [int(row[0]) for row in reader]
        return numbers

    # Шукаємо максимальне значення
    def find_max(numbers):
        sorted_numbers = sorted(numbers)
        max_number = sorted_numbers[-1]
        return max_number

    # Шукаємо мінімальне значення
    def find_min(numbers):
        sorted_numbers = sorted(numbers)
        min_number = sorted_numbers[0]
        return min_number

    # Шукаємо медіану 
    def find_median(numbers):
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        if n % 2 == 1:
            return sorted_numbers[n // 2]
        else:
            mid1 = sorted_numbers[n // 2 - 1]
            mid2 = sorted_numbers[n // 2]
            return (mid1 + mid2) / 2

    # Шукаємо середнє арифметичне значення
    def find_mean(numbers):
        total = 0
        for number in numbers:
            total += number
        return total / len(numbers)

    # Шукаємо найбільшу послідовність чисел (які ідуть один за одним), яка збільшується
    def longest_increasing_sequence(numbers):
        longest_seq = []
        current_seq = []

        for i in range(len(numbers) - 1):
            if numbers[i] < numbers[i + 1]:
                current_seq.append(numbers[i])
            else:
                current_seq.append(numbers[i])
                if len(current_seq) > len(longest_seq):
                    longest_seq = current_seq
                current_seq = []

        if len(current_seq) > len(longest_seq):
            longest_seq = current_seq

        return longest_seq

    # Шукаємо найбільшу послідовність чисел (які ідуть один за одним), яка зменшується
    def longest_decreasing_sequence(numbers):
        longest_seq = []
        current_seq = []

        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                current_seq.append(numbers[i])
            else:
                current_seq.append(numbers[i])
                if len(current_seq) > len(longest_seq):
                    longest_seq = current_seq
                current_seq = []

        if len(current_seq) > len(longest_seq):
            longest_seq = current_seq

        return longest_seq
 

    numbers = read_numbers_from_file(file_path)

    max_number = find_max(numbers)
    min_number = find_min(numbers)
    median_number = find_median(numbers)
    mean_number = find_mean(numbers)
    longest_inc_seq = longest_increasing_sequence(numbers)
    longest_dec_seq = longest_decreasing_sequence(numbers)

    print("Максимальне число в файлі:", max_number)
    print("Мінімальне число в файлі:", min_number)
    print("Медіана:", median_number)
    print("Середнє арифметичне значення:", mean_number)
    print("Найбільшу послідовність чисел (які ідуть один за одним), яка збільшується:", longest_inc_seq)
    print("Найбільшу послідовність чисел (які ідуть один за одним), яка зменшується", longest_dec_seq)


if __name__ == '__main__':

    setup_code = "from __main__ import main"
    execution_time = timeit.timeit("main()", setup=setup_code, number=1)

    print(f"Час виконання: {execution_time} секунд")