import discord


async def info(client, message, *args):
    args = args[0].split(' ')
    if args[0] == 'update':
        del args[0]

        new_info = ' '.join(args)
        with open("..\config\information.txt", "wt") as out_file:
            out_file.write(new_info)
        out_file.close()
        await client.send_message(message.channel, 'Information was updated, the new '
                                                   'information is: ```' + new_info + '```')

    else:
        # Read a file
        with open("..\config\information.txt", "rt") as in_file:
            text = in_file.read()
        in_file.close()

        await client.send_message(message.channel, '```Description: \n' + text + '```')
