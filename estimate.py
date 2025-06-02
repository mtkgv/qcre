from typeguard import check_type
import numpy as np

from bqskit.ir.circuit import Circuit

from utils import DurationMap


def estimate_runtime(circuit: Circuit, duration_map: DurationMap) -> float:
    """
    Estimate the runtime (in seconds) of the the circuit.
    Args:
        circuit (Circuit): Quantum circuit to estimate the runtime of

        duration_map (DurationMap): Dictionary of all gate execution times
            for all possible hardware locations. These are indexed in a hierarchy by 
            the operation's number of qudits, location, and qasm name. Operations
            which are not part of the quantum runtime (e.g. measurement, reset) are
            indexed with -1 number of qudits.
    """

    check_type(duration_map, DurationMap)

    qudit_runtimes = np.zeros(circuit.num_qudits, dtype=float)
    for op in circuit:
        duration = duration_map[op.num_qudits][op.location][op.gate.qasm_name]
        new_runtime = max(qudit_runtimes[list(op.location)]) + duration
        qudit_runtimes[list(op.location)] = new_runtime
    return float(max(qudit_runtimes))