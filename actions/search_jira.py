
from st2common.runners.base_action import Action
from jira import JIRA


class jira(Action):
    def run(self, userName):
        jira_url = self.config['jira_url']
        username = self.config['username']
        password = self.config['jira_password']
        self.jira_client = JIRA(jira_url, basic_auth=(username, password))
        query = "assignee=" + userName
        allJira = self.jira_client.search_issues(query)
        userJira = {issue.key: issue for issue in allJira}
        if (len(allJira) == 0 ):
            msg = "There are no issues assigned to " + userName
        else:
            msg = "Issues assigned to " + userName + " are \n"
            for jiran in range(0, len(allJira)):
                msg+= str(allJira[jiran]) + "\n"
        return msg
