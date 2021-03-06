#!/usr/bin/env python # syntax highlightning

# This is .tac file for running OpenNSA directly from the source directory
# without installing OpenNSA. Handy for testing.
# Run directly in the terminal with: twistd -ny opennsa.tac
# Spawn deamon with twistd -y opennsa.tac


from opennsa import setup
from dotenv import load_dotenv


load_dotenv()  ## Loads ENV values from .env file
# you can get debug and/or payload info in the log by setting one of the flags to true
application = setup.createApplication('config/opennsa.conf', payload=False, debug=False)

