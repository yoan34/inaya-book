import json


with open("dataset_stories.json", "r") as file:
    data = json.load(file)
    

def print_file_group_syllabes(data, x):
    syllabes = []
    for word, value in data.items():
        syl = value["syllabes"]
        syllabes.append(syl)
            
    result = []
    syllabes = sorted(syllabes)
    start = syllabes[0].split('-')[0]
    sub = []
    for syl in syllabes:
        if syl.split('-')[0] == start:
            sub.append(syl)
        else:
            result.append(sub)
            sub = [syl]
            start = syl.split('-')[0]


    for r in result:
        print(r)
        
    new_result = []
    for arr in result:
        syl1 = []
        syl2 = []
        syl3 = []
        syl4 = []
        syl5 = []
        syl6 = []
        syl7 = []
        for word in arr:
            n = len(word.split('-'))
            if n == 1:
                syl1.append(word)
            if n == 2:
                syl2.append(word)
            if n == 3:
                syl3.append(word)
            if n == 4:
                syl4.append(word)
            if n == 5:
                syl5.append(word)
            if n == 6:
                syl6.append(word)
            if n == 7:
                syl7.append(word)
        
        new_result.append(syl1+syl2+syl3+syl4+syl5+syl6+syl7)
        
    tt = [arr for arr in new_result if len(arr) >= x]
    header = f"TOTAL groupe de syllabes différentes: {len(tt)}\n"

    with open(f"result_syl_{x}.txt", "w") as f:
        f.write(header)
        for r in new_result:
            if len(r) > n:
                s = "\n".join(r)
                f.write(f"{s}\n\n")
        
        
def show_top_syllables(data):
    syllabes = {}
    for word, value in data.items():
        for key, item in value["possibilities"].items():
            syl = item["syllables"].split('-')
            for s in syl:
                if s not in syllabes:
                    syllabes[s] = 0
                syllabes[s] += 1
    syllabes = sorted(syllabes.items(), key=lambda item: item[1], reverse=True)
    with open("all_syl_count.txt", "w") as f:
        for s, item in syllabes:
            f.write(f"{s:<5} count={item}\n")
    

def show_top_word(data):
    words = {}
    with open("mot_top_count.txt", "w") as f:
        for word, value in data.items():
            f.write(f"{word:<20} count={value['count']}\n")
        
show_top_word(data)