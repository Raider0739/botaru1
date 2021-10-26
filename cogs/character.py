import discord
from discord.ext import commands
import sqlite3
import random
import math
import asyncio
import datetime
from collections.abc import Sequence

CHARACTER_HP = 10
MONSTER_HP = 15

conn1 = sqlite3.connect("exp.db")
c = conn1.cursor()


def make_sequence(seq):
    if seq is None:
        return ()
    if isinstance(seq, Sequence) and not isinstance(seq, str):
        return seq
    else:
        return (seq,)

def reaction_check(message=None, emoji=None, author=None, ignore_bot=True):
    message = make_sequence(message)
    message = tuple(m.id for m in message)
    emoji = make_sequence(emoji)
    author = make_sequence(author)
    def check(reaction, user):
        if ignore_bot and user.bot:
            return False
        if message and reaction.message.id not in message:
            return False
        if emoji and reaction.emoji not in emoji:
            return False
        if author and user not in author:
            return False
        return True
    return check

class Character(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def start(self, ctx):

        if c.execute(f"SELECT 1 FROM Exp WHERE User_ID='{ctx.author.id}'").fetchone():
            await ctx.send("You already have a character")
        else:
            c.execute(f"INSERT INTO Exp VALUES ('{ctx.author.id}', '0', '1', '0')")
            c.execute(f"INSERT INTO Stats VALUES ('{ctx.author.id}', '1', '1', '1', '0')")
            embed = discord.Embed(title="I have created your character", colour=discord.Colour.blue())
            await ctx.send(embed=embed)
            conn1.commit()
        
        
    @commands.command()
    @commands.cooldown(1, 150, commands.BucketType.user)
    async def hunt(self, ctx):
        MONSTER_HP = 15
        conn1 = sqlite3.connect("exp.db")
        c = conn1.cursor()
        itemdrop = random.randint(0,100)
        if c.execute(f"SELECT 1 FROM Exp WHERE User_ID='{ctx.author.id}'").fetchone():
            if MONSTER_HP == 15:
                #Stat check
                c.execute(f"SELECT User_ID, Str, Agi, Int, Point FROM Stats WHERE User_ID = '{ctx.author.id}'")
                stat = c.fetchone()
                stren = int(stat[1])
                agi = int(stat[2])
                intel = int(stat[3])
                #Emoji
                emoji1 = self.client.get_emoji(826833818069631056)
                #hit damage
                sword_dmg = random.randint(8,14)
                bow_dmg = random.randint(9,13)
                book_dmg = random.randint(7,13)
                hit_dmg = 2 * int(stren/3)
                if hit_dmg < 3:
                    hit_dmg = 3
                if c.execute(f"SELECT equip FROM Inventory WHERE User_ID = '{ctx.author.id}' AND itemid = 6").fetchone():
                    c.execute(f"SELECT equip FROM Inventory WHERE User_ID = '{ctx.author.id}' AND itemid = 6")
                    equip = c.fetchone()
                    sword = equip[0]
                    if sword == 1:
                        hit_dmg = sword_dmg
                        #Emoji
                        emoji1 = self.client.get_emoji(828739864778244120)
                    else:
                        pass
                if c.execute(f"SELECT equip FROM Inventory WHERE User_ID = '{ctx.author.id}' AND itemid = 7").fetchone():
                    c.execute(f"SELECT equip FROM Inventory WHERE User_ID = '{ctx.author.id}' AND itemid = 7")
                    equip = c.fetchone()
                    bow = equip[0]
                    if bow == 1:
                        hit_dmg = bow_dmg
                        #Emoji
                        emoji1 = self.client.get_emoji(828681668713906223)
                    else:
                        pass  
                if c.execute(f"SELECT equip FROM Inventory WHERE User_ID = '{ctx.author.id}' AND itemid = 8").fetchone():
                    c.execute(f"SELECT equip FROM Inventory WHERE User_ID = '{ctx.author.id}' AND itemid = 8")
                    equip = c.fetchone()
                    spell = equip[0]
                    if spell == 1:
                        hit_dmg = book_dmg
                        #Emoji
                        emoji1 = self.client.get_emoji(828681818877329500)
                    else:
                        pass
                else:
                    hit_dmg = 2 * int(stren/3)   
                
                #Level check
                c.execute(f"SELECT User_ID, Exp, Level FROM Exp WHERE User_ID = '{ctx.author.id}'")
                monster_lvl = c.fetchone()   
                monster_new = int(monster_lvl[2]) 
                bal_gain = random.randint(10,20)
                #Exp gains
                if monster_new <= 5:
                    exp_gain = int(5 + (intel / 2))
                if 5 < monster_new < 10:
                    exp_gain = int(8 + (intel / 2))
                if 10 <= monster_new <= 20:
                    exp_gain = int(10 + (intel / 2))
                if 20 < monster_new <= 30:
                    exp_gain = int(13 + (intel / 2))
                if monster_new > 30:
                    exp_gain = int(15 + (intel / 2))
                #Monsters
                if monster_new <=5:
                    embed = discord.Embed(title="Monster has spawned react to attack it", colour=discord.Colour.blue())
                    embed.set_image(url="https://cdn.discordapp.com/attachments/798913238229188608/826442762936516618/2231125f94e8f1a32241b16ba2d68930.gif")
                if 5 < monster_new < 10:
                    MONSTER_HP = 20
                    embed = discord.Embed(title="Monster has spawned react to attack it", colour=discord.Colour.blue())
                    embed.set_image(url="https://cdn.discordapp.com/attachments/827500709909626920/827500757317451776/662480907cfb2e26aec3f27cd419869a.gif")
                if 10 <= monster_new <= 20:
                    MONSTER_HP = 30
                    embed = discord.Embed(title=f"Monster has spawned react to attack it", colour=discord.Colour.blue())
                    embed.set_image(url="https://cdn.discordapp.com/attachments/827500709909626920/827500757317451776/662480907cfb2e26aec3f27cd419869a.gif")
                if 20 < monster_new <= 30:
                    MONSTER_HP = 45
                    embed = discord.Embed(title=f"Monster has spawned react to attack it", colour=discord.Colour.blue())
                    embed.set_image(url="https://cdn.discordapp.com/attachments/827500709909626920/827500757614985236/5d27099922e5fa89a861563885703ace.gif")
                if monster_new > 30:
                    MONSTER_HP = 60
                    embed = discord.Embed(title=f"Monster has spawned react to attack it", colour=discord.Colour.blue())
                    embed.set_image(url="https://cdn.discordapp.com/attachments/827500709909626920/827500757614985236/5d27099922e5fa89a861563885703ace.gif")
                msg = await ctx.send(embed=embed)
                await msg.add_reaction(emoji1)
                #Embeds 
                if 0 <= itemdrop <= 70: 
                    new_embed = discord.Embed(title=f"You have slain the monster and gained {exp_gain} exp, {bal_gain} coins and a monster meat", colour=discord.Colour.blue())
                    new_embed.set_image(url="https://cdn.discordapp.com/attachments/798913238229188608/826832532019478578/kisspng-headstone-grave-cemete.png")
                        
                if 70 < itemdrop <= 80:
                    new_embed = discord.Embed(title=f"You have slain the monster and gained {exp_gain} exp, {bal_gain} coins, monster meat and a Sword", colour=discord.Colour.blue())
                    new_embed.set_image(url="https://cdn.discordapp.com/attachments/798913238229188608/826832532019478578/kisspng-headstone-grave-cemete.png")
                        
                if 80 < itemdrop <= 90:
                    new_embed = discord.Embed(title=f"You have slain the monster and gained {exp_gain} exp, {bal_gain} coins, monster meat and a Bow", colour=discord.Colour.blue())
                    new_embed.set_image(url="https://cdn.discordapp.com/attachments/798913238229188608/826832532019478578/kisspng-headstone-grave-cemete.png")
                        
                if 90 < itemdrop <= 100:
                    new_embed = discord.Embed(title=f"You have slain the monster and gained {exp_gain} exp, {bal_gain} coins, monster meat and a Spell Book", colour=discord.Colour.blue())
                    new_embed.set_image(url="https://cdn.discordapp.com/attachments/798913238229188608/826832532019478578/kisspng-headstone-grave-cemete.png")
                
                lvl_embed = discord.Embed(title="You leveled up and gained 2 skill points", colour=discord.Colour.blue())
                lvl_embed.set_image(url="https://cdn.discordapp.com/attachments/798913238229188608/826833342694686830/ezgif.com-gif-maker_19.gif")
                check = reaction_check(message=msg, author=ctx.author, emoji=(emoji1))
                remain = MONSTER_HP
                hit_chance = random.randint(0,15)
                #agility stats 
                if agi > 5:
                    hit_chance = random.randint(5,15)
                if agi > 15:
                    hit_chance = random.randint(10,15)
                #reaction loop  
                while remain > 0:        
                    #reaction try 
                    try: 
                        reaction, user = await self.client.wait_for('reaction_add', timeout=10.0, check=check)
                        if reaction.emoji == emoji1:
                            #agility hits  
                            if 0 <= hit_chance < 5:
                                
                                hit = random.choice([0, int(hit_dmg/4), int(hit_dmg/3), int(hit_dmg/2), hit_dmg])                              
                                remain = remain - hit
                                if remain < 0:
                                    remain = 0
                                if monster_new <= 5:
                                    hit_embed = discord.Embed(title=f"Monster has {remain}HP left and you dealt {hit} damage", colour=discord.Colour.blue())
                                    hit_embed.set_image(url="https://cdn.discordapp.com/attachments/798913238229188608/826442762936516618/2231125f94e8f1a32241b16ba2d68930.gif")
                                if 5 < monster_new < 10:
                                    MONSTER_HP = 20
                                    hit_embed = discord.Embed(title=f"Monster has {remain}HP left and you dealt {hit} damage", colour=discord.Colour.blue())
                                    hit_embed.set_image(url="https://cdn.discordapp.com/attachments/827500709909626920/827500757317451776/662480907cfb2e26aec3f27cd419869a.gif")
                                if 10 <= monster_new <= 20:
                                    MONSTER_HP = 30
                                    hit_embed = discord.Embed(title=f"Monster has {remain}HP left and you dealt {hit} damage", colour=discord.Colour.blue())
                                    hit_embed.set_image(url="https://cdn.discordapp.com/attachments/827500709909626920/827500757317451776/662480907cfb2e26aec3f27cd419869a.gif")
                                if 20 < monster_new <= 30:
                                    MONSTER_HP = 45
                                    hit_embed = discord.Embed(title=f"Monster has {remain}HP left and you dealt {hit} damage", colour=discord.Colour.blue())
                                    hit_embed.set_image(url="https://cdn.discordapp.com/attachments/827500709909626920/827500757614985236/5d27099922e5fa89a861563885703ace.gif")
                                if monster_new > 30:
                                    MONSTER_HP = 60
                                    hit_embed = discord.Embed(title=f"Monster has {remain}HP left and you dealt {hit} damage", colour=discord.Colour.blue())
                                    hit_embed.set_image(url="https://cdn.discordapp.com/attachments/827500709909626920/827500757614985236/5d27099922e5fa89a861563885703ace.gif")
                                await asyncio.sleep(1)
                                await msg.edit(embed=hit_embed)
                                await msg.remove_reaction(emoji1, ctx.author)
                                
                                
                            #agility hits      
                            elif 5 <= hit_chance < 10:
                                hit1 = random.choice([int(hit_dmg/3), int(hit_dmg/2), hit_dmg])
                                remain = remain - hit1
                                if remain < 0:
                                    remain = 0
                                if monster_new <= 5:
                                    hit_embed = discord.Embed(title=f"Monster has {remain}HP left and you dealt {hit1} damage", colour=discord.Colour.blue())
                                    hit_embed.set_image(url="https://cdn.discordapp.com/attachments/798913238229188608/826442762936516618/2231125f94e8f1a32241b16ba2d68930.gif")
                                if 5 < monster_new < 10:
                                    MONSTER_HP = 20
                                    hit_embed = discord.Embed(title=f"Monster has {remain}HP left and you dealt {hit1} damage", colour=discord.Colour.blue())
                                    hit_embed.set_image(url="https://cdn.discordapp.com/attachments/827500709909626920/827500757317451776/662480907cfb2e26aec3f27cd419869a.gif")
                                if 10 <= monster_new <= 20:
                                    MONSTER_HP = 30
                                    hit_embed = discord.Embed(title=f"Monster has {remain}HP left and you dealt {hit1} damage", colour=discord.Colour.blue())
                                    hit_embed.set_image(url="https://cdn.discordapp.com/attachments/827500709909626920/827500757317451776/662480907cfb2e26aec3f27cd419869a.gif")
                                if 20 < monster_new <= 30:
                                    MONSTER_HP = 45
                                    hit_embed = discord.Embed(title=f"Monster has {remain}HP left and you dealt {hit1} damage", colour=discord.Colour.blue())
                                    hit_embed.set_image(url="https://cdn.discordapp.com/attachments/827500709909626920/827500757614985236/5d27099922e5fa89a861563885703ace.gif")
                                if monster_new > 30:
                                    MONSTER_HP = 60
                                    hit_embed = discord.Embed(title=f"Monster has {remain}HP left and you dealt {hit1} damage", colour=discord.Colour.blue())
                                    hit_embed.set_image(url="https://cdn.discordapp.com/attachments/827500709909626920/827500757614985236/5d27099922e5fa89a861563885703ace.gif")
                                await asyncio.sleep(1)
                                await msg.edit(embed=hit_embed)
                                await msg.remove_reaction(emoji1, ctx.author)
                                
                                
                            #agility hits    
                            elif 10<= hit_chance <=15:
                                hit2 = random.choice([int(hit_dmg/2), hit_dmg])
                                remain = remain - hit2
                                if remain < 0:
                                    remain = 0
                                if monster_new <= 5:
                                    hit_embed = discord.Embed(title=f"Monster has {remain}HP left and you dealt {hit2} damage", colour=discord.Colour.blue())
                                    hit_embed.set_image(url="https://cdn.discordapp.com/attachments/798913238229188608/826442762936516618/2231125f94e8f1a32241b16ba2d68930.gif")
                                if 5 < monster_new < 10:
                                    MONSTER_HP = 20
                                    hit_embed = discord.Embed(title=f"Monster has {remain}HP left and you dealt {hit2} damage", colour=discord.Colour.blue())
                                    hit_embed.set_image(url="https://cdn.discordapp.com/attachments/827500709909626920/827500757317451776/662480907cfb2e26aec3f27cd419869a.gif")
                                if 10 <= monster_new <= 20:
                                    MONSTER_HP = 30
                                    hit_embed = discord.Embed(title=f"Monster has {remain}HP left and you dealt {hit2} damage", colour=discord.Colour.blue())
                                    hit_embed.set_image(url="https://cdn.discordapp.com/attachments/827500709909626920/827500757317451776/662480907cfb2e26aec3f27cd419869a.gif")
                                if 20 < monster_new <= 30:
                                    MONSTER_HP = 45
                                    hit_embed = discord.Embed(title=f"Monster has {remain}HP left and you dealt {hit2} damage", colour=discord.Colour.blue())
                                    hit_embed.set_image(url="https://cdn.discordapp.com/attachments/827500709909626920/827500757614985236/5d27099922e5fa89a861563885703ace.gif")
                                if monster_new > 30:
                                    MONSTER_HP = 60
                                    hit_embed = discord.Embed(title=f"Monster has {remain}HP left and you dealt {hit2} damage", colour=discord.Colour.blue())
                                    hit_embed.set_image(url="https://cdn.discordapp.com/attachments/827500709909626920/827500757614985236/5d27099922e5fa89a861563885703ace.gif")
                                await asyncio.sleep(1)
                                await msg.edit(embed=hit_embed)
                                await msg.remove_reaction(emoji1, ctx.author)
                                
                                                        
                    except asyncio.TimeoutError:
                        self.hunt.reset_cooldown(ctx)
                        await msg.delete()
                        emb = discord.Embed(title="Oops, Seems like you forgot to actually attack this time", colour=discord.Colour.blue())
                        await ctx.send(embed=emb)
                if remain <= 0:
                    if 0 <= itemdrop <= 70: 
                        if c.execute(f"SELECT * FROM Inventory WHERE User_ID = '{ctx.author.id}' AND itemid = 5").fetchone():
                            c.execute(f"UPDATE Inventory SET itemcount = itemcount + 1 WHERE User_ID = '{ctx.author.id}' AND itemid = 5")
                        else:
                            c.execute(f"INSERT INTO Inventory VALUES ('{ctx.author.id}', '5', '1', '0')")
                    if 70 < itemdrop <= 80:
                        if c.execute(f"SELECT * FROM Inventory WHERE User_ID = '{ctx.author.id}' AND itemid = 6").fetchone():
                            
                            c.execute(f"UPDATE Inventory SET itemcount = itemcount + 1 WHERE User_ID = '{ctx.author.id}' AND itemid = 6")
                        else:
                            c.execute(f"INSERT INTO Inventory VALUES ('{ctx.author.id}', '6', '1', '0')")
                    if 80 < itemdrop <= 90:
                        if c.execute(f"SELECT * FROM Inventory WHERE User_ID = '{ctx.author.id}' AND itemid = 7").fetchone():
                            
                            c.execute(f"UPDATE Inventory SET itemcount = itemcount + 1 WHERE User_ID = '{ctx.author.id}' AND itemid = 7")
                        else:
            
                            c.execute(f"INSERT INTO Inventory VALUES ('{ctx.author.id}', '7', '1', '0')")
                    if 90 < itemdrop <= 100:
                        if c.execute(f"SELECT * FROM Inventory WHERE User_ID = '{ctx.author.id}' AND itemid = 8").fetchone():
                            
                            c.execute(f"UPDATE Inventory SET itemcount = itemcount + 1 WHERE User_ID = '{ctx.author.id}' AND itemid = 8")
                        else:
                
                            c.execute(f"INSERT INTO Inventory VALUES ('{ctx.author.id}', '8', '1', '0')")
                    c.execute(f"UPDATE Exp SET Exp = Exp + {str(exp_gain)} WHERE User_ID = '{ctx.author.id}'")
                    c.execute(f"UPDATE Exp SET balance = balance + {bal_gain} WHERE User_ID = '{ctx.author.id}'")
                    conn1.commit()
                    
                    c.execute(f"SELECT User_ID, Exp, Level FROM Exp WHERE User_ID = '{ctx.author.id}'")
                    result = c.fetchone()
                    exp = int(result[1])
                    lvl = int(result[2])
                    req_exp = math.floor(5 * (lvl ** 2) / 2)
                    
                    
                    if req_exp <= exp:
                        c.execute(f"UPDATE Exp SET Exp = Exp - {str(req_exp)} WHERE User_ID = '{ctx.author.id}'")
                        c.execute(f"UPDATE Exp SET Level = Level + 1 WHERE User_ID = '{ctx.author.id}'")
                        c.execute(f"UPDATE Stats SET Point = Point + 2 WHERE User_ID = '{ctx.author.id}'")
                        conn1.commit()
                        await msg.clear_reaction(emoji1)
                        await asyncio.sleep(2)
                        await msg.edit(embed=lvl_embed)
                    else:
                        
                        await msg.clear_reaction(emoji1)
                        await asyncio.sleep(2)
                        await msg.edit(embed=new_embed)
                    
                    conn1.close()
                
        else:
            self.hunt.reset_cooldown(ctx)
            await ctx.send("You don't have a character yet please type $start to create one")
            
    @hunt.error
    async def hunt_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):

            em = discord.Embed(title=f"Slow it down bro!",description=f"Try again in {error.retry_after:.2f}s.", colour=discord.Colour.blue())
            await ctx.send(embed=em)

    @commands.command()
    async def stats(self, ctx):
        if c.execute(f"SELECT 1 FROM Exp WHERE User_ID='{ctx.author.id}'").fetchone():
            c.execute(f"SELECT User_ID, Exp, Level, balance FROM Exp WHERE User_ID = '{ctx.author.id}'")
            results = c.fetchone()
            exp = int(results[1])
            lvl = int(results[2])
            bal = results[3]
            req_exp = math.floor(5 * (lvl ** 2) / 2)
            c.execute(f"SELECT User_ID, Str, Agi, Int, Point FROM Stats WHERE User_ID = '{ctx.author.id}'")
            res = c.fetchone()
            stren = int(res[1])
            agi = int(res[2])
            intel = int(res[3])
            point = int(res[4])
            
            if c.execute(f"SELECT 1 FROM Jobs WHERE User_ID = '{ctx.author.id}'").fetchone():
                c.execute(f"SELECT User_ID, fish_lvl, mine_lvl, craft_lvl FROM Jobs WHERE User_ID = '{ctx.author.id}'")
                jobs = c.fetchone()
                fish = int(jobs[1])
                mine = int(jobs[2])
                craft = int(jobs[3])    
                embed = discord.Embed(title=f"{ctx.author.name}'s Stats", colour=discord.Colour.blue())
                embed.add_field(name="Player Name", value=ctx.author.name, inline=False)
                embed.add_field(name="Experience / Required Experience", value=f"{exp} / {req_exp}", inline=True)
                embed.add_field(name="Balance", value=bal, inline=False)
                embed.add_field(name="Level", value=lvl, inline=False)
                embed.add_field(name="Mining Level", value=mine, inline=True)
                embed.add_field(name="Fishing Level", value=fish, inline=True)
                embed.add_field(name="Crafting Level", value=craft, inline=True)
                embed.add_field(name="Skill Points", value=point, inline=False)
                embed.add_field(name="Strength", value=stren, inline=True)
                embed.add_field(name="Agility", value=agi, inline=True)
                embed.add_field(name="Intelligence", value=intel, inline=True)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title=f"{ctx.author.name}'s Stats", colour=discord.Colour.blue())
                embed.add_field(name="Player Name", value=ctx.author.name, inline=False)
                embed.add_field(name="Experience / Required Experience", value=f"{exp} / {req_exp}", inline=True)
                embed.add_field(name="Balance", value=bal, inline=False)
                embed.add_field(name="Level", value=lvl, inline=False)
                embed.add_field(name="Skill Points", value=point, inline=False)
                embed.add_field(name="Strength", value=stren, inline=True)
                embed.add_field(name="Agility", value=agi, inline=True)
                embed.add_field(name="Intelligence", value=intel, inline=True)
                embed.set_footer(text="$job to be able to do jobs")
                await ctx.send(embed=embed)
        else:
            await ctx.send("You don't have a character yet please create one using $start")

    @commands.group()
    async def upgrade(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title="You need to pick what to upgrade", colour=discord.Colour.blue())
            await ctx.send(embed=embed)

    @upgrade.command(name="str")
    async def _strength(self, ctx, amount = None):
        conn1 = sqlite3.connect("exp.db")
        c = conn1.cursor()
        try:
            amount = int(amount)
        except:
            amount = None
        if amount is None:
            await ctx.send("Please specify an amount")
        elif amount < 0:
            await ctx.send("Please enter a correct number")
        else:
            c.execute(f"SELECT User_ID, Str, Agi, Int, Point FROM Stats WHERE User_ID = '{ctx.author.id}'")
            pts = c.fetchone()
            point = int(pts[4])
            if amount > point:
                await ctx.send("You dont have enough points to do that")
            else:
                c.execute(f"UPDATE Stats SET Str = Str + {str(amount)} WHERE User_ID = '{ctx.author.id}'")
                c.execute(f"UPDATE Stats SET Point = Point - {str(amount)} WHERE User_ID = '{ctx.author.id}'")
                c.execute(f"SELECT User_ID, Str, Agi, Int, Point FROM Stats WHERE User_ID = '{ctx.author.id}'")
                new = c.fetchone()
                new_str = int(new[1])
                new_pts = int(new[4])
                new_emb = discord.Embed(title=f"Congrats you added {str(amount)} points to your Strength now it is {new_str}, You got {new_pts} skill points left", colour=discord.Colour.blue())
                await ctx.send(embed=new_emb)
                conn1.commit()
                conn1.close()
    
    @upgrade.command(name="int")
    async def _intelligence(self, ctx, amount = None):
        conn1 = sqlite3.connect("exp.db")
        c = conn1.cursor()
        try:
            amount = int(amount)
        except:
            amount = None
        if amount is None:
            m = await ctx.send("Please specify an amount")
            await asyncio.sleep(10)
            await m.delete()
        elif amount < 0:
            await ctx.send("Please enter a correct number")
        else:
            c.execute(f"SELECT User_ID, Str, Agi, Int, Point FROM Stats WHERE User_ID = '{ctx.author.id}'")
            pts = c.fetchone()
            point = int(pts[4])
            if amount > point:
                msg = await ctx.send("You dont have enough points to do that")
                await asyncio.sleep(10)
                await msg.delete()
            else:
                c.execute(f"UPDATE Stats SET Int = Int + {str(amount)} WHERE User_ID = '{ctx.author.id}'")
                c.execute(f"UPDATE Stats SET Point = Point - {str(amount)} WHERE User_ID = '{ctx.author.id}'")
                c.execute(f"SELECT User_ID, Str, Agi, Int, Point FROM Stats WHERE User_ID = '{ctx.author.id}'")
                new = c.fetchone()
                new_intel = int(new[3])
                new_pts = int(new[4])
                new_emb = discord.Embed(title=f"Congrats you added {str(amount)} points to your Intelligence now it is {new_intel}, You got {new_pts} skill points left", colour=discord.Colour.blue())
                await ctx.send(embed=new_emb)
                conn1.commit()
                conn1.close()

    @upgrade.command(name="agi")
    async def _agility(self, ctx, amount = None):
        conn1 = sqlite3.connect("exp.db")
        c = conn1.cursor()
        try:
            amount = int(amount)
        except:
            amount = None
        if amount is None:
            m = await ctx.send("Please specify an amount")
            await asyncio.sleep(10)
            await m.delete()
        elif amount < 0:
            await ctx.send("Please enter a correct number")
        else:
            c.execute(f"SELECT User_ID, Str, Agi, Int, Point FROM Stats WHERE User_ID = '{ctx.author.id}'")
            pts = c.fetchone()
            point = int(pts[4])
            if amount > point:
                msg = await ctx.send("You dont have enough points to do that")
                await asyncio.sleep(10)
                await msg.delete()
            else:
                c.execute(f"UPDATE Stats SET Agi = Agi + {str(amount)} WHERE User_ID = '{ctx.author.id}'")
                c.execute(f"UPDATE Stats SET Point = Point - {str(amount)} WHERE User_ID = '{ctx.author.id}'")
                c.execute(f"SELECT User_ID, Str, Agi, Int, Point FROM Stats WHERE User_ID = '{ctx.author.id}'")
                new = c.fetchone()
                new_intel = int(new[2])
                new_pts = int(new[4])
                new_emb = discord.Embed(title=f"Congrats you added {str(amount)} points to your Agility now it is {new_intel}, You got {new_pts} skill points left", colour=discord.Colour.blue())
                await ctx.send(embed=new_emb)
                conn1.commit()
                conn1.close()
    
    @commands.command()
    @commands.cooldown(1, 7200, commands.BucketType.user)
    async def reset(self, ctx):
        conn1 = sqlite3.connect("exp.db")
        c = conn1.cursor()
        if c.execute(f"SELECT 1 FROM Exp WHERE User_ID='{ctx.author.id}'").fetchone():
            c.execute(f"SELECT User_ID, Exp, Level FROM Exp WHERE User_ID = '{ctx.author.id}'")
            lvl = c.fetchone()
            count = int(lvl[2])
            first_embed = discord.Embed(title="Are you sure you want to reset your stats?", colour=discord.Colour.blue())
            second_embed = discord.Embed(title="Your stats are reseted", colour=discord.Colour.blue())
            third_embed = discord.Embed(title="Your stats remain the same", colour=discord.Colour.blue())
            msg = await ctx.send(embed=first_embed)
            emoji1 = self.client.get_emoji(827281392479764590)
            emoji2 = self.client.get_emoji(827280864265371658)
            await msg.add_reaction(emoji1)
            await msg.add_reaction(emoji2)
            try: 
                reaction, user = await self.client.wait_for('reaction_add', timeout=20.0, check=reaction_check(author=ctx.author))
                if reaction.emoji == emoji1:
                    c.execute(f"UPDATE Stats SET Agi = 1 WHERE User_ID = '{ctx.author.id}'")
                    c.execute(f"UPDATE Stats SET Str = 1 WHERE User_ID = '{ctx.author.id}'")
                    c.execute(f"UPDATE Stats SET Int = 1 WHERE User_ID = '{ctx.author.id}'")
                    c.execute(f"UPDATE Stats SET Point = {str((count-1)*2)} WHERE User_ID = '{ctx.author.id}'")
                    conn1.commit()
                    conn1.close()
                    await msg.clear_reaction(emoji1)
                    await msg.clear_reaction(emoji2)
                    await msg.edit(embed=second_embed)
                if reaction.emoji == emoji2:
                    await msg.clear_reaction(emoji1)
                    await msg.clear_reaction(emoji2)
                    await msg.edit(embed=third_embed)
            except asyncio.TimeoutError:
                await msg.delete()
                self.reset.reset_cooldown(ctx)
                emb = discord.Embed(title="Oops, Seems like you forgot to actually attack this time", colour=discord.Colour.blue())
                await ctx.send(embed=emb)    
        else:
            self.reset.reset_cooldown(ctx)
            await ctx.send("Please create a character by typing $start first")

    @reset.error
    async def reset_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):

            msg = 'Try again in {:}'.format(str(datetime.timedelta(seconds=int(error.retry_after))))
            await ctx.send(msg)
        else:
            raise error

    @commands.command()
    async def job(self, ctx):
        if ctx.invoked_subcommand is None:
            if c.execute(f"SELECT 1 FROM Jobs WHERE User_ID = '{ctx.author.id}'").fetchone():
                c.execute(f"SELECT User_ID, mine_lvl, mine_exp, fish_lvl, fish_exp, craft_lvl, craft_exp FROM Jobs WHERE User_ID = '{ctx.author.id}'")
                results = c.fetchone()
                minelvl = int(results[1])
                mineexp = int(results[2])
                fishlvl = int(results[3])
                fishexp = int(results[4])
                craftlvl = int(results[5])
                craftexp = int(results[6])
                mine_req = 10 + int(3 * minelvl**3)
                fish_req = 10 + int(3 * fishlvl**3)
                craft_req = 10 + int(3 * craftlvl**3)
                embed = discord.Embed(title="Job Stats", colour=discord.Colour.blue())
                embed.add_field(name="Player Name", value=ctx.author.name, inline=False)
                embed.add_field(name="Mining Level", value=minelvl, inline=True)
                embed.add_field(name="Mining Exp / Required Exp", value=f"{mineexp} / {mine_req}", inline=False)
                embed.add_field(name="Fishing Level", value=fishlvl, inline=True)
                embed.add_field(name="Fishing Exp / Required Exp", value=f"{fishexp} / {fish_req}", inline=False)
                embed.add_field(name="Crafting Level", value=craftlvl, inline=True)
                embed.add_field(name="Crafting Exp / Required Exp", value=f"{craftexp} / {craft_req}", inline=False)
                await ctx.send(embed=embed)
            else:
                c.execute(f"INSERT INTO Jobs VALUES ('{ctx.author.id}', '1', '0', '1', '0', '1', '0')")
                conn1.commit()
                await ctx.send("Now you can do the jobs")
        
    @commands.command()
    @commands.cooldown(1, 180, commands.BucketType.user)
    async def mine(self, ctx):
        conn1 = sqlite3.connect("exp.db")
        c = conn1.cursor()
        if c.execute(f"SELECT 1 FROM Jobs WHERE User_ID = '{ctx.author.id}'").fetchone():
            c.execute(f"SELECT User_ID, mine_lvl, mine_exp FROM Jobs WHERE User_ID = '{ctx.author.id}'")
            mine_res = c.fetchone()
            minelvl = int(mine_res[1])
            mineexp = int(mine_res[2])
            pickemote = self.client.get_emoji(827525117458251796)
            c.execute(f"SELECT User_ID, Str FROM Stats WHERE User_ID = '{ctx.author.id}'")
            stren_res = c.fetchone()
            stren = int(stren_res[1])
            mining_exp = 5 + int(stren/3)
            norm_exp = 10 + int(minelvl/2)
            mine_req = 10 + int(3 * minelvl**3)
            chance = random.randint(0,100)
            if 0 <= chance <= 50:
                oreemote = self.client.get_emoji(828325308956540960)
                second_embed = discord.Embed(title=f"Congrats you mined a bronze {oreemote} successfully and gained {mining_exp} mining exp and {norm_exp} exp", colour= discord.Colour.blue())           
                        
            if 50 < chance <= 80:
                oreemote = self.client.get_emoji(828325493337489468)
                second_embed = discord.Embed(title=f"Congrats you mined an iron {oreemote} successfully and gained {mining_exp} mining exp and {norm_exp} exp", colour= discord.Colour.blue()) 
                        
            if 80 < chance <= 100:
                oreemote = self.client.get_emoji(828325340430336030)
                second_embed = discord.Embed(title=f"Congrats you mined a gold {oreemote} successfully and gained {mining_exp} mining exp and {norm_exp} exp", colour= discord.Colour.blue())
            first_embed = discord.Embed(title="React to mine and gain exp", colour=discord.Colour.blue())
            
            msg = await ctx.send(embed=first_embed)
            await msg.add_reaction(pickemote)
            check = reaction_check(message=msg, author=ctx.author, emoji=(pickemote))
            lvl_embed = discord.Embed(title="You leveled up and gained 2 skill points", colour=discord.Colour.blue())
            lvl_embed.set_image(url="https://cdn.discordapp.com/attachments/798913238229188608/826833342694686830/ezgif.com-gif-maker_19.gif")
            try: 
                reaction, user = await self.client.wait_for('reaction_add', timeout=20.0, check=check)
                if reaction.emoji == pickemote:
                    if 0 <= chance <= 50:
                        if c.execute(f"SELECT * FROM Inventory WHERE User_ID = '{ctx.author.id}' AND itemid = 2").fetchone():
                            c.execute(f"UPDATE Inventory SET itemcount = itemcount + 1 WHERE User_ID = '{ctx.author.id}' AND itemid = 2")
                        else:
                            c.execute(f"INSERT INTO Inventory VALUES ('{ctx.author.id}', '2', '1', '0')")
                        
                    if 50 < chance <= 80:
                        if c.execute(f"SELECT * FROM Inventory WHERE User_ID = '{ctx.author.id}' AND itemid = 3").fetchone():
                            c.execute(f"UPDATE Inventory SET itemcount = itemcount + 1 WHERE User_ID = '{ctx.author.id}' AND itemid = 3")
                        else:
                            c.execute(f"INSERT INTO Inventory VALUES ('{ctx.author.id}', '3', '1', '0')")
                    if 80 < chance <= 100:
                        if c.execute(f"SELECT * FROM Inventory WHERE User_ID = '{ctx.author.id}' AND itemid = 4").fetchone():
                            c.execute(f"UPDATE Inventory SET itemcount = itemcount + 1 WHERE User_ID = '{ctx.author.id}' AND itemid = 4")
                        else:
                            c.execute(f"INSERT INTO Inventory VALUES ('{ctx.author.id}', '4', '1', '0')")
                    c.execute(f"UPDATE Jobs SET mine_exp = mine_exp + {str(mining_exp)} WHERE User_ID = '{ctx.author.id}'")
                    c.execute(f"UPDATE Exp SET Exp = Exp + {str(norm_exp)} WHERE User_ID = '{ctx.author.id}'")
                    conn1.commit()
                    c.execute(f"SELECT User_ID, Exp, Level FROM Exp WHERE User_ID = '{ctx.author.id}'")
                    result = c.fetchone()
                    exp = int(result[1])
                    lvl = int(result[2])
                    req_exp = math.floor(5 * (lvl ** 2) / 2)
                    c.execute(f"SELECT User_ID, mine_lvl, mine_exp FROM Jobs WHERE User_ID = '{ctx.author.id}'")
                    mineresult = c.fetchone()
                    mineexpup = int(mineresult[2])
                    if mineexpup >= mine_req and req_exp <= exp:
                        c.execute(f"UPDATE Jobs SET mine_lvl = mine_lvl + 1 WHERE User_ID = '{ctx.author.id}'")
                        c.execute(f"UPDATE Exp SET Exp = Exp - {str(req_exp)} WHERE User_ID = '{ctx.author.id}'")
                        c.execute(f"UPDATE Exp SET Level = Level + 1 WHERE User_ID = '{ctx.author.id}'")
                        c.execute(f"UPDATE Stats SET Point = Point + 2 WHERE User_ID = '{ctx.author.id}'")
                        conn1.commit()
                        await msg.clear_reaction(pickemote)
                        await asyncio.sleep(2)
                        await msg.edit(embed=lvl_embed)
                    elif mineexpup >= mine_req:
                        c.execute(f"UPDATE Jobs SET mine_lvl = mine_lvl + 1 WHERE User_ID = '{ctx.author.id}'")
                        conn1.commit()
                        c.execute(f"SELECT User_ID, mine_lvl, mine_exp FROM Jobs WHERE User_ID = '{ctx.author.id}'")
                        resultmine = c.fetchone()
                        newmine_lvl = int(resultmine[1])
                        third_embed = discord.Embed(title=f"Congrats your mining level increased to level {newmine_lvl}", colour=discord.Colour.blue())
                        await msg.clear_reaction(pickemote)
                        await msg.edit(embed=third_embed)
                    elif req_exp <= exp:
                        c.execute(f"UPDATE Exp SET Exp = Exp - {str(req_exp)} WHERE User_ID = '{ctx.author.id}'")
                        c.execute(f"UPDATE Exp SET Level = Level + 1 WHERE User_ID = '{ctx.author.id}'")
                        c.execute(f"UPDATE Stats SET Point = Point + 2 WHERE User_ID = '{ctx.author.id}'")
                        conn1.commit()
                        await msg.clear_reaction(pickemote)
                        await asyncio.sleep(2)
                        await msg.edit(embed=lvl_embed)
                    else:
                        await msg.clear_reaction(pickemote)
                        await msg.edit(embed=second_embed)
            except asyncio.TimeoutError:
                self.mine.reset_cooldown(ctx)
                await msg.delete()
                emb = discord.Embed(title="Oops, Seems like you forgot to actually react this time", colour=discord.Colour.blue())
                await ctx.send(embed=emb) 
        else:
            self.mine.reset_cooldown(ctx)
            await ctx.send("Please do $job first to be able to use the command")
    @mine.error
    async def mine_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):

            em = discord.Embed(title=f"Slow it down bro!",description=f"Try again in {error.retry_after:.2f}s.", colour=discord.Colour.blue())
            await ctx.send(embed=em)
    
    @commands.command()
    @commands.cooldown(1, 180, commands.BucketType.user)
    async def fish(self, ctx):
        conn1 = sqlite3.connect("exp.db")
        c = conn1.cursor()
        if c.execute(f"SELECT 1 FROM Jobs WHERE User_ID = '{ctx.author.id}'").fetchone():
            c.execute(f"SELECT User_ID, fish_lvl, fish_exp FROM Jobs WHERE User_ID = '{ctx.author.id}'")
            fish_res = c.fetchone()
            fishlvl = int(fish_res[1])
            pickemote = self.client.get_emoji(827563500616024074)
            fishemote = self.client.get_emoji(828326028833062952)
            catchemote = self.client.get_emoji(830534160036790382)
            c.execute(f"SELECT User_ID, Agi FROM Stats WHERE User_ID = '{ctx.author.id}'")
            agi_res = c.fetchone()
            agi = int(agi_res[1])
            mining_exp = 10 + int(agi/3)
            norm_exp = 25 + int(fishlvl/2)
            mine_req = 10 + int(3 * fishlvl**3)
            first_embed = discord.Embed(title="React to fish and gain exp", colour=discord.Colour.blue())
            second_embed = discord.Embed(title=f"Congrats you caught a fish {fishemote} successfully and gained {mining_exp} fishing exp and {norm_exp} exp", colour= discord.Colour.blue())
            lost_embed = discord.Embed(title=f"Seems like your fish got away try again later", colour=discord.Colour.blue())
            msg = await ctx.send(embed=first_embed)
            await msg.add_reaction(pickemote)
            await msg.add_reaction(catchemote)
            catchchance = random.randint(0, 1)
            check = reaction_check(message=msg, author=ctx.author, emoji=(pickemote, catchemote))
            lvl_embed = discord.Embed(title="You leveled up and gained 2 skill points", colour=discord.Colour.blue())
            lvl_embed.set_image(url="https://cdn.discordapp.com/attachments/798913238229188608/826833342694686830/ezgif.com-gif-maker_19.gif")
            try: 
                reaction, user = await self.client.wait_for('reaction_add', timeout=20.0, check=check)
                if catchchance == 0:
                    if reaction.emoji == pickemote:
                        if c.execute(f"SELECT * FROM Inventory WHERE User_ID = '{ctx.author.id}' AND itemid = 1").fetchone():
                            c.execute(f"UPDATE Inventory SET itemcount = itemcount + 1 WHERE itemid = 1")
                        else:
                            c.execute(f"INSERT INTO Inventory VALUES ('{ctx.author.id}', '1', '1', '0')")
                        c.execute(f"UPDATE Jobs SET fish_exp = fish_exp + {str(mining_exp)} WHERE User_ID = '{ctx.author.id}'")
                        c.execute(f"UPDATE Exp SET Exp = Exp + {str(norm_exp)} WHERE User_ID = '{ctx.author.id}'")
                        conn1.commit()
                        c.execute(f"SELECT User_ID, Exp, Level FROM Exp WHERE User_ID = '{ctx.author.id}'")
                        result = c.fetchone()
                        exp = int(result[1])
                        lvl = int(result[2])
                        req_exp = math.floor(5 * (lvl ** 2) / 2)
                        c.execute(f"SELECT User_ID, fish_lvl, fish_exp FROM Jobs WHERE User_ID = '{ctx.author.id}'")
                        mineresult = c.fetchone()
                        mineexpup = int(mineresult[2])
                        if mineexpup >= mine_req:
                            c.execute(f"UPDATE Jobs SET fish_lvl = fish_lvl + 1 WHERE User_ID = '{ctx.author.id}'")
                            conn1.commit()
                            c.execute(f"SELECT User_ID, fish_lvl, fish_exp FROM Jobs WHERE User_ID = '{ctx.author.id}'")
                            resultmine = c.fetchone()
                            newmine_lvl = int(resultmine[1])
                            third_embed = discord.Embed(title=f"Congrats your fishing level increased to level {newmine_lvl}", colour=discord.Colour.blue())
                            await msg.clear_reaction(pickemote)
                            await msg.clear_reaction(catchemote)
                            await msg.edit(embed=third_embed)
                        elif req_exp <= exp:
                            c.execute(f"UPDATE Exp SET Exp = 0 WHERE User_ID = '{ctx.author.id}'")
                            c.execute(f"UPDATE Exp SET Level = Level + 1 WHERE User_ID = '{ctx.author.id}'")
                            c.execute(f"UPDATE Stats SET Point = Point + 2 WHERE User_ID = '{ctx.author.id}'")
                            conn1.commit()
                            await asyncio.sleep(2)
                            await msg.clear_reaction(pickemote)
                            await msg.clear_reaction(catchemote)
                            await msg.edit(embed=lvl_embed)
                        else:
                            await msg.clear_reaction(pickemote)
                            await msg.clear_reaction(catchemote)
                            await msg.edit(embed=second_embed)
                    if reaction.emoji == catchemote:
                        await msg.clear_reaction(pickemote)
                        await msg.clear_reaction(catchemote)
                        await msg.edit(embed=lost_embed)
                if catchchance == 1:
                    if reaction.emoji == catchemote:
                        if c.execute(f"SELECT * FROM Inventory WHERE User_ID = '{ctx.author.id}' AND itemid = 1").fetchone():
                            c.execute(f"UPDATE Inventory SET itemcount = itemcount + 1 WHERE itemid = 1")
                        else:
                            c.execute(f"INSERT INTO Inventory VALUES ('{ctx.author.id}', '1', '1', '0')")
                        c.execute(f"UPDATE Jobs SET fish_exp = fish_exp + {str(mining_exp)} WHERE User_ID = '{ctx.author.id}'")
                        c.execute(f"UPDATE Exp SET Exp = Exp + {str(norm_exp)} WHERE User_ID = '{ctx.author.id}'")
                        conn1.commit()
                        c.execute(f"SELECT User_ID, Exp, Level FROM Exp WHERE User_ID = '{ctx.author.id}'")
                        result = c.fetchone()
                        exp = int(result[1])
                        lvl = int(result[2])
                        req_exp = math.floor(5 * (lvl ** 2) / 2)
                        c.execute(f"SELECT User_ID, fish_lvl, fish_exp FROM Jobs WHERE User_ID = '{ctx.author.id}'")
                        mineresult = c.fetchone()
                        mineexpup = int(mineresult[2])
                        if mineexpup >= mine_req:
                            c.execute(f"UPDATE Jobs SET fish_lvl = fish_lvl + 1 WHERE User_ID = '{ctx.author.id}'")
                            conn1.commit()
                            c.execute(f"SELECT User_ID, fish_lvl, fish_exp FROM Jobs WHERE User_ID = '{ctx.author.id}'")
                            resultmine = c.fetchone()
                            newmine_lvl = int(resultmine[1])
                            third_embed = discord.Embed(title=f"Congrats your fishing level increased to level {newmine_lvl}", colour=discord.Colour.blue())
                            await msg.clear_reaction(pickemote)
                            await msg.clear_reaction(catchemote)
                            await msg.edit(embed=third_embed)
                        elif req_exp <= exp:
                            c.execute(f"UPDATE Exp SET Exp = 0 WHERE User_ID = '{ctx.author.id}'")
                            c.execute(f"UPDATE Exp SET Level = Level + 1 WHERE User_ID = '{ctx.author.id}'")
                            c.execute(f"UPDATE Stats SET Point = Point + 2 WHERE User_ID = '{ctx.author.id}'")
                            conn1.commit()
                            await asyncio.sleep(2)
                            await msg.clear_reaction(pickemote)
                            await msg.clear_reaction(catchemote)
                            await msg.edit(embed=lvl_embed)
                        else:
                            await msg.clear_reaction(pickemote)
                            await msg.clear_reaction(catchemote)
                            await msg.edit(embed=second_embed)
                    if reaction.emoji == pickemote:
                        await msg.clear_reaction(pickemote)
                        await msg.clear_reaction(catchemote)
                        await msg.edit(embed=lost_embed)
            except asyncio.TimeoutError:
                self.fish.reset_cooldown(ctx)
                await msg.delete()
                emb = discord.Embed(title="Oops, Seems like you forgot to actually react this time", colour=discord.Colour.blue())
                await ctx.send(embed=emb)
        else:
            self.fish.reset_cooldown(ctx)
            await ctx.send("Please do $job first to be able to use the command") 

    @fish.error
    async def fish_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):

            em = discord.Embed(title=f"Slow it down bro!",description=f"Try again in {error.retry_after:.2f}s.", colour=discord.Colour.blue())
            await ctx.send(embed=em)
    
    @commands.command()
    @commands.cooldown(1, 180, commands.BucketType.user)
    async def craft(self, ctx):
        conn1 = sqlite3.connect("exp.db")
        c = conn1.cursor()
        if c.execute(f"SELECT 1 FROM Jobs WHERE User_ID = '{ctx.author.id}'").fetchone():
            c.execute(f"SELECT User_ID, craft_lvl, craft_exp FROM Jobs WHERE User_ID = '{ctx.author.id}'")
            craft_res = c.fetchone()
            craftlvl = int(craft_res[1])
            craftexp = int(craft_res[2])
            pickemote = self.client.get_emoji(827563481942458462)
            c.execute(f"SELECT User_ID, Int FROM Stats WHERE User_ID = '{ctx.author.id}'")
            int_res = c.fetchone()
            intel = int(int_res[1])
            mining_exp = 5 + int(intel/3)
            norm_exp = 10 + int(craftlvl/2)
            mine_req = 10 + int(3 * craftlvl**3)
            first_embed = discord.Embed(title="React to craft and gain exp", colour=discord.Colour.blue())
            second_embed = discord.Embed(title=f"Congrats you did crafting successfully and gained {mining_exp} crafting exp and {norm_exp} exp", colour= discord.Colour.blue())
            msg = await ctx.send(embed=first_embed)
            await msg.add_reaction(pickemote)
            check = reaction_check(message=msg, author=ctx.author, emoji=(pickemote))
            lvl_embed = discord.Embed(title="You leveled up and gained 2 skill points", colour=discord.Colour.blue())
            lvl_embed.set_image(url="https://cdn.discordapp.com/attachments/798913238229188608/826833342694686830/ezgif.com-gif-maker_19.gif")
            try: 
                reaction, user = await self.client.wait_for('reaction_add', timeout=20.0, check=check)
                if reaction.emoji == pickemote:
                    c.execute(f"UPDATE Jobs SET craft_exp = craft_exp + {str(mining_exp)} WHERE User_ID = '{ctx.author.id}'")
                    c.execute(f"UPDATE Exp SET Exp = Exp + {str(norm_exp)} WHERE User_ID = '{ctx.author.id}'")
                    conn1.commit()
                    c.execute(f"SELECT User_ID, Exp, Level FROM Exp WHERE User_ID = '{ctx.author.id}'")
                    result = c.fetchone()
                    exp = int(result[1])
                    lvl = int(result[2])
                    req_exp = math.floor(5 * (lvl ** 2) / 2)
                    c.execute(f"SELECT User_ID, craft_lvl, craft_exp FROM Jobs WHERE User_ID = '{ctx.author.id}'")
                    mineresult = c.fetchone()
                    mineexpup = int(mineresult[2])
                    if mineexpup >= mine_req and req_exp <= exp:
                        c.execute(f"UPDATE Jobs SET craft_lvl = craft_lvl + 1 WHERE User_ID = '{ctx.author.id}'")
                        c.execute(f"UPDATE Exp SET Exp = Exp - {str(req_exp)} WHERE User_ID = '{ctx.author.id}'")
                        c.execute(f"UPDATE Exp SET Level = Level + 1 WHERE User_ID = '{ctx.author.id}'")
                        c.execute(f"UPDATE Stats SET Point = Point + 2 WHERE User_ID = '{ctx.author.id}'")
                        conn1.commit()
                        await asyncio.sleep(2)
                        await msg.clear_reaction(pickemote)
                        await msg.edit(embed=lvl_embed)
                    elif mineexpup >= mine_req:
                        c.execute(f"UPDATE Jobs SET craft_lvl = craft_lvl + 1 WHERE User_ID = '{ctx.author.id}'")
                        conn1.commit()
                        c.execute(f"SELECT User_ID, craft_lvl, craft_exp FROM Jobs WHERE User_ID = '{ctx.author.id}'")
                        resultmine = c.fetchone()
                        newmine_lvl = int(resultmine[1])
                        third_embed = discord.Embed(title=f"Congrats your crafting level increased to level {newmine_lvl}", colour=discord.Colour.blue())
                        await msg.clear_reaction(pickemote)
                        await msg.edit(embed=third_embed)
                    elif req_exp <= exp:
                        c.execute(f"UPDATE Exp SET Exp = Exp - {str(req_exp)} WHERE User_ID = '{ctx.author.id}'")
                        c.execute(f"UPDATE Exp SET Level = Level + 1 WHERE User_ID = '{ctx.author.id}'")
                        c.execute(f"UPDATE Stats SET Point = Point + 2 WHERE User_ID = '{ctx.author.id}'")
                        conn1.commit()
                        await asyncio.sleep(2)
                        await msg.clear_reaction(pickemote)
                        await msg.edit(embed=lvl_embed)
                    else:
                        await msg.clear_reaction(pickemote)
                        await msg.edit(embed=second_embed)
            except asyncio.TimeoutError:
                self.craft.reset_cooldown(ctx)
                await msg.delete()
                emb = discord.Embed(title="Oops, Seems like you forgot to actually react this time", colour=discord.Colour.blue())
                await ctx.send(embed=emb)
        else:
            self.craft.reset_cooldown(ctx)
            await ctx.send("Please do $job first to be able to use the command")
    @craft.error
    async def craft_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):

            em = discord.Embed(title=f"Slow it down bro!",description=f"Try again in {error.retry_after:.2f}s.", colour=discord.Colour.blue())
            await ctx.send(embed=em)

    @commands.command(aliases=['inv'])
    async def inventory(self, ctx):
        if c.execute(f"SELECT * FROM Inventory WHERE User_ID = {ctx.author.id}").fetchall():
            c.execute(f"""SELECT a.*, b.* 
                        FROM Inventory AS a
                        INNER JOIN Items
                        AS b ON a.itemid = b.itemid WHERE User_ID = '{ctx.author.id}'""")
            items = c.fetchall()
            names = []
            counts = []
            for item in items:
                names.append(item[5])
                counts.append(item[2])
                #names = f"{names}\n{str(item[2])}         {item[4]}"
            if len(names) == 0:
                embed = discord.Embed(title="Inventory", colour=discord.Colour.blue())
                embed.add_field(name=f"{ctx.author.name}'s Items" ,value="You got no items yet")
                await ctx.send(embed=embed)   
            if 0< len(names) <=1 :
                embed = discord.Embed(title="Inventory", colour=discord.Colour.blue())
                embed.add_field(name=names[0] ,value=counts[0], inline=False)
                await ctx.send(embed=embed)
            if 1 < len(names) <= 2:
                embed = discord.Embed(title="Inventory", colour=discord.Colour.blue())
                embed.add_field(name=names[0] ,value=counts[0], inline=False)        
                embed.add_field(name=names[1] ,value=counts[1], inline=False)
                await ctx.send(embed=embed)
            if 2 < len(names) <= 3:
                embed = discord.Embed(title="Inventory", colour=discord.Colour.blue())
                embed.add_field(name=names[0] ,value=counts[0], inline=False)        
                embed.add_field(name=names[1] ,value=counts[1], inline=False)
                embed.add_field(name=names[2] ,value=counts[2], inline=False)                
                await ctx.send(embed=embed)
            if 3 < len(names) <= 4:
                embed = discord.Embed(title="Inventory", colour=discord.Colour.blue())
                embed.add_field(name=names[0] ,value=counts[0], inline=False)        
                embed.add_field(name=names[1] ,value=counts[1], inline=False)
                embed.add_field(name=names[2] ,value=counts[2], inline=False)      
                embed.add_field(name=names[3] ,value=counts[3], inline=False)
                await ctx.send(embed=embed)
            if 4 < len(names) <= 5:
                embed = discord.Embed(title="Inventory", colour=discord.Colour.blue())
                embed.add_field(name=names[0] ,value=counts[0], inline=False)        
                embed.add_field(name=names[1] ,value=counts[1], inline=False)
                embed.add_field(name=names[2] ,value=counts[2], inline=False)      
                embed.add_field(name=names[3] ,value=counts[3], inline=False)
                embed.add_field(name=names[4] ,value=counts[4], inline=False)
                await ctx.send(embed=embed)
            if 5 < len(names) <= 6:
                embed = discord.Embed(title="Inventory", colour=discord.Colour.blue())
                embed.add_field(name=names[0] ,value=counts[0], inline=False)        
                embed.add_field(name=names[1] ,value=counts[1], inline=False)
                embed.add_field(name=names[2] ,value=counts[2], inline=False)      
                embed.add_field(name=names[3] ,value=counts[3], inline=False)
                embed.add_field(name=names[4] ,value=counts[4], inline=False)
                embed.add_field(name=names[5] ,value=counts[5], inline=False)
                await ctx.send(embed=embed)
            if 6 < len(names) <= 7:
                embed = discord.Embed(title="Inventory", colour=discord.Colour.blue())
                embed.add_field(name=names[0] ,value=counts[0], inline=False)        
                embed.add_field(name=names[1] ,value=counts[1], inline=False)
                embed.add_field(name=names[2] ,value=counts[2], inline=False)      
                embed.add_field(name=names[3] ,value=counts[3], inline=False)
                embed.add_field(name=names[4] ,value=counts[4], inline=False)
                embed.add_field(name=names[5] ,value=counts[5], inline=False)
                embed.add_field(name=names[6] ,value=counts[6], inline=False)
                await ctx.send(embed=embed)
            if 7 < len(names) <= 8:
                embed = discord.Embed(title="Inventory", colour=discord.Colour.blue())
                embed.add_field(name=names[0] ,value=counts[0], inline=False)        
                embed.add_field(name=names[1] ,value=counts[1], inline=False)
                embed.add_field(name=names[2] ,value=counts[2], inline=False)      
                embed.add_field(name=names[3] ,value=counts[3], inline=False)
                embed.add_field(name=names[4] ,value=counts[4], inline=False)
                embed.add_field(name=names[5] ,value=counts[5], inline=False)
                embed.add_field(name=names[6] ,value=counts[6], inline=False)
                embed.add_field(name=names[7] ,value=counts[7], inline=False)
                await ctx.send(embed=embed)
        else:
            await ctx.send("You dont have any items yet!")
    @commands.command()
    async def equip(self, ctx, message=None):
        if message == None:
                await ctx.send("Please tell me what you want to equip")
        else:
            if c.execute(f"SELECT * FROM Inventory WHERE User_ID = {ctx.author.id}").fetchall():
                if c.execute(f"SELECT * FROM Inventory WHERE User_ID = '{ctx.author.id}' AND equip = 1").fetchall():
                    c.execute(f"UPDATE Inventory SET equip = 0 WHERE User_ID = '{ctx.author.id}'")
                    conn1.commit()
                    await ctx.send("You unequipped your item!")
                
                else:

                    if message == "sword" or message == "Sword":
                        c.execute(f"SELECT * FROM Inventory WHERE User_ID = {ctx.author.id} AND itemid = 6")
                        count = c.fetchone()
                        checkitem = count[2]
                        c.execute(f"SELECT User_ID, Str FROM Stats WHERE User_ID = '{ctx.author.id}'")
                        strcheck = c.fetchone()
                        checkstren = int(strcheck[1])
                        if checkstren >= 10:

                            if checkitem >= 1:
                                if c.execute(f"SELECT * FROM Inventory WHERE User_ID = {ctx.author.id} AND itemid = 6").fetchone():
                                    c.execute(f"UPDATE Inventory SET equip = 1 WHERE User_ID= '{ctx.author.id}' and itemid = 6")
                                    conn1.commit()
                                    await ctx.send("You succesfully equipped a Sword")
                                else:
                                    await ctx.send("You dont have a sword")
                            else:
                                await ctx.send("You dont have a sword")
                        else:
                            await ctx.send("Your stats are too low for the Sword you need at least 10 Strength")
                    elif message == "bow" or message == "Bow":
                        c.execute(f"SELECT * FROM Inventory WHERE User_ID = {ctx.author.id} AND itemid = 7")
                        count = c.fetchone()
                        checkitem = count[2]
                        c.execute(f"SELECT User_ID, Agi FROM Stats WHERE User_ID = '{ctx.author.id}'")
                        strcheck = c.fetchone()
                        checkstren = int(strcheck[1])
                        if checkstren >= 10:
                            if checkitem >= 1:
                                if c.execute(f"SELECT * FROM Inventory WHERE User_ID = {ctx.author.id} AND itemid = 7").fetchone():
                                    c.execute(f"UPDATE Inventory SET equip = 1 WHERE User_ID= '{ctx.author.id}' and itemid = 7")
                                    conn1.commit()
                                    await ctx.send("You succesfully equipped a Bow")
                                else:
                                    await ctx.send("You dont have a bow")
                            else:
                                await ctx.send("You dont have a bow")
                        else:
                            await ctx.send("Your stats are too low for the Bow you need at least 10 Agility")
                    elif message == "spellbook" or message == "Spellbook" or message == "spell book":
                        c.execute(f"SELECT * FROM Inventory WHERE User_ID = {ctx.author.id} AND itemid = 8")
                        count = c.fetchone()
                        checkitem = count[2]
                        c.execute(f"SELECT User_ID, Int FROM Stats WHERE User_ID = '{ctx.author.id}'")
                        strcheck = c.fetchone()
                        checkstren = int(strcheck[1])
                        if checkstren >= 20:
                            if checkitem >= 1:
                                if c.execute(f"SELECT * FROM Inventory WHERE User_ID = {ctx.author.id} AND itemid = 8").fetchone():
                                    c.execute(f"UPDATE Inventory SET equip = 1 WHERE User_ID= '{ctx.author.id}' and itemid = 8")
                                    conn1.commit()
                                    await ctx.send("You succesfully equipped a Spell Book")
                                else:
                                    await ctx.send("You dont have a spell book")
                            else:
                                await ctx.send("You dont have a spell book")
                        else:
                            await ctx.send("Your stats are too low for the spell book you need at least 20 Intelligence")
                    
            else:
                await ctx.send("Seems like you dont have anything to equip")
    
    @commands.command()
    @commands.is_owner()
    async def additem(self, ctx, itemid: int, name: str, rarity: int, *, desc: str):
        c.execute("SELECT * FROM Items")
        items = c.fetchall()
        idstuff = []
        for item in items:
            idstuff.append(item[0])
        if itemid in idstuff:
            await ctx.send("This already exists")
        else:
            c.execute(f"INSERT INTO Items VALUES ('{itemid}', '{name}', '{desc}', '{rarity}')")
            conn1.commit()

    @commands.command()
    async def sell(self, ctx,message=None, amount=None):
        if message == None:
            await ctx.send("You need to specify what you wanna sell")

        else:
            if amount == None:
                amount = 1
                if message == "Fish" or message == "fish":
                    c.execute(f"SELECT * FROM Inventory WHERE User_ID = '{ctx.author.id}' AND itemid = 1")
                    fishies = c.fetchone()
                    fishcount = fishies[2]
                    if fishcount > 0:
                        c.execute(f"UPDATE Inventory SET itemcount = itemcount - {amount} WHERE User_ID = '{ctx.author.id}' AND itemid = 1")
                        c.execute(f"UPDATE Exp SET balance = balance + 5 WHERE User_ID = '{ctx.author.id}'")
                        conn1.commit()
                        await ctx.send("You successfully sold a fish for 5 coins")
                    else:
                        await ctx.send("You don't have a fish to sell")
                else:
                    await ctx.send("That isn't sellable")
            else:
                amount = int(amount)
                
                if message == "Fish" or message == "fish":
                    c.execute(f"SELECT * FROM Inventory WHERE User_ID = '{ctx.author.id}' AND itemid = 1")
                    fishies = c.fetchone()
                    fishcount = int(fishies[2])
                    if fishcount > 0:

                        if amount > fishcount:
                            await ctx.send("You dont have enough")
                        elif amount < 0:
                            await ctx.send("You can't do that")
                        
                        else:
                            c.execute(f"UPDATE Inventory SET itemcount = itemcount - {amount} WHERE User_ID = '{ctx.author.id}' AND itemid = 1")
                            c.execute(f"UPDATE Exp SET balance = balance + {amount * 5} WHERE User_ID = '{ctx.author.id}'")
                            conn1.commit()
                            await ctx.send(f"You successfully sold {amount} fish for {amount * 5} coins")
                    else:
                        await ctx.send("You don't have a fish to sell") 
                else:
                    await ctx.send("That isn't sellable")
                

def setup(client):
    client.add_cog(Character(client))