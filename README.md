# Random-feature-model

Implementation and numerical experiments for random feature neural networks for solving partial differential equations (PDEs).

## Overview

This repository contains the implementation of Product Random Feature (PRF) neural networks and the associated numerical experiments. The experiments evaluate the approximation performance of the proposed random feature models on several PDE problems and provide numerical verification of the theoretical results.

## Preprint

A detailed description of the model, methodology, and numerical results
is available in the following preprint:

- **Title:** Physics Informed Random Feature Neural Networks for Solving PDEs
- **Authors:** C. Chen, C. Liao, M. Zhong.
- **Link:** https://arxiv.org/abs/2609.16406

## Model Description: 
Abstract: Machine learning-based partial differential equations (PDEs) solvers have attracted4
significant attention in recent years. Most progress in this area has been driven by deep neural5
networks such as physics-informed neural networks (PINNs) and kernel method (such as physics-
informed Gaussian Processes). We introduce a physics-informed random feature method for coun-
tering part of the spectral bias which PINN-based solvers are facing for a certain class of PDEs.
Random feature method was originally proposed to approximate large-scale kernel machines and can
be viewed as a specialized randomized neural network. Compared to other state-of-the-art PINN-
based solvers which require a large number of collocation points, our proposed method reduces the
computational complexity. In this paper, we develop a rigorous approximation error analysis and
derive high-probability error bounds on the H1 norm. We provide extensive numerical tests for veri-
fying our theoretical guarantees on error decay rates, as well as several comparison tests to showcase
our claimed capability for combating spectral bias in these deep learning based methods 

## Contents of This Repository

### Numerical Experiments and Model Comparisons

Contains numerical experiments for several PDEs, including:

- [`1D_Wave_equation/`](./1D_Wave_equation/) — Wave equation experiments and comparisons.
- [`Helmholtz_equation/`](./Helmholtz_equation/) — Helmholtz equation experiments and comparisons.
- [`Linear_Transport_equation/`](./Linear_Transport_equation/) — Linear transport equation experiments and comparisons.
- [`Linear_Advection_Diffusion/`](./Linear_Advection_Diffusion/) - Linear advection-diffusion experiments.


The notebooks compare Product Random Feature Networks (PRF) with Random Feature Networks (RFN), 
Physics-Informed Neural Networks (PINNs), Self-Adaptive PINNs (SA-PINNs), and Extreme Learning Machines (ELMs).

### Verification of Theoretical Results

Contains numerical experiments for verifying the theoretical approximation
results. In particular, the [`Nonlinear_Poisson_convergence_rate/`](./Nonlinear_Poisson_convergence_rate/) directory
contains experiments for evaluating the $L^2$ and $H^1$ convergence rates
of Product Random Feature Networks in higher-dimensional nonlinear Poisson
problems.

The repository includes numerical experiments verifying the theoretical approximation results of the Product Random Feature (PRF) model. In particular, the `Nonlinear_Poisson_convergence_rate/` directory contains experiments investigating the $L^2$ and $H^1$ convergence rates for nonlinear Poisson problems in different dimensions.

![L2 convergence rate](Nonlinear_Poisson_convergence_rate/figures/Nonlinear_Poisson_L2_Convergence_Rate.pdf)

![H1 convergence rate](Nonlinear_Poisson_convergence_rate/figures/Nonlinear_Poisson_H1_Convergence_Rate.pdf)

### Utility Modules

Contains shared Python modules in `utils/` for constructing neural-network
architectures, generating data, and supporting the numerical experiments:

- `ELM_structure.py`
- `PINN_structure.py`
- `RFN_structure.py`
- `SA_PINN_structure.py`
- `data.py`

## Repository Structure

```text
.
├── 1D_Wave_equation/
│   ├── ELM_Wave.ipynb
│   ├── PINN_Wave.ipynb
│   ├── RFN_Product_Wave.ipynb
│   ├── SA_PINN_Wave.ipynb
│   ├── Wave_Equation_training_points_sets.npy
│   └── Wave_utils.py
├── Helmholtz_equation/
│   ├── ELM_Helmholtz.ipynb
│   ├── Helmholtz_utils.py
│   ├── PINN_Helmholtz.ipynb
│   ├── RFN_Product_Helmholtz.ipynb
│   └── SA_PINN_Helmholtz.ipynb
├── Linear_Advection_Diffusion/
│   ├── Linear_Advection_Diffusion_training_points_sets.npy
│   ├── RFN_Product_Advection_Diffusion.ipynb
│   └── RFN_Uniform_Linear_Advection_Diffusion.ipynb
├── Linear_Transport_equation/
│   ├── ELM_Linear_Transport.ipynb
│   ├── Linear_Transport_training_points_5000_sets.npy
│   ├── Linear_Transport_utils.py
│   ├── PINN_Linear_Transport.ipynb
│   ├── RFN_Product_Linear_Transport.ipynb
│   └── SA_PINN_Linear_Transport.ipynb
├── Nonlinear_Poisson_convergence_rate/
│   ├── Nonlinear_Poisson_2d_data.pt
│   ├── Nonlinear_Poisson_4d_data.pt
│   ├── Nonlinear_Poisson_8d_data.pt
│   ├── Nonlinear_Poisson_H1_Convergence_Rate.pdf
│   ├── Nonlinear_Poisson_L2_Convergence_Rate.pdf
│   └── RFN_Nonlinear_high_dim_Poisson.ipynb
├── utils/
│   ├── ELM_structure.py
│   ├── PINN_structure.py
│   ├── RFN_structure.py
│   ├── SA_PINN_structure.py
│   └── data.py
├── README.md
```

## Notes on Reproducibility

The numerical experiments in this repository are designed to be reproducible. The corresponding experiment directories contain the code and parameter settings used to generate the reported results and figures.

Unless otherwise specified, randomized experiments are repeated over multiple independent trials, with random features and training samples generated independently for each trial. The reported results are aggregated across these trials.

The main implementation details, including model parameters, numbers of random features and training points, optimization settings, and evaluation procedures, are specified in the corresponding experiment scripts.

## Environment

The experiments were developed and tested with:

- Python 3.x
- PyTorch
- NumPy
- SciPy
- Matplotlib

## Scope and Limitations

This work focuses on PDEs exhibiting inhomogeneous variations along the spatial and/or temporal axes, where the solution varies across different directions of the computational domain.

The proposed random feature models are evaluated on the types of problems considered in this work. However, they may have difficulty resolving solutions with sharp gradients or localized structures. For example, for convection-dominated problems such as the viscous Burgers’ equation in regimes with steep solution gradients, the current random feature models may not accurately capture these sharp features.



## Citation
If you use this code or build upon the numerical experiments, please consider citing the following works.

### Our Work
The Random Feature models and related results implemented in this repository are based on our preprint:

```bibtex
@article{chen2026physics,
  title={Physics Informed Random Feature Neural Networks for Solving PDEs},
  author={Chen, Chi-An and Liao, Chunyang and Zhong, Ming},
  journal={arXiv preprint arXiv:2609.16406},
  year={2026}
}
```

### Related Works:
The following references provide the methods and/or experimental settings implemented for comparison with the Random Feature models in this repository:

- **[1]** McClenny, Levi D. and Braga-Neto, Ulisses M., *Self-adaptive physics-informed neural networks*, 2023.  
  Used as the methodological reference for our **Self-Adaptive PINN** implementation.

- **[2]** Krishnapriyan, Aditi and Gholami, Amir and Zhe, Shandian and Kirby, Robert and Mahoney, Michael, *Characterizing possible failure modes in physics-informed neural networks*, 2021.  
  Provides the basis for the numerical setup of selected PDE problems and examples in this repository.

- **[3]** Liao, Chunyang, *Solving partial differential equations with random feature models*, 2025.  
  Serves as the methodological reference for the **Uniform Random Feature (URF)** model implemented in this repository. The nonlinear Poisson problem is used for verification of the convergence-rate results, while the linear advection-diffusion problem is used for comparison with the proposed **Product Random Feature (PRF)** model.

- **[4]** Huang, Guang-Bin and Zhu, Qin-Yu and Siew, Chee-Kheong, *Extreme Learning Machine: Theory and Applications*, 2006.  
  Provides the methodological reference for the **Extreme Learning Machine (ELM)** baseline implemented in this repository.


