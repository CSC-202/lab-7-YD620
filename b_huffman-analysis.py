# huffman-analysis.py
## author - nick s.
### get huffman.py working first, then work on this file

import matplotlib.pyplot as plt

# DATA - lyrics
DONT_SAY = 'Yesterday, We were only kids could never fade away. Running thru the wind and pouring rain.Memories at the door.Burning bright from long before.We don/t talk anymore.What are we fighting for.I went my way. You went sideways. We were always running. Out of time. Don/t say we didn/t try. Don/t say we could ever be the same together. We/re not what we used to be. Don/t say you wanted me. Don/t say you wanted me. Don/t say you wanted me. Seasons change. I kept getting colder. Breathing shades of grey. You were climbing higher you/d say. Memories at the door. Burning bright from long before. We don/t talk anymore. What are we fighting for. I went my way. You went sideways. We were always running. Out of time. Don/t say we didn/t try. Don/t say we could ever be the same together. We/re not what we used to be. Don/t say you wanted me. Don/t say you wanted me. Don/t say you wanted me. Don/t say you wanted me'
HEAT_WAVE = 'Last night, all I think about is you. Don/t stop, baby, you can walk through. Don/t wanna, but I think about you. You know that I/m never gonna lose. Road shimmer, wiggling the vision. Heat, heat waves, I/m swimming in a mirror. Road shimmer, wiggling the vision. Heat, heat waves, I/m swimmin/ in a. Sometimes all I think about is you. Late nights in the middle of June. Heat waves been faking me out. Can/t make you happier now. Sometimes all I think about is you. Late nights in the middle of June. Heat waves been faking me out. Can/t make you happier now. Usually, I put something on TV. So we never think about you and me. But today, I see our reflections clearly in Hollywood. Laying on the screen. You just need a better life than this. You need something I can never give. Fake water all across the road. It/s gone now, the night has come, but. Sometimes all I think about is you. Late nights in the middle of June. Heat waves been faking me out. Can/t make you happier now. You can/t fight it, you can/t breathe. You say something so loving, but. Now I gotta let you go. You/ll be better off with someone new I don/t wanna be alone. You know it hurts me too. You look so broken when you cry. One more and then I say goodbye. Sometimes all I think about is you. Late nights in the middle of June. Heat waves been faking me out. Can/t make you happier now. Sometimes all I think about is you. Late nights in the middle of June. Heat waves been faking me out. Can/t make you happier now. I just wonder what you/re dreaming of. When you sleep and smile so comfortable. I just wish that I could give you that. That look that/s perfectly un-sad. Sometimes all I think about is you. Late nights in the middle of June. Heat waves been faking me out. Heat waves been faking me out. Sometimes all I think about is you. Late nights in the middle of June. Heat waves been faking me out. Can/t make you happier now. Sometimes all I think about is you. Late nights in the middle of June. Heat waves been faking me out. Can/t make you happier now. Road shimmer wiggling the vision. Heat, heat waves, I/m swimming in a mirror. Road shimmer wiggling the vision. Heat, heat waves, I/m swimming in a mirror'
MILLION_DAYS = 'I don/t do this often. You caught me off guard. All of my friends said you moved out west. You tell me stories underneath sun sets. Could it be more than just one night? Kiss in the cab ride. Head turning left right. Get a ticket for two. To wherever you choose. Drinking some red out of the blue. You say my name with your accent. Makes me remember. How much I missed ya. Hope you/re planning to stay. For a million days. You/ll be my summer in December. Hey boy. Trust my intuitions. Always. I/m not superstitious. I got lucky. I stole your heart. And it was mine for the taking. I/m bad at pretending, you know I/ll be true. Sunday mornings, midnight lights. Turn into songs that you watch me write. Stole your sweater on that night. You took a picture. I keep by my bedside. So you/re mine when you/re gone. Baby please don/t be long. I got my ticket to the westside. You say my name with your accent. Makes me remember. How much I missed ya. Hope you/re planning to stay. For a million days. You/ll be my summer in December. Hey boy. Trust my intuitions. Always. I/m not superstitious. I got lucky. Stole your heart. And it was mine for the taking. It was mine for the taking. It was mine for a million days. Hmm, in a million ways. Stole your heart, and I got lucky. Stole your heart and it was mine in a million ways. Hmm, for a million days'

# DATA - mantras
GREEN_LATTERN = 'In brightest day, in blackest night, No evil shall escape my sight. Let those who worship evil\'s might, Beware my power... Green Lantern\'s light!'
JEDI_CODE = 'Emotion, yet peace. Ignorance, yet knowledge. Passion, yet serenity. Chaos, yet harmony. Death, yet the Force.'
SITH_CODE = 'Peace is a lie. There is only Passion. Through Passion, I gain Strength. Through Strength, I gain Power. Through Power, I gain Victory. Through Victory my chains are Broken. The Force shall free me.'

# the input, what we want to encode
def huffman(message:str) -> float:
    message = message.upper()

    # the output, should be all 0's and 1s
    result: str = str()

    # for counting the letter frequencies
    freq: dict = dict() # key  -> a letter
                        # item -> num of occurences

    # for holding the nodes of the huffman tree
    nodes: list = list() 

    # for storing the code for each letter
    coding: dict = dict()   # key  -> a letter
                            # item -> a binary encoding

# STEP 0 - TODO
## defining our data structures
    class Node: # NOT given to students
        weight: int
        letters: str
        left: any
        right: any

        def __init__(self, weight = None, letters = None, left = None, right = None):
            self.weight = weight
            self.letters= letters
            self.left = left
            self.right = right

## defining operations
### recursively traverses the huffman tree to record the codes
    def retrieve_codes(v: Node, path: str=''):
        if v.letters != None: # if 'TODO': # TODO
            coding[v.letters] = path # TODO
        else:
            retrieve_codes(v.left, path + '0') # TODO
            retrieve_codes(v.right, path + '1') # TODO

# STEP 1
## counting the frequencies - TODO
    for i in message:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1


# STEP 2
## initialize the nodes - TODO
    for letters, count in freq.items():
        nodes.append(Node(count, letters))

# STEP 3 - TODO
## combine each nodes until there's only one item in the nodes list
    while len(nodes) > 1:
    ## sort based on weight
        nodes.sort(key=lambda x: x.weight, reverse=True)

    ## get the first min
        min_a: Node = nodes.pop()

    ## get the second min
        min_b: Node = nodes.pop()

    ## combine the two
        combined = Node(min_a.weight + min_b.weight, None, min_a, min_b) # TODO

    ## put the combined nodes back in the list of nodes
        nodes.append(combined)

# STEP 4
## reconstruct the codes
    huff_root = nodes[0]
    retrieve_codes(huff_root)
    for i in message:
        result += str(coding[i]) # TODO (hint coding[letter] -> code)


    # STEP 5
    ## analyize compression performance
    n_original_bits: int = len(message) * 8
    n_encoded_bits: int = len(result)
    compression_ratio: float = 1 - (n_encoded_bits / n_original_bits)

    return result, coding, compression_ratio

# LYRICS
plt.subplot(2, 1, 1)
plt.suptitle('Lab 7 - Ye Analyzing Huffman')

MAX_N: int = int(128 * 3 / 2)

# PLOT 1
## POKEMON
data: str = DONT_SAY
ratios: list = list()
for i in range(1, len(data)):
    x = data[0: i]
    compressed, coding, ratio = huffman(x)
    ratios.append(ratio)
min_ratio = min(ratios)
min_idx = ratios.index(min_ratio)

plt.plot(ratios[:MAX_N], label=f'DONT_SAY (n={len(coding)})', color ='red', linestyle='dashdot')

## JIGGLE JIGGLE
data: str = HEAT_WAVE
ratios: list = list()
for i in range(1, len(data)):
    x = data[0: i]
    compressed, coding, ratio = huffman(x)
    ratios.append(ratio)
min_ratio = min(ratios)
min_idx = ratios.index(min_ratio)

plt.plot(ratios[:MAX_N], label=f'HEAT_WAVE (n={len(coding)})', color ='blue', linestyle='dashdot')

## ALPHABET
data: str = MILLION_DAYS
ratios: list = list()
for i in range(1, len(data)):
    x = data[0: i]
    compressed, coding, ratio = huffman(x)
    ratios.append(ratio)
min_ratio = min(ratios)
min_idx = ratios.index(min_ratio)

plt.plot(ratios[:MAX_N], label=f'MILLION_DAYS (n={len(coding)})', color ='green', linestyle='dashdot')

# PLOT 2
plt.subplot(2, 1, 2)

## SITH CODE
data: str = SITH_CODE
ratios: list = list()
for i in range(1, len(data)):
    x = data[0: i]
    compressed, coding, ratio = huffman(x)
    ratios.append(ratio)
min_ratio = min(ratios)
min_idx = ratios.index(min_ratio)

plt.plot(ratios[:MAX_N], label=f'SITH_CODE (n={len(coding)})', color ='red', linestyle='dashdot')

## GREEN LATERN'S OATH
data: str = GREEN_LATTERN
ratios: list = list()
for i in range(1, len(data)):
    x = data[0: i]
    compressed, coding, ratio = huffman(x)
    ratios.append(ratio)
min_ratio = min(ratios)
min_idx = ratios.index(min_ratio)

plt.plot(ratios[:MAX_N], label=f'GREEN_LATTERN (n={len(coding)})', color ='blue', linestyle='dashdot')

## JEDI CODE
data: str = JEDI_CODE
ratios: list = list()
for i in range(1, len(data)):
    x = data[0: i]
    compressed, coding, ratio = huffman(x)
    ratios.append(ratio)
min_ratio = min(ratios)
min_idx = ratios.index(min_ratio)

plt.plot(ratios[:MAX_N], label=f'JEDI_CODE (n={len(coding)})', color ='green', linestyle='dashdot')

plt.savefig('./figs/Ye_lab7_analysis.png')
plt.show()
