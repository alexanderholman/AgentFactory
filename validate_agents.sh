#!/bin/bash
# validate_agents.sh
# Validation script for Agent Factory
# This script runs all MUST requirement tests

set -e

echo "======================================"
echo "Agent Factory Validation Suite"
echo "======================================"
echo ""

PASSED=0
FAILED=0
TOTAL=0

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test function
run_test() {
    local test_id=$1
    local test_name=$2
    local test_command=$3
    
    TOTAL=$((TOTAL + 1))
    echo "Running ${test_id}: ${test_name}"
    
    if eval "$test_command"; then
        echo -e "${GREEN}✓ PASS${NC}: ${test_id}"
        PASSED=$((PASSED + 1))
    else
        echo -e "${RED}✗ FAIL${NC}: ${test_id}"
        FAILED=$((FAILED + 1))
    fi
    echo ""
}

# TEST-001-1: Verify no nested directories beyond one level
echo "=== SPEC-001: File Structure ==="
if [ -d "agents" ]; then
    run_test "TEST-001-1" \
        "Verify flat file structure (no nested directories)" \
        "[ -z \"\$(find agents/ -mindepth 2 -type f 2>/dev/null)\" ]"
else
    echo "Note: agents/ directory does not exist yet - skipping TEST-001-1"
    echo ""
fi

# TEST-002-1: Verify required headings in agent files
echo "=== SPEC-002: Agent File Format ==="
if [ -d "agents" ] && [ "$(find agents/ -maxdepth 1 -name '*.md' -type f 2>/dev/null | wc -l)" -gt 0 ]; then
    for file in agents/*.md; do
        [ -f "$file" ] || continue
        run_test "TEST-002-1" \
            "Verify required headings in $(basename $file)" \
            "grep -q '## Purpose' '$file' && grep -q '## Inputs' '$file' && grep -q '## Outputs' '$file' && grep -q '## Behavior' '$file' && grep -q '## Constraints' '$file'"
    done
else
    echo "Note: No agent markdown files found yet - skipping TEST-002-1"
    echo ""
fi

# TEST-003-2: Verify agent IDs are unique
echo "=== SPEC-003: Tags and Metadata ==="
run_test "TEST-003-2" \
    "Verify agent IDs are unique in agents.yaml" \
    "! grep -A1 'agents:' agents.yaml | grep 'id:' | sort | uniq -d | grep -q ."

# TEST-004-1: Verify append-only files are only appended to
echo "=== SPEC-004: Append-Only Files ==="
echo "Note: TEST-004-1 requires git history - checking files exist"
run_test "TEST-004-1" \
    "Verify append-only files exist" \
    "[ -f specs.md ] && [ -f agent_runs.md ] && [ -f decisions.md ]"

# TEST-005-1: Citations verification (manual review required)
echo "=== SPEC-005: No Fabrication ==="
echo "Note: TEST-005-1 (Citation verification) requires manual review"
echo ""

# TEST-006-1: Verify documentation uses .md extension
echo "=== SPEC-006: Markdown Output ==="
run_test "TEST-006-1" \
    "Verify key documentation files use .md extension" \
    "[ -f agents.md ] && [ -f specs.md ] && [ -f agent_runs.md ] && [ -f decisions.md ]"

# Summary
echo "======================================"
echo "Validation Summary"
echo "======================================"
echo "Total tests run: $TOTAL"
echo -e "${GREEN}Passed: $PASSED${NC}"
if [ $FAILED -gt 0 ]; then
    echo -e "${RED}Failed: $FAILED${NC}"
    echo ""
    echo "Please fix the failing tests before proceeding."
    exit 1
else
    echo -e "${GREEN}All tests passed!${NC}"
    exit 0
fi
