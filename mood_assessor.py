import datetime
import os

def assess_mood():

    def limit_input():
        f = open('data/mood_diary.txt', 'r')
        date_today = datetime.date.today()
        date_today = str(date_today)
        for line in f:
            if date_today in line:
                return True
            else:
                return False


    def mood_to_number(current_mood):
        if current_mood == 'happy':
            return 2
        elif current_mood == 'relaxed':
            return 1
        elif current_mood == 'apathetic':
            return 0 
        elif current_mood == 'sad':
            return -1
        elif current_mood == 'angry':
            return -2

    def number_to_mood(current_number):
        if current_number == 2:
            return 'happy'
        elif current_number == 1:
            return 'relaxed'
        elif current_number == 0:
            return 'apathetic'
        elif current_number == -1:
            return 'sad'
        elif current_number == -2:
            return 'angry'

    def mood_entry():
        if not limit_input():
            while True:
                current_mood = input("What is your current mood: ")
                if current_mood in ['happy', 'relaxed', 'apathetic', 'sad', 'angry']:
                    mood_number = mood_to_number(current_mood)
                    date_today = str(datetime.date.today())
                    os.makedirs('data', exist_ok=True)
                    f = open('data/mood_diary.txt', 'a')
                    f.write(f"{mood_number},{date_today}\n")
                    break
        else:
            print('Sorry, you have already entered your mood today.')

    def mood_diagnostic():
        f = open('data/mood_diary.txt', 'r')
        lines = f.readlines()
        num_entries = len(lines)

        if num_entries >= 7:
            mood_data = [int(line.split(',')[0]) for line in lines[-7:]]  

            num_happy = mood_data.count(2)
            num_sad = mood_data.count(-1)
            num_apathetic = mood_data.count(0)
            
            if num_happy >= 5:
                print("manic")
            elif num_sad >= 4:
                print('depressive')
            elif num_apathetic >= 6:
                print('schizoid')
            else:
                    avg_mood = round(sum(mood_data) / len(mood_data))
                    mood = number_to_mood(avg_mood)
                    print(f"Your diagnosis: {mood}")
        else:
            return None

    mood_entry()
    if not limit_input():
        mood_diagnostic()
