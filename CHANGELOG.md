# Changelog

All notable changes to this project will be documented in this file.

## [0.0.6.3] - 2026-08-13

### Fixed

- Fixed DateSelector parsing issues
- Fixed "Unknown error occurred" during configuration
- Fixed date comparison logic in Config Flow

### Added

- Validation for all aquarium date fields
- Prevention of future dates
- User-friendly validation error messages

### Improved

- Improved configuration flow reliability
- Better handling of optional date fields

## [0.0.6.2] - 2026-08-13

### Added

- Validation for all aquarium date fields
- Prevention of future dates in configuration
- User-friendly validation messages

### Improved

- Enhanced configuration data validation


## [0.0.6] - 2026-08-11

### Added

- Date picker support for all date fields
- Human readable configuration labels

### Improved

- Replaced interval sliders with numeric input fields

## [0.0.5] - 2026-08-11

### Added

- Aquarium Manager device support
- Days Since Water Test sensor
- Days Since Filter Clean sensor
- Days Since Filter Maintenance sensor
- Days Since Partial Water Change sensor
- Days Since Hungry Day sensor
- Shared maintenance sensor base class

### Improved

- Grouped all entities under a single Aquarium Manager device

## [0.0.3] - 2026-08-11

### Added

- Aquarium Manager device
- Device Registry support

## [0.0.2] - 2026-08-11

### Added

- Initial Home Assistant custom integration skeleton
- Config Flow support
- Aquarium Name configuration
- Start Date configuration
- Aquarium Manager Age sensor