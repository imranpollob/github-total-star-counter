# Gitstar

A command-line tool to calculate the total number of stars earned by a GitHub user.

## Installation

Install via pip:

```bash
pip install gitstar
```

## Usage

Basic usage:

```bash
gitstar <username>
```

Limit the output to the top N repositories:

```bash
gitstar <username> <limit>
```

### Examples

Get total stars for user `pollmix`:

```bash
gitstar pollmix
```

Get total stars and list top 5 repositories:

```bash
gitstar pollmix 5
```