# Changelog

All notable changes to this project will be documented in this file.

## [0.0.7] - 2026-08-13

### Added

- Multi-step Setup Wizard
- Aquarium Information step
- Maintenance Settings step

### Added Validation

- Required Aquarium Start Date validation
- Future date validation for all maintenance dates
- Future date validation for Aquarium Start Date

### Improved

- Simplified aquarium onboarding
- Reduced configuration complexity
- Better setup experience

## [0.0.6.5] - 2026-08-13

### Added

- Aquarium Manager branding assets
- Integration icon
- Integration logo

### Improved

- Replaced missing integration icon
- Improved visual appearance in Home Assistant
- Enhanced project branding

## [0.0.6.4] - 2026-08-13

### Fixed

- Fixed aquarium start date workflow
- Fixed DateSelector initial value behaviour
- Improved date validation messages

### Added

- Required Aquarium Start Date validation
- User-friendly validation messages

### Improved

- Improved aquarium creation experience

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