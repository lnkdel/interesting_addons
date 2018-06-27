# -*- coding: utf-8 -*-
# Copyright 2018 Jarvis (www.odoomod.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import os,argparse

parser = argparse.ArgumentParser()
# classify_image_graph_def.pb:
#   Binary representation of the GraphDef protocol buffer.
# imagenet_synset_to_human_label_map.txt:
#   Map from synset ID to a human readable string.
# imagenet_2012_challenge_label_map_proto.pbtxt:
#   Text representation of a protocol buffer mapping a label to synset ID.
parser.add_argument(
    '--model_dir',
    type=str,
    default=os.path.join(os.path.dirname(__file__), 'imagenet'),
    help="""\
  Path to classify_image_graph_def.pb,
  imagenet_synset_to_human_label_map.txt, and
  imagenet_2012_challenge_label_map_proto.pbtxt.\
  """
)
parser.add_argument(
    '--image_file',
    type=str,
    default='',
    help='Absolute path to image file.'
)
parser.add_argument(
    '--num_top_predictions',
    type=int,
    default=1,
    help='Display this many predictions.'
)
FLAGS, unparsed = parser.parse_known_args()