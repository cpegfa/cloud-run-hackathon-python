
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
import game
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'R', 'L', 'T']

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    request.get_data()

    data=request.json
    logger.info("Myself - logger")
    logging.info("Myself - logging")
    print("Myself - print")
    #logger.info(request.json)
    
    # TODO add your implementation here to replace the random response

    #game.get_game_state(request.json)

    #logger.info("(", game.self['x'],",",game.self['y'],") facing ", game.self['direction'])

"""
    userlist=[['x'(int),'y'(int),'direction'(char),'wasHit'(bool),'score'(int)]
              ,['x','y','direction','wasHit','score']
              ,['x','y','direction','wasHit','score']
              ,['x','y','direction','wasHit','score']
              ,['x','y','direction','wasHit','score']
                ...
                ]

"""

    
    return moves[random.randrange(len(moves))]

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
