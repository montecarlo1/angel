#
# Tencent is pleased to support the open source community by making Angel available.
#
# Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
#
# Licensed under the BSD 3-Clause License (the "License") you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
#
# https:#opensource.org/licenses/BSD-3-Clause
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
#

import tempfile

from pyangel.conf import AngelConf
from pyangel.context import Configuration
from pyangel.ml.conf import MLConf
from pyangel.ml.gbdt.runner import GBDTRunner


class GBDTExample(object):

    def __init__(self):
        self.conf = Configuration()

    def set_conf(self):
        # Input Path, please modify ${YOUR_ANGEL_HOME} as your local angel installation path,
        # e.g. if your path is /home/angel/angel_1.3.0, your input_path should be:
        # "file:///home/angel/angel_1.3.0/data/exampledata/GBDTLocalExampleData/agaricus.txt.train",
        # and your out_path could be: "file:///home/angel/angel_1.3.0/data/output"
        input_path = "file:///${YOUR_ANGEL_HOME}/data/exampledata/GBDTLocalExampleData/agaricus.txt.train"
        output_path = "file:///${YOUR_ANGEL_HOME}/data/output"
        # Feature number of train data
        feature_num = 127
        # Number of nonzero features
        feature_nzz = 25
        # Tree number
        tree_num = 2
        # Tree depth
        tree_depth = 2
        # Split number
        split_num = 10
        # Feature sample ratio
        sample_ratio = 1.0

        # Data format
        data_fmt = "libsvm"

        # Learning rate
        learn_rate = 0.01

        # Set GBDT category feature
        cate_feat = "0:2,1:2,2:2,3:2,4:2,5:2,6:2,7:2,8:2,9:2,10:2,11:2,12:2,13:2,14:2,15:2,16:2,17:2,18:2,19:2,20:2," \
            "21:2,22:2,23:2,24:2,25:2,26:2,27:2,28:2,29:2,30:2,31:2,32:2,33:2,34:2,35:2,36:2,37:2,38:2,39:2,40:2," \
            "41:2,42:2,43:2,44:2,45:2,46:2,47:2,48:2,49:2,50:2,51:2,52:2,53:2,54:2,55:2,56:2,57:2,58:2,59:2,60:2," \
            "61:2,62:2,63:2,64:2,65:2,66:2,67:2,68:2,69:2,70:2,71:2,72:2,73:2,74:2,75:2,76:2,77:2,78:2,79:2,80:2," \
            "81:2,82:2,83:2,84:2,85:2,86:2,87:2,88:2,89:2,90:2,91:2,92:2,93:2,94:2,95:2,96:2,97:2,98:2,99:2,100:2," \
            "101:2,102:2,103:2,104:2,105:2,106:2,107:2,108:2,109:2,110:2,111:2,112:2,113:2,114:2,115:2,116:2,117:2," \
            "118:2,119:2,120:2,121:2,122:2,123:2,124:2,125:2,126:2"

        # set input, output path
        self.conf[AngelConf.ANGEL_TRAIN_DATA_PATH] = input_path
        self.conf[AngelConf.ANGEL_SAVE_MODEL_PATH] = output_path

        # Set GBDT algorithm parameters
        self.conf[MLConf.ML_DATA_FORMAT] = data_fmt
        self.conf[MLConf.ML_FEATURE_NUM] = feature_num
        self.conf[MLConf.ML_FEATURE_NNZ] = feature_nzz
        self.conf[MLConf.ML_GBDT_TREE_NUM] = tree_num
        self.conf[MLConf.ML_GBDT_TREE_DEPTH] = tree_depth
        self.conf[MLConf.ML_GBDT_SPLIT_NUM] = split_num
        self.conf[MLConf.ML_GBDT_SAMPLE_RATIO] = sample_ratio
        self.conf[MLConf.ML_LEARN_RATE] = learn_rate
        self.conf[MLConf.ML_GBDT_CATE_FEAT] = cate_feat

    def train(self):
        self.set_conf()
        runner = GBDTRunner()
        runner.train(self.conf)

    def predict(self):
        self.set_conf()
        # Load Model from HDFS.
        tmp_path = tempfile.gettempdir()
        self.conf["gbdt.split.feature"] = tmp_path + "/out/xxx"
        self.conf["gbdt.split.value"] = tmp_path + "/out/xxx"
        runner = GBDTRunner()
        runner.predict(self.conf)


example = GBDTExample()
example.train()
