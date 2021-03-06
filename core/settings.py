import os
from config import *
from .utils import randomize_round_id
from config import COMPILER_USER_UID, COMPILER_GROUP_GID


class RoundSettings:

    def __init__(self, data, round_id):
        """
        :param data: should include:
        max_time, max_sum_time, max_memory, problem_id
        :param round_id: round id
        """
        self.max_time = data['max_time']
        self.max_sum_time = data['max_sum_time']
        self.max_memory = data['max_memory']
        self.problem_id = data['problem_id']
        self.round_id = round_id
        self.data_dir = os.path.join(DATA_DIR, str(self.problem_id))
        self.round_dir = os.path.join(ROUND_DIR, str(self.round_id))
        self.input_path = os.path.join(self.round_dir, 'in')
        self.output_path = os.path.join(self.round_dir, 'out')
        self.ans_path = os.path.join(self.round_dir, 'ans')

        # OS init
        if not os.path.exists(self.data_dir):
            raise FileNotFoundError
        if not os.path.exists(self.round_dir):
            os.mkdir(self.round_dir)

        os.chown(self.round_dir, COMPILER_USER_UID, COMPILER_GROUP_GID)
