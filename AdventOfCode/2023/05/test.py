import re

text = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".split(
    "\n\n"
)

# text = open("day5.txt").read().split("\n\n")

# dest range start, source range start, length

# Any source numbers that aren't mapped correspond to the same destination number

pattern = re.compile(r"\d+")
seeds = re.findall(pattern, text[0])
seed_to_soil = re.findall(pattern, text[1])
soil_to_fertilizer = re.findall(pattern, text[2])
fertilizer_to_water = re.findall(pattern, text[3])
water_to_light = re.findall(pattern, text[4])
light_to_temperature = re.findall(pattern, text[5])
temperature_to_humidity = re.findall(pattern, text[6])
humidity_to_location = re.findall(pattern, text[7])

seeds = [int(number) for number in seeds]
seed_to_soil = [int(number) for number in seed_to_soil]
soil_to_fertilizer = [int(number) for number in soil_to_fertilizer]
fertilizer_to_water = [int(number) for number in fertilizer_to_water]
water_to_light = [int(number) for number in water_to_light]
light_to_temperature = [int(number) for number in light_to_temperature]
temperature_to_humidity = [int(number) for number in temperature_to_humidity]
humidity_to_location = [int(number) for number in humidity_to_location]

locations = []


def translator(number, map):
    for i in range(0, len(map), 3):
        dest_start, source_start, length = map[i], map[i + 1], map[i + 2]
        if number in range(source_start, source_start + length):
            return dest_start + (number - source_start)

    return number


for seed in seeds:
    soil = translator(seed, seed_to_soil)
    fertilizer = translator(soil, soil_to_fertilizer)
    water = translator(fertilizer, fertilizer_to_water)
    light = translator(water, water_to_light)
    temperature = translator(light, light_to_temperature)
    humidity = translator(temperature, temperature_to_humidity)
    location = translator(humidity, humidity_to_location)
    locations.append(location)


part1 = min(locations)
print("Part 1:", part1)


def translate_range(input_range, map_entry):
    dest_start, source_start, length = map_entry
    source_end = source_start + length

    # Calculate the overlap between the input range and the source range in the map
    overlap_start = max(input_range[0], source_start)
    overlap_end = min(input_range[1], source_end)

    # If there's an overlap, translate it to the destination range
    if overlap_start < overlap_end:
        translated_start = dest_start + (overlap_start - source_start)
        translated_end = translated_start + (overlap_end - overlap_start)

        input_start, input_end = input_range
        if overlap_start == input_start:
            input_start = overlap_end
        if overlap_end == input_end:
            input_end = overlap_start
        return [translated_start, translated_end], [input_start, input_end]
    return None, input_range


def translate_ranges(ranges, map):
    translated_ranges = []

    for input_range in ranges:
        for i in range(0, len(map), 3):
            map_entry = map[i : i + 3]
            translated_range, input_range = translate_range(input_range, map_entry)
            if translated_range:
                translated_ranges.append(translated_range)
    if input_range[0] != input_range[1] and input_range[0] < input_range[1]:
        translated_ranges.append(input_range)
    return translated_ranges


seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_start, length = seeds[i], seeds[i + 1]
    seed_end = seed_start + length
    seed_ranges.append([seed_start, seed_end])

soil = translate_ranges(seed_ranges, seed_to_soil)
fertilizer = translate_ranges(soil, soil_to_fertilizer)
water = translate_ranges(fertilizer, fertilizer_to_water)
light = translate_ranges(water, water_to_light)
temperature = translate_ranges(light, light_to_temperature)
humidity = translate_ranges(temperature, temperature_to_humidity)
location = translate_ranges(humidity, humidity_to_location)


mini = float("inf")
for loc in location:
    mini = min(mini, min(loc))

print(location)
