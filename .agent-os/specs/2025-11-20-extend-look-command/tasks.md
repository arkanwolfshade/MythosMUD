# Spec Tasks

## Tasks

- [ ] 1. Command Model Extensions
  - [ ] 1.1 Write tests for LookCommand model with new fields (target_type, look_in, instance_number)
  - [ ] 1.2 Update LookCommand model in server/models/command.py to add target_type, look_in, and instance_number fields
  - [ ] 1.3 Verify all LookCommand model tests pass

- [ ] 2. Command Parser Updates
  - [ ] 2.1 Write tests for explicit syntax parsing (/look player <name>, /look item <name>, /look container <name>)
  - [ ] 2.2 Write tests for container inspection syntax (/look in <container>)
  - [ ] 2.3 Write tests for instance targeting parsing (backpack-2, backpack 2)
  - [ ] 2.4 Write tests for diagonal direction removal
  - [ ] 2.5 Update _create_look_command() in server/utils/command_parser.py to parse explicit syntax
  - [ ] 2.6 Add instance targeting parsing logic
  - [ ] 2.7 Remove diagonal directions from direction validation
  - [ ] 2.8 Verify all command parser tests pass

- [ ] 3. Helper Functions and Utilities
  - [ ] 3.1 Write tests for _parse_instance_number() helper function
  - [ ] 3.2 Write tests for _get_health_label() helper function
  - [ ] 3.3 Write tests for _get_sanity_label() helper function
  - [ ] 3.4 Write tests for _get_visible_equipment() helper function
  - [ ] 3.5 Implement _parse_instance_number() in server/commands/exploration_commands.py
  - [ ] 3.6 Implement _get_health_label() helper function
  - [ ] 3.7 Implement _get_sanity_label() helper function
  - [ ] 3.8 Implement _get_visible_equipment() helper function
  - [ ] 3.9 Verify all helper function tests pass

- [ ] 4. Player Look Functionality
  - [ ] 4.1 Write tests for _get_players_in_room() helper function
  - [ ] 4.2 Write tests for player look with various health/sanity states
  - [ ] 4.3 Write tests for player look with visible equipment display
  - [ ] 4.4 Write tests for player look instance targeting
  - [ ] 4.5 Write tests for player look error cases (not found, multiple matches)
  - [ ] 4.6 Implement _get_players_in_room() helper function
  - [ ] 4.7 Implement player look functionality in handle_look_command()
  - [ ] 4.8 Add player look to target resolution priority logic
  - [ ] 4.9 Verify all player look tests pass

- [ ] 5. Item Look Functionality
  - [ ] 5.1 Write tests for _find_item_in_room() helper function
  - [ ] 5.2 Write tests for _find_item_in_inventory() helper function
  - [ ] 5.3 Write tests for _find_item_in_equipped() helper function
  - [ ] 5.4 Write tests for _find_item_in_containers() helper function
  - [ ] 5.5 Write tests for item look in different locations (room, inventory, equipped, container)
  - [ ] 5.6 Write tests for item look with prototype description lookup
  - [ ] 5.7 Write tests for item look instance targeting
  - [ ] 5.8 Write tests for item look error cases
  - [ ] 5.9 Implement _find_item_in_room() helper function
  - [ ] 5.10 Implement _find_item_in_inventory() helper function
  - [ ] 5.11 Implement _find_item_in_equipped() helper function
  - [ ] 5.12 Implement _find_item_in_containers() helper function
  - [ ] 5.13 Implement item look functionality in handle_look_command()
  - [ ] 5.14 Add item prototype registry integration for description lookup
  - [ ] 5.15 Add item look to target resolution priority logic
  - [ ] 5.16 Verify all item look tests pass

- [ ] 6. Container Look Functionality
  - [ ] 6.1 Write tests for _find_container_in_room() helper function
  - [ ] 6.2 Write tests for _find_container_wearable() helper function
  - [ ] 6.3 Write tests for container look with contents listing
  - [ ] 6.4 Write tests for container look with capacity information
  - [ ] 6.5 Write tests for container look with lock status display
  - [ ] 6.6 Write tests for container look instance targeting
  - [ ] 6.7 Write tests for container look error cases
  - [ ] 6.8 Implement _find_container_in_room() helper function
  - [ ] 6.9 Implement _find_container_wearable() helper function
  - [ ] 6.10 Implement container look functionality in handle_look_command()
  - [ ] 6.11 Add container look to target resolution priority logic
  - [ ] 6.12 Verify all container look tests pass

- [ ] 7. Target Resolution Priority and Integration
  - [ ] 7.1 Write tests for priority resolution (Players > NPCs > Items > Containers > Directions)
  - [ ] 7.2 Write tests for explicit type syntax overriding priority
  - [ ] 7.3 Write integration tests for player look with real players
  - [ ] 7.4 Write integration tests for item look across all locations
  - [ ] 7.5 Write integration tests for container look with real containers
  - [ ] 7.6 Write integration tests for instance targeting with multiple items/containers
  - [ ] 7.7 Implement priority resolution logic in handle_look_command()
  - [ ] 7.8 Verify all priority resolution and integration tests pass

- [ ] 8. Help Documentation Updates
  - [ ] 8.1 Update help_content.py with new look command examples
  - [ ] 8.2 Verify help documentation displays correctly

- [ ] 9. Final Verification and Testing
  - [ ] 9.1 Run full test suite and verify ≥80% coverage in touched modules
  - [ ] 9.2 Run linting and formatting checks
  - [ ] 9.3 Verify all tests pass (unit, integration)
  - [ ] 9.4 Code review and final validation
