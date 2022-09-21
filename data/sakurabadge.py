# Sakura Badges

import discord

from utils import Bot


BADGES = {
    "1ksp": {
        "name": "1,000 Sakura Point",
        "emoji": None,
        "description": "累計SakuraPointが1000を超えています。",
        "condition": lambda u, b: 1000000 > b.cogs["SakuraPoint"].cache[u.id] > 1000
    },
    "1msp": {
        "name": "1,000,000 Sakura Point",
        "emoji": None,
        "description": "累計SakuraPointが100万を超えています。",
        "condition": lambda u, b: b.cogs["SakuraPoint"].cache[u.id] > 1000000
    },
    "sk_project_member": {
        "name": "Sakura Project Member",
        "emoji": None,
        "description": "このBotの開発チームのメンバーです。",
        "condition": lambda u, b: u.id in b.owner_ids
    }
}


def get_badge(user: discord.Member | discord.User, bot: Bot) -> list[str]:
    "バッヂを取得します。"
    badgelist = []
    for id_, badge in BADGES.items():
        if badge["condition"](user, bot):
            badgelist.append(id_)
    return badgelist
