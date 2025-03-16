# Primary node
primary_data = {}

# Replica nodes
replica1_data = {}
replica2_data = {}

# Replication log
replication_log = set()

def write_to_primary(key, value):
    """Add or update a key-value pair in the primary."""
    primary_data[key] = value
    # Log the operation
    replication_log.add(key)
    # Return success message
    return f"Value '{value}' written to key '{key}' in primary"

def replicate_to_replicas():
    """Propagate all changes from primary to replicas."""
    if primary_data is empty?
       replication_log = set()
       write_to_primary
    elif if adding new data to primary data so updated all replicas ...
        # Copy all data from primary to replicas
        replica1_data.clear()
        replica1_data.update(primary_data)
        replica2_data.clear()
        replica2_data.update(primary_data)
        return "Replication completed"

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
    
