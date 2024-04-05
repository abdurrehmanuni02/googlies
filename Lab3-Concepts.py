
#dictionary

food = {
        "burger":10,
        "soda":5,
        "salad":15,
        "donut":25
        }

print(food)
print(food["soda"])
food["tea"] = 14
print(food)
for key in food:
    print(key , " : " , food[key])
food.update({"soda":6})
print(food)   

#list

foodList = list(food.values())
print(foodList)
foodList.