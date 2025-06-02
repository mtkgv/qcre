from qiskit_ibm_runtime import QiskitRuntimeService

from bqskit.ir.circuit import Circuit

from utils import save_ibm_instruction_durations
from utils import translate_ibm_instruction_durations
from estimate import estimate_runtime


device_name = "ibm_sherbrooke"
qasm_file = "qft4.qasm"

# Get instruction durations from IBM backend
backend = QiskitRuntimeService().backend(device_name)
inst_dur = backend.instruction_durations

# Save raw instruction durations
save_ibm_instruction_durations(inst_dur, "out.txt")

# Translate to duration map
duration_map = translate_ibm_instruction_durations(inst_dur)

# Estimate runtime
circuit = Circuit.from_file(qasm_file)
runtime = estimate_runtime(circuit, duration_map)
print(f"Est. runtime for {qasm_file} (s): {runtime} ")