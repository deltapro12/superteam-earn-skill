#!/bin/bash
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
TARGET="$SKILLS_DIR/superteam-earn"

mkdir -p "$SKILLS_DIR"
rm -rf "$TARGET"
mkdir -p "$TARGET"
cp -r "$SCRIPT_DIR/skill/"* "$TARGET/"
cp -r "$SCRIPT_DIR/scripts" "$TARGET/"
echo "Installed superteam-earn-skill to $TARGET"