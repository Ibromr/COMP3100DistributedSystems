# Primary node
primary_data = {}

# Replica nodes
replica1_data = {}
replica2_data = {}

# Replication log
replication_log = set()

#Fault detection
status_of_primary = True


def write_to_primary(key, value):
    """Add or update a key-value pair in the primary."""
    primary_data[key] = value
    # Log the operation
    replication_log.add(key)
    # Return success message
    return f"Value '{value}' written to key '{key}' in primary"

def replicate_to_replicas():
    """Propagate all changes from primary to replicas."""
    
    """ This is not a efficient way 
    # Copy all data from primary to replicas
    replica1_data.clear()
    replica1_data.update(primary_data)
    replica2_data.clear()
    replica2_data.update(primary_data)
    """

    # Check if there are any modified or new keys
    if replication_log:
        # Only replicate keys that are in the replication log
        for key in replication_log:
            replica1_data[key] = primary_data.get(key)
            replica2_data[key] = primary_data.get(key)

        # After replication, clear the log to acoud redundat replication
        replication_log.clear()
        return ("Replication_log is cleared.\n"
        "Replication completed.")
    else: 
        return "No changes to replicate"

def read_from_primary(key):
    """Read a value from the primary."""
    return primary_data.get(key, f"Key '{key}' not found")

def read_from_replica(replica_num, key):
    """Read a value from a specific replica."""
    if replica_num == 1:
        return replica1_data.get(key, f"Key '{key}' not found in replica 1")
    elif replica_num == 2:
        return replica2_data.get(key, f"Key '{key}' not found in replica 2")
    else:
        return "Invalid replica number"


def detect_status_of_primary():
    global status_of_primary
    if status_of_primary == False:
        promote_replica()
        return "primary_data is unavailable.\n Initiating new primary_data as replica1_data"
    else: 
        return "primary_data is working correctly."

def promote_replica():
    global primary_data #why???
    global status_of_primary #why???

    if replica1_data:
        primary_data = replica1_data.copy()
        print("Replica 1 promoted to Primary")
        #status_of_primary = True
    elif replica2_data:
        primary_data = replica2_data.copy()
        print("Replica 2 promoted to Primary")
        #status_of_primary = True
    else:
        primary_data = {} # No data left
        print("No replicas avaliable to promote.")
        status_of_primary = False

    return status_of_primary