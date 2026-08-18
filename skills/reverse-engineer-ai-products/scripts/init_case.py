#!/usr/bin/env python3
"""Create a non-destructive product teardown case scaffold."""

from __future__ import annotations

import argparse
from pathlib import Path


FILES = {
    "00-范围与证据规则.md": """# {product}｜范围与证据规则

## 分析范围

- 产品：{product}
- 快照时间：
- 任务/项目：
- 允许操作：只读（如有额外授权，在此写明）
- 禁止操作：发送、生成、重试、发布、删除、购买、充值、覆盖资产

## 证据等级

- 【已确认】
- 【合理推断】
- 【建议设计】
- 【未知】

## 证据缺口

""",
    "01-用户旅程-页面取证版.md": "# {product}｜用户旅程（页面取证版）\n\n",
    "02-Agent契约-页面证据版.md": "# {product}｜Agent 契约（页面证据版）\n\n",
    "03-目标Agent-功能等价SystemPrompt.md": "# {product}｜目标 Agent 功能等价 System Prompt\n\n",
    "04-产品全景架构-证据分层版.md": "# {product}｜产品全景架构（证据分层版）\n\n",
    "evidence/evidence-ledger.md": """# 证据台账

| 证据编号 | 时间/顺序 | 来源类型 | 页面/位置 | 原文或可见对象 | Agent | 操作/状态变化 | 截图 | 支持结论 | 等级 | 冲突/备注 |
|---|---|---|---|---|---|---|---|---|---|---|
""",
}


def safe_case_name(product: str) -> str:
    cleaned = product.strip().replace("/", "-").replace("\\", "-")
    if not cleaned or cleaned in {".", ".."}:
        raise ValueError("product must contain a usable name")
    return f"{cleaned}-产品拆解"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--product", required=True, help="Product name")
    parser.add_argument("--output-dir", required=True, type=Path, help="Parent output directory")
    args = parser.parse_args()

    case_dir = args.output_dir.expanduser().resolve() / safe_case_name(args.product)
    if case_dir.exists():
        raise SystemExit(f"Refusing to overwrite existing path: {case_dir}")

    for relative, template in FILES.items():
        target = case_dir / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(template.format(product=args.product.strip()), encoding="utf-8")
    (case_dir / "evidence" / "screenshots").mkdir(parents=True, exist_ok=True)

    print(case_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
