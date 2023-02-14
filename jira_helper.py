from jira import JIRA

USERNAME='petyai1999@yandex.ru'
TOKEN='ATATT3xFfGF0-oNg7pUFA0I0p6jwetUQu9ehqwTy805TvvHjDjhyEvmkAqDfbhz6pxFD0m87UpmVU_7-lXCGKOcIEYEw0QgycTH63z7VgeRZCYfJRVusnDkESUOxurR80EUdHUHL0AAfAwlX-mWf0a5XILG90YS6iCMjgFSgsrif4MzGh_3BTfQ=826D320E'

jira_options = {'server': 'https://include1310.atlassian.net/'}
jira = JIRA(options=jira_options, basic_auth=(USERNAME, TOKEN))
jql = 'project = SCRUM'
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

