
# Model body segments as weighted 1D linkages.
class BodySegment:
    def __init__(self, weight_=0, length_=0, cog_=0):
        self.weight = weight_
        self.length = length_
        self.proximal_cog_pos = cog_
    weight = 0
    length = 0
    proximal_cog_pos = 0

# Model joints as transferring reaction torques and forces in 2D.
class JointReaction:
    force_x = 0
    force_y = 0
    moment = 0

class Human:
    def __str__(self):
        total_height = self.foot_segment.length + self.shank_segment.length + self.thigh_segment.length \
                    + self.trunk_segment.length + self.head_segment.length
        total_weight = 2*self.foot_segment.weight + 2*self.shank_segment.weight \
                    + 2*self.thigh_segment.weight + self.trunk_segment.weight \
                    + self.head_segment.weight + 2*self.upper_arm_segment.weight \
                    + 2*self.forearm_segment.weight + 2*self.hand_segment.weight
        return 'Total Height:' + str(total_height) + '\nTotal Weight:' + str(total_weight)

    # Model floor reaction force as acting at a point.
    floor_force = 0
    floor_force_position = 0 # ex: is_falling = floor_force_position > foot_length - ankle_position

    # Model foot as a flat triangle which has surface contact with the ground.
    foot_length = 0
    foot_height = 0
    ankle_position = 0

    foot_segment = BodySegment()
    ankle_reaction = JointReaction()
    shank_segment = BodySegment()
    shank_angle = 0
    knee_reaction = JointReaction()
    thigh_segment = BodySegment()
    thigh_angle = 0
    hip_reaction = JointReaction()
    trunk_segment = BodySegment()
    trunk_angle = 0
    neck_reaction = JointReaction()
    head_segment = BodySegment()
    head_angle = 0

    shoulder_reaction = JointReaction()
    upper_arm_segment = BodySegment()
    upper_arm_angle = 0
    elbow_reaction = JointReaction()
    forearm_segment = BodySegment()
    forearm_angle = 0
    wrist_reaction = JointReaction()
    hand_segment = BodySegment()
    hand_angle = 0