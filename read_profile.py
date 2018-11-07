import os
import csv
from human import *

def read_profile(profile_name, total_height, total_weight):
    human = Human()
    segment_checklist = {'Head': False, 'Trunk': False, 'Upperarm': False,
                         'Forearm': False, 'Hand': False, 'Thigh': False,
                         'Shank': False, 'Foot': False};

    with open('profiles/'+profile_name, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        try:
            headers = reader.next()
        except StopIteration as error:
            print('Error: Unable to read CSV File')
            print(error)
            return None

        try:
            seg_name_idx = headers.index('Segment')
            weight_idx = headers.index('Weight')
            length_idx = headers.index('Length')
            cog_idx = headers.index('CoG')
        except ValueError as error:
            print('Error: CSV File does not contain necessary headers')
            print(error)
            print(headers)
            return None

        for row in reader:
            seg_name = row[seg_name_idx]
            weight = float(row[weight_idx])*total_weight
            length = float(row[length_idx])*total_height
            cog = float(row[cog_idx])

            if (not(seg_name in segment_checklist)):
                continue

            segment_checklist[seg_name] = True

            segment = BodySegment(weight, length, cog)

            if (seg_name == 'Head'):
                human.head_segment = segment
            if (seg_name == 'Trunk'):
                human.trunk_segment = segment
            if (seg_name == 'Upperarm'):
                human.upper_arm_segment = segment
            if (seg_name == 'Forearm'):
                human.forearm_segment = segment
            if (seg_name == 'Hand'):
                human.hand_segment = segment
            if (seg_name == 'Thigh'):
                human.thigh_segment = segment
            if (seg_name == 'Shank'):
                human.shank_segment = segment
            if (seg_name == 'Foot'):
                human.foot_segment = segment

        if (all(checked for checked in segment_checklist.values())):
            return human

    return None


