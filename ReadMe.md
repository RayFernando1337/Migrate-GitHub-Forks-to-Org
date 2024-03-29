# GitHub Repository Transfer Script

This script automates the process of transferring your forked repositories to a specified GitHub organization. It utilizes the GitHub API to list all your forked repositories and then transfers them to an organization of your choosing.

## Prerequisites

- **Python**: Ensure you have Python installed on your system. This script is tested with Python 3.10.
- **Personal Access Token**: A GitHub Personal Access Token (PAT) with `repo` and `admin:org` scopes.
- **GitHub Organization**: You need to be an owner or have sufficient privileges in the target GitHub organization.

## Setup Instructions

### 1. Clone the Repository
*If you are using Replit this will be taken care of for you.

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
```

### 2. Install Dependencies
*If you are using Replit this will be taken care of for you.

This script requires the `requests` Python library. Install it using pip:

```bash
pip install requests
```

### 3. Set Environment Variables

- **Replit - Add Secrets**
Use the + New Secret button to add new Secrets to your Repl. You can add the Secret Key, and Value of your choice and select Add Secret.

Set the following environment variables on your system:
```
GITHUB_USERNAME
GITHUB_ORGANIZATION
GITHUB_TOKEN
```

- **Linux/macOS**:

```bash
export GITHUB_USERNAME='your_username'
export GITHUB_ORGANIZATION='your_organization_name'
export GITHUB_TOKEN='your_personal_access_token'
```

- **Windows Command Prompt**:

```cmd
set GITHUB_USERNAME=your_username
set GITHUB_ORGANIZATION=your_organization_name
set GITHUB_TOKEN=your_personal_access_token
```

- **Windows PowerShell**:

```powershell
$env:GITHUB_USERNAME="your_username"
$env:GITHUB_ORGANIZATION="your_organization_name"
$env:GITHUB_TOKEN="your_personal_access_token"
```

Replace `your_username`, `your_organization_name`, and `your_personal_access_token` with your GitHub username, the name of the target organization, and your personal access token, respectively.

## Usage

Run the script from the terminal or command prompt:

```bash
python main.py
```

The script will list all your forked repositories and start transferring them to the specified organization. It will print the status of each transfer attempt.

## Notes

- Ensure you have the necessary permissions to transfer repositories into the target organization.
- The transfer process is subject to GitHub's rate limiting. Consider running the script during off-peak hours if you have a large number of repositories.
- Always verify the successful transfer of repositories to the target organization.

## Getting Variables from GitHub
To fill in the environment variables required by the script (`GITHUB_USERNAME`, `GITHUB_ORGANIZATION`, and `GITHUB_TOKEN`), you will need to gather information from your GitHub account and create a personal access token. Here's how to obtain this information:

### 1\. **GitHub Username**

Your GitHub username is the name you chose when you created your GitHub account. It's visible on your GitHub profile page and in the URL of your profile page, which looks like `https://github.com/your_username`.

### 2\. **GitHub Organization Name**

If you've created or are a member of a GitHub organization to which you want to transfer repositories, you can find the organization's name listed on your GitHub dashboard or by visiting the organization's page directly. The organization's name is also in the organization's page URL, similar to `https://github.com/organization_name`. Ensure you have administrative privileges in the organization for repository transfers.

### 3\. **Personal Access Token (PAT)**

A personal access token (PAT) is used instead of a password for authentication to GitHub, especially when using the GitHub API or the command line. Here’s how to create a PAT:

1.  **Navigate to GitHub Settings**: Click on your profile icon in the top right corner of any GitHub page, then click "Settings."
2.  **Access Developer Settings**: Scroll down the sidebar and click on "Developer settings," located towards the bottom.
3.  **Personal Access Tokens**: In the left sidebar, click on "Personal access tokens."
4.  **Generate New Token**: Click on the "Generate new token" button.
5.  **Note and Scopes**: Give your token a descriptive name in the "Note" field. For the script to work, you must select scopes that grant the permissions your script needs. In this case, you'll need:
    *   `repo` - Grants full access to private and public repositories.
    *   `admin:org` - Grants access to manage organization resources, necessary for transferring repositories to an organization.
6.  **Generate Token**: Once you’ve selected the appropriate scopes, scroll to the bottom of the page and click "Generate token."
7.  **Copy Your New Token**: After generating the token, make sure to copy it to a safe place. GitHub won’t show the token again once you navigate away from the page.



## Contributing

Contributions are welcome! If you have suggestions for improvements or encounter any issues, please open an issue or submit a pull request.

## License

Specify the license under which the script is made available. Common licenses for open-source projects include MIT, GPL, and Apache 2.0.
