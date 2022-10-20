"""
Copyright 2022 Rafael Galvan

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os, sys, logging, discord, platform, simplimod
from dotenv import load_dotenv

print(f"""
   _____ _                 ___ __  ___          __
  / ___/(_)___ ___  ____  / (_)  |/  /___  ____/ /
  \__ \/ / __ `__ \/ __ \/ / / /|_/ / __ \/ __  / 
 ___/ / / / / / / / /_/ / / / /  / / /_/ / /_/ /  
/____/_/_/ /_/ /_/ .___/_/_/_/  /_/\____/\__,_/   
                /_/                               
                /_/    {simplimod.__version__}                            

    Copyright © 2022 Rafael Galvan
    discord.py {discord.__version__} by rapptz
    python-dotenv by Saurabh Kumar

    {platform.system()} {platform.release()} {os.name}
""")

load_dotenv()

log_channel = os.getenv("LOG_CHANNEL")
log_level = os.getenv("LOG_LEVEL")

logger = logging.getLogger("simplimod")
logger.setLevel(logging.DEBUG)
log_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')

log_stream_handler = logging.StreamHandler(sys.stdout)
log_stream_handler.setLevel(logging.DEBUG)
log_stream_handler.setFormatter(log_formatter)

log_file_handler = logging.FileHandler('simplimod.log')
log_file_handler.setLevel(logging.DEBUG)
log_file_handler.setFormatter(log_formatter)

logger.addHandler(log_stream_handler)
logger.addHandler(log_file_handler)

app_name = os.getenv("APP_NAME")
app_debug = os.getenv("APP_DEBUG")

class SimpliMod(discord.Client):
    async def on_ready(self):
        logging.info('')

    async def on_message(self, message):
        pass

intents = discord.Intents.all()

if __name__ == '__main__':
    client = SimpliMod(intents)
    client.run()