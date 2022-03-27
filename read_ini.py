from configparser import ConfigParser

conf = ConfigParser()
conf.read("data/jira_item.ini",encoding="utf-8")
userEmail = conf.get("jirainfo","userEmail")
api_token = conf.get("jirainfo","api_token")
# print(userEmail,api_token)
reporter = conf.get("jql","reporter")
print(reporter)

project_key = conf.get("project","project_key")
print(project_key)