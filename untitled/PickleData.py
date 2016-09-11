import pickle, shelve

print("Pickling lists")

variety = ["ogurci", "pomidory", "kapusta"]
shape = ["celie", "kubikami", "solomkoy"]
brand = ["Glavprodukt", "Chumak", "Boduel"]

f = open("pickles1.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("Unpickling lists")

f = open("pickles1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
f.close()

print(variety)
print(shape)
print(brand)

print("\nShelving into file")

s = shelve.open("pickles2.dat")

s["variety"] = ["ogurci", "pomidory", "kapusta"]
s["shape"] = ["celie", "kubikami", "solomkoy"]
s["brand"] = ["Glavprodukt", "Chumak", "Boduel"]
s.sync()

print("\nExtracting lists")
print("Brand names - ", s["brand"])
print("Product shapes - ", s["shape"])
print("Variety of products - ", s["variety"])
s.close()





