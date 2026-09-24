# Random-feature-model
Codes for the random feature model

# Model Description: RFN  
Abstract: Machine learning-based partial differential equations (PDEs) solvers have attracted4
significant attention in recent years. Most progress in this area has been driven by deep neural5
networks such as physics-informed neural networks (PINNs) and kernel method (such as physics-6
informed Gaussian Processes). We introduce a physics-informed random feature method for coun-7
tering part of the spectral bias which PINN-based solvers are facing for a certain class of PDEs.8
Random feature method was originally proposed to approximate large-scale kernel machines and can9
be viewed as a specialized randomized neural network. Compared to other state-of-the-art PINN-10
based solvers which require a large number of collocation points, our proposed method reduces the11
computational complexity. In this paper, we develop a rigorous approximation error analysis and12
derive high-probability error bounds on the H1 norm. We provide extensive numerical tests for veri-13
fying our theoretical guarantees on error decay rates, as well as several comparison tests to showcase14
our claimed capability for combating spectral bias in these deep learning based methods 

# Each folder: each equation; comparison of different Deep learning models 



Citation

If you use this code or build upon the numerical experiments, please consider citing the following works.

The Random Feature models and related results implemented in this repository are based on our preprint:

* [Your preprint citation]

The following references provide the methods and/or experimental settings implemented for comparison with the Random Feature models in this repository:


- **[1]** Author et al., *Paper Title*, Year.
  
  Used as the reference implementation for [method].

- **[2]** Author et al., *Paper Title*, Year.

  Provides the numerical setup for [PDE/problem].

- **[3]** Author et al., *Paper Title*, Year.

  Used for comparison with [method].
* [Reference 1]
* [Reference 2]
* [Reference 3]


# Preprint: 

## @misc{chen2025unifiedlearningprofilefunction,
      title={Unified Learning of the Profile Function in Discrete Keller-Segel Models}, 
      author={Chi-An Chen and Chun Liu and Ming Zhong},
      year={2025},
      eprint={2510.23381},
      archivePrefix={arXiv},
      primaryClass={math.NA},
      url={https://arxiv.org/abs/2510.23381}, 
}

Please cite the following 
bit 
