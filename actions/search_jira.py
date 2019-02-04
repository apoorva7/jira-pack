
from st2common.runners.base_action import Action
from jira import JIRA


class jira(Action):
    def run(self, userName):
        jira_url = self.config['jira_url']
        username = self.config['username']
#        password = self.config['password']
        password = self.config['jira_password']
        self.jira_client = JIRA(jira_url, basic_auth=(username, password))
#        tmp = '"""' + assignee + '"""'
#        a = tmp.split(' ')
#        assign = a[-1].split('"')
#        assign1 = assign[1]
#        print assign1
        query = "assignee=" + userName
        allJira = self._jira_client.search_issues(query)
        userJira = {issue.key: issue for issue in allJira}
        if (len(allJira) == 0 ):
            msg = "There are no issues assigned to " + userName
        #return userJira
