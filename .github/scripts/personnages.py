#!/usr/bin/env python3

import os
import logging
import pathlib
import glob

import json

from jinja2 import Environment, FileSystemLoader

import colorlog

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter("%(log_color)s%(levelname)s:%(name)s:%(message)s"))

logger = colorlog.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

SOURCE_DIR = os.environ.get("SOURCE_DIR", "./source")
SOURCE_JSON = os.path.join(SOURCE_DIR, "personnages.json")
TARGET_FILE = os.path.join(SOURCE_DIR, "personnages.html")

jinja_env = Environment(loader=FileSystemLoader(SOURCE_DIR))
current_template = jinja_env.get_template("personnages.html.tpl")

with open(SOURCE_JSON, "r") as source_file:
    logger.info("Loading information from JSON file %s...", SOURCE_JSON)
    source_data = json.load(source_file)
    logger.info("JSON data loaded.")

    processed_data = {}
    for character_name, character_data in source_data.items():
        if "pic" not in character_data:
            # no picture defined, try to find one from the character name
            current_glob = glob.glob(pathname=os.path.join(SOURCE_DIR, "pics", character_name.replace(" ", "_") + ".*"))
            if len(current_glob) > 0:
                glob_path = pathlib.Path(current_glob[0])
                character_data["pic"] = glob_path.relative_to(SOURCE_DIR)

        processed_data[character_name] = character_data

    with open(TARGET_FILE, "w", encoding="UTF-8") as output_file:
        logger.info("Writing output file %s ...", TARGET_FILE)
        output_file.write(current_template.render(characters=processed_data))
        logger.info("Output file written.")
