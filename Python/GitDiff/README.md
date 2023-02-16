# Mass Git Diff

Executes git diff for multiple files simultaneously and generates a greppable changelog file.

Authored by Leonard Haddad, provided in accords with the MIT License.

## Usage

- Open the file and set the `commit` to the hash of whatever commit you'd like to compare to.
- Fill the `changed_files` list with a list of file names that you'd like to check for changes as strings.
- *Optional:* Add your own enumeration at the bottom of the file.

```bash
~> ./massgdiff
Output log written to changelog.log
```