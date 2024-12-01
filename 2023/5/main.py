import fileinput

file = "".join(fileinput.input())
seeds, *raw_mappings = file.split("\n\n")
seeds = [int(x) for x in seeds.split()[1:]]

mappings = []
for m in raw_mappings:
    nums = m.split("\n")[1:]
    mapping = [[int(x) for x in line.split()] for line in nums]
    mappings.append(mapping)
print(mappings)

def seed_to_location(seed, mappings):
    curr = seed

    for mapping in mappings:
        for dst_rng_start, src_rng_start, rng_len in mapping:
            if src_rng_start <= 

                
