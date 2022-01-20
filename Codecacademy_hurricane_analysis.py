# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages # Function converts letters to numerical values.
def converter():
    updated_damages = []
    for damage in damages:
        if damage == 'Damages not recorded':
            updated_damages.append(damage)
        else:
            if "M" in damage:
                M_remove = damage.replace("M", "")
                updated_damages.append(float(M_remove) * conversion["M"])
            elif "B" in damage:
                B_remove = damage.replace("B", "")
                updated_damages.append(float(B_remove) * conversion["B"])
    return updated_damages

updated_damages = converter()


# write your construct hurricane dictionary function here: # Function makes dictionary with data for every hurricane.

def update_huricane():
    hurricanes = {}
    for index in range(len(names)):
        hurricanes[names[index]] = {"Name": names[index],
                                    "Month": months[index],
                                    "Year": years[index],
                                    "Max Sustained Wind": max_sustained_winds[index],
                                    "Areas Affected": areas_affected[index],
                                    "Damage": updated_damages[index],
                                    "Deaths": deaths[index]}
    return hurricanes

hurricanes = update_huricane()

# write your construct hurricane by year dictionary function here: # Function returns year and how many hurricanes occurred in it.

def year_converter():
    hurricane_by_year = {}
    for values in hurricanes.values():
        current_year = values["Year"]
        hurricane_by_year[current_year] = []
        for values in hurricanes.values():
            if current_year == values["Year"]:
                hurricane_by_year[current_year].append(values)
    return hurricane_by_year

hurricane_by_year = year_converter()

# write your count affected areas function here: # Function counts how many hurricanes occurred in every area.

def area_converter():
    zipped_areas = []
    for areas in areas_affected:
        zipped_areas += areas
    area_count = dict(zip(zipped_areas,[zipped_areas.count(i) for i in zipped_areas]))
    return area_count

hurricane_by_area = area_converter()

# write your find most affected area function here: # Function returns area with most hurricanes.

def most_hurricanes():
    max_area = 'Central America'
    max_area_count = 0
    for key, value in hurricane_by_area.items():
        if value > max_area_count:
            max_area_count = value
            max_area = key
    m_h = {max_area: max_area_count}
    return m_h

most_hurricanes()

# write your greatest number of deaths function here: # Function counts how many deaths occurres through each hurricane.

def deaths_converter():
    hurricane_by_death = {}
    for index in range(len(names)):
        hurricane_by_death[names[index]] = deaths[index]
    return hurricane_by_death

hurricane_by_death = deaths_converter()

# Function returns area with most deaths.

def most_deaths():    
    max_death = 'Central America'
    max_death_count = 0
    for key, value in hurricane_by_death.items():
        if value > max_death_count:
            max_death_count = value
            max_death = key
    m_h = {max_death: max_death_count}
    return m_h

most_lethal = most_deaths()

# write your categorize by mortality function here: # Function categorizes hurricanes by mortality.

def mortality_counter():
    hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for keys, values in hurricane_by_death.items():
        if values == 0:
            hurricanes_by_mortality[0].append(hurricanes[keys])
        elif values <= 100:
            hurricanes_by_mortality[1].append(hurricanes[keys])
        elif values <= 500:
            hurricanes_by_mortality[2].append(hurricanes[keys])
        elif values <= 1000:
            hurricanes_by_mortality[3].append(hurricanes[keys])
        elif values <= 10000:
            hurricanes_by_mortality[4].append(hurricanes[keys])
        elif values <= 50000:
            hurricanes_by_mortality[5].append(hurricanes[keys])
    return hurricanes_by_mortality

mortality_counter()


# write your greatest damage function here: # Function sets how much damage each hurricane dealt.

def damage_converter():
    hurricane_by_damage = {}
    for index in range(len(names)):
        if updated_damages[index] != 'Damages not recorded':
            hurricane_by_damage[names[index]] = updated_damages[index]
    return hurricane_by_damage

hurricane_by_damage = damage_converter()

# Function returns area with most damage taken.

def most_damage():
    max_area = 'Central America'
    max_area_damage = 0
    for key, value in hurricane_by_damage.items():
        if value > max_area_damage:
            max_area_damage = value
            max_area = key
    m_h = {max_area: max_area_damage}
    return m_h

most_pricy = most_damage()


# write your categorize by damage function here: # Function categorizes hurricanes by damage.
def damage_counter():
    hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for keys, values in hurricane_by_damage.items():
        if values == 0:
            hurricanes_by_damage[0].append(hurricanes[keys])
        elif values <= 100000000:
            hurricanes_by_damage[1].append(hurricanes[keys])
        elif values <= 1000000000:
            hurricanes_by_damage[2].append(hurricanes[keys])
        elif values <= 10000000000:
            hurricanes_by_damage[3].append(hurricanes[keys])
        elif values <= 50000000000:
            hurricanes_by_damage[4].append(hurricanes[keys])
        elif values <= 500000000000:
            hurricanes_by_damage[5].append(hurricanes[keys])
    return hurricanes_by_damage

hurricanes_by_damage = damage_counter()