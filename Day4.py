# This is the fourth day challenge

import random

# r_num = random.randint(1, 6)
# print(r_num)
#
# r_float = random.random()
#
# print(r_float)
#
# in_flot = (r_float + r_num) -1
# print(in_flot)
#
# print(r_float *5)

# r_float = random.random()
# if (r_float *2 >= 1):
#     print("head")
# else:
#     print("tail")
#

# states_list = ["Delaware", "Pennsylvania"]
#
# states_list.append("Puert Rico")
#
# print(states_list)
#
# states_list.extend(["DC", "California", "Virginia"])
#
# print(states_list)


#%%


guests = input("Please input the names of individuals ? \n")


guests = guests.split(", ")
print(len(guests))

payer_id = random.randint(0,len(guests))
print(payer_id)

print(f"Ok, the bill will be paid by {guests[payer_id - 1]} ")

p_person = random.choice(guests)
print(p_person)


# The treasure game, I will play it later

# So do, the ruck and papger game

#%%
print("Hello this is Mosa Rahimi. ")



#%%
