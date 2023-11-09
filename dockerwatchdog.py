import discord
import datetime
import asyncio
import docker
import os
import yaml
from discord.ext import tasks

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
Server_ID = os.environ["SERVER_ID"]
Channel_ID = os.environ["CHANNEL_ID"]
docker_client = docker.from_env()

# Define a variable to store the previous message ID
previous_message_id = None

@tasks.loop(seconds=10)
async def myLoop():
    global previous_message_id

    await client.change_presence(activity=discord.Game(name="Checking Containers"))
    server = client.get_guild(int(Server_ID))
    channel = discord.utils.get(server.channels, id=int(Channel_ID))

    containers = docker_client.containers.list(all=True)
    x = datetime.datetime.now()
    embedVar = discord.Embed(title="Plex Server Status", description="Made by Super Awesome Name of the guy using this", color=0x00ff00)

    embedVar.add_field(name="Last Heartbeat", value=f"{x}", inline=False)

    # Define a list of container names you want to monitor
    with open('/etc/dockerwatchdog/config.yml','r') as file:
        driver = yaml.safe_load(file)
        containers_to_monitor = driver['docker']['containers']

    for container in docker_client.containers.list(all=True):
        container_name = container.name

        # Check if the container is in the list of containers to monitor
        if container_name in containers_to_monitor:
            human_readable_name = container_name.capitalize()

            if container.status == "running":
                created_time_str = container.attrs['Created']
                created_time_str = created_time_str.split(".")[0]
                created_time = datetime.datetime.strptime(created_time_str, '%Y-%m-%dT%H:%M:%S')
                uptime = datetime.datetime.now() - created_time

                days = uptime.days
                hours, remainder = divmod(uptime.seconds, 3600)
                uptime_str = f"{days} days, {hours} hours"

                embedVar.add_field(name=human_readable_name, value=f"{container.status} 🟢 Uptime: {uptime_str}", inline=False)
            else:
                embedVar.add_field(name=human_readable_name, value="Not Running 🔴", inline=False)

    # Check if any expected containers were not found
    for expected_name in containers_to_monitor:
        #human_readable_name = container_mapping.get(expected_name, expected_name)
        human_readable_name = container_name.capitalize()
        if not any(container.name == expected_name for container in docker_client.containers.list(all=True)):
            embedVar.add_field(name=human_readable_name, value="Not Found 🔴", inline=False)

    # Delete the previous message if it exists
    if previous_message_id:
        try:
            previous_message = await channel.fetch_message(previous_message_id)
            await previous_message.delete()
        except discord.errors.NotFound:
            pass

    # Send a new message
    new_message = await channel.send(embed=embedVar)

    # Store the message ID of the newly sent message
    previous_message_id = new_message.id

    await client.change_presence(activity=discord.Game(name="Done Checking Containers"))
    await asyncio.sleep(60)  # Task runs every 60 seconds

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')
    print('Bot is now running and will perform an action every 60 seconds.')
    myLoop.start()

client.run(os.environ["BOT_TOKEN"])