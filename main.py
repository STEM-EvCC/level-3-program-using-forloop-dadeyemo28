
# Ekundayo Adeyemo

# 05/24/2024

# Data
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

# 1: Count total number of space missions
total_missions = len(mission_names)
print(f"Total number of missions: {total_missions}")

# 2: Count number of successful missions
successful_missions = sum(mission_success)
print(f"Number of successful missions: {successful_missions}")

# 3: Calculate success rate
success_rate = (successful_missions / total_missions) * 100
print(f"Success rate: {success_rate:.2f}%")

# 4: List missions launched before the year 2000
missions_before_2000 = [name for name, year in zip(mission_names, mission_years) if year < 2000]
print("Missions launched before the year 2000:")
for mission in missions_before_2000:
    print(f"- {mission}")
