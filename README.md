# 📈 Stock Portfolio Tracker (Advanced Edition - 2025)

A Python-based terminal application that helps users *track real-time stock prices* of multiple top companies. Built with yfinance for fetching live market data and tabulate for displaying it beautifully in a table.

> ✅ Internship Project for CodeAlpha - Task 2

---

## 🚀 Features

- 📊 Live stock price tracking
- ⏱ Real-time data updates
- 📋 Company name, current price, change, volume & more
- 🧩 Easy to customize — add your own stock symbols
- 📱 Clean tabular interface in the terminal

---

## 🛠 Technologies Used

| Tool        | Purpose                       |
|-------------|-------------------------------|
| Python    | Core programming language     |
| yfinance  | To get stock data from Yahoo Finance |
| tabulate  | To display data in a neat table format |

---

## 📦 Requirements

Install the required libraries:

```bash
pip install yfinance tabulate

Sample Output;
  +-------------+----------+-----------+------------+---------------+
| Company     | Symbol   | Price ($) | Change %   | Volume        |
+-------------+----------+-----------+------------+---------------+
| Apple       | AAPL     | 191.62    | +0.23%     | 52,347,891    |
| Microsoft   | MSFT     | 369.88    | -0.12%     | 30,211,117    |
| ...         | ...      | ...       | ...        | ...           |
+-------------+----------+-----------+------------+---------------+
