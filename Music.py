import asyncio
import discord
from discord.ext import commands
if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
    discord.opus.load_opus('opus')

def __init__(self, bot):
        self.bot = bot

class VoiceEntry:
    def __init__(self, message, player):
        self.requester = message.author
        self.channel = message.channel
        self.player = player

    def __str__(self):
        fmt = ' {0.title} uploaded by {0.uploader} and added by {1.display_name}'
        duration = self.player.duration
        if duration:
            fmt = fmt + ' [length: {0[0]}m {0[1]}s]'.format(divmod(duration, 60))
        return fmt.format(self.player, self.requester)

class VoiceState:
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.play_next_song = asyncio.Event()
        self.songs = asyncio.Queue()
        self.skip_votes = set() # a set of user_ids that voted
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    def is_playing(self):
        if self.voice is None or self.current is None:
            return False

        player = self.current.player
        return not player.is_done()

    @property
    def player(self):
        return self.current.player

    def skip(self):
        self.skip_votes.clear()
        if self.is_playing():
            self.player.stop()

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

    async def audio_player_task(self):
        while True:
            self.play_next_song.clear()
            self.current = await self.songs.get()
            await self.bot.send_message(self.current.channel, "```Now playing {}```".format(str(self.current)))
            self.current.player.start()
            await self.play_next_song.wait()
class Music:
    """Voice related commands.
    Works in multiple servers at once.
    """
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state

        return state

    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.server)
        state.voice = voice

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    @commands.command(pass_context=True, no_pm=True)
    async def join(self, ctx, *, channel : discord.Channel):
        """Joins a voice channel."""
        try:
            await self.create_voice_client(channel)
        except discord.ClientException:
            embed = discord.Embed(title="Error:", color=0xFFFF00)
            embed.add_field(value="Already in a voice channel, retard.")
            await self.bot.say(embed=embed)
        except discord.InvalidArgument:
            embed = discord.Embed(title="Error:", color=0xFFFF00)
            embed.add_field(value="This isn't a voice channel, retard.")
            await self.bot.say(embed=embed)
        else:
            embed = discord.Embed(title="Music:", color=0xFFFF00)
            embed.add_field(name="Joined Voice channel:", value="Ready to play audio in ```{}```".format(channel.name))
            await self.bot.say(embed=embed)
            #await self.bot.say('Ready to play audio in ```{}```'.format(channel.name))

    @commands.command(pass_context=True, no_pm=True)
    async def summon(self, ctx):
        """Summons the bot to join your voice channel."""
        summoned_channel = ctx.message.author.voice_channel
        if summoned_channel is None:
            embed = discord.Embed(title="Error:", color=0xFFFF00)
            embed.add_field(value="You're not in a channel, cunt.")
            await self.bot.say(embed=embed)
            return False

        state = self.get_voice_state(ctx.message.server)
        if state.voice is None:
            state.voice = await self.bot.join_voice_channel(summoned_channel)
        else:
            await state.voice.move_to(summoned_channel)

        return True

    @commands.command(pass_context=True, no_pm=True)
    async def play(self, ctx, *, song : str):
        """Plays a song.
        If there is a song currently in the queue, then it is
        queued until the next song is done playing.
        This command automatically searches as well from YouTube.
        The list of supported sites can be found here:
        https://rg3.github.io/youtube-dl/supportedsites.html
        """
        state = self.get_voice_state(ctx.message.server)
        opts = {
            'default_search': 'auto',
            'quiet': True,
        }

        if state.voice is None:
            success = await ctx.invoke(self.summon)
            embed = discord.Embed(title="Loading:", color=0xFFFF00)
            embed.add_field(value="Loading the song be patient nigga...")
            await self.bot.say(embed=embed)
            if not success:
                return

        try:
            player = await state.voice.create_ytdl_player(song, ytdl_options=opts, after=state.toggle_next)
        except Exception as e:
            fmt = 'OOPSIE I made an OOPSIE: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
        else:
            player.volume = 0.6
            entry = VoiceEntry(ctx.message, player)
            embed = discord.Embed(title="Music:", color=0xFFFF00)
            embed.add_field(name="Song added:", value="Added {}".format(str(entry)))
            await self.bot.say(embed=embed)
            await state.songs.put(entry)

    @commands.command(pass_context=True, no_pm=True)
    async def volume(self, ctx, value : int):
        """Sets the volume of the currently playing song."""

        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.volume = value / 100
            embed = discord.Embed(title="Music:", color=0xFFFF00)
            embed.add_field(name="Internal Volume:", value="I've set the volume to {:.0%}".format(player.volume))
            await self.bot.say(embed=embed)
            #await self.bot.say("I've set the volume to {:.0%}".format(player.volume))
    @commands.command(pass_context=True, no_pm=True)
    async def resume(self, ctx):
        """Resumes the currently played song."""
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.resume()

    @commands.command(pass_context=True, no_pm=True)
    async def leave(self, ctx):
        """Stops playing audio and leaves the voice channel.
        This also clears the queue.
        """
        server = ctx.message.server
        state = self.get_voice_state(server)

        if state.is_playing():
            player = state.player
            player.stop()

        try:
            state.audio_player.cancel()
            del self.voice_states[server.id]
            await state.voice.disconnect()
            embed = discord.Embed(title="Music:", color=0xFFFF00)
            embed.add_field(value="Ok leaving the voice channel now..")
            await self.bot.say(embed=embed)
        except:
            pass

    @commands.command(pass_context=True, no_pm=True)
    async def skip(self, ctx):
        """Vote to skip a song. The song requester can automatically skip.
        3 skip votes are needed for the song to be skipped.
        """

        state = self.get_voice_state(ctx.message.server)
        if not state.is_playing():
            embed = discord.Embed(title="Music:", color=0xFFFF00)
            embed.add_field(value="stfu nigga I ain't playin anything")
            await self.bot.say(embed=embed)
            return

        voter = ctx.message.author
        voterID = ctx.message.author.id
        if voter == state.current.requester:
            embed = discord.Embed(title="Music:", color=0xFFFF00)
            embed.add_field(name="Song skip requested:", value="Skipping song...")
            await self.bot.say(embed=embed)
            state.skip()
        elif voter.id not in state.skip_votes:
            state.skip_votes.add(voter.id)
            total_votes = len(state.skip_votes)
            if total_votes >= 3:
                embed = discord.Embed(title="Music:", color=0xFFFF00)
                embed.add_field(name="Song skip requested:", value="Skip vote passed, skipping song...")
                await self.bot.say(embed=embed)
                state.skip()
            else:
                embed = discord.Embed(title="Music:", color=0xFFFF00)
                embed.add_field(name="Song skip requested:", value="Skip vote added, currently at [{}/3]".format(total_votes))
                await self.bot.say(embed=embed)
        elif voter.id == "238175982689845258":
            embed = discord.Embed(title="Music:", color=0xFFFF00)
            embed.add_field(name="Song skip requested:", value="Skipping song for daddy Kira ^.^")
            await self.bot.say(embed=embed)
            state.skip()
        else:
            embed = discord.Embed(title="Music:", color=0xFFFF00)
            embed.add_field(name="Song skip error:", value="You have already voted to skip this song.")
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def playing(self, ctx):
        """Shows info about the currently played song."""

        state = self.get_voice_state(ctx.message.server)
        if state.current is None:
            embed = discord.Embed(title="Music:", color=0xFFFF00)
            embed.add_field(name="Currently playing:", value="Go away, bitch. I'm not playing anything.")
            await self.bot.say(embed=embed)
        else:
            skip_count = len(state.skip_votes)
            embed = discord.Embed(title="Music:", color=0xFFFF00)
            embed.add_field(name="Currently playing:", value="Now playing {} [skips: {}/3]".format(state.current, skip_count))
            await self.bot.say(embed=embed)
            
            
def setup(bot):
    bot.add_cog(Music(bot))
    print('Music is loaded')
