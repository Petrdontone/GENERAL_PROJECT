from jira import JIRA

USERNAME='petyai1999@yandex.ru'
TOKEN='ATATT3xFfGF0PrZMMwwxfX4d1s8U5U6jq-Tjs9g9x98y54eb0GbxViC94etAZu_k81rjQizccMMwy-rRA1X--52Qvr13KkAR5fqbBpM49flte-vC0DpLXricO54MK69_Z6cFzVU4qK7-KgVBsIhfUPoZu0wRugH-th-6FlYIFNIeVIEuVqKvIZ4=F61F876A'

jira_options = {'server': 'https://include1310.atlassian.net/'}
jira = JIRA(options=jira_options, basic_auth=(USERNAME, TOKEN))
jql = 'project = SCRUM ORDER BY Rank ASC'
result_issues = jira.search_issues(jql_str=jql, maxResults=100)
for issue_list in result_issues:
    print(issue_list.fields.reporter)

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

