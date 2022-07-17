"""The lightly_plus_time.lightly.loss package provides loss functions for self-supervised learning. """

# Copyright (c) 2020. Lightly AG and its affiliates.
# All Rights Reserved

from lightly_plus_time.lightly.loss.barlow_twins_loss import BarlowTwinsLoss
from lightly_plus_time.lightly.loss.dcl_loss import DCLLoss, DCLWLoss
from lightly_plus_time.lightly.loss.dino_loss import DINOLoss
from lightly_plus_time.lightly.loss.negative_cosine_similarity import NegativeCosineSimilarity
from lightly_plus_time.lightly.loss.ntx_ent_loss import NTXentLoss
from lightly_plus_time.lightly.loss.swav_loss import SwaVLoss
from lightly_plus_time.lightly.loss.sym_neg_cos_sim_loss import SymNegCosineSimilarityLoss
