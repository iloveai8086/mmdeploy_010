_base_ = ['../../_base_/onnx_config.py']

onnx_config = dict(
    input_names=['img', 'cam2img', 'cam2img_inverse'],
    output_names=['bboxes', 'scores', 'labels', 'dir_scores', 'attrs'],
    input_shape=None,
)
codebase_config = dict(
    type='mmdet3d',
    task='MonocularDetection',
    model_type='end2end',
    ann_file='tests/test_codebase/test_mmdet3d/data/nuscenes/n008-2018-08-01-15-16-36-0400__CAM_BACK__1533151619437558.json',
)
