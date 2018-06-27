# -*- coding: utf-8 -*-
# Copyright 2018 Jarvis (www.odoomod.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import os, base64

from odoo import api, models, fields

from .config import FLAGS
from .classify_image import run_inference_on_image, maybe_download_and_extract


class ImageRecognition(models.Model):
    _name = 'ai.image.recognition'

    name = fields.Char(string='Result', required=True)
    sample = fields.Binary(string='Sample', required=True)
    score = fields.Float(string='Score')

    @api.model_cr
    def init(self):
        maybe_download_and_extract()

    @api.onchange('sample')
    def _onchange_sample(self):
        if self.sample:
            image_name = 'sample.jpg'
            image_path = os.path.join(FLAGS.model_dir, image_name)
            with open(image_path, "wb") as f:
                f.write(base64.b64decode(self.sample))
            self.name, score = run_inference_on_image(image_path)
            self.score = score * 100
