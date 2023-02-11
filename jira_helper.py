from jira import JIRA
from credentinals import TOKEN, USERNAME

jira_options = {'server': 'https://include1310.atlassian.net/'}
jira = JIRA(options=jira_options, basic_auth=(USERNAME, TOKEN))
jql = 'project = SCRUM'
result_issues = jira.search_issues(jql_str=jql, maxResults=100)
for issue_list in result_issues:
    print(issue_list.fields)

#
issue_dict = {
    'project': {'key': 'SCRUM'},
    'summary': 'Testing issue from Python Jira Handbook',
    'description': 'Detailed ticket description.',
    'issuetype': {'name': 'Bug'},
    'customfield_10020': 2
}

new_issue = jira.create_issue(fields=issue_dict)
print(new_issue)
