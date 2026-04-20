cities = ("Lucknow", "Delhi", "Mumbai", "Pune", "Jaipur")
print(cities)
print(type(cities))
print(cities[0])
print(len(cities))
print("Delhi" in cities)
print("Gurgaon" in cities)

t = (12, 24, 36)
print(t)
# print(t.append(1)) AttributeError: 'tuple' object has no attribute 'append'

ENV_API_URLS = tuple(["abc.com/get", "xyz.com/post", "pqr.com/put"])
print(ENV_API_URLS)
print(type(ENV_API_URLS))
print(ENV_API_URLS[0])

colors = ("red", "green", "blue")
for color in colors:
    print(color)
    print(color.upper())
    print(color.lower())
    print(color.title())

numbers = (1, 2, 3) * 4
print(numbers)

names = ("Mumbai", "Delhi", "Pune") * 3
print(names)

print("----")

num = (1, 2, 2, 3, 2)
print(len(num))
print(num.count(2))
print(num.index(2))