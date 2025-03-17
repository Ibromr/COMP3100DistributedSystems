from primary_replica_replication import (primary_data, replica1_data, replica2_data, replication_log, status_of_primary,
                                         write_to_primary, replicate_to_replicas, read_from_primary, read_from_replica, detect_status_of_primary,)

def test_basic_replication():
    """Test basic write and replication functionality."""
    print("\n=== BASIC WRITE AND REPLICATION ===")
    
    # Clear all data
    primary_data.clear()
    replica1_data.clear()
    replica2_data.clear()
    replication_log.clear()
   
    # Add data to primary
    print("Writing data to primary...")
    print(write_to_primary("student1", "Alice"))
    print(write_to_primary("student2", "Bob"))
    print(write_to_primary("student3", "Charlie"))
    
    # Check data in primary
    print("\nReading from primary:")
    print(f"student1: {read_from_primary('student1')}")
    print(f"student2: {read_from_primary('student2')}")
    print(f"student3: {read_from_primary('student3')}")
    
    # Check data in replicas before replication
    print("\nReading from replicas before replication:")
    print(f"Replica 1 - student1: {read_from_replica(1, 'student1')}")
    print(f"Replica 2 - student2: {read_from_replica(2, 'student2')}")
    
    # Perform replication
    print("\nPerforming replication...")
    print(replicate_to_replicas())
    
    # Check data in replicas after replication
    print("\nReading from replicas after replication:")
    print(f"Replica 1 - student1: {read_from_replica(1, 'student1')}")
    print(f"Replica 1 - student2: {read_from_replica(1, 'student2')}")
    print(f"Replica 2 - student1: {read_from_replica(2, 'student1')}")
    print(f"Replica 2 - student3: {read_from_replica(2, 'student3')}")


    """Test promotion to primary functionality."""
    print("\n\n====== CREATE NEW PRIMARY WITH REPLICA =======")

    # Simulate primary failure
    global status_of_primary
    status_of_primary = False

     # Detect primary status
    status_message = detect_status_of_primary()
    print(status_message)
    print(f"Status of primary after detection: {status_of_primary}")

     # Check data in primary_data after failure
    print("\nReading from primary_data after Failure:")
    print(f"student1: {read_from_primary('student1')}")
    print(f"student2: {read_from_primary('student2')}")



if __name__ == "__main__":      # what is this?
    test_basic_replication()






