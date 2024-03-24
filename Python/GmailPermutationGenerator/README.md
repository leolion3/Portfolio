# Gmail Email Permutation Generator

Few people know that Gmail ignores some special characters and allows emails to be permutated in a variety of ways.
For example, the below email addresses are all one and the same address:

```
test@gmail.com
test@googlemail.com
t.ES.t@gmail.com
t.est+netflix@gmail.com
```

Gmail inherently ignores dots `[.]` and character cases within email addresses, as well as allowing suffixes to be added to your email (using `+`) based on the website you're signing up for:

```
test+netflix@gmail.com
test+disneyplus@gmail.com
test+instagram@gmail.com
```

This tool generates these combinations and exports them for you to use.

## Usage

Using the tool is pretty straightforward:

```bash
python3 ./permutate.py username <charcase - True/False> [optional service name] [optional export file name]
```

- Username: your Gmail username.
- Charcase: Permutate character case as well?
- Service name (optional): include a service name (such as `+netflix`).
- Export file name: Where output should be written to.

## Demo

No Charcase, service included:

![Demo No Charcase](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/GmailPermutationGenerator/media/demo.png)


No service:

![Demo No Service](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/GmailPermutationGenerator/media/demo2.png)

Service and charcase:

![Demo Service and Charcase](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/GmailPermutationGenerator/media/demo3.png)
