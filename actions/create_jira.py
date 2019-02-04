from st2common.runners.base_action import Action
from jira import JIRA


class jira(Action):
    def run(self, summary):
        jira_url = self.config['jira_url']
        username = self.config['jira_username']
#        password = self.config['password']
        password = self.config['jira_password']
        self.jira_client = JIRA(jira_url, basic_auth=(username, password))
        jiraNum = self.jira_client.create_issue(project = "TS", summary = summary, description = summary, issuetype= "Story")
        msg = "Jira " + str(jiraNum) + " is created"
        return msg
