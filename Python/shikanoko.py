import random
shikanoko = ["しか", "のこ", "こし", "たん"]

output = ""

while output != "しかのこのこのここしたんたん":
    output += random.choice(shikanoko)
    print(output)
    if "しかのこのこのここしたんたん" in output:
        print("鹿")
        break