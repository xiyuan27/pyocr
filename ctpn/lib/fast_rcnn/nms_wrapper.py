from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
from fast_rcnn.config import cfg
from utils.cython_nms import nms as cython_nms
try:
    from utils.gpu_nms import gpu_nms
except:
    pass

def nms(dets, thresh):
    if dets.shape[0] == 0:
        return []
    if cfg.USE_GPU_NMS:
        try:
            return gpu_nms(dets, thresh, device_id=cfg.GPU_ID)
        except:
            return cython_nms(dets, thresh)
    else:
        return cython_nms(dets, thresh)
