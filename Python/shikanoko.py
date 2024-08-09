import random
import time
from deer_aa import aa_print

# list。ここから7つ選んで、タイトルを完成させる
shikanoko = ["しか", "のこ", "こし", "たん"]

# listから14文字のランダムな文字列を作成する関数 # ちなみにantlerはツノのこと
def antler():
    output = ""
    for _ in range(7):
        output += random.choice(shikanoko)
    if output == "しかのこのこのここしたんたん":
            return True, output
    return False, output

start_time = time.time()

while True:
    bool, output = antler()
    if bool == True:
        end_time = time.time()
        time_diff = end_time - start_time
        print(output)
        print(f"time_diff:{time_diff}")
        print("鹿")
        aa_print()
        break
    else:
        print(output)
