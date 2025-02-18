# numbers=[1,2,3]
# new_numbers=[n+1 for n in numbers]
# print(new_numbers)
# name="Angela"
# new_list=[letter for letter in name]
# print(new_list[1])
# new_list=[number+1  for number in range(1,5)]
# print(new_list)
# names=["Alex","Beth","Caroline","Dave","Elanor","Freddie"]
# capital_name=[name.upper() for name in names if len(name)>5]
# print(capital_name)
# item="Hello"
# new_item=[new_item for new_item in item if len(new_item)<5]
# import random
# names=["Alex","Beth","Caroline","Dave","Elanor","Freddie"]
# student_score={student_name:random.randint(1,100) for student_name in names}
# passed_student={passed_name:score for (passed_name,score) in student_score.items() if score>60}
# print(passed_student)
from http.cookiejar import uppercase_escaped_char

from pygments.lexer import words

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# new_list=sentence.split()
# word_len_list={word:len(word) for word in new_list}
# print(word_len_list)
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
# weather_f = {temp_c_day:(temp_c * 9/5) + 32 for (temp_c_day,temp_c) in weather_c.items()}
#
# print(weather_f)

# student_dict={
#     "student":["angela","james","Lily"],
#     "score":[56,76,98]
# }
# # for (key,value) in student_dict.items():
# #     print(value)
#
# import pandas
# student_data_frame=pandas.DataFrame(student_dict)
# for (index,row) in student_data_frame.iterrows():
#     print(index)
import pandas
import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict={row.letter:row.code for (index,row) in data.iterrows()}
user_input=input("ENTER THE WORD:").upper()
word=[new_dict[letter] for letter in user_input ]
print(word)