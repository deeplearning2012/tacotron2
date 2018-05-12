import tensorflow as tf

hparams = tf.contrib.training.HParams(

    # Audio
    num_mels=80,
    num_freq=1025,
    sample_rate=20000,
    frame_length_ms=50,
    frame_shift_ms=12.5,
    min_level_db=-100,
    ref_level_db=20,

    # Dataset
    num_symbols=126, # ord('~')

    # Model:
    outputs_per_step=5,
    drop_rate=0.5,

    ## Embedding
    embedding_dim=256,

    ## Encoder V1
    cbhg_out_units=256,
    conv_channels=128,
    max_filter_width=16,
    projection1_out_channels=128,
    projection2_out_channels=128,
    num_highway=4,
    encoder_prenet_out_units=(256, 128),

    ## Decoder V1
    decoder_prenet_out_units=(256, 128),
    attention_out_units=256,
    decoder_out_units=256,

    ## Post net
    post_net_cbhg_out_units=256,
    post_net_conv_channels=128,
    post_net_max_filter_width=8,
    post_net_projection1_out_channels=256,
    post_net_projection2_out_channels=80,
    post_net_num_highway=4,

    # Training:
    batch_size=32,
    adam_beta1=0.9,
    adam_beta2=0.999,
    adam_eps=1e-8,
    initial_learning_rate=0.002,
    decay_learning_rate=True,
    save_summary_steps=50,
    log_step_count_steps=1,
    alignment_save_steps=100,
    approx_min_target_length=100,
    batch_bucket_width=40,
    batch_num_buckets=50,

    # Eval:
    max_iters=200,
    griffin_lim_iters=60,
    power=1.5, # Power to raise magnitudes to prior to Griffin-Lim
    num_evaluation_steps=32,
    eval_start_delay_secs=1800,
    eval_throttle_secs=600,
)


def hparams_debug_string():
    values = hparams.values()
    hp = ['  %s: %s' % (name, values[name]) for name in sorted(values)]
    return 'Hyperparameters:\n' + '\n'.join(hp)