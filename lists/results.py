results = ["Mario", "Luigi"]

results.append("Princess")

results.append(["Bowser", "Donkey kong jr"])  # added list to the last index of list
results.remove(["Bowser", "Donkey kong jr"])  # removed list from list
results.insert(0, "Bowser")  # added Bowser on 0 index on list
results.remove("Bowser")  # removed Bowser from the list
results.insert(2, "Yoshi")  # added Yoshid on 2nd index on list
results.extend(
    ["Bowser", "Donkey kong"]
)  # added Bowser and Donkey king to the last two indexes of the list

print(results)
# the expected result should be ['Mario', 'Luigi', 'Yoshi', 'Princess', 'Bowser', 'Donkey kong jr']

# now printing results on reverse order
# Using reverse() method (modifies original list)
results.reverse()  # This modifies the original list and returns None
print("Reversed list:", results)
