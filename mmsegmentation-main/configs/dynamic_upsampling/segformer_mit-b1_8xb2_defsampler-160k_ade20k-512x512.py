_base_ = ['../segformer/segformer_mit-b0_8xb2-160k_ade20k-512x512.py']

checkpoint = 'https://download.openmmlab.com/mmsegmentation/v0.5/pretrain/segformer/mit_b1_20220624-02e5a6a1.pth'  # noqa

# model settings
model = dict(
    backbone=dict(
        init_cfg=dict(type='Pretrained', checkpoint=checkpoint),
        embed_dims=64,
        num_heads=[1, 2, 5, 8],
        num_layers=[2, 2, 2, 2]),
    decode_head=dict(
        type='SegformerHead_Upsample',
        num_classes=150,
        in_channels=[64, 128, 320, 512],
        upsample_cfg=dict(type='defsampler',
                          guided=False)
    ),
)
