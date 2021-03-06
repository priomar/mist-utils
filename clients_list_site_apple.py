#!/usr/bin/env python
"""
clients_list_site_apple.py - List Apple clients on a site

This script will list all Apple clients on a specific site.

To use this script, you must set the following environmental variables that
are used by the script:

    MIST_TOKEN - A valid API token created for access to your organization
    MIST_SITE_ID - A valid side ID

This is required to prevent the requirement for hard coding them in to
script of an accompanying config file. It should be created as an env_var
that is private to your environment, not a global var on the machine that
you are working on.
"""

import os
import sys
from pprint import pprint

from modules.core.logger import ScriptLogger
from modules.core.mist_verbs import MistVerbs
from modules.core.stopwatch import StopWatch
from modules.core.get_vars import GetVars
from modules.core.banner import header, footer

logger = ScriptLogger('mist-api')
logger.info("Starting script...")

# supply required token
vars_obj = GetVars()
vars_found = vars_obj.find_vars()
api_token = vars_found.get('token')
site_id = vars_found.get('site_id')

# define URLs
base_url = "https://api.mist.com"
clients_url = "{}/api/v1/sites/{}/clients/sessions/search?client_manufacture=Apple".format(base_url, site_id)

def main():

    timer = StopWatch()
    timer.start()

    if not api_token:
        print("You must define a valid API key using the MIST_TOKEN environmental variable name to use this script...exiting.")
        sys.exit()
    
    if not site_id:
        print("You must define a valid site ID using the MIST_SITE_ID environmental variable name to use this script...exiting.")
        sys.exit()
    
    header()

    logger.info("Getting clients.")
    
    verb_obj = MistVerbs(api_token)
    clients = verb_obj.mist_read(clients_url)
    pprint(clients)

    logger.info("Script complete.")
    timer.stop()

    footer()
    
if __name__ == "__main__":
    main()


