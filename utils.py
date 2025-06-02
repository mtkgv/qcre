from typing import Dict
from io import StringIO

from qiskit.transpiler import InstructionDurations


DurationMap = Dict[int, Dict[tuple, Dict[str, float]]]


def save_ibm_instruction_durations(inst_dur: InstructionDurations, file_path) -> None:
    """
    Save IBM InstructionDurations in text format
    Args:
        inst_dur (InstructionDurtions): IBM InstructionDurations
            from the target device.

        file_path: Output file name
    """

    if not isinstance(inst_dur, InstructionDurations):
        bad_type = type(instruction_durations)
        m = f'Expected InstructionDurations for inst_dur, got {bad_type}'
        raise TypeError(m)

    with open(file_path, "w") as f:
        f.write(str(inst_dur))        


def translate_ibm_instruction_durations(inst_dur: InstructionDurations) -> DurationMap:
    """
    Translate IBM InstructionDurations to DurationMap
    Args:
        inst_dur (InstructionDurtions): IBM InstructionDurations
            from the target device.
    """

    if not isinstance(inst_dur, InstructionDurations):
        bad_type = type(instruction_durations)
        m = f'Expected InstructionDurations for inst_dur, got {bad_type}'
        raise TypeError(m)
    
    duration_map: DurationMap = {}
    
    # Write instruction durations to buffer for parsing
    buffer = StringIO(newline="\n")
    buffer.write(str(inst_dur))
    
    # Convert each line to dictionary entry
    buffer.seek(0)
    for line in buffer.readlines():

        # Import gate info
        line = line.strip()
        qasm_name, end = line.split("(")
        end = "(" + end
        location, end = end.split(":")
        _, time, _ = end.split(" ")
        location = eval(location)
        time = float(time)
        if qasm_name in ['id','rx','rz', 'sx', 'x',]:
            num_qudits = 1
        elif qasm_name in ['cz', 'ecr',]:
            num_qudits = 2
        else:
            num_qudits = -1
        
        # Add gate info to dictionary
        if num_qudits not in duration_map.keys():
            duration_map[num_qudits] = {}
        if location not in duration_map[num_qudits].keys():
            duration_map[num_qudits][location] = {}
        if qasm_name not in duration_map[num_qudits][location].keys():
            duration_map[num_qudits][location][qasm_name] = time
    
    return duration_map