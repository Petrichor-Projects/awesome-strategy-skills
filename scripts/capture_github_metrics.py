#!/usr/bin/env python3
"""Capture a point-in-time GitHub traffic snapshot without external packages."""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen


API_ROOT = "https://api.github.com"


def api_get(path: str, token: str) -> object:
    request = Request(
        f"{API_ROOT}{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "awesome-strategy-skills-metrics",
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            return json.load(response)
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API {exc.code} for {path}: {detail}") from exc


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN")
    repository = os.environ.get("GITHUB_REPOSITORY", "Petrichor-Projects/awesome-strategy-skills")
    output = Path(os.environ.get("METRICS_OUTPUT", "metrics-snapshot.json"))

    if not token:
        print("GITHUB_TOKEN is required", file=sys.stderr)
        return 2

    repo = api_get(f"/repos/{repository}", token)
    views = api_get(f"/repos/{repository}/traffic/views", token)
    clones = api_get(f"/repos/{repository}/traffic/clones", token)
    referrers = api_get(f"/repos/{repository}/traffic/popular/referrers", token)
    paths = api_get(f"/repos/{repository}/traffic/popular/paths", token)

    snapshot = {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "repository": repository,
        "counts": {
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "watchers": repo["subscribers_count"],
            "open_issues": repo["open_issues_count"],
            "traffic_views": views["count"],
            "traffic_unique_visitors": views["uniques"],
            "clones": clones["count"],
            "unique_cloners": clones["uniques"],
        },
        "daily_views": views["views"],
        "daily_clones": clones["clones"],
        "top_referrers": referrers,
        "top_paths": paths,
    }
    output.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

