#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.api import images
from libs.gaesite import BaseHandler
from application.database import *

class get_image(BaseHandler):
    def get(self, key):
        rsize_w = self.request.get('width')  if self.request.get('width') is not None else None
        rsize_h = self.request.get('height') if self.request.get('height') is not None else None
        crop_w = self.request.get('crop_w') if self.request.get('crop_w') is not None else None
        crop_h = self.request.get('crop_h') if self.request.get('crop_h') is not None else None
        img = db.get(key)
        if img is None:
            self.error(404)

        if rsize_w is None or rsize_h is None or rsize_w == '' or rsize_h == '':
            self.response.headers['Content-Type'] = "image/png"
            self.response.out.write(img.original)
        elif int(rsize_w) == 125 or int(rsize_h) == 125:
            self.response.headers['Content-Type'] = "image/png"
            self.response.out.write(img.system_thumbnail)
        else:
            width = int(rsize_w)
            height = int(rsize_h)
            if crop_h is None or crop_w is None or crop_h == '' or crop_w == '':
                self.response.headers['Content-Type'] = "image/png"
                self.response.out.write(images.resize(img.original, width, height))
            else:
                image = images.Image(img.original)
                r = image.width / image.height
                if image.width < image.height:
                    image.resize(width, width * r)
                else:
                    image.resize(height * r, height)
                thumbnail = image.execute_transforms(output_encoding=images.PNG)
                self.response.headers['Content-Type'] = "image/png"
                self.response.out.write(thumbnail)
        self.__is_render__ = True


class upload_image(BaseHandler):
    def post(self):
        """ 上傳圖片 """
        img = DBImage()
        img.thumbnail = images.resize(self.request.get("Filedata"), 125, 125)
        img.original = images.resize(self.request.get("Filedata"),800,800)
        img.put()
        self.info = str(img.key())