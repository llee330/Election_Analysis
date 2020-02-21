import csv
import os

file_to_load = os.path.join("Resources/election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}   #Declare empty dictionary
county_options = []
county_votes = {}       #Declare empty dictionary for county

# Track the winning candidates
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the most county votes
winning_county = ""
county_count = 0
county_percentage = 0

# Open file to read 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        county_name = row[1]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #setting each candidate's vote count to zero
            candidate_votes[candidate_name] = 0   #vote count
        candidate_votes[candidate_name] += 1    #candidate's count

        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1
    
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
#print(candidate_votes)

    for county in county_votes:
        vote = county_votes[county]
        vote_percentages = float(vote) / float(total_votes) * 100

        if (vote > county_count) and (vote_percentages > county_percentage):
            county_count = vote
            winning_county = county
            county_percentage = vote_percentages

        county_results = (
            f"{county}: {vote_percentages:.1f}% ({vote:,})\n")
        print(county_results)
        txt_file.write(county_results)

    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    txt_file.write(winning_county_summary)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
    
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
        
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

##txt_file.write(winning_candidate_summary)
# Add a vote to that candidate's count
        
# Save the results to out text file.
    ##with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    ##election_results = (
        ##f"\nElection Results\n"
        ##f"-------------------------\n"
        ##f"Total Votes: {total_votes:,}\n"
        ##f"-------------------------\n")
    ##print(election_results, end="")
    # Save the final vote count to the text file.
    ##txt_file.write(election_results)

    ##txt_file.close()
