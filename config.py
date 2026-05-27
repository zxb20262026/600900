#!/usr/bin/env python3
"""长江电力(600900) 日监控 — 全局配置"""

import os, re
from datetime import datetime

# ── GitHub ──
GITHUB_TOKEN = os.environ.get("CATL_GITHUB_TOKEN", "")
REPO_OWNER = "zxb20262026"
REPO_NAME = "600900"
PAGES_URL = f"https://{REPO_OWNER}.github.io/{REPO_NAME}/"
REPO_DIR = os.path.dirname(os.path.abspath(__file__))

if not GITHUB_TOKEN and os.path.exists(os.path.expanduser("~/catl-hermes-auto/catl_auto.py")):
    with open(os.path.expanduser("~/catl-hermes-auto/catl_auto.py")) as f:
        m = re.search(r'GITHUB_TOKEN\s*=\s*"([^"]+)"', f.read())
        if m: GITHUB_TOKEN = m.group(1)

# ── 持仓 ──
HOLDING_SHARES = 0        # 待设置
GROWTH_ASSUMPTION = 8      # 水电稳定增长 ~8%
COST_PRICE = 25            # 用户持仓成本（需手动更新）

# ── PEG ──
PEG_UNDERVALUE = 1.0
PEG_OVERVALUE = 1.5

# ── 均线窗口 ──
MA_WINDOWS = [5, 20, 60]

# ── 大盘指数 ──
MARKET_INDICES = {
    "上证指数": "sh000001",
    "沪深300": "sh000300",
}

# ── 产业链相关（水电无传统上游，改为电力产业链）──
UPSTREAM_STOCKS = {
    "中国电建": "sh601669", "东方电气": "sh600875",
    "国电南瑞": "sh600406", "特变电工": "sh600089",
}

# ── 竞争对手 ──
COMPETITORS = {
    "华能水电": "sh600025", "国投电力": "sh600886", "川投能源": "sh600674",
}

# ── 同行估值对比（电力行业）──
VALUATION_PEERS = {
    "长江电力": "sh600900",
    "华能水电": "sh600025",
    "国投电力": "sh600886",
    "川投能源": "sh600674",
    "桂冠电力": "sh600236",
    "中国核电": "sh601985",
}

# ── 板块指数 ──
SECTOR_INDICES = {
    "电力行业": "sh000160", "公用事业": "sh000007",
    "绿色电力": "sh000860", "水力发电": "sh000170",
}

# 归属行业（KPI卡片显示）
CATL_INDUSTRY = "水电"                  # 显示名称
CATL_INDUSTRY_SOURCE = "电力行业"        # 实际数据源

# ── 新闻关键词 ──
NEWS_KEYWORDS = {
    "长江电力": ["长江电力"],
    "机构观点": ["长江电力 评级", "长江电力 目标价"],
    "行业趋势": ["水电 行业", "电力 政策"],
    "来水数据": ["长江 水位", "三峡 入库流量"],
    "电价政策": ["上网电价", "电力市场化"],
    "分红派息": ["长江电力 分红", "长江电力 股息"],
}

# ── 关键指标参考 ──
# 水电无传统原材料，改为关键运营指标
MATERIAL_REFERENCE = {
    "三峡入库流量": {"price": 25000, "unit": "m³/s", "low_6m": 5000, "high_6m": 60000},
    "上网电价(含税)": {"price": 0.28, "unit": "元/kWh", "low_6m": 0.25, "high_6m": 0.35},
    "资产负债率":   {"price": 58.0, "unit": "%", "low_6m": 55, "high_6m": 65},
}
MATERIAL_DISPLAY_ORDER = ["三峡入库流量", "上网电价(含税)", "资产负债率"]

# ── 操作建议参数 ──
TRADING = {
    "target_pe_range": (20, 25),       # 水电合理PE区间
    "stop_loss_price": 22,              # 止损位
    "ma60_tolerance": 0.5,              # MA60附近容差(元)
    "volume_threshold": 20,             # 放量阈值(亿) — 长江电力日成交通常10-30亿
}

# ── 时间 ──
def get_mode():
    return "早报 ☀️" if datetime.now().hour < 14 else "晚报 🌙"

def get_date_str():
    return datetime.now().strftime("%Y-%m-%d")

def get_datetime_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
