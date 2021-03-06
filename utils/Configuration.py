import yaml

MASTER_CONFIG = dict()
MASTER_LOADED = False
BOT = None

def initialize(bot):
    global BOT
    BOT = bot
    load_master()

def load_master():
    global MASTER_CONFIG, MASTER_LOADED
    try:
        with open('config/master.yaml', 'r') as yamlfile:
            MASTER_CONFIG = yaml.load(yamlfile)
            MASTER_LOADED = True
    except FileNotFoundError:
        print.error("Unable to load config, running with defaults.")
    except Exception as e:
        print.error("Failed to parse configuration.")
        print(e)
        raise e
        
def get_master_var(key, default=None):
    global MASTER_CONFIG, MASTER_LOADED
    if not MASTER_LOADED:
        load_master()
    if not key in MASTER_CONFIG.keys():
        MASTER_CONFIG[key] = default
        save_master()
    return MASTER_CONFIG[key]


def save_master():
    global MASTER_CONFIG
    with open('config/master.yaml', 'w') as yamlfile:
        yaml.dump(MASTER_CONFIG, yamlfile, default_flow_style=False)


def get_role(ctx, name):
    return ctx.guild.get_role(get_master_var("ROLES")[name.upper()])

def role_assignment(ctx, name):
    return ctx.guild.get_role(get_master_var("ROLES_ASSIGNMENT")[name.upper()])

def get_channel(ctx, name):
    return ctx.bot.get_channel(get_master_var("CHANNELS")[name.upper()])

def get_minecraftrole(ctx, name):
    return ctx.guild.get_role(get_master_var("MINECRAFTROLE")[name.upper()])

def get_minecraftchannel(ctx, name):
    return ctx.bot.get_channel(get_master_var("MINECRAFTCHANNEL")[name.upper()])

