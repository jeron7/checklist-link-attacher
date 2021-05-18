# checklist-link-attacher 🔗

A command-line app that helps attach links and finish checkitemns of a checklist in Trello.

## Motivation

I have an habit to read some random articles from web and when i find something interesting i append in a card that contains various articles. This app facilitate this process.


## How to configure and run?

1. Create a .env file with OAUTH_API_KEYS, OAUTH_TOKEN.
1. Those env variables should be get from [Trello API Authorization page](https://developer.atlassian.com/cloud/trello/guides/rest-api/authorization/).
1. Run:
```
python3 main.py