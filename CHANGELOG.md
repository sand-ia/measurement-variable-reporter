# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Backward incompatible changes will only be introduced in major versions with advance notice in the **Deprecated** section of releases.

## [Unreleased]

## [v0.3.0] - 2022-12-09

### Changed

- Rename project from shiny-palm-tree to measurement-variable-reporter
- Update test file structure to match src

### Removed

- Remove unused bounded context measurement-variable-analyser
- Remove unused bounded context analysis-reporter
- Remove unused flask startup test
- Remove share folder

## [v0.2.0] - 2022-07-09

### Added

- Add analysis reporter bounded context.
- Add measurement variable analyser bounded context.
- Add measurement variable reporter bounded context.
- Omit init file and dependencies from test coverage.
- Mappers folder added.

### Changed

- Rename Organisation name Bestables to Sandia.
- Remove dotenv from init file, because flask already use it.
- Commands folder renamed to clis.

### Removed

- Add communication bounded context.
- Add report bounded context.
- Add administration bounded context.

## [v0.1.0] - 2022-21-04

### Added

- First pre-release! 🎉

[unreleased]: https://github.com/sand-ia/measurement-variable-reporter/compare/v0.3.0...HEAD
[v0.3.0]: https://github.com/sand-ia/measurement-variable-reporter/compare/v0.2.0...v0.3.0
[v0.2.0]: https://github.com/sand-ia/measurement-variable-reporter/compare/v0.1.0...v0.2.0
[v0.1.0]: https://github.com/sand-ia/measurement-variable-reporter/releases/tag/v0.1.0
