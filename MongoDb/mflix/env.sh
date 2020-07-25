#!/bin/bash

export FLASK_APP=mflix/mflix.py
export FLASK_DEBUG=false
export MFLIX_DB_URI="mongodb://analytics:analytics-password@mflix-shard-00-00-1yerg.mongodb.net:27017,mflix-shard-00-01-1yerg.mongodb.net:27017,mflix-shard-00-02-1yerg.mongodb.net:27017/mflix?ssl=true&replicaSet=mflix-shard-0&authSource=admin&retryWrites=true&w=majority" 
# Replace XXXX with your MongoDB Connection URI