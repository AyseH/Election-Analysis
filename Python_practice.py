# counties = ["Arapahoe", "Denver", "Jefferson"]
# if "El Paso" in counties:
#     print("True")
# else:
#     print("False")
#     if "Arapahoe" in counties or "EL Paso" in counties:
#         print("Arapahoe or El Paso is in the list of counties")
#     else:
#         print("Arapahoe and El Paso are not in the list of counties")
#     if "Arapahoe" in counties and "El Paso" not in counties:
#         print("Only Arapahoe is in the list of counties. ")
#     else:
#         print("Arapahoe is in the list of counties and El Paso is not in the list of counties. ")
# """ 
# for county in counties:
#     print(county)
# for num in range(5):
#     print(num)
# for i  in range(len(counties)):
#     print(counties[i])  """
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#     print(county)
# for county in counties_dict.keys():
#     print(county)
# for county in counties_dict.values():
#     print(county)
# for voters in counties_dict.values():
#     print(voters)
# for county in counties_dict:
#     print(counties_dict[county])
# for county in counties_dict:
#     print(counties_dict.get(county))
#     print(counties_dict)


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]






# for county_dict in voting_data:

#      print(county_dict['registered_voters'])


# for county_dict in voting_data:  

#      print(county_dict["county"])
# for county in counties_dict:
#      print(county)
# for voters in counties_dict:
#      print(voters)
# for voters in counties_dict.values():
#      print(voters)
# for county in counties_dict:
     # print(counties_dict[county])   
#Arapahoe county has 422829 registered voters.
#Denver county has 463353 registered voters.
#Jefferson county has 432438 registered voters.

# for county, voters in counties_dict.items():
#      print(county + " county has " +  str(voters) +  " registered voters ")

# for county, voters in counties_dict.items ():
#      print(f" {county} county has {voters} registered voters")


# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# print(f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")
# for county in counties_dict.keys():
#      print(county)
# for voters in counties_dict.values():
#     print(voters)
# for county in counties_dict:
#     print(counties_dict[county])
# for county, voters in counties_dict.items():
#      print(county+ ' county has '+ str(voters)+ ' registered voters.')
# for county,voters in counties_dict.items():
#      print(f"{county} county has {voters :,} registered voters")
# for  counties_dict in voting_data:
#      print(counties_dict['registered_voters'])
# for  counties_dict in voting_data:
#      print(counties_dict['county'])


# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
# print(voting_data)
# print(counties_dict.items())

# for county, voters in counties_dict.items():
#      print(f"{county} county has {voters} registered voters")
# for data in voting_data:
#      county = list(data.values ())[0]
#      registered_voters = list(data.values())[1]
#      print(f"{county} county has {registered_voters:,} registered voters")
for counties_dict in voting_data:
    county=counties_dict.get("county")
    registered_voters=counties_dict.get('registered_voters')
    print(f"{county} county has {registered_voters:,}")
    
    


