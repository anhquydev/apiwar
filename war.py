import requests
import time
import re
import sys
import random
import os

lag_messages = [
    "L̸̢͝҉̷̧̕҉̴̨͠҉̵̷̡̨̛͊͝҉̵̢̆̕҈̢͠҉̶̷̈́̕͢͜͡҉̶̷̨̧̊͠͠҉҉̷̢̧̎͝͞҉҈̸̨̧͒҇̕҉҉̵̢̡̛̌̕҉̶̷̧̡̛҇̈҉̸̶̢̢̉͠͡҉̴̢҇̅҈̡̕҉̵̵̨҇͑͜͠҉̸̸̧̅͢͡͡҉̴̶̢́҇͢͠҉̷̸̧̢҇̄͠҉҈̷̧̒̕͜͞҉҈̢̛͒҉̨҇҉̷̇͜͠҈̨҇҉҉̛̀͜҉̧̕҉̶̵̧̧͗̕͝҉̵̴̢̡̇͠͝҉̵̸̡̓̕̕͜҉̷̵̡̨̅̕͠҉̷͖͢͠҈̧̕҉҉̸̨͍̕̕͜҉҉̪҇͜҈̨̕҉̷̢̫͞҉̨҇҉̴̸̨̧̩͠͞҉̸̞̕͢҉̨҇҉҈̶̧̢̛̛̥҉̵̶̧̨̛͎͝҉̶̶̡̧̛̜͝҉҈̨͔͠҉̧̛҉̵̧͙͞҉̧͞҉҉̶̙͜͜͞͠҉̷̷̢̠̕͢͝҉̴̴̢̡̛͇͡҉̵̨͕͠҉̧͡҉̷̢͞҉̷͢͡҉҉̷̸̡̕͢͠҉̵̵̡̨҇̐҇҉̷̶̧̛҇̐͢҉̸̡́͞҉̢͠҉̷̸̢̧҇̔҇҉҉̢̈́͠҉̡͡҉̷̢̅͝҉͢͡҉̴̵̧̀͜͠͡҉҈̧͆̕҉̡̛҉̶̶̨̧͗͠͡҉̴̸̡̡̛̉҇҉̶̸̢̢̀͞͡҉̷̶̧̢̋҇̕҉̵̷̢̨͗͠͡҉̷̸̢̢̈́̕̕҉̵̶̢̡̏͝͝҉̸̵̧̾͜͡͞҉̵̶̧̈̕͜͞҉̷̴̨̛͐̕͜҉̶̴̧̓͢͡͞҉̶̴̡̨̛̅̕҉҈̶͆͢͢͡͡҉҉̸̢̧̯̕͝҉̶̡͙҇҉͢͠҉҉̷̧̧̟҇͡҉̸͍͢͡҈̧͝҉҈̶̧̢̛̳͝҉̵̸̨͇͢͝͞҉҈̷̧̛͈̕͢҉҉̴͍͜͢͠͡҉̷̢̘͞҈͜͞҉̵̸̢͕͜͝͝҉̶̵̢͈̕͜͞҉̸̧̛̤҈̕͜҉̷̡̱͞҉̧͡҉̷̛̰͢҈̛͜҉̵̴̧̤͢͠͝҉̴̧̪͞҈̛͢҉̴̸̢̛͍҇͢҉҉̵̨̡̛͈͡҉̷̴̡̟͢͡͞҉҈̵̧̧̳̕͡҉҈̛̳͢҉̨͠҉̷̶̡̢̮̕͠҉҉̧̘̕҈̢҇҉̵̖͢͡҉͢͠҉̵̡͞i̸̢͠҉̴̶̷̢̢͡͞҉̸̶̡̡̛҇́҉̸̸̢̢҇̓͠҉̶̷̧͊͜͞͡҉҈̴̢̨̃͞͡҉̶̨̏͡҉̧̕҉҈̶̧̨͆̕̕҉҈̴̢̛҇̆͜҉̵̨̓̕҉̧͡҉̷̷̨̓͢͝͝҉̷̷̡͐̕̕͢҉҈̸͒͢͜͞͞҉҉̸̡͑͢͞͝҉҉̋͜͞҈҇͢҉҉͐͢͠҈̕͜҉҉̶̨̂͢͠͠҉̸̵̨̨̛̂҇҉̵̸̢̨͛҇͠҉̶̶̨̽͢͝͠҉̸̨̲͠҈͜͝҉̴̴̡̦҇͢͠҉҈̡̦͝҉̢̕҉̸̸̡̧͈͠͝҉̷̵̢͈̕̕͢҉҈̵̢̛͇͜͠҉҉̴̢̨̩͞͠҉̸̴̨̡̛͉͞҉̵̴̢̢͓͡͠҉̸̸̨̢̛͓͡҉̶̴̨̮̕͜͠҉̴̸̧̭̕͜͡҉҈̷̧̮͜͡͝҉҉̨̛͍҈̢͞҉̵̸̧̧̰̕͞҉҉̷̧͖͢͞͠҉҉̷̧̨̳҇҇҉҉̸̡̬҇҇͢҉̴̡̫̕҈̨͞҉̴̶̡̙҇̕͜҉҉̵̧̨̱҇͡҉҉̵̨̢̛̛̪҉҈̴̧̡͎͞͡҉̵͜͡҉̵̕͜҉҉̷͢͠҉͢͝҉҉̧̛͌҈̧͞҉̷̷̡̛̀͜͡҉҉̵̢̐͢͞͡҉̶̶̢̛̓͜͞҉̶̡̛̑҉͜͝҉҉̨̓͠҈͜͝҉̷̡̅͞҈͜͠҉̷̨̇͞҈͜͝҉̷̸̧̨҇̋͠҉̸̵̡̈͢͝͞҉̸͛͢͡҉͢͠҉҉̷̢̿̕͢͝҉̸̛̒͜҈̨҇҉̴̵̧҇̋̕͜҉̶̷̡̧̿͠͡҉̷̵̧̡̃͡͝҉҉̶̡̡́͠͠҉̵̶̡̨̛̛̂҉҉̴̧̛͕͢͞҉̸̴̡̡̛̭҇҉̵̷̢̡̤͠͠҉̴̷̡̛̱͜͝҉҈̷̢̡̛̟͡҉̷̸̧̧̛͔͝҉҉̷̢̖̕͜͝҉҉̡̗͠҈̨̛҉̴̵̡̛͕͜͞҉̴̛͎͢҉̨̕҉҈̵̗͢͜͡͠҉̶̴̡̨̛̕ͅ҉̵̸̢̯͜͞͝҉̷̴̧̢̯҇͠҉̴̷̨̨̬҇͠҉҉̶̡̡͈҇̕҉̶̴̧̨̛̣̕҉҉̸̢̨͉͞͠҉̸̶̧̦҇͜͠҉҈̴̨̢̙҇͞҉҈̯͜͠҉͢͡҉҈̢̫͞҈̨҇҉̵̡̬҇҈̡͡҉̴̸̨̨̛̦҇҉̴̨҇g̶͜͠҉̵̧̕҈҈̨͝҉̶̢҇́҉̨̕҉҈̷̧͗̕̕͜҉̵̴̨̅͜͞͞҉҈̷͊̕͜͢͠҉̸̸̢̾͜͠͞҉̵̵̡̢̂̕͡҉҉͗͜͞҈͜͠҉҈̢̽͠҈̡͞҉̵̛̊͜҈̢̕҉҈̸̨̧̉͡͞҉̵̷̡҇͑͜͝҉̴̧̊̕҉̨͡҉̷҇̇͜҉̢͝҉̷̵̨̢҇̈́͡҉҈̸̨̧҇͆҇҉̷̴̨̨̉͝͡҉̸̵̢̧̉͡͠҉҈̡̛͇҈̨͠҉҉̶̢̧̙͝͠҉̶̨̗͝҉̨̕҉̶̸̢̥̕͜͠҉̶̵̨̡̯҇̕҉҈̛̲͜҈͜͞҉̸̴̧̡̛̤҇҉̸̴̡̨̱͝͠҉̸̢͉͡҉̡̛҉̵̵̢͓҇҇͢҉̵̵̨̛̮҇͜҉҉̧̘͞҉͜͠҉̷̢͠҉̵̡͝҉̷̵̢͝҉̨͞҉҉̵̡̔҇͜͝҉̵̶̧̊͜͝͞҉̴̵̧̂͜͠͠҉҉̏͢͞҈͜͝҉҈̢͊͠҈͜͝҉̷̸̢҇̑҇͜҉̷̢҇̑҈̡͠҉̵̨̀͡҈͜͠҉̷̸̔̕͜͢͡҉҉̷̨̀̕͢͝҉̷̴̢͋҇͜͠҉҈̴̛̍͜͢͡҉̸̨҇̒҉̡͡҉̴̵̢҇̀͢͝҉̵̶̢̛͑̕͜҉̴̵̢̧̝҇̕҉̶̴̨͉҇̕͜҉҉̶̨̛͕҇͢҉̷̶̠҇҇͜͜҉̷̴̧̛̛̫͢҉҈̷̢͖̕͜͠҉̸̡̯҇҉̢̛҉̷̸̨̛̲͜͝҉҈̡̠͝҈̧҇҉̵̸̡͈͢͝͝҉̷̵̨̗͜͞͞҉̶̴̡̡̛̗͝҉̶̶̛̘͢͢͝҉̷̯͢͞҉̢͞҉̸̢̛͍҉҇͜҉̷҇͢ḩ̷͠҉̷̴̴̢̢͠͞҉̸̶̧̢̀͡͝҉̸̡̉͠҈̡͝҉҈̸̡̉͢͝͝҉̴̴̨̽͢͡͡҉̸̸̡̢҇̓͝҉҈̶̢́͢͞͞҉̶̷̡̛̐̕͢҉̸̴̡̀͢͠͡҉̴̸̨̓̕̕͢҉̴̵̨̍҇̕͜҉҈̵̨̂͜͠͝҉҉̡̄͝҈̛͢҉̷̵̛̈͢͜͝҉҉̴̡̢̓̕͞҉̶̶̨̢̓͠͡҉̵̷̛̈́͜͜͠҉̸̽̕͢҉̡͡҉̵̡̈́͠҉̧̕҉̵̨҇̈́҉͜͞҉҈̢͈̕҈̧͡҉̵̷̨̨͙҇͠҉̶̷͙҇͜͜͡҉̷̡͔҇҈̕͢҉̷̷̧̛͓͜͡҉̸̶̧̨̥͞͡҉̶̵̨̦҇͜͝҉̴̵̡̨̯̕͝҉̴̵̡̘͜͡͞҉҈̵̨͕҇͜͡҉̶̢͕͞҉̢͞҉̴̴̢̢̟͞͞҉̷̴̡̗҇͢͡҉̸͜͝҉҉̨̛҉̴͢͡҈҈̢͠҉҈̴̢̢̛̄͡҉҈̶̧̧̒̕͡҉̸̢̀͝҈̨͝҉̵̈͢͡҉̡͝҉̶̴̨́͢͝͞҉̸̷̢̡̀͞͠҉̷̴̧̧҇͗͡҉҈̢҇̈҉͢͝҉҉̵̨̌҇͢͞҉̵̷̨̨҇͆͠҉̵̶̧̧̇͝͞҉̵̵̡̨͋̕̕҉҈̸̨͒̕͜͡҉̵̸̧̡̀͡͡҉҉̵̨̧̛̈́͝҉҈̸̡̛̔̕͜҉҉͈̕͜҈̢҇҉҈̴̧̢͚͠͝҉̷̡̘͠҉̨̛҉̴̶̧̖̕͢͠҉҉̞͢͝҉̡͝҉̵̶̨̨̭͠͠҉̴̴̢̛̱͜͝҉̸̮͜͠҈̢҇҉̵̵̧̧͍҇͝҉̵̛͎͜҈̨͡҉̴̴̗͜͜͞͡҉̸̴̡̡̛͔҇҉̴҇͜t̷̡͝҉̵̶̷̧͜͞͞҉̸̴̛́̕͢͜҉̷̵̨̛́͢͡҉҈̸̡̛̌͢͝҉̴̴̢͂͜͠͞҉҈̶̨͊̕͢͞҉҈̢͌͠҉̡҇҉̴̸̢̧҇͊͠҉̸̴̢̨͌̕̕҉̵̶̡̈́̕͜͡҉̷̴̡̛͆͢͝҉҉̴̢͐̕͜͡҉̷̵̧̈́͢͝͝҉҈̷̢̜҇҇͢҉̷͓͜͡҈̧҇҉̶̢͚͝҈̨͡҉̴̷̢̨̫͝͞҉̶̷̛͖҇͢͜҉̵̥͜͠҈͢͠҉̴̞͢͞҈̕͜҉̵̧̠҇҉̡͝҉̶̛͢ͅ҈҇͢҉̷̸̨̧̦͡͠҉̴̴̧̢̛̛̝҉҈̵̡̨̣͝͡҉҉̨̤҇҈̧͠҉҈̶̨̧̗̕͡҉̶̠͜͝҈̕͢҉̸҇͜҉҈̡͞҉̴̶͢͝҈̕͢҉̷̷̧̡̛͛͝҉̷̷̢͗̕͢͞҉҉̧̽͡҉̢͞҉̸̷̛̚͜͢͞҉̴̸̢̐͢͡͡҉҉̡͒͞҈̨̛҉̴̷̨̚͜͠͠҉҈͒͢͞҈̧҇҉҈̧̛̉҉̧̛҉҈̡҇́҈̛͢҉҉̵̨̧҇͛̕҉̴̧́͝҉͜͝҉̸̴̛҇̉͜͢҉̵̢̛̒҉̧͞҉̵̨̓̕҈̧͞҉̶̵̡̋͜͝͝҉҉̧̏͠҈̕͢҉̸̸̢͛͜͠͡҉҈̨̉͠҈͢͡҉҉̵̨̡͋̕͠҉̴̸̡̀̕͜͡҉҉̸̧҇͑͢͞҉̵͕͢͠҈̛͜҉̴̢̦͝҈̧͞҉̷̧̛ͅ҉̢͠҉̶̷̢͔͜͝͞҉҉̢̦҇҈̢͞҉̴̝͜͠҈̢̕҉̸̧̱͡҉҇͜҉̵̷̧̧͍͝͝҉̶̧̗͠҉̧̕҉̷͕̕͢҉͜͡҉҉̴̡̨̠͠͝҉̶̵̢̛̘͜͞҉̴̯͜͡҉̡̕҉̵̵̧̧̰͞͠҉̶̴̛͓̕͢͢҉̶̵̦͢͢͠͡҉҉̷̢̛̘͢͠҉̶̷̡̛͉͢͞҉̶̷̢̞͢͡͡҉̷̸̨̥͢͡͝҉̸̡͓͠҉̡҇҉̸̨͡ ҉̷͜͞҉̶̢͝҉҉҇͜҉̷͜͝҉҈̴̢̃̕͜͡҉̴̨҇̄҉̧͝҉҉̵̧̛̏͜͠҉҈̴̧̀҇͢͝҉̸̧͒͞҈̢͞҉҈̡̛̽҈͜͞҉̴̶̧̢҇̀̕҉̷̢̌͞҉̧̛҉̵̸̧͒̕͢͝҉̶̧͛͞҉̢͝҉̶̴̢̢̛͋͡҉҈̶̡̌̕͢͞҉̷̸̈́҇͢͢͠҉҈̷̨̃͢͝͡҉҉̸́͢͢͠͝҉҈҇̍͜҉̛͜҉҈̨̛̈́҈̨͠҉̵̧̽͡҈҇͢҉̸̧͌̕҈̧҇҉̸̶̨̢͋̕͡҉̴̵̢̢̛̪͠҉̶̵̢͖͜͞͝҉̴̵̨̭̕͢͝҉̶̸̛̮͢͢͠҉҈̴̨͔͜͡͠҉̶̴̧̤̕͜͡҉̷̵̢̡͓͞͡҉̷̵̨̨̛̟͡҉̸̵̧̧̭̕͠҉̵̶̡̛̭͜͡҉҉̸̨͓͜͡͞҉̴̸̨̡͚̕͝҉̵̜͜͡҉̢͝҉̸̵̧̨̯̕͝҉҈̵̲͢͢͠͠҉̵̴̧̩͜͡͝҉̵̸̡̨̰҇͝҉̸̸̢̢̛̦͞҉̶̢̛̯҈̨͝҉̸̵̨͈҇҇͢҉̴̷̝͜͜͡͠҉̴̸̧̨̰͠͞҉̷̶̧̥̕͢͡҉̵̶̨̝͜͡͞҉̷̨҇T̶͜͝҉҉̶̷̕͢͜͡҉̴̵̧̢͋͞͡҉̶̵̡̧͌̕͡҉̴̾̕͜҉̨͡҉̸̧҇̔҉̡͡҉҈̴̡̛̇̕͢҉̸̨̋͡҈̕͢҉҈̷̧͐͢͠͠҉̴̵̨̡̛̽͝҉҉̶̢̽͜͠͝҉̸͑̕͢҉̧̕҉̷̢̚͡҉̨͞҉̷̸̨̛͑҇͢҉̸̇̕͢҉͢͡҉̵̷̨̡̛̛͂҉҈̵̨̛̊̕͢҉҉̴̧̡̛͑͝҉̵̸̨̢̎̕͞҉̷̴̡̧͒̕͝҉҉̶̢̢҇̋̕҉̴̴̡̛͋͢͞҉̷̴̢̧҇͆͞҉̶̷̧̣̕͜͠҉̵̟͜͞҉̧͝҉̶̵҇҇͢͜ͅ҉̴̴̨̡̭҇͞҉̷̵̢̧̦҇͞҉̵̶̡̧͎͠͞҉̷̸̡̧͎̕͝҉̴̴̡̧͎͠͞҉҉̷̢̡̛̬͝҉҉̧̩͞҉͢͝҉҉̸̧̨̪҇͡҉̵̵̢̧̱͡͞҉҉̷̤҇͢͜͞҉̷̴̨̛̛̖͢҉̷̛̯͢҈̢̛҉̷̴̨̛͚҇͜҉̵̨̛̤҈̨҇҉̷̡̬͞҈̡͝҉̴̴̨̰͜͡͝҉̶̸̡̧͈͞͠҉̴̨͡҉̸̢͝҉҉̷̢͝҉̛͢҉҉̷̊͜͢͞͡҉̶̸̡͗̕͢͡҉̶̧̑͠҉̨͠҉̸̵̧̧҇̽҇҉̴̸̡̧͌͞͠҉̷̷̧̎͢͠͞҉̷̴̢҇̓͜͠҉҈̷̨̡̆̕͝҉̴̸̊͢͜͞͞҉҉̵̧҇̉҇͜҉҉̧̾̕҉̧͝҉̴̶̛̆̕͢͜҉̴̸̢̨̀̕͞҉̸̶̢̛̇͜͞҉̵̸̡̛̐͢͡҉҈̵̡͊҇͢͠҉̸̷̇̕͜͜͝҉̴̷̢̧̣͝͞҉̶̵̨͎҇͢͡҉҈̵̡̧̰҇͡҉̵̢̛͈҉̨̕҉̴̷̢͉҇͜͠҉̵̴̨̤҇̕͜҉̷̴̧̧҇͞ͅ҉̶̡͙͞҉̡̕҉̴̸̢̨̛͚͞҉҈͕͜͝҈̢͠҉҈̵̧̨̱͝͠҉̸̡̛̮҈̨̛҉̵̸̨̡̛͉҇҉̵̴̢̨̩̕͞҉̵̡̛̣҈̡͠҉̸̶̧̧̘̕͝҉̵̨͞ŗ̷͠҉̶̷̸҇͜͜͝҉̶̸̧̨̽͡͠҉̵̴̧҇͑͜͡҉̶̴̛̿͜͜͡҉̷̴̢̛̈́͜͠҉̶̷̧̡̎͡͡҉̴̴̧̢̚̕͞҉̴̴̧̢͛̕͞҉̷̵̢҇͆͢͞҉̵̴̢̧̛̑҇҉҉̧̇͡҈̧͡҉҈̇̕͜҈̧҇҉̷̶̨͒͜͝͠҉̶̵̢̨͆̕̕҉̷̷̨̨̛̆͠҉҈̢̀͝҈̢̛҉҉̴̢̔͢͡͡҉҉̧͆͝҉̢̕҉̵̴̢̛̎͢͞҉҈̸̢̢̛̎҇҉҉̷̨́̕͢͝҉̷̷̢̢̛̛̋҉̸̵̨̱͜͠͠҉̴̴̧̡̭҇͡҉҉̴̢͇҇͜͡҉̸̴̧̡͎҇̕҉҉̵̡̗͢͞͠҉̶̵̢̢̖͡͝҉̸̞͢͡҈̡͡҉̴̶̧̡̰҇͠҉҉̸̡̤͢͡͡҉̵̢͇͡҉̨͞҉̵̢̩͠҉̡̛҉̸̸̜҇͜͜͡҉̴̕͜҉҈̨͠҉̷̷̡҇҈҇͜҉̷͌͢͞҈̧̕҉̵̷̧̛͆҇͢҉̴̷̢̡̛͊͠҉̶҇̊͜҈̡͞҉̵̴̧̓͢͝͡҉̸̵̧̓͢͝͡҉҉̵̧̢̛̌҇҉҉̶͌҇͢͢͝҉̷̨҇̇҉҇͜҉̷̶̨̡҇̒҇҉̸̴̢̡̀͞͞҉̷̷̡҇̉͜͡҉҉̶̡̛͗͜͡҉̵̨̈́͡҉̡҇҉҉̧̃͝҉̢͠҉҉̶̢̨҇̍҇҉̴̢̠͠҉̡͡҉̴̡̛͉҈̡͝҉̴̷̢͔͢͡͝҉̵̡̠͞҈̡̛҉҈̶̨̢̣͡͞҉̷̦͜͞҉҇͜҉̴̵͚҇̕͢͢҉҉͎̕͢҈͢͝҉҈̴̢̣̕͢͠҉̶̵̧̧̯͡͞҉҈̷̨̙̕͢͡҉̵̧̘҇҈͢͡҉̸̷̧̧̦҇͡҉҈̷̨͍҇͢͡҉̵̴̢̩҇͢͡҉̶̧̮͠҈̡҇҉҉̡͞ừ̸͜҉҉̡͞҉̴̡͠҉̷̴̡҇͐͢͞҉̴̷̡͛҇͢͞҉̶̢̑̕҉̕͜҉̶̶̢̧̛͊͞҉҉̵̡̔҇͜͞҉̵̵̨҇́͜͠҉҉̷̨̧̌҇̕҉̸̵̨̛̐͢͞҉̶̷̨̢̀͝͡҉҉̸̧̧́͝͝҉̸̷̧̡̊̕͝҉̴̸̧̧̛̓͡҉̷̷̧̧̉̕͠҉̶̵̨̧͍̕͡҉̷̸̨̙͜͡͡҉̷̵̡̢͍̕͠҉̶̸̡̨̛̲͞҉̵̶̡̨̬҇͞҉҈̵̡͓͢͡͝҉̴̵̝҇͜͜͝҉̸̵͓͢͢͠͝҉̷̸̡͖̕͢͡҉̷̶̡̕̕͜ͅ҉҈̸̧͚̕͢͝҉̶̡͖͠҈̢͠҉̶̴̡̛̛͙͜҉̵̴̨̢̛͞ͅ҉̷̴̨̞͢͝͡҉҈̢̞͞҈̕͜҉҈̶̢̛͈҇͢҉̵̵̨͖̕͜͞҉҈̸̢̭҇͜͡҉҉͢͞҉̵̨҇҉̸̶̧͝҈̢͞҉̷̴̡̇͢͡͞҉̵̷̢҇̆̕͢҉̶̵̨̡̆͡͡҉҉̵̨̡̛̐͠҉̶̵̢̒͜͞͡҉̷̴̢̨̛̔͡҉̷̧͑̕҉͜͠҉̵̴̧̄͢͡͠҉҉̶̨̢̉̕͞҉̴̵̢̡͗̕̕҉̷̴҇̈̕͜͜҉̵̵̢́̕͢͠҉̷̶̧̡̿̕͝҉҉̶̨҇̅͢͠҉҉̵̧̚͢͡͝҉҉̴̡̡̛͑͡҉̷́͜͞҉͜͞҉҈̶̧̨͛͡͡҉̸̸̡̀͜͠͝҉̶̶̨̨̒͡͝҉̴̷̢̧҇͛͠҉̷̡̜͝҈̕"
]

unicode_invisible = ("ㅤ")
def gradient(text, start_color=(255, 0, 255), end_color=(0, 255, 255)):
    result = ""
    length = len(text)
    for i, char in enumerate(text):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * i / (length - 1))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * i / (length - 1))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * i / (length - 1))
        result += f"\033[38;2;{r};{g};{b}m{char}"
    result += "\033[0m"  # Reset màu về mặc định
    return result

def gradient_tutu(text):
    def rgb_to_ansi(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    start_color = (255, 192, 203)  # 🌸 Hồng phấn
    mid_color   = (152, 251, 152)  # 🌿 Mint nhạt
    end_color   = (255, 255, 102)  # 💛 Vàng chanh pastel

    steps = len(text)
    result = ""

    for i, char in enumerate(text):
        t = i / (steps - 1 if steps > 1 else 1)

        if t < 0.5:
            t2 = t / 0.5
            r = int(start_color[0] + (mid_color[0] - start_color[0]) * t2)
            g = int(start_color[1] + (mid_color[1] - start_color[1]) * t2)
            b = int(start_color[2] + (mid_color[2] - start_color[2]) * t2)
        else:
            t2 = (t - 0.5) / 0.5
            r = int(mid_color[0] + (end_color[0] - mid_color[0]) * t2)
            g = int(mid_color[1] + (end_color[1] - mid_color[1]) * t2)
            b = int(mid_color[2] + (end_color[2] - mid_color[2]) * t2)

        result += rgb_to_ansi(r, g, b) + char

    return result + "\033[0m"
    
def inp(text, colors=None):
    if not colors:
        # Default gradient màu tím - xanh biển - xanh lá
        colors = [129, 93, 57, 63, 69, 75, 81, 87, 93, 99, 105, 111, 117, 123]
    result = ""
    for i, c in enumerate(text):
        color = colors[i % len(colors)]
        result += f"\033[38;5;{color}m{c}"
    return result + "\033[0m"


        
def get_user_id(cookie):
    match = re.search(r"c_user=(\d+)", cookie)
    return match.group(1) if match else None

def load_or_get_cookie():
    cookie_file = "cookies.txt"
    if os.path.exists(cookie_file):
        with open(cookie_file, "r", encoding="utf-8") as f:
            cookie = f.read().strip()
            print("\033[1;32mCookies Trông File cookies.txt Vẫn Sử Dụng Được")
            if check_cookie(cookie):
                return cookie
            else:
                print("\033[1;31mXin Lỗi Bạn Nhưng Cookie Bạn Không Hợp Lệ!")
    cookie = input(gradient_tutu("""\n╭─────[ Nhập Cookie Facebook ] - [ DarkNess -   Anh Quý ]
│ 
╰─➤   """)).strip()
    if check_cookie(cookie):
        with open(cookie_file, "w", encoding="utf-8") as f:
            f.write(cookie)
        print("\033[1;32mCookie Đã Được Lưu Lại, Chúc Bạn Sài Tool Vui Vẻ!")
        return cookie
    else:
        print("\033[1;31mCookie Sai Hoặc Die!")
        return None

def check_cookie(cookie):
    headers = {"User-Agent": "Mozilla/5.0", "Cookie": cookie}
    try:
        res = requests.get("https://mbasic.facebook.com/profile", headers=headers)
        if "Đăng nhập" in res.text or "login" in res.url:
            print("\033[1;31mCookie Đã Die Vui Lòng Lấy Cookie Khác")
            return False
        uid = get_user_id(cookie)
        name = re.search(r'<title>(.*?)</title>', res.text)
        name = name.group(1).strip() if name else None
        print("\033[1;32mStatuses : Successful Cookies")
        if uid: print("\033[1;33m🆔 User ID:", uid)
        if name: print("\033[1;36m👤 Tên người dùng: \033[1;31mKhông Tìm Thấy")
        return True
    except Exception as e:
        print("\033[1;31m Lỗi khi kiểm tra cookie:", e)
        return False

def get_fb_dtsg(cookie):
    headers = {"Cookie": cookie, "User-Agent": "Mozilla/5.0"}
    res = requests.get("https://m.facebook.com", headers=headers)
    token = re.search(r'name="fb_dtsg" value="(.*?)"', res.text)
    if token:
        return token.group(1)
    raise Exception("Không lấy được fb_dtsg")

def send_message(cookie, user_id, thread_id, message):
    fb_dtsg = get_fb_dtsg(cookie)
    timestamp = str(int(time.time() * 1000))
    data = {
        "fb_dtsg": fb_dtsg,
        "__user": user_id,
        "body": message,
        "action_type": "ma-type:user-generated-message",
        "timestamp": timestamp,
        "offline_threading_id": timestamp,
        "message_id": timestamp,
        "thread_fbid": thread_id,
        "source": "source:chat:web",
        "client": "mercury"
    }
    headers = {
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = requests.post("https://www.facebook.com/messaging/send/", data=data, headers=headers)
    return res.status_code == 200

def spam_all_groups(cookie, delay):
    try:
        with open("id_groups.txt", "r", encoding="utf-8") as f:
            group_ids = [x.strip() for x in f if x.strip()]
        with open("messages.txt", "r", encoding="utf-8") as f:
            messages = [x.strip() for x in f if x.strip()]
    except:
        print("\033[1;31m❌ Không đọc được id_groups.txt hoặc messages.txt")
        return

    user_id = get_user_id(cookie)
    print(f"\033[1;33m[ DarkNess ] \033[1;32mBot Đang Được Triển Khai Với Số Lượng Là \033[1;33m{len(group_ids)} \033[1;32mNhóm (delay \033[1;33m{delay}s\033[1;32m)")
    while True:
        for thread_id in group_ids:
            message = random.choice(messages)
            ok = send_message(cookie, user_id, thread_id, message)
            print(f"\033[1;36mMessager: \033[1;33m\"{message}\"\n\033[1;36mNhóm: \033[1;33m{thread_id}")
            time.sleep(delay)

def spam_treo_ngon(cookie, delay, thread_id, message_file):
    try:
        with open(message_file, "r", encoding="utf-8") as f:
            messages = [x.strip() for x in f if x.strip()]
    except:
        print("\033[1;31m❌ Không đọc được file tin nhắn!")
        return

    user_id = get_user_id(cookie)
    index = 0
    print(f"\033[1;32m Bắt Đầu Triển Khai Vào Nhóm \033[1;33m{thread_id} \033[1;32m(delay\033[1;33m {delay}s\033[1;32m)")
    while True:
        message = messages[index % len(messages)]
        ok = send_message(cookie, user_id, thread_id, message)
        print(f"\033[1;36mMessager: \033[1;33m{message}\n\033[1;36mThread ID: \033[1;33m{thread_id}\n")
        index += 1
        time.sleep(delay)

def spam_treo_ngon_theo_name(cookie, delay, thread_id, message_file, name):
    # Lấy user_id giống như spam_treo_ngon
    user_id = get_user_id(cookie)
    if not user_id:
        print("❌ Không thể lấy user_id. Kiểm tra lại cookie!")
        return

    # Đọc file ngôn
    with open(message_file, "r", encoding="utf-8") as file:
        messages = file.read().splitlines()

    print(f" Bắt Đầu Treo Ngôn Theo Tên '{name}' Vào Nhóm {thread_id} (delay {delay}s)")

    # Lặp vô hạn như spam_treo_ngon
    while True:
        for message in messages:
            # Thay {name} bằng tên người dùng nhập
            message = message.replace("{name}", name)

            ok = send_message(cookie, user_id, thread_id, message)
            if ok:
                print(f"Messager: {message}\nThread ID: {thread_id}")
            else:
                print("❌ Gửi thất bại! Kiểm tra cookie hoặc kết nối mạng.")

            time.sleep(delay)

def spam_lag_in_code(cookie, delay, thread_id):
    user_id = get_user_id(cookie)
    index = 0
    while True:
        message = lag_messages[index % len(lag_messages)]
        ok = send_message(cookie, user_id, thread_id, message)
        print(f"\033[1;33m[ DarkNess ] \033[1;32mĐã Gửi Tin Nhắn Unicode Lag Đến Nhóm \033[1;33m{thread_id}")
        index += 1
        time.sleep(delay)

def spam_unicode_invisible(cookie, delay, thread_id):
    user_id = get_user_id(cookie)
    count = 0
    while True:
        ok = send_message(cookie, user_id, thread_id, unicode_invisible)
        print(f"\033[1;33m[ DarkNess ] \033[1;32mĐã Gửi Thành Công Unicode Ẩn Lần Thứ \033[1;33m{count+1}")
        count += 1
        time.sleep(delay)
#def gradient(text):
 #   colors = [
#        "\033[38;5;196m",  # 🔴 Đỏ
#        "\001[1;1:1m",  # 🟠 Cam
##        "",  # 🟡 Vàng
 #       "",   # 🟢 Xanh lá
  #      "",   # 🔵 Xanh cyan
     #   "",  # 🟣 Tím hồng
#  *      "",   # 💖 Tím pastel
 #   ]
#    result = ""
#    for i, char in enumerate(text):
  #      result += colors[i % len(colors)] + char
  #  return result + "\033[0m"
q = "\033[38;5;196m"
w = "\033[38;5;202m"
e = "\033[38;5;226m"
r = "\033[38;5;46m"
t = "\033[38;5;51m"
y = "\033[38;5;201m"
u = "\033[38;5;93m"

def input_with_box(prompt):
    user_input = input(prompt)
    box_width = len(user_input) + 2
    print("┌" + "─" * box_width + "┐")
    print("│ " + user_input + " │")
    print("└" + "─" * box_width + "┘")
    return user_input
    
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print(gradient("               ╭━━━╮╱╱╱╱╭╮╱╭━╮╱╭╮"))
        print(gradient("               ╰╮╭╮┃╱╱╱╱┃┃╱┃┃╰╮┃┃"))
        print(gradient("               ╱┃┃┃┣━━┳━┫┃╭┫╭╮╰╯┣━━┳━━┳━━╮  "))
        print(gradient("               ╱┃┃┃┃╭╮┃╭┫╰╯┫┃╰╮┃┃┃━┫━━┫━━┫ "))
        print(gradient("               ╭╯╰╯┃╭╮┃┃┃╭╮┫┃╱┃┃┃┃━╋━━┣━━┃ "))
        print(gradient("               ╰━━━┻╯╰┻╯╰╯╰┻╯╱╰━┻━━┻━━┻━━╯ "))
        print("    \033[1;31m ╔═                                        ═╗")
        print(gradient("       ┌──────────────────────────────────────┐"))
        print(gradient("       │     Credits : DarkNess -  Anh Quý    │"))
        print(gradient("       └──────────────────────────────────────┘"))
        print(gradient("       ╔══════════════════════════════════════╗"))
        print(gradient("       ║             🛡️ COMMAND 🛡️              ║"))
        print(gradient("       ╠══════════════════════════════════════╣"))
        print(gradient("       ║ 1   •> Rải tin nhắn nhiều nhóm         ║"))
        print(gradient("       ║ 2   •> Treo ngôn.                      ║"))
        print(gradient("       ║ 2.1 •> Treo ngôn theo tên            ║"))
        print(gradient("       ║ 3   •> Gửi spam lag (code)             ║"))
        print(gradient("       ║ 4   •> Gửi Unicode tàng hình           ║"))
        print(gradient("       ║ 5   •> Thoát                           ║"))
        print(gradient("       ╚══════════════════════════════════════╝"))
        print("    \033[1;31m ╚═                                        ═╝")
        choice = input(gradient_tutu("""╭───[ Nhập Lựa Chọn ] • [ DarkNess -   Anh Quý ]
│ 
╰─➤  """))

        if choice == "5":
            print(gradient ("Đã Thoát Tool War By DarkNess - Anh Quý"))
            break

        cookie = load_or_get_cookie()
        if not cookie:
            continue

        try:
            delay = int(input(gradient_tutu("""\n╭─────[ Nhập Delay ] - [ DarkNess -   Anh Quý ]
│ 
╰─➤   """)))
        except:
            delay = 5

        if choice == "1":
            spam_all_groups(cookie, delay)

        elif choice == "2":
            thread_id = input(gradient_tutu("""\n╭─────[ Nhập ID Nhóm ] - [ DarkNess -   Anh Quý ]
│ 
╰─➤  """))
            message_file = input_with_box(gradient_tutu("""\n╭─────[ Nhập File Chứa Ngôn ] - [ DarkNess -   Anh Quý ]
│ 
╰─➤   """))
            spam_treo_ngon(cookie, delay, thread_id, message_file)

        elif choice == "3":
            thread_id = input(gradient_tutu("""\n╭─────[ Nhập ID Nhóm ] - [ DarkNess -   Anh Quý ]
│ 
╰─➤  """))
            spam_lag_in_code(cookie, delay, thread_id)

        elif choice == "4":
            thread_id = input(gradient_tutu("""\n╭─────[ Nhập ID Nhóm ] - [ DarkNess -   Anh Quý ]
│ 
╰─➤  """))
            spam_unicode_invisible(cookie, delay, thread_id)
            
        elif choice == "5":
            thread_id = input(gradient_tutu("""\n╭─────[ Nhập ID Nhóm ] - [ DarkNess -   Anh Quý ]
│ 
╰─➤  """))

        else:
            print("\033[1;31m❌ Lựa chọn không hợp lệ!")

def get_all_group_ids(cookie):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Cookie": cookie,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    url = "https://www.facebook.com/api/graphql/"
    data = {
        "fb_api_req_friendly_name": "MessengerGroupsQuery",
        "variables": '{"limit":1000,"platform":"WEB"}',
        "doc_id": "5300413786679518"  # Mã truy vấn các nhóm Messenger
    }
    try:
        res = requests.post(url, data=data, headers=headers)
        json_data = res.json()
        threads = json_data["data"]["viewer"]["message_threads"]["nodes"]
        group_ids = [t["thread_key"]["thread_fbid"] for t in threads if t["thread_key"].get("thread_fbid")]
        return group_ids
    except Exception as e:
        print("❌ Không thể lấy danh sách nhóm:", e)
        return []

def spam_all_groups(cookie, delay):
    user_id = get_user_id(cookie)
    try:
        with open("id_groups.txt", "r", encoding="utf-8") as f:
            group_ids = [x.strip() for x in f if x.strip()]
        if not group_ids:
            print("\033[1;31m⚠️ File id_groups.txt rỗng. Vui lòng thêm ít nhất 1 ID nhóm vào.")
            return
    except FileNotFoundError:
        print("\033[1;31m❌ Không tìm thấy file id_groups.txt. Vui lòng tạo file này và thêm ID nhóm.")
        return

    try:
        with open("messages.txt", "r", encoding="utf-8") as f:
            messages = [x.strip() for x in f if x.strip()]
    except:
        print("\033[1;31m❌ Không đọc được messages.txt")
        return

    print(f"\033[1;33m[ DARKNESS ] \033[1;32mBot Đang Triển Khai Gửi Tin Nhắn Vào \033[1;33m{len(group_ids)} \033[1;32mNhóm (delay\033[1;33m {delay}s\033[1;32m)")
    while True:
        for thread_id in group_ids:
            message = random.choice(messages)
            ok = send_message(cookie, user_id, thread_id, message)
            print(f"\033[1;36mMessager: \033[1;33m\"{message}\" \n\033[1;34mThread ID: \033[1;33m{thread_id}\n")
            time.sleep(delay)
            
if __name__ == "__main__":
    menu()
