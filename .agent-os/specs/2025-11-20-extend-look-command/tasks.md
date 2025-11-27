# Spec Tasks

## Tasks

- [x] 1. Command Model Extensions
  - [x] 1.1 Write tests for LookCommand model with new fields (target_type, look_in, instance_number)
  - [x] 1.2 Update LookCommand model in server/models/command.py to add target_type, look_in, and instance_number fields
  - [x] 1.3 Verify all LookCommand model tests pass

- [x] 2. Command Parser Updates
  - [x] 2.1 Write tests for explicit syntax parsing (/look player <name>, /look item <name>, /look container <name>)
  - [x] 2.2 Write tests for container inspection syntax (/look in <container>)
  - [x] 2.3 Write tests for instance targeting parsing (backpack-2, backpack 2)
  - [x] 2.4 Write tests for diagonal direction removal
  - [x] 2.5 Update _create_look_command() in server/utils/command_parser.py to parse explicit syntax
  - [x] 2.6 Add instance targeting parsing logic
  - [x] 2.7 Remove diagonal directions from direction validation
  - [x] 2.8 Verify all command parser tests pass

- [x] 3. Helper Functions and Utilities
  - [x] 3.1 Write tests for _parse_instance_number() helper function
  - [x] 3.2 Write tests for _get_health_label() helper function
  - [x] 3.3 Write tests for _get_sanity_label() helper function
  - [x] 3.4 Write tests for _get_visible_equipment() helper function
  - [x] 3.5 Implement _parse_instance_number() in server/commands/exploration_commands.py
  - [x] 3.6 Implement _get_health_label() helper function
  - [x] 3.7 Implement _get_sanity_label() helper function
  - [x] 3.8 Implement _get_visible_equipment() helper function
  - [x] 3.9 Verify all helper function tests pass

- [x] 4. Player Look Functionality
  - [x] 4.1 Write tests for _get_players_in_room() helper function
  - [x] 4.2 Write tests for player look with various health/sanity states
  - [x] 4.3 Write tests for player look with visible equipment display
  - [x] 4.4 Write tests for player look instance targeting
  - [x] 4.5 Write tests for player look error cases (not found, multiple matches)
  - [x] 4.6 Implement _get_players_in_room() helper function
  - [x] 4.7 Implement player look functionality in handle_look_command()
  - [x] 4.8 Add player look to target resolution priority logic
  - [x] 4.9 Verify all player look tests pass

- [x] 5. Item Look Functionality
  - [x] 5.1 Write tests for _find_item_in_room() helper function
  - [x] 5.2 Write tests for _find_item_in_inventory() helper function
  - [x] 5.3 Write tests for _find_item_in_equipped() helper function
  - [x] 5.4 Write tests for _find_item_in_containers() helper function
  - [x] 5.5 Write tests for item look in different locations (room, inventory, equipped, container)
  - [x] 5.6 Write tests for item look with prototype description lookup
  - [x] 5.7 Write tests for item look instance targeting
  - [x] 5.8 Write tests for item look error cases
  - [x] 5.9 Implement _find_item_in_room() helper function
  - [x] 5.10 Implement _find_item_in_inventory() helper function
  - [x] 5.11 Implement _find_item_in_equipped() helper function
  - [x] 5.12 Implement _find_item_in_containers() helper function
  - [x] 5.13 Implement item look functionality in handle_look_command()
  - [x] 5.14 Add item prototype registry integration for description lookup
  - [x] 5.15 Add item look to target resolution priority logic
  - [x] 5.16 Verify all item look tests pass

- [x] 6. Container Look Functionality
  - [x] 6.1 Write tests for _find_container_in_room() helper function
  - [x] 6.2 Write tests for _find_container_wearable() helper function
  - [x] 6.3 Write tests for container look with contents listing
  - [x] 6.4 Write tests for container look with capacity information
  - [x] 6.5 Write tests for container look with lock status display
  - [x] 6.6 Write tests for container look instance targeting
  - [x] 6.7 Write tests for container look error cases
  - [x] 6.8 Implement _find_container_in_room() helper function
  - [x] 6.9 Implement _find_container_wearable() helper function
  - [x] 6.10 Implement container look functionality in handle_look_command()
  - [x] 6.11 Add container look to target resolution priority logic
  - [x] 6.12 Verify all container look tests pass

- [x] 7. Target Resolution Priority and Integration
  - [x] 7.1 Write tests for priority resolution (Players > NPCs > Items > Containers > Directions)
  - [x] 7.2 Write tests for explicit type syntax overriding priority
  - [x] 7.3 Write integration tests for player look with real players
  - [x] 7.4 Write integration tests for item look across all locations
  - [x] 7.5 Write integration tests for container look with real containers
  - [x] 7.6 Write integration tests for instance targeting with multiple items/containers
  - [x] 7.7 Implement priority resolution logic in handle_look_command()
  - [x] 7.8 Verify all priority resolution and integration tests pass

- [x] 8. Help Documentation Updates
  - [x] 8.1 Update help_content.py with new look command examples
  - [x] 8.2 Verify help documentation displays correctly

- [x] 9. Final Verification and Testing
  - [x] 9.1 Run full test suite and verify ≥80% coverage in touched modules
  - [x] 9.2 Run linting and formatting checks
  - [x] 9.3 Verify all tests pass (unit, integration)
  - [x] 9.4 Code review and final validation
