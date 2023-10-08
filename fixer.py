import requests

from bs4 import BeautifulSoup




url = 'https://sgimera.github.io/mai_RatingAnalyzer/scripts_maimai/maidx_in_lv_data_festivalplus.js'

response = requests.get(url)

text_content = response.text

text_content = text_content.replace("javascript:","").replace("var","").replace("const","")


text_content = "\n".join(x.strip() for x in text_content.splitlines())

exec(text_content)

update_mlist_orig = update_mlist

update_llist_orig = update_llist

print("javascript:")

song_db_std = {}

song_db_DX = {}

char_to_idx = 'baemr' # basic, advanced, expert, master, re:master

for lv in range(1,16):
    try:
        list_to_parse = eval(f"lv{lv}_rslt")
        #print(list_to_parse)
    except Exception as e:
        continue

    for i, sub_levels in enumerate(list_to_parse):
        exact_level = (lv+0.1*(len(list_to_parse)-i-1))
        #print(sub_levels)
        for song_element in sub_levels:
            #print(song_element)
            soup = BeautifulSoup(song_element) # we'll change if it proves to be too slow
            song_name = soup.select("span")[0].text
            dx = False
            if song_name.endswith("[dx]"):
                song_name = song_name[:-4]
                dx = True
            song_type = soup.select("span")[0]['class'][0][-1]
            print(exact_level, song_type, dx, song_name)

            dictionary_to_edit = song_db_DX if dx else song_db_std
            original_entry = dictionary_to_edit.get(song_name, [0,0,0,0,0])
            original_entry[char_to_idx.find(song_type)] = exact_level
            dictionary_to_edit[song_name] = original_entry

for plus_or_not in 'pm':
    for lv in range(1,16):
        try:
            list_to_parse = eval(f"lv{lv}{plus_or_not}")
            #print(list_to_parse)
        except Exception as e:
            continue

        

        approx_level = lv + (0.7 if plus_or_not == "p" else 0)

        for song_element in list_to_parse:
            #print(song_element)
            soup = BeautifulSoup(song_element) # we'll change if it proves to be too slow
            song_name = soup.select("span")[0].text
            dx = False
            if song_name.endswith("[dx]"):
                song_name = song_name[:-4]
                dx = True
            song_type = soup.select("span")[0]['class'][0][-1]
            print(f"lv{lv}{plus_or_not}", lv, approx_level, song_type, dx, song_name)

            dictionary_to_edit = song_db_DX if dx else song_db_std
            original_entry = dictionary_to_edit.get(song_name, [0,0,0,0,0])
            original_entry[char_to_idx.find(song_type)] = -approx_level
            dictionary_to_edit[song_name] = original_entry
            other_spans = []
            if len(soup.select("span")) > 1:
                # there are other charts as well
                other_spans = soup.select("span")[1:]
                for other_span in other_spans:
                    song_type = other_span['class'][0][-1]
                    approx_level_custom = int(other_span.text.replace("+","")) + (0.7 if "+" in other_span.text else 0)


                    dictionary_to_edit = song_db_DX if dx else song_db_std
                    original_entry = dictionary_to_edit.get(song_name, [0,0,0,0,0])
                    original_entry[char_to_idx.find(song_type)] = -approx_level_custom
                    dictionary_to_edit[song_name] = original_entry







print(song_db_std)

print(song_db_DX)


dx = 'dx'
v = 'v'
lv='lv'
n = 'n'
nn = 'nn'
ico = 'ico'

url = "https://sgimera.github.io/mai_RatingAnalyzer/scripts_maimai/maidx_in_lv_buddies.js"

response = requests.get(url)

text_content = response.text

text_content = text_content.replace("javascript:","").replace("var","").replace("const","")

text_content = "\n".join(x.strip().replace("`", "'''" if "411" in x else '"""').split("//",1)[0] for x in text_content.splitlines() if not "NameAlias" in x)

exec(text_content)

in_lv = [x for x in in_lv if x['v'] < 21]
# to get rid of new version charts

print(in_lv)
import math

def who_is_the_bettter_bet(mine, yours):
    if mine == 0: # no data on festival, use buddies data
        return yours
    elif mine < 0 and yours > 0: # festival unsure, buddies sure, use buddies data WITH CONDITION!!!
        if yours < abs(mine): # mine was -11 but now you say 10.9. I reject downgrades!
            print("No downgrades!", mine, yours)
            input()
            return mine
        if math.isclose(abs(mine)%1, 0.7) and yours > abs(mine) + 0.25: # mine was -11.7 but you say it is 12 or higher
            print("No upgrades! (+)", mine, yours, abs(mine) + 0.25)
            input()
            return mine # maybe return upper bound?
        if not math.isclose(abs(mine)%1, 0.7) and yours > abs(mine) + 0.65: # mine was -11 but you say it is 11.7 or higher
            print("No upgrades!", mine, yours)
            input()
            return mine # maybe return upper bound?
        return yours
    elif mine > 0 and yours < 0: # festival sure, buddies unsure, use festival data
        return mine
    else:
        return mine 
        # if both festival and buddies sure, use festival. 
        # if both festival and buddies unsure, use festival.

for idx in range(len(in_lv)):
    current_elem = in_lv[idx]
    dictionary_to_read = song_db_DX if current_elem[dx] else song_db_std
    array_better_info = dictionary_to_read.get(current_elem.get('nn', current_elem['n']), [0,0,0,0,0]) # yes nn is used if available
    for mine, yours in zip(array_better_info, in_lv[idx]['lv']):
        if mine != yours and mine != 0:
            print(current_elem['n'], array_better_info, current_elem['lv'], [who_is_the_bettter_bet(mine, yours) for mine, yours in zip(array_better_info, in_lv[idx]['lv'])])
            #input()
    in_lv[idx]['lv'] = [who_is_the_bettter_bet(mine, yours) for mine, yours in zip(array_better_info, in_lv[idx]['lv'])]


in_lv.append({dx:1, v:16, lv:[-2, -7, -10, 12.5, 0], n:"Shiny Smily Story", ico:"634d7f6007a3af76"})
in_lv.append({dx:1, v:16, lv:[-1, -5, -7.7, -10.7, 13.0], n:"冬のこもりうた", ico:"7eb9f64eda816b98"})
in_lv.append({dx:1, v:16, lv:[-3, -6, -8.7, -11, -12.7], n:"秒針を噛む", ico:"6cc2f7748e087bd5"})

print(in_lv)

with open("maidx_in_lv_festivalplus.evnchn.js", 'w', encoding='utf-8') as f:
    f.write("javascript:\n")
    f.write(f'''var update_mlist = "{update_mlist_orig}"; // By evnchn. Best guess from gathered festival and buddies data. Refer to https://github.com/evnchn/fix-mai-internal-lv\n''')
    f.write(f'''var update_dlist = "{update_llist_orig}";\n''')
    f.write(f'var in_lv = [\n')

    for in_lv_item in in_lv:
        f.write("	{")
        f.write(f"dx:{in_lv_item['dx']}, ")
        f.write(f"v:{in_lv_item['v']}, ")
        f.write(f"lv:{in_lv_item['lv']}, ")
        f.write(f"n:`{in_lv_item['n']}`, ")
        try:
            f.write(f"nn:`{in_lv_item['nn']}`, ")
        except:
            pass
        f.write(f"ico:`{in_lv_item['ico']}`")
        f.write("}\n")




