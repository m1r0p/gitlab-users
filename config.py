###### settings
##### GitLab settings
GITLAB_BASE_URL = 'git.example.com'
GITLAB_USERS_URL = "https://" + GITLAB_BASE_URL + "/api/v4/users?per_page=200;page="
AMOUNT_OF_PAGES = 2
GITLAB_TOKEN='<your_token>'
VALID_DOMAINS = ['example.com', 'example2.com']
GITLAB_VERSION_URL="https://" + GITLAB_BASE_URL + "/api/v4/version"

##### old squash settings
OLD_SQUASH_BASE_URL="http://<ip_or_name>:8030/squash"
OLD_SQUASH_ADMIN_URL = OLD_SQUASH_BASE_URL + '/administration'
OLD_SQUASH_USER="<your_user>"
OLD_SQUASH_PASS="<your_pass>"

