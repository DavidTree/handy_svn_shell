# handy_svn_shell

A collection of lightweight shell scripts for simplifying the setup of multiple Subversion (SVN) repositories and user accounts on a Linux server.

Designed to automate repetitive tasks, `handy_svn_shell` helps you create repositories, configure access permissions, and generate passwords without manually writing the same commands over and over again.

No fancy abstractions. Just handy scripts that get the job done.

## Features

- **Automatic password generation** — Generate passwords for SVN accounts.
- **Bulk setup** — Create multiple repositories with a shared user and a service account.
- **Quick setup** — Create a single repository with multiple users and a service account.
- **Guided walkthrough** — Follow a step-by-step guide to learn how to create and configure repositories.
- **Command generation** — Run the scripts locally and copy the generated commands to your server.

## Getting Started

### Prerequisites

Before getting started, you'll need:

- A Linux-based server.
- Apache HTTP Server installed and configured for SVN access.
- Subversion installed and configured on the server.
- Appropriate permissions to create repositories and configure access controls.

For installation and setup documentation, see the [Apache Subversion website](https://subversion.apache.org/).

### Usage

1. Clone or download this repository to your local machine.
2. Open the script you want to use.
3. Update the configuration variables to match your server environment.
4. Run the script locally.
5. Review the generated commands and copy them to your server.
6. Execute the commands on your server and verify that the repositories and permissions are configured correctly.

**Note:** The scripts generate commands for you to execute on your server. They do not automatically connect to or configure the remote server.

## Configuration

Each script contains three configuration variables that should be reviewed and updated before use.

| Variable | Description |
| --- | --- |
| `tech_username` | The service account to add to all repositories created by the script. |
| `svn_path_on_server` | Absolute path on the server to the directory where SVN repositories are stored. Must start with `/`. |
| `server_unc_path` | The UNC path used to reference the server or repository location from your environment. |

### Example

```bash
tech_username = "svn_service"
svn_path_on_server = "/var/svn/repos"
server_unc_path = "//server/svn"
```

The values above are examples only. Replace them with paths and account names appropriate for your environment. Check the expected path format in each script before running it.

## Available Scripts

The project provides three workflows:

### Bulk

Create a batch of repositories using a common user and a service account. Ideal for setting up multiple repositories in one go.

### Quick

Create a single repository and configure access for multiple users alongside the service account. Useful for smaller, one-off setups.

### Walkthrough

A step-by-step guide to creating repositories and configuring their access. Best suited to users who want to understand the process rather than simply generate commands.

## Security Considerations

- Review generated commands before executing them on your server.
- Protect generated passwords and avoid committing credentials to version control.
- Ensure Apache and Subversion are configured securely for your environment.

## Contributing

If you have an improvement in mind, feel free to open an issue or submit a pull request. Keep changes focused on making the scripts more useful, reliable, and easy to understand.

## Disclaimer

These scripts were originally written to save a few minutes of repetitive work. They follow a simple philosophy: **form follows function**.

They work for their intended purpose, but they are deliberately lightweight and may not cover every server configuration or edge case. Review and test the generated commands before using them in a production environment.

Use them as they are, adapt them to your needs, and improvements are always welcome.

## License

See the [LICENSE](LICENSE) file for licensing information.
