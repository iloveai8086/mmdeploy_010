import tensorrt as trt
from mmdeploy.backend.tensorrt import load_tensorrt_plugin
from mmdeploy.backend.tensorrt.utils import from_onnx
load_tensorrt_plugin()
def get_plugin_names():
    return [pc.name for pc in trt.get_plugin_registry().plugin_creator_list]
print(get_plugin_names())

# export LD_LIBRARY_PATH=/media/ros/A666B94D66B91F4D/ros/new_deploy/cuda/lib64:/media/ros/A666B94D66B91F4D/ros/new_deploy/TensorRT-8.2.3.0.Linux.x86_64-gnu.cuda-11.4.cudnn8.2/TensorRT-8.2.3.0/lib:$LD_LIBRARY_PATH

"""

python tools/deploy.py configs/mmdet3d/monocular-detection/monocular-detection_tensorrt_static-928x1600.py /media/ros/A666B94D66B91F4D/ros/new_deploy/new_mm3d/mmdetection3d/configs/fcos3d/fcos3d_r101_caffe_fpn_gn-head_dcn_2x8_1x_nus-mono3d.py tools/fcos3d_r101_caffe_fpn_gn-head_dcn_2x8_1x_nus-mono3d_finetune_20210717_095645-8d806dc2.pth /media/ros/A666B94D66B91F4D/ros/new_deploy/new_mm3d/mmdetection3d/data/nuscenes/samples/CAM_FRONT/n008-2018-08-01-15-16-36-0400__CAM_FRONT__1533151609512404.jpg --work-dir tools/workspace --device cuda:0 --show

"""

"""

{'img_prefix': '/media/ros/A666B94D66B91F4D/ros/learning/deploy/mmdeploy/tests/test_codebase/test_mmdet3d/data/nuscenes', 'img_info': {'filename': 'n015-2018-07-24-11-22-45+0800__CAM_BACK__1532402927637525.jpg'}, 'box_type_3d': <class 'mmdet3d.core.bbox.structures.cam_box3d.CameraInstance3DBoxes'>, 'box_mode_3d': <Box3DMode.CAM: 1>, 'img_fields': [], 'bbox3d_fields': [], 'pts_mask_fields': [], 'pts_seg_fields': [], 'bbox_fields': [], 'mask_fields': [], 'seg_fields': []}
{'img_prefix': '/media/ros/A666B94D66B91F4D/ros/learning/deploy/mmdeploy/tests/test_codebase/test_mmdet3d/data/nuscenes', 'img_info': {'filename': 'n015-2018-07-24-11-22-45+0800__CAM_BACK__1532402927637525.jpg'}, 'box_type_3d': <class 'mmdet3d.core.bbox.structures.cam_box3d.CameraInstance3DBoxes'>, 'box_mode_3d': <Box3DMode.CAM: 1>, 'img_fields': [], 'bbox3d_fields': [], 'pts_mask_fields': [], 'pts_seg_fields': [], 'bbox_fields': [], 'mask_fields': [], 'seg_fields': []}
{'img_prefix': '/media/ros/A666B94D66B91F4D/ros/learning/deploy/mmdeploy/tests/test_codebase/test_mmdet3d/data/nuscenes', 'img_info': {'filename': 'n008-2018-08-01-15-16-36-0400__CAM_FRONT__1533151612862404.jpg'}, 'box_type_3d': <class 'mmdet3d.core.bbox.structures.cam_box3d.CameraInstance3DBoxes'>, 'box_mode_3d': <Box3DMode.CAM: 1>, 'img_fields': [], 'bbox3d_fields': [], 'pts_mask_fields': [], 'pts_seg_fields': [], 'bbox_fields': [], 'mask_fields': [], 'seg_fields': []}


"""
