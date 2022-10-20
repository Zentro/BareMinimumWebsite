**_This is still very much in the early stages of development! Some features may not yet be complete or some aspects of the bot may not function!_**

[![Multi-Mod-logo.png](https://i.postimg.cc/4xnBFMCD/Multi-Mod-logo.png)](https://postimg.cc/w18X1wj2)

## Introduction

SimpliMod (MultiMod) is a no-nonsense lightweight bot you can use to moderate your Discord server.

## Installing

### Creating a Discord application

This is an important step when self-hosting a Discord bot is registering a bot with Discord to get a token.
1. Browse to https://discord.com/developers/ and be sure that you're logged into your Discord account.
2. Click the **New Application** button at the top.
3. Provide a name and select a team, either personal or an organization you're part of, and then click Create.
4. In the side on the left, click **Bot** under Settings.
5. Click the **Add Bot** button at the top and then click **Yes, do it!**.

### Adding the bot to your Discord server

Now that you've registered a bot with Discord and got your token, you'll want to add it to your server with the needed 

**Note: Enabling privileged intents does not require you to go through bot verification until your bot is in over 100 guids.**

### Running the bot

**Python 3.8 or higher is required.**

```
# Should work on Windows, Linux, and macOS
```

You can then install the required packages.

```
pip install -r requirements.txt
```

Then to run it.

```
python simplimod.py
```

and you're good to go!

### A few things to consider


## License

Code released under the [MIT License](./LICENSE).