from __future__ import annotations

import argparse
import json

from .config import MatchConfig
from .match import MatchSimulation


def main() -> None:
    parser = argparse.ArgumentParser(prog="pmcw")
    sub = parser.add_subparsers(dest="command", required=True)

    match = sub.add_parser("match", help="Run a single-match simulation.")
    match.add_argument("--home", required=True)
    match.add_argument("--away", required=True)
    match.add_argument("--lambda-home", type=float, required=True)
    match.add_argument("--lambda-away", type=float, required=True)
    match.add_argument("--simulations", type=int, default=100_000)
    match.add_argument("--seed", type=int, default=20260702)

    args = parser.parse_args()

    if args.command == "match":
        cfg = MatchConfig(
            home_team=args.home,
            away_team=args.away,
            lambda_home=args.lambda_home,
            lambda_away=args.lambda_away,
            n_simulations=args.simulations,
            seed=args.seed,
        )
        result = MatchSimulation(cfg).run().summary()
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
