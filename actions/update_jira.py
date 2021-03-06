
from st2common.runners.base_action import Action
from jira import JIRA


class jira(Action):
    def run(self, description, summary, jiranum):
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
        updateIssue = self._jira_client.issue.update(summary, description, jiranum)
        msg = "Issue updated"
        return msg
