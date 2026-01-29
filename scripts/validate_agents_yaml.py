#!/usr/bin/env python3
import argparse
import sys


def strip_quotes(value: str) -> str:
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_key_value(text: str):
    key, _, value = text.partition(":")
    key = key.strip()
    value = value.strip()
    if not value:
        return key, None
    return key, strip_quotes(value)


def parse_agents_yaml(path: str):
    agents = []
    allowed_tags = []
    in_agents = False
    in_allowed_tags = False
    in_tags = False
    current_agent = None

    with open(path, "r", encoding="utf-8") as handle:
        lines = handle.readlines()

    for line in lines:
        raw = line.rstrip("\n")
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue

        indent = len(raw) - len(raw.lstrip(" "))

        if stripped == "agents:":
            in_agents = True
            in_allowed_tags = False
            in_tags = False
            current_agent = None
            continue

        if stripped == "allowed_tags:":
            in_allowed_tags = True
            in_agents = False
            in_tags = False
            current_agent = None
            continue

        if in_allowed_tags:
            if indent == 2 and stripped.startswith("- "):
                allowed_tags.append(strip_quotes(stripped[2:].strip()))
                continue
            if indent == 0:
                in_allowed_tags = False

        if in_agents:
            if indent == 2 and stripped.startswith("- "):
                current_agent = {}
                agents.append(current_agent)
                in_tags = False
                rest = stripped[2:].strip()
                if rest:
                    key, value = parse_key_value(rest)
                    current_agent[key] = value
                continue

            if current_agent is None:
                continue

            if indent == 4 and stripped.startswith("tags:"):
                current_agent.setdefault("tags", [])
                in_tags = True
                continue

            if in_tags and indent == 6 and stripped.startswith("- "):
                current_agent.setdefault("tags", []).append(
                    strip_quotes(stripped[2:].strip())
                )
                continue

            if indent == 4 and ":" in stripped:
                in_tags = False
                key, value = parse_key_value(stripped)
                current_agent[key] = value
                continue

            if indent <= 2:
                in_tags = False

    return agents, allowed_tags


def check_tags_present(path: str) -> int:
    agents, _ = parse_agents_yaml(path)
    missing = [agent.get("id", "<unknown>") for agent in agents if not agent.get("tags")]
    if missing:
        sys.stderr.write(
            "Agents missing tags: " + ", ".join(missing) + "\n"
        )
        return 1
    return 0


def check_unique_ids(path: str) -> int:
    agents, _ = parse_agents_yaml(path)
    ids = [agent.get("id") for agent in agents if agent.get("id")]
    duplicates = sorted({agent_id for agent_id in ids if ids.count(agent_id) > 1})
    if duplicates:
        sys.stderr.write("Duplicate agent IDs: " + ", ".join(duplicates) + "\n")
        return 1
    return 0


def check_tags_allowed(path: str) -> int:
    agents, allowed_tags = parse_agents_yaml(path)
    if not allowed_tags:
        return 0
    allowed = set(allowed_tags)
    invalid = []
    for agent in agents:
        for tag in agent.get("tags", []):
            if tag not in allowed:
                invalid.append(tag)
    if invalid:
        sys.stderr.write(
            "Tags not in allowed_tags: " + ", ".join(sorted(set(invalid))) + "\n"
        )
        return 1
    return 0


def main():
    parser = argparse.ArgumentParser(description="Validate agents.yaml fields.")
    parser.add_argument(
        "--file",
        default="agents.yaml",
        help="Path to agents.yaml (default: agents.yaml)",
    )
    parser.add_argument("--check-tags-present", action="store_true")
    parser.add_argument("--check-unique-ids", action="store_true")
    parser.add_argument("--check-tags-allowed", action="store_true")

    args = parser.parse_args()

    if args.check_tags_present:
        return check_tags_present(args.file)
    if args.check_unique_ids:
        return check_unique_ids(args.file)
    if args.check_tags_allowed:
        return check_tags_allowed(args.file)

    parser.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
