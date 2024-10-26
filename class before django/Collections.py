# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# thislist.insert(2, "watermelon")
# print(thislist.clear())
# for x in thislist:
#     print(x)
# if "apple" in thislist:
#     print("apple")
# print(thislist in "apple")
# print("apple" in thislist)

# list2 = list(thislist)
# print(list2)


# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)



# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset)


# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict["year2"] = 2018
# print(thisdict)



myfamily = {
  "child1" : {"name" : "Emil","year" : 2004},
  "child2" : {"name" : "Tobias","year" : 2007},
  "child3" : {"name" : "Linus","year" : 2011}
}

for x, obj in myfamily.items():
    print(x)
    print(obj)
    
    for y in obj:
        print(y + ':', obj[y])
