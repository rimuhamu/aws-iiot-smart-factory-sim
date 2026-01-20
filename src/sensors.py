import random
import time
from src import config

def get_machine_a_data():
    """
    Machine A (The Feeder): Tracks raw input and availability.
    Simulates: Occasional jams (status=0).
    """
    is_jammed = random.random() < config.Jammed_Probability # chance of jamming
    status = 0 if is_jammed else 1 # 0 = stopped, 1 = running

    return{
        "machine_id": "machine_A",
        "timestamp": time.time(),
        "status": status,
        "input_count": 0 if is_jammed else random.randint(50,60), # 50-60 items fed into the production line
    }

def get_machine_b_data():
    """
    Machine B (The Processor): Tracks speed and health.
    Simulates: Temperature rising creates efficiency loss.
    """
    temp = random.normalvariate(45, 5)  # Normal distribution around 45 degrees
    cycle_time = 2.5 if temp < 50 else 3.5  # Slower if hot

    return{
        "machine_id": "machine_B",
        "timestamp": time.time(),
        "temperature": round(temp, 2),
        "cycle_time": cycle_time
    }


def get_machine_c_data():
    """
    Machine C (The Quality Scanner): Tracks final output.
    Simulates: Defect rate.
    """
    produced = random.randint(45, 55)
    defects = random.randint(0, 5)

    return {
        "machine_id": "machine_C",
        "timestamp": time.time(),
        "total_produced": produced,
        "defect_count": defects
    }
