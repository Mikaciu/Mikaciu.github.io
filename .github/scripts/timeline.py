#!/usr/bin/env python3

import csv
import datetime
import json
import logging
import os
from typing import Tuple

import colorlog

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
	'%(log_color)s%(levelname)s:%(name)s:%(message)s'))

logger = colorlog.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

SOURCE_DIR = os.environ.get('SOURCE_DIR', './source')
RESULT_DIR = os.environ.get('RESULT_DIR', './result')

def generate_vehicle_json():
    vehicle_json = [
        {"id": 0, "treeLevel": 1, "title": "Affectation", "className": "piquet"},
    ]
    vehicle_name_to_id = {}
    last_id = 1

    with open(os.path.join(SOURCE_DIR, 'vehicles.json'), 'r') as source_file:
        vehicles = json.load(source_file)
        for vehicle_name, vehicle_data in vehicles.items():
            current_item = {
                'id': last_id,
                'treeLevel': 1,
                'title': vehicle_name,
                'content': vehicle_name
            }
            sub_items = []
            if 'affectations' in vehicle_data:
                last_id += 1
                # generate the sub items and add them to the parent
                for current_affectation in vehicle_data['affectations']:
                    current_subitem = {
                        'id': last_id,
                        'treeLevel': 2,
                        'title': current_affectation,
                        'content': current_affectation,
                        'className': vehicle_data['classname']
                    }

                    sub_items.append(last_id)
                    vehicle_name_to_id[f'{vehicle_name}>{current_affectation}'] = last_id, vehicle_data['classname']
                    last_id += 1

                    vehicle_json.append(current_subitem)
                
                # Add the list of children to the parent
                current_item['nestedGroups'] = sub_items

                if 'showNested' in vehicle_data:
                    current_item['showNested'] = vehicle_data['showNested']
            else:
                # no affectation : this means the current item has no subitems. Add the classname so it can be visible on the timeline
                current_item['className'] = vehicle_data['classname']
                vehicle_name_to_id[vehicle_name] = last_id, vehicle_data['classname']
                last_id += 1

            vehicle_json.append(current_item)
    
    with open(os.path.join(RESULT_DIR, 'timeline_groups_dataset.json'), 'w') as vehicles_dataset:
        json.dump(vehicle_json, vehicles_dataset)

    return vehicle_name_to_id

# TODO handle multiple years
def generate_timeline_json(vehicle_id):
    hidden_dates = []
    dataset = []
    last_end_date = ""
    first_timeline_date = ""
    last_timeline_date = ""

    with open(os.path.join(SOURCE_DIR, 'timeline_source.json'), 'r') as source_file:
        source_dict = json.load(source_file)

        for duty_date in sorted(source_dict.keys()):
            duty_data = source_dict[duty_date]
            date_start, date_end = get_period(duty_date)

            if date_end <= date_start:
                logger.error('The start time (%s) should be before the end time (%s)', date_start, date_end)
                continue
            
            # sanity checks
            if 'affectations' not in duty_data:
                logger.error('Could not find an "affectations" section for the period %s', duty_date)
                continue

            # Add team data
            if 'team' in duty_data:
                dataset.append({
                    'start': date_start.isoformat(),
                    'end': date_end.isoformat(),
                    'group': 0,
                    'content': f'{duty_data["team"]}',
                    'title': f'Équipe {duty_data["team"]}',
                })
            else:
                logger.warning(
                    'Could not find a "team" section for the period %s', duty_date)
            
            for current_vehicle_name, current_vehicle_data in duty_data['affectations'].items():
                group, classname = vehicle_id[current_vehicle_name]
                if current_vehicle_data:
                    affectation_date_start, affectation_date_end = get_period(current_vehicle_data)

                dataset.append({
                    'start': affectation_date_start.isoformat() if current_vehicle_data else date_start.isoformat(),
                    'end': affectation_date_end.isoformat() if current_vehicle_data else date_end.isoformat(),
                    'group': group,
                    'className': classname,
                    'type': 'background'
                })

            if last_end_date:
                hidden_dates.append({
                    'start': last_end_date.isoformat(),
                    'end': (date_start + datetime.timedelta(hours=-1)).isoformat()
                })
                logger.info('hidden dates : last_end_date %s, start %s', last_end_date,
                            date_start + datetime.timedelta(hours=-1))
            
            if not first_timeline_date or date_start < first_timeline_date:
                first_timeline_date = date_start + datetime.timedelta(days=-1)
            
            logger.debug('last_timeline_date : %s, date_end : %s', last_timeline_date, date_end)
            if not last_timeline_date or date_end > last_timeline_date:
                last_timeline_date = date_end + datetime.timedelta(days=1)
            
            # To hide the periods between two guard duty, add one hour to the last duty end time
            last_end_date = date_end + datetime.timedelta(hours=1)
            
    options_json = {
        'min': first_timeline_date.isoformat(),
        'max': last_timeline_date.isoformat(),
        'start': first_timeline_date.isoformat(),
        'end': last_timeline_date.isoformat(),
        'maxHeight': '95%',
        'nextStartDate': (last_timeline_date + datetime.timedelta(days=-60)).isoformat(),
        'stack': False,
        'locale': 'fr',
        'hiddenDates': hidden_dates,
        "horizontalScroll": True,
        'zoomKey': 'ctrlKey',
        'zoomMin': 72000000,
        'zoomMax': 31536000000,
    }

    with open(os.path.join(RESULT_DIR, 'timeline_options.json'), 'w') as hidden_dates_file:
        json.dump(options_json, hidden_dates_file)
    
    for intervention in get_inter(vehicle_id):
        dataset.append(intervention)

    with open(os.path.join(RESULT_DIR, 'timeline_dataset.json'), 'w') as timeline_output_file:
        json.dump(dataset, timeline_output_file)


def get_inter(vehicle_id):
    with open(os.path.join(SOURCE_DIR, 'interventions.csv'), 'r', encoding='UTF-8') as interventions_file:
        for current_intervention in csv.DictReader(interventions_file):
            group, classname = vehicle_id[current_intervention['affectation']]
            del current_intervention['affectation']
            yield {
                **current_intervention,
                **{
                    'title': "{} : {} - {}".format(current_intervention['content'], current_intervention['start'], current_intervention['end']),
                    'group': group,
                    'className': classname
                }
            }

def get_period(date_str: str) -> Tuple[datetime.datetime, datetime.datetime]:
    if '>' in date_str:
        start, end = date_str.split('>')
        return datetime.datetime.fromisoformat(start), datetime.datetime.fromisoformat(end)
 
    if '+' in date_str:
        start, delta = date_str.split('+')
        date_start = datetime.datetime.fromisoformat(start)
        return date_start, date_start + datetime.timedelta(hours=int(delta))

    return (None, None)


if __name__ == '__main__':
    vehicle_id = generate_vehicle_json()
    generate_timeline_json(vehicle_id)
