# Quantum Circuit Runtime Estimator (QCRE)

The quantum circuit runtime estimator (QCRE) is a tool for
estimating the wall time of quantum circuits using device
gate times. It has been extracted as a standalone tool from
its original use in the paper *Is Circuit Depth Accurate for 
Comparing Quantum Circuit Runtimes?.*[^1]

## Installation

All required dependencies can be installed using:
```sh
pip install -r requirements.txt
```

QCRE minimally requires the [bqskit](https://github.com/BQSKit/bqskit),
[numpy](https://numpy.org/install/), and
[typeguard](https://pypi.org/project/typeguard/) packages to estimate
runtime.

For users targeting IBM devices, the repository includes helper
functions that automatically retrieve device gate times via the
IBM Quantum API. These helper functions additionally require the
[qiskit](https://docs.quantum.ibm.com/guides/install-qiskit) and
[qiskit_ibm_runtime](https://docs.quantum.ibm.com/guides/install-qiskit)
packages, as well as API access. You can learn how to set up API
access using the
[Qiskit documentation](https://docs.quantum.ibm.com/guides/setup-channel).


The example usage script uses these helper functions, and therefore
requires all previous dependencies.

### Required Packages by Task

| Package | Runtime Estimation | IBM Device Helpers | Example Script
|:---:|:---:|:---:|:---:
| [bqskit](https://github.com/BQSKit/bqskit)|X||X
| [numpy](https://numpy.org/install/)|X||X
| [typeguard](https://pypi.org/project/typeguard/)|X||X
| [qiskit](https://docs.quantum.ibm.com/guides/install-qiskit)||X|X
| [qiskit_ibm_runtime](https://docs.quantum.ibm.com/guides/install-qiskit)||X|X

## Usage

1. Compile a circuit for a given device.
2. Construct a **duration map** specifying the execution time of every native 
gate at every possible location in the device's coupling map.
3. Pass the circuit and duration map to the `estimate_runtime` function:
```python
runtime = estimate_runtime(circuit, duration_map)
```

The example usage script `example.py` provides provides a basic implementation
estimating the runtime of a 4-qubit quantum Fourier transform on the IBM
Sherbrooke QPU. It can be run using:
```sh
python example.py
```

## License

Apache License 2.0

## References

[^1]: M. Tremba, J. Liu, and P. Hovland, "Is circuit depth accurate for comparing quantum circuit runtimes?," *arXiv preprint: [arXiv:2505.16908](https://doi.org/10.48550/arXiv.2505.16908)*, 2025.