## append Method of Lists initial Version

#results = ["Mario", "Luigi"]

#results.append("Princess")
#results.append("Yoshi")
#results.append("Koopa Troopa")
#results.append("Toad")

#results.append(["Bowser", "Donkey Kong Jr."])
#results.remove(["Bowser", "Donkey Kong Jr."])
#results.extend(["Bowser", "Donkey Kong Jr."])

## and so on...

#print(results)

## Updated Version

results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr"]

results.remove("Bowser")
results.insert(0, "Bowser")
results.reverse()


print(results)