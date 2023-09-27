import json

with open('all_repos.json') as f:
    data = json.load(f)

# print(data["results"][0]["repo_name"]) # gets the name of the repository
# print(data["results"][0]["latest_commit_analysis_results"]["test_execution_results"]) # gets the list of test execution results
# print(data["results"][0]["latest_commit_analysis_results"]["pom_files_count"])


for repo in data['results']:
    print(repo["repo_name"])

    if len(repo["latest_commit_analysis_results"]["test_execution_results"]) > 0 and repo["latest_commit_analysis_results"]["pom_files_count"] == 1:

        f = open('repos_with_pom.csv','a')
        f.write(str(repo["repo_name"]) + '\n') #Give your csv text here.
        f.close()


